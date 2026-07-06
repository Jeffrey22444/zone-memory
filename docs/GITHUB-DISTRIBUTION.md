# GitHub Distribution Notes

This repository is ready for GitHub-based installation because the repository
root contains:

- `install.py`
- `build_release.py`
- `VERSION`
- `README.md`
- `skills/zone-memory/...`

## Recommended Delivery Modes

1. Git repository delivery
   - User clones the repo and runs `python3 install.py --agent ...`
2. ZIP release delivery
   - User downloads a release ZIP, extracts it, and runs the same installer

## Recommended First Publish Flow

```bash
git init -b main
git add .
git commit -m "Initial portable Zone Memory release"
git remote add origin https://github.com/Jeffrey22444/zone-memory.git
git push -u origin main
```

## Optional Release Flow

```bash
python3 build_release.py --dist dist --overwrite
git tag v0.1.0
git push origin v0.1.0
```

Then attach `dist/zone-memory-skill-0.1.0.zip` to the GitHub Release.
