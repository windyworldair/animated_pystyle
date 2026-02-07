# animated_pystyle

`animated_pystyle` is a lightweight Python library for rendering animated, colored text in a terminal using 24-bit ANSI escape codes.

## Install

From PyPI:

```bash
pip install animated_pystyle
```

Or directly from GitHub:

```bash
pip install git+https://github.com/zalcus/animated_pystyle.git
```

## Quick start

```python
from animated_pystyle import animate_text

animate_text(
    text="Animated gradient text!",
    colors=[(255, 0, 255), (0, 255, 255), (255, 255, 0)],
    duration=3,
    speed=2.2,
    spacing=0.35,
    fps=30,
)
```

## Class-based API

```python
from animated_pystyle import AnimatedGradient

animator = AnimatedGradient(
    text="Hello from animated_pystyle",
    colors=[(255, 80, 80), (80, 80, 255), (80, 255, 180)],
    speed=2.0,
    spacing=0.3,
    fps=20,
)

animator.animate(duration=2)
```

## Publish to PyPI

If you maintain this package and want it downloadable via `pip install animated_pystyle`:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

## Notes

- Requires a terminal with true-color support.
- Press `Ctrl+C` to stop long-running animations.
