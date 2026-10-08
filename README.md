# omeoray-site

The Omeoray Ltd company site. Three static files, no build step, no dependencies.

```
index.html        the home page — hero + the three project cards
contact/          the contact page (served at /contact/)
styles.css        all styling, light + dark
favicon.svg       the bearing mark
```

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

## Before it goes live: legal disclosures

UK companies must show, on their website, the registered company name, the company
registration number, the place of registration (England and Wales) and the registered
office address. The footers in `index.html` and `contact/index.html` currently carry only
the name and place of registration — add the company number and the registered office
address to both before pointing a public domain at this.

There's an HTML comment at each footer marking the spot.
