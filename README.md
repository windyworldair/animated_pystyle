# animated_pystyle

`animated_pystyle` is a lightweight Python library for rendering animated, colored text in a terminal using 24-bit ANSI escape codes.

## Install

### Option 1: From PyPI (after package is published)

```bash
pip install animated_pystyle
```

### Option 2: Directly from GitHub (works immediately)

```bash
pip install git+https://github.com/zalcus/animated_pystyle.git
```

## If you see `No matching distribution found for animated_pystyle`

That means the package has not been uploaded to PyPI yet (or the version isn’t published yet).
Use the GitHub install command above, or publish a release (see **Publish to PyPI**).

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

This repo includes GitHub Actions workflow `.github/workflows/publish-pypi.yml` that builds and publishes on **GitHub Release published**.

One-time setup:
- Create a PyPI project named `animated_pystyle`.
- Configure trusted publishing between your PyPI project and this GitHub repository.

Then publish:
1. Push your changes.
2. Create and publish a GitHub Release/tag.
3. The workflow uploads the package to PyPI.

After that, users can run:

```bash
pip install animated_pystyle
```

## Notes

- Requires a terminal with true-color support.
- Press `Ctrl+C` to stop long-running animations.
