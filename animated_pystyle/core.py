from __future__ import annotations

import math
import signal
import sys
import time
from dataclasses import dataclass
from typing import Iterable, Sequence, Tuple

RGB = Tuple[int, int, int]


@dataclass
class AnimationConfig:
    """Configuration options for gradient animation."""

    speed: float = 2.0
    spacing: float = 0.3
    fps: int = 20


class AnimatedGradient:
    """Animate colorful text in terminals that support 24-bit ANSI colors.

    Example:
        >>> from animated_pystyle import AnimatedGradient
        >>> animator = AnimatedGradient("Hello", [(255, 0, 255), (0, 255, 255)])
        >>> animator.animate(duration=2)
    """

    def __init__(
        self,
        text: str,
        colors: Sequence[RGB],
        speed: float = 2.0,
        spacing: float = 0.3,
        fps: int = 20,
    ) -> None:
        if not text:
            raise ValueError("text must not be empty")
        if len(colors) < 2:
            raise ValueError("colors must contain at least 2 RGB tuples")
        if fps <= 0:
            raise ValueError("fps must be > 0")

        self.text = text
        self.colors = tuple(self._normalize_colors(colors))
        self.config = AnimationConfig(speed=speed, spacing=spacing, fps=fps)
        self.frame_delay = 1 / fps

        try:
            signal.signal(signal.SIGINT, self._cleanup_signal)
        except ValueError:
            # Signal handling can fail in non-main threads.
            pass

    @staticmethod
    def _normalize_colors(colors: Sequence[RGB]) -> Iterable[RGB]:
        for c in colors:
            if len(c) != 3:
                raise ValueError(f"Invalid RGB color: {c!r}")
            r, g, b = c
            if any(not isinstance(v, int) for v in (r, g, b)):
                raise ValueError(f"RGB values must be ints: {c!r}")
            if any(v < 0 or v > 255 for v in (r, g, b)):
                raise ValueError(f"RGB values must be between 0 and 255: {c!r}")
            yield (r, g, b)

    @staticmethod
    def _lerp(a: RGB, b: RGB, t: float) -> RGB:
        return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))  # type: ignore[return-value]

    def _gradient(self, t: float) -> RGB:
        n = len(self.colors) - 1
        pos = max(0.0, min(1.0, t)) * n
        idx = min(int(pos), n - 1)
        t_local = pos - idx
        return self._lerp(self.colors[idx], self.colors[idx + 1], t_local)

    def _build_frame(self, now: float) -> str:
        chunks = []
        for i, ch in enumerate(self.text):
            t = (math.sin(now * self.config.speed + i * self.config.spacing) + 1) / 2
            r, g, b = self._gradient(t)
            chunks.append(f"\033[38;2;{r};{g};{b}m{ch}")
        return "".join(chunks)

    @staticmethod
    def reset_styles() -> None:
        """Reset terminal color/style and show cursor."""
        sys.stdout.write("\033[0m\033[?25h")
        sys.stdout.flush()

    def _cleanup_signal(self, sig=None, frame=None) -> None:  # noqa: ANN001,ANN201
        self.reset_styles()
        raise SystemExit(0)

    def animate(self, duration: float | None = None, stream=None) -> None:
        """Animate text.

        Args:
            duration: Time in seconds. If ``None``, animate forever until interrupted.
            stream: Output stream (defaults to ``sys.stdout``).
        """
        out = stream or sys.stdout
        out.write("\033[?25l")
        out.flush()

        start = time.time()
        try:
            while True:
                now = time.time()
                out.write("\r" + self._build_frame(now))
                out.flush()
                if duration is not None and now - start >= duration:
                    break
                time.sleep(self.frame_delay)
        finally:
            self.reset_styles()
            out.write("\n")
            out.flush()


def animate_text(
    text: str,
    colors: Sequence[RGB],
    duration: float | None = 2.0,
    speed: float = 2.0,
    spacing: float = 0.3,
    fps: int = 20,
) -> None:
    """Convenience helper to quickly animate colored terminal text."""
    AnimatedGradient(text, colors, speed=speed, spacing=spacing, fps=fps).animate(duration=duration)
