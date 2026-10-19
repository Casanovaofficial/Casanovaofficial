# CV

`cv.html` is the only file you edit. Everything else is generated from it.

| File | What it is |
| --- | --- |
| `cv.html` | The CV content and layout. Edit this. |
| `headshot.jpg` | Photo used in the header. Replace it to change the photo. |
| `Erick_Casanova_CV.pdf` | Generated. Rebuilt automatically on every push. |

## Updating the CV

1. Edit `cv.html` on GitHub (pencil icon) or locally.
2. Commit to `main`.
3. The **Build and publish CV** action rebuilds the PDF, commits it back, and updates the web version at <https://casanovaofficial.github.io/Casanovaofficial/>.

The build fails on purpose if the CV grows past two pages, so it never ships a broken layout.

## Building locally

```bash
pip install -r scripts/requirements.txt
python -m playwright install chromium
python scripts/build_cv.py
```

## Privacy

The public version leaves out the phone number. Send the version with your phone number directly to recruiters instead of linking it here.
