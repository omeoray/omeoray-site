# omeoray-site

The Omeoray Ltd company site. Three static files, no build step, no dependencies.

```
index.html        the home page — hero + the three project cards
contact/          the contact page (served at /contact/)
styles.css        all styling, light + dark
favicon.svg       the bearing mark (placeholder — see "The logo" below)
assets/           app icons, pulled from each product's own repo
```

The app icons came straight from the repos, resized to 256px:

| File | Source |
| --- | --- |
| `assets/b33n.png` | `Been` → `ios/Been/Images.xcassets/AppIcon.appiconset/App-Icon-1024x1024@1x.png` |
| `assets/plug.png` | `Plug` → `artifacts/plug-fm-ios/assets/images/icon.png` |
| `assets/auntyrun.png` | `Aunty_Run` → `aunty-ghost-mansion/icon-512.png` |

## The logo

`assets/omeoray-mark.png` is the circular monogram, cropped out of the full Omeoray Ltd
lockup, squared with 6% padding and recoloured to pure black on transparent. Pure black is
deliberate: dark mode is then a single exact `filter: invert(1)` in `styles.css` rather than
a second export to keep in sync. `favicon.svg` embeds a 128px copy and inverts it the same
way under a dark browser UI; `assets/apple-touch-icon.png` is the opaque version Apple wants.

The wordmark beside the mark is set in type, not an image, so it stays crisp and selectable.

**If you ever have the mark as vector**, replacing the PNG with an SVG is worth doing — the
mark is dense at favicon size and vector would sharpen it. The swap is `src="…"` in two HTML
files plus `favicon.svg`.

Open `index.html` in a browser to see it. That's the whole workflow.

## Links currently on the site

| Project | Web | App Store |
| --- | --- | --- |
| B33n | `b33n.link` | `apps.apple.com/gb/app/b33n/id6809171479` |
| Plug.fm | `plug.fm` | — |
| Aunty Run | `aunty-run.replit.app` | `apps.apple.com/gb/app/auntyrun/id6780049104` |

To add a store link to Plug.fm, copy an existing `App Store` button from another card in
`index.html` and change the `href`.

## Adding a project

Copy a whole `<li class="project">` block, change the name, the description and the links,
and give it a `--bearing` angle no other project uses:

```html
<li class="project reveal" style="--bearing:315deg">
```

The bearing is the identity system — one ring, one tick, a different heading per product.
Angles in use: Omeoray `0deg`, B33n `45deg`, Plug.fm `120deg`, Aunty Run `200deg`.

## Deploying on GitHub Pages

Settings → Pages → Source: *Deploy from a branch* → `main` / `root`. Live within a minute
or two at `https://omeoray.github.io/omeoray-site/`.

For `omeoray.com`: add a file called `CNAME` at the root containing just `omeoray.com`, point
the domain's DNS at GitHub Pages (four `A` records for the apex, or a `CNAME` for `www`), then
set the custom domain in Settings → Pages. Don't add the `CNAME` file before the DNS is
pointed — Pages will fail its check and the site goes down until you remove it.

## Legal disclosures

UK companies must show, on their website, the registered company name, the company
registration number, the place of registration (England and Wales) and the registered
office address. Both `index.html` and `contact/index.html` currently include these
details in their footers.
