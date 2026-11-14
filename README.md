# 52carparts-website

The 52carparts.co.za website: Home (`/`), Suppliers (`/suppliers`) and a 404 page. Policies live on vyftwee.co.za and are linked from the footer.

- `site/` is what is published (Azure Static Web App, app location `/site`).
- Edit the values and copy at the top of `build.py`, then run `python build.py`; it rewrites `site/index.html`, `site/suppliers/index.html` and `site/404.html`.
- CI does not run `build.py`: commit the generated files in `site/`.
- `site/staticwebapp.config.json` holds the redirects for old URLs, the 404 page and the security headers.
- The logos (`site/images/`) and icons (site root) come from the 52 Car Parts brand kit. The fonts are self-hosted in `site/fonts/`: Inter 4.1 (web build) and a Saira 600–700 variable subset made from google/fonts, each with its OFL.
