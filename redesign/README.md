# Dakota Digital redesign prototype

A working mock-up of three pages for dakotadigital.com, built from the
"Dash Finder" design (PDF + design export). Plain HTML, CSS and JavaScript:
no build step, no frameworks.

## Pages

| File | What it is |
| --- | --- |
| `index.html` | Homepage with the Dash Finder hero: pick car, years and a look, see a key-on gauge preview |
| `camaro-1969-rtx.html` | Product page for the 1969 Camaro RTX: real photos, Turn the key, backlight colors, buy box with live total |
| `dealers.html` | Find a dealer: ZIP search, pick up to 3 shops, install quote form |

Shared files: `styles.css` (all styles), `garage.js` (My Garage and the shared fitment data),
`dash-finder.js` (finder logic), `img/` (WebP images).

## Compare all five looks

The product page ends with "Every system for the 1969 Camaro": GRFX, RTX, HDX, VHX and VFD3
side by side with real prices, photos and specs from the live product pages (Oct 2026).
Desktop shows five aligned columns; phones get swipeable cards. A link under the price jumps there.

## My Garage

Every page has a garage button in the header. Pick a car once (in the finder or from the
button) and the site remembers it in this browser:

- The finder opens on your car.
- Product pages say "Fits your 1969 Camaro", or warn when the kit is for a different car
  and link to what fits.
- The dealer quote form fills in your car.

## View it

Open `index.html` in a browser, or serve the folder so every page behaves the same:

    python -m http.server 5178

then go to http://localhost:5178.

## What is real and what is not

- Real: prices, SKUs, add-ons, specs, manuals and photos on the product page come from the live site
  (Oct 2026). Category links in the finder open real dakotadigital.com pages.
- Needs checking: the finder's fitment data (which years get which systems) comes from the design file.
- Placeholder: the 12 dealers are sample data from the design (ZIP 57107 only; other ZIPs link to the live locator).
- Not wired up: Add to cart and Send request only show a note. They need the store's cart and dealer data.

Product names, photos and the logo belong to Dakota Digital, Inc. Do not publish without their approval.
