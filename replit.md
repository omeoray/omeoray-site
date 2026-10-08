# Running on Replit

This is an existing static HTML/CSS website. Keep the current structure; no
framework, dependency installation, database, or secrets are needed.

Use the **Start application** workflow (or Replit's Run button) to start:

```sh
python3 -m http.server 5000 --bind 0.0.0.0
```

Open the web preview to view the home page at `/` and the contact page at
`/contact/`. HTML, CSS, and asset edits are served directly; refresh the preview
to see changes.

The Python server is for development preview, not production hosting. Replit
static publishing is configured to run `python3 scripts/prepare_static.py` and
serve `dist/`. The staging script copies only the website's pages, stylesheet,
favicon, and images. `dist/` is generated output; do not store source files there.

The README's legal-disclosure warning is outdated: both current HTML footers
already include a company number and registered office address.
