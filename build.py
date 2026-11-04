# Builds the four pages from one header and footer. Edit the values below,
# run `python build.py`. It writes the pages into site/; site/ is what is published.
WA_API_NUMBER   = "27795255987"          # the WhatsApp number clients message (no + or spaces)
WA_API_NUMBER_DISPLAY  = "+27 79 525 5987"      # the same number as people read it
WA_BUSINESS_NUMBER = "27645260397"     # the business number: suppliers asking to join (a person replies)
WA_BUSINESS_NUMBER_DISPLAY = "+27 64 526 0397"  # the same, as people read it
EMAIL       = "info@52carparts.co.za"
CITY        = "Pretoria"               # the city of the controlled start
REG_NUMBER  = "2026/271349/07"
LEGAL_NAME  = "Vyf Twee (Pty) Ltd"   # exactly as on the CIPC certificate
OFFICER     = "Hennie Botha"
ADDRESS     = "565 Coert Steynberg Street, Constantia Park, Pretoria, 0010"
UPDATED     = "28 October 2026"

WA_API_LINK = f"https://wa.me/{WA_API_NUMBER}"
WA_BUSINESS_LINK = f"https://wa.me/{WA_BUSINESS_NUMBER}"

PAGES = [("index.html", "Clients"), ("suppliers.html", "Suppliers"), ("about.html", "About us"), ("privacy.html", "Privacy policy")]

def page(file, title, description, body):
    nav = "".join(
        f'<li><a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{t}</a></li>' for f, t in PAGES)
    return f"""<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="index.html">52 Car Parts</a>
    <nav class="site-nav" aria-label="Main"><ul>{nav}</ul></nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <p><strong>52 Car Parts is a brand of Vyf Twee</strong></p>
      <p>{LEGAL_NAME}, registration number {REG_NUMBER}</p>
      <p>{ADDRESS}</p>
    </div>
    <div>
      <p><strong>Contact</strong></p>
      <p>WhatsApp: <a href="{WA_API_LINK}">{WA_API_NUMBER_DISPLAY}</a></p>
      <p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <p><strong>Pages</strong></p>
      <ul>{"".join(f'<li><a href="{f}">{t}</a></li>' for f, t in PAGES)}</ul>
      <p><a href="https://vyftwee.co.za/">Vyf Twee</a></p>
    </div>
  </div>
</footer>
</body>
</html>
"""

CLIENTS = f"""
<section class="hero">
  <div class="wrap">
    <div>
      <h1>Send us your licence disc. We’ll find the part.</h1>
      <p class="lead">52 Car Parts sources car parts for private clients in {CITY}, entirely on WhatsApp. Suppliers quote, you choose, and we collect and deliver. You pay only once you’ve inspected the part.</p>
      <div class="actions">
        <a class="btn" href="{WA_API_LINK}">Request a part on WhatsApp</a>
        <a href="#how">How it works</a>
      </div>
    </div>
    <div class="disc" aria-hidden="true">
      <div class="big">52</div>
      <div class="name">Car Parts</div>
      <dl><dt>VIN</dt><dd>AAVZZZ6RZEU123456</dd><dt>Eng. Nr.</dt><dd>CJZ 123456</dd><dt>Reg. Nr.</dt><dd>CA 123-456</dd></dl>
    </div>
  </div>
</section>

<section class="band raised" id="how">
  <div class="wrap">
    <h2>How it works</h2>
    <ol class="steps">
      <li><h3>Send a photo</h3><p>Message us and send a photo of your vehicle licence disc. We read the VIN, engine and registration numbers from it.</p></li>
      <li><h3>Describe the part</h3><p>Tell us which part you need, its position, and the types you’d accept: new, aftermarket, reconditioned or used.</p></li>
      <li><h3>Choose a quote</h3><p>We ask our suppliers and send you their offers. Every price already includes collection and delivery.</p></li>
      <li><h3>We deliver</h3><p>Our courier collects the part from the supplier and brings it to you.</p></li>
      <li><h3>Inspect, then pay</h3><p>Check the part. If it’s right, accept it and pay by EFT against your invoice. If it isn’t, reject it and it goes back.</p></li>
    </ol>
  </div>
</section>

<section class="band">
  <div class="wrap two">
    <div class="fact"><h3>One price, delivery included</h3><p>The price you accept is the price you pay. Collection and delivery are part of it.</p></div>
    <div class="fact"><h3>Pay after inspection</h3><p>You pay by EFT only after you’ve accepted the part. Use the request number on your invoice as the reference.</p></div>
    <div class="fact"><h3>Everything on WhatsApp</h3><p>No app to install and no account to create. Every step happens in your WhatsApp chat with us.</p></div>
  </div>
</section>

<section class="band raised">
  <div class="wrap">
    <h2>Questions</h2>
    <dl class="qa">
      <dt>Which areas do you deliver to?</dt>
      <dd>For now, {CITY} only. We’ll add more areas as we grow.</dd>
      <dt>What if I don’t have my licence disc?</dt>
      <dd>You can type your vehicle details instead. The VIN, engine and registration numbers help suppliers find the exact part.</dd>
      <dt>Can I order more than one part?</dt>
      <dd>Each request is for one part. Send a new request for every other part you need.</dd>
      <dt>What if the part is wrong?</dt>
      <dd>Reject it when you inspect it and tell us why. The part goes back to the supplier, and you don’t pay for it.</dd>
    </dl>
    <div class="actions"><a class="btn" href="{WA_API_LINK}">Request a part on WhatsApp</a></div>
  </div>
</section>
"""

SUPPLIERS = f"""
<section class="hero">
  <div class="wrap">
    <div>
      <h1>Sell more parts without chasing buyers.</h1>
      <p class="lead">We send you requests from private clients in {CITY} who need parts you stock. You quote on WhatsApp, and our courier collects the parts you sell.</p>
      <div class="actions"><a class="btn" href="{WA_BUSINESS_LINK}">Ask to join on WhatsApp</a></div>
    </div>
    <div class="disc" aria-hidden="true">
      <div class="big">52</div>
      <div class="name">Supplier network</div>
    </div>
  </div>
</section>

<section class="band raised">
  <div class="wrap">
    <h2>How quoting works</h2>
    <ol class="steps">
      <li><h3>You receive a request</h3><p>A WhatsApp message with the vehicle, the part and its position, from a client looking for a part you carry.</p></li>
      <li><h3>You quote</h3><p>Tap to open the quote form and enter a price for each type you have: OEM, aftermarket, reconditioned or used.</p></li>
      <li><h3>The client chooses</h3><p>We show the client the quotes. If yours is chosen, we let you know straight away.</p></li>
      <li><h3>We collect</h3><p>Our courier confirms a collection time with you and collects the part from your premises.</p></li>
    </ol>
  </div>
</section>

<section class="band">
  <div class="wrap two">
    <div class="fact"><h3>Joining</h3><p>We onboard suppliers by phone: WhatsApp or call us on <a href="{WA_BUSINESS_LINK}">{WA_BUSINESS_NUMBER_DISPLAY}</a>. We’ll ask which makes and part types you carry, and confirm your business address and contact person.</p></div>
    <div class="fact"><h3>Your own pace</h3><p>Quote on the requests that suit you. If you don’t have the part, ignore the request.</p></div>
    <div class="fact"><h3>Stop any time</h3><p>Reply STOP to any of our messages and we won’t send you requests again.</p></div>
  </div>
</section>
"""

ABOUT = f"""
<section class="doc">
  <div class="wrap">
    <h1>About us</h1>
    <p class="lead">52 Car Parts is a brand of Vyf Twee, a South African business. “Vyf twee” is Afrikaans for “five two”: 52.</p>
    <p>We started 52 Car Parts because finding a car part still means phoning around, comparing prices that leave out delivery, and taking time off to collect. We bring that onto WhatsApp: you send one request, suppliers quote, and we deliver.</p>
    <p>We’re starting small and local, with private clients in {CITY}, a network of trusted suppliers we onboard personally, and our own courier partner. We’ll grow from there.</p>
    <h2>The business behind the brand</h2>
    <div class="table-wrap"><table>
      <tr><th>Brand</th><td>52 Car Parts (52carparts.co.za)</td></tr>
      <tr><th>Business</th><td>{LEGAL_NAME} (<a href="https://vyftwee.co.za/">vyftwee.co.za</a>)</td></tr>
      <tr><th>{LEGAL_NAME} registration number</th><td>{REG_NUMBER}</td></tr>
      <tr><th>Address</th><td>{ADDRESS}</td></tr>
      <tr><th>WhatsApp</th><td><a href="{WA_API_LINK}">{WA_API_NUMBER_DISPLAY}</a></td></tr>
      <tr><th>Email</th><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr>
    </table></div>
  </div>
</section>
"""

PRIVACY = f"""
<section class="doc">
  <div class="wrap">
    <h1>Privacy policy</h1>
    <p class="meta">Last updated: {UPDATED}</p>
    <p>This policy explains how Vyf Twee, trading as 52 Car Parts, collects and uses personal information, in line with the Protection of Personal Information Act, 2013 (POPIA). It applies to clients, suppliers and couriers who use our WhatsApp service, and to visitors of this website.</p>

    <h2>Who is responsible</h2>
    <p>{LEGAL_NAME} ({REG_NUMBER}), {ADDRESS}, is the responsible party. Our Information Officer is {OFFICER}, reachable at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h2>What we collect</h2>
    <h3>Clients</h3>
    <ul>
      <li>Your WhatsApp number, name and the messages you send us.</li>
      <li>Your vehicle details: the photo of your licence disc and what we read from it (VIN, engine number, registration number, make, model and year).</li>
      <li>The part you request and your choices on quotes, inspection and payment.</li>
      <li>Your delivery address, or a location pin if you share one.</li>
    </ul>
    <h3>Suppliers and couriers</h3>
    <ul>
      <li>Business name, contact person, phone and WhatsApp numbers, business address and operating hours.</li>
      <li>Your quotes, collection and delivery arrangements, and messages with us.</li>
    </ul>
    <h3>Website visitors</h3>
    <p>This website uses no cookies, analytics or tracking, and loads nothing from other sites.</p>

    <h2>Why we use it</h2>
    <ul>
      <li>To process your part request: finding suppliers, collecting quotes and arranging collection and delivery.</li>
      <li>To invoice you and record payments.</li>
      <li>To keep you informed about your request on WhatsApp.</li>
      <li>To meet our legal obligations, such as keeping financial records.</li>
    </ul>
    <p>We use your information because it’s needed to provide the service you asked for, and where the law requires us to. We don’t sell it, and we don’t use it for advertising.</p>

    <h2>Who we share it with</h2>
    <div class="table-wrap"><table>
      <tr><th>Who</th><th>What they receive</th><th>Why</th></tr>
      <tr><td>Suppliers</td><td>Vehicle details and the part requested. Not your name, number or address.</td><td>To quote on your request</td></tr>
      <tr><td>Our courier</td><td>The client’s name, number and delivery address; the supplier’s name, number and address</td><td>To collect and deliver the part</td></tr>
      <tr><td>Meta (WhatsApp)</td><td>Our WhatsApp messages with you</td><td>WhatsApp is how the service works</td></tr>
      <tr><td>Microsoft Azure</td><td>All the information above, stored and processed in South Africa</td><td>Hosting our system</td></tr>
      <tr><td>Google (Maps)</td><td>Delivery and collection addresses</td><td>To check and locate addresses</td></tr>
    </table></div>
    <p>Meta and Google may process information outside South Africa, under their own privacy terms and safeguards.</p>

    <h2>How long we keep it</h2>
    <p>We keep request and invoice records for five years, as South African tax law requires. Other personal information is kept only while it’s needed for the service, and deleted or anonymised after that.</p>

    <h2>How we protect it</h2>
    <p>Access is limited to the people who run the service. Information is stored in secured cloud services, and credentials are kept in a protected key vault.</p>

    <h2>Your rights</h2>
    <ul>
      <li>Ask what personal information we hold about you, and for a copy.</li>
      <li>Ask us to correct or delete it.</li>
      <li>Object to how we use it.</li>
      <li>Stop our messages: reply STOP to any message.</li>
    </ul>
    <p>Send requests to <a href="mailto:{EMAIL}">{EMAIL}</a> or message us on WhatsApp. If you’re not satisfied with our response, you can complain to the Information Regulator at <a href="https://inforegulator.org.za/">inforegulator.org.za</a>.</p>

    <h2>Changes to this policy</h2>
    <p>If we change this policy, we’ll update the date at the top of this page.</p>
  </div>
</section>
"""

for f, title, desc, body in [
    ("index.html", "52 Car Parts | Car parts sourced and delivered on WhatsApp", "Send a photo of your licence disc on WhatsApp. Suppliers quote, you choose, we deliver, and you pay after inspection.", CLIENTS),
    ("suppliers.html", "Suppliers | 52 Car Parts", "Receive part requests from private clients on WhatsApp, quote in a tap, and we collect the parts you sell.", SUPPLIERS),
    ("about.html", "About us | 52 Car Parts", "52 Car Parts is a brand of Vyf Twee, sourcing car parts for private clients on WhatsApp.", ABOUT),
    ("privacy.html", "Privacy policy | 52 Car Parts", "How Vyf Twee, trading as 52 Car Parts, collects and uses personal information under POPIA.", PRIVACY),
]:
    open("site/" + f, "w", encoding="utf-8").write(page(f, title, desc, body))
print("built", [p for p, _ in PAGES])
