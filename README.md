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

That error means `animated_pystyle` is not published on PyPI yet (or your requested version is not published yet).

Use one of these fixes:
- Install from GitHub (`pip install git+https://github.com/zalcus/animated_pystyle.git`), or
- Publish to PyPI using the steps below.

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

### Recommended: GitHub Actions Trusted Publishing

This repo includes `.github/workflows/publish-pypi.yml`, which publishes automatically when you publish a GitHub Release.

One-time setup:
1. Create a project on PyPI named `animated_pystyle`.
2. In PyPI project settings, configure **Trusted Publisher** for this GitHub repo:
   - owner/repo: `zalcus/animated_pystyle`
   - workflow file: `.github/workflows/publish-pypi.yml`
   - environment (if required): `pypi`
3. Ensure your GitHub repository has the `pypi` environment available.

Release steps:
1. Push changes to GitHub.
2. Create and publish a GitHub Release (tag like `v0.3.1`).
3. GitHub Actions builds and uploads to PyPI.
4. Verify with:

```bash
pip install animated_pystyle
```

### Manual fallback (local upload)

If you prefer manual publishing:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

## Notes

- Requires a terminal with true-color support.
- Press `Ctrl+C` to stop long-running animations.
