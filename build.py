# Builds the pages from one header and footer. Edit the values below, then run
# `python build.py`. It writes the pages into site/; site/ is what is published
# (CI does not run this script, so commit the generated files).
WA_CLIENT_NUMBER          = "27795255987"      # the number clients message (no + or spaces)
WA_CLIENT_NUMBER_DISPLAY  = "+27 79 525 5987"  # the same number as people read it
WA_SUPPLIER_NUMBER         = "27645260397"     # suppliers asking to join (a person replies)
WA_SUPPLIER_NUMBER_DISPLAY = "+27 64 526 0397"
REG_NUMBER  = "2026/271349/07"
LEGAL_NAME  = "Vyf Twee (Pty) Ltd"   # exactly as on the CIPC certificate
ADDRESS     = "565 Coert Steynberg Street, Constantia Park, Pretoria, 0010"

SITE    = "https://www.52carparts.co.za"
VYFTWEE = "https://www.vyftwee.co.za"

# Pre-filled WhatsApp messages. The client text goes to the bot; the workshop and
# supplier texts go to the business number, where a person replies.
CLIENT_TEXT   = "Hi, I'd like to get a quote."
WORKSHOP_TEXT = "Hi, I'm from a workshop or panel beater and would like to talk about sourcing parts regularly."
SUPPLIER_TEXT = "Hi, I'm a parts supplier in Gauteng and would like to join the 52 Car Parts network."

# TEMPORARY: the WhatsApp bot currently routes any message containing one of these
# substrings (case-insensitive, even inside a word) down a different path, so the
# client text must not contain any of them. Remove this check once the WhatsApp
# platform routes clients by customer type instead of keywords.
BOT_KEYWORDS = ["part", "parts", "bumper", "panel", "light", "mirror", "engine", "gearbox", "door",
                "bonnet", "boot", "vin", "exhaust", "radiator", "strut", "shock", "alternator",
                "headlight", "taillight", "grille", "fender", "mudguard", "starter", "battery",
                "clutch", "brake", "caliper"]
_hits = [k for k in BOT_KEYWORDS if k in CLIENT_TEXT.lower()]
if _hits:
    raise SystemExit(f"build failed: CLIENT_TEXT contains bot routing keyword(s) {_hits}: {CLIENT_TEXT!r}")

from urllib.parse import quote
def wa(number, text):
    return f"https://wa.me/{number}?text={quote(text, safe='')}"

# Meta's official WhatsApp glyph, copied unchanged from the brand folder. It is
# referenced as a file, not inlined, so its colours and markup stay exactly as supplied.
WA_GLYPH = '<img class="wa-icon" src="/images/whatsapp-glyph.svg" alt="" aria-hidden="true" width="20" height="20">'

def wa_button(href, label, cls=""):
    return f'<a class="btn btn-primary btn-wa{" " + cls if cls else ""}" href="{href}">{WA_GLYPH}<span>{label}</span></a>'

WA_CLIENT   = wa(WA_CLIENT_NUMBER, CLIENT_TEXT)
WA_WORKSHOP = wa(WA_SUPPLIER_NUMBER, WORKSHOP_TEXT)
WA_SUPPLIER = wa(WA_SUPPLIER_NUMBER, SUPPLIER_TEXT)
POLICIES = [("Terms", "terms"), ("Privacy", "privacy"), ("Refunds", "refunds"),
            ("Cancellations", "cancellations"), ("Delivery", "delivery")]

LOGO_LIGHT = "/images/52carparts-logo-light.svg"
LOGO_DARK  = "/images/52carparts-logo-dark.svg"
LOGO_WH    = 'width="167" height="134"'   # the logo's viewBox, for layout before load


def header(current):
    def link(href, text, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{href}"{cur}>{text}</a></li>'
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="logo" href="/"><picture><source media="(prefers-color-scheme: dark)" srcset="{LOGO_DARK}"><img src="{LOGO_LIGHT}" alt="52 Car Parts" {LOGO_WH}></picture></a>
    <nav class="site-nav" aria-label="Main">
      <ul>{link("/#how", "How it works", "how")}{link("/suppliers", "Suppliers", "suppliers")}{link("/#about", "About", "about")}</ul>
    </nav>
    {wa_button(WA_CLIENT, '<span class="long">Start on </span>WhatsApp', "header-cta")}
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer on-dark">
  <div class="wrap">
    <div class="footer-cols">
      <div><img class="footer-logo" src="{LOGO_DARK}" alt="52 Car Parts" {LOGO_WH}></div>
      <div>
        <h2 class="footer-heading">52 Car Parts</h2>
        <ul><li><a href="/#how">How it works</a></li><li><a href="/suppliers">Suppliers</a></li><li><a href="{WA_CLIENT}">WhatsApp {WA_CLIENT_NUMBER_DISPLAY}</a></li></ul>
      </div>
      <div>
        <h2 class="footer-heading">Policies</h2>
        <ul>{"".join(f'<li><a href="{VYFTWEE}/{p}">{t}</a></li>' for t, p in POLICIES)}</ul>
      </div>
    </div>
    <div class="footer-legal">
      <p>52 Car Parts is a brand of {LEGAL_NAME} · Registration number {REG_NUMBER} · {ADDRESS}</p>
      <p>This site uses no cookies, analytics or tracking.</p>
    </div>
  </div>
</footer>"""


def page(path, title, description, body, current=None, noindex=False):
    url = SITE + path
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    canonical = "" if noindex else f'\n<link rel="canonical" href="{url}">'
    return f"""<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">{canonical}{robots}
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#17191D">
<meta property="og:type" content="website">
<meta property="og:site_name" content="52 Car Parts">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/android-chrome-512.png">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/saira-600-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
{header(current)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>
"""


def hero(kicker, h1_first, h1_accent, intro, actions, h1_class="", id_attr=""):
    return f"""<section class="hero on-dark"{id_attr}>
  <div class="wrap hero-grid">
    <img class="hero-logo" src="{LOGO_DARK}" alt="" {LOGO_WH}>
    <div class="hero-text">
      <p class="kicker">{kicker}</p>
      <h1 class="{h1_class}">{h1_first} <span class="accent">{h1_accent}</span></h1>
      <p class="intro">{intro}</p>
      {actions}
    </div>
  </div>
</section>"""


def steps(items, cls):
    return f'<ol class="steps {cls}">' + "".join(
        f"\n      <li><h3>{t}</h3><p>{p}</p></li>" for t, p in items) + "\n    </ol>"


def benefits(items):
    return '<ul class="benefits">' + "".join(
        f"\n      <li><h3>{t}</h3><p>{p}</p></li>" for t, p in items) + "\n    </ul>"


HOME_INTRO = ("New, aftermarket, reconditioned and used parts from independent suppliers in Gauteng, "
              "delivered anywhere in South Africa. Inspect the part when it arrives and pay only if you "
              "accept it.")

HOME = hero(
    "Sourced in Gauteng · Delivered nationwide",
    "You need the part.", "We’ll find it.",
    HOME_INTRO,
    f"""<div class="actions">{wa_button(WA_CLIENT, "Start on WhatsApp")}<a class="btn btn-secondary" href="#how">How it works</a></div>
      <p class="hero-note">WhatsApp opens with a message ready. Tap Send and we’ll reply with the next steps.</p>""",
    id_attr=' id="top"',
) + f"""

<section class="band" id="how">
  <div class="wrap">
    <h2>How it works</h2>
    <p class="lead">Everything happens on WhatsApp. No app to install, no account to create.</p>
    {steps([
        ("Send your licence disc", f"Send a photo of your licence disc to {WA_CLIENT_NUMBER_DISPLAY} on WhatsApp, then complete the short request form."),
        ("Get one price", "We ask our suppliers and send you one total, including delivery. Your quote is valid for 48 hours."),
        ("Agree delivery", "Accept the quote and agree a delivery date and time with us."),
        ("The courier delivers", "A courier collects the part from the supplier and brings it to your door, anywhere in South Africa."),
        ("Inspect, then pay", "Accept the part and pay through a secure PayFast link, or reject it and pay nothing."),
    ], "steps-5")}
    {benefits([
        ("Pay only for what you accept", "You see the part before you pay. Reject it and it costs you nothing."),
        ("One price, no surprises", "Your quote includes the part and delivery. There are no extra delivery charges."),
        ("Your details stay private", "Suppliers see your vehicle and the part, never your name, number or address."),
    ])}
  </div>
</section>

<section class="band band-tight">
  <div class="wrap">
    <div class="panel panel-surface">
      <div>
        <h2>Workshops and panel beaters</h2>
        <p>Need parts regularly? Talk to us on WhatsApp about how 52 Car Parts can work for your business.</p>
      </div>
      {wa_button(WA_WORKSHOP, "Talk to us on WhatsApp")}
    </div>
  </div>
</section>

<section class="band" id="about">
  <div class="wrap about">
    <h2>About 52 Car Parts</h2>
    <p>52 Car Parts is a brand of Vyf Twee (Pty) Ltd, a South African company that builds and runs digital ventures.</p>
    <p><a class="text-link" href="{VYFTWEE}">About Vyf Twee</a></p>
  </div>
</section>"""

SUPPLIERS_INTRO = ("Receive ready-made requests on WhatsApp for the makes and stock you carry. You set your "
                   "price; we handle the client, the delivery and the payment.")

SUPPLIERS = hero(
    "For parts suppliers in Gauteng",
    "Sell more parts,", "without the phone calls.",
    SUPPLIERS_INTRO, "", h1_class="h1-suppliers",
) + f"""

<section class="band">
  <div class="wrap">
    <h2>How it works for suppliers</h2>
    {steps([
        ("Requests for your stock", "Each request shows the vehicle, VIN, part and part type, only for the makes and stock you carry."),
        ("Quote in a short form", "Open the form in WhatsApp and send your price, including VAT if you charge it."),
        ("Our courier collects", "If your quote wins, we collect the part. A part the client rejects comes back to you at our cost."),
        ("Get paid by EFT", "Within 2 working days after the client’s payment reaches us, with a remittance advice for each request."),
    ], "steps-4")}
    {benefits([
        ("Your price stays yours", "We add our margin on top of your quote. Nothing is deducted from what you charge."),
        ("Nothing to install", "Everything runs on WhatsApp, on the phone you already use."),
        ("Stop at any time", "Reply STOP to any request and you will receive no further messages."),
    ])}
  </div>
</section>

<section class="band band-tight band-last">
  <div class="wrap">
    <div class="panel panel-dark on-dark">
      <div>
        <h2>Join our supplier network</h2>
        <p>We onboard every supplier personally. Send us a WhatsApp message and we will call you to set you up.</p>
      </div>
      {wa_button(WA_SUPPLIER, f'Message us: <span class="nowrap">{WA_SUPPLIER_NUMBER_DISPLAY}</span>')}
    </div>
  </div>
</section>"""

NOT_FOUND = hero(
    "Error 404",
    "Page not found.", "Let’s get you back.",
    "The page you were looking for isn’t here. Start again from the home page, or see how we work with suppliers.",
    """<div class="actions"><a class="btn btn-primary" href="/">Go to the home page</a><a class="btn btn-secondary" href="/suppliers">Suppliers</a></div>""",
    h1_class="h1-suppliers",
)

import os
os.makedirs("site/suppliers", exist_ok=True)
for out, path, title, desc, body, current, noindex in [
    ("site/index.html", "/", "52 Car Parts | Car parts sourced in Gauteng, delivered nationwide", HOME_INTRO, HOME, None, False),
    ("site/suppliers/index.html", "/suppliers", "Suppliers | 52 Car Parts", SUPPLIERS_INTRO, SUPPLIERS, "suppliers", False),
    ("site/404.html", "/404.html", "Page not found | 52 Car Parts", "This page could not be found.", NOT_FOUND, None, True),
]:
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(page(path, title, desc, body, current, noindex))
    print("built", out)
