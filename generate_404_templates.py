#!/usr/bin/env python3
import os
import textwrap
from urllib.parse import quote

ROOT = "/workspace"
OUT_DIR = ROOT


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def svg_favicon_svg(primary: str, accent: str, letter: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{accent}"/>
    </linearGradient>
  </defs>
  <rect rx="14" ry="14" x="4" y="4" width="56" height="56" fill="url(#g)"/>
  <circle cx="20" cy="20" r="6" fill="rgba(255,255,255,0.35)"/>
  <circle cx="44" cy="46" r="5" fill="rgba(255,255,255,0.3)"/>
  <text x="50%" y="57%" text-anchor="middle" dominant-baseline="middle"
        font-family="'Inter', system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica Neue, Arial, 'Apple Color Emoji', 'Segoe UI Emoji'"
        font-size="32" font-weight="800" fill="white">{letter}</text>
</svg>'''


def inline_favicon_data_uri(primary: str, accent: str, letter: str) -> str:
    svg = svg_favicon_svg(primary, accent, letter)
    return f"data:image/svg+xml;utf8,{quote(svg)}"


def inline_logo_svg(primary: str, accent: str, brand: str) -> str:
    initials = ''.join([w[0] for w in brand.split()[:2]]).upper()
    return f'''<svg class="logo-svg" width="144" height="44" viewBox="0 0 144 44" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="{brand} logo">
  <defs>
    <linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{accent}"/>
    </linearGradient>
    <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="12" stdDeviation="10" flood-color="{accent}" flood-opacity="0.25"/>
    </filter>
  </defs>
  <rect x="0" y="2" rx="12" ry="12" width="44" height="40" fill="url(#lg)" filter="url(#shadow)"/>
  <text x="22" y="28" text-anchor="middle" dominant-baseline="middle" font-family="Inter, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica Neue, Arial" font-size="20" font-weight="800" fill="#fff">{initials}</text>
  <g transform="translate(56,6)">
    <text x="0" y="22" font-family="Inter, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica Neue, Arial" font-size="22" font-weight="900" fill="url(#lg)">{brand}</text>
  </g>
  <g opacity="0.25">
    <circle cx="128" cy="8" r="4" fill="{accent}"/>
    <circle cx="116" cy="16" r="3" fill="{primary}"/>
  </g>
 </svg>'''


palettes = [
    ("#7F00FF", "#E100FF"),  # purple-magenta
    ("#00C6FF", "#0072FF"),  # cyan-blue
    ("#F7971E", "#FFD200"),  # orange-gold
    ("#00F5A0", "#00D9F5"),  # mint-cyan
    ("#FF5858", "#F09819"),  # red-orange
    ("#43C6AC", "#191654"),  # teal-indigo
    ("#3EECAC", "#EE74E1"),  # green-pink
    ("#FBAB7E", "#F7CE68"),  # peach-sun
    ("#8EC5FC", "#E0C3FC"),  # babyblue-lilac
    ("#F5515F", "#A1051D"),  # coral-burgundy
]


google_fonts = [
    "Inter:wght@400;600;800",
    "Poppins:wght@400;600;800",
    "Montserrat:wght@400;700;900",
    "DM+Sans:wght@400;700;900",
    "Outfit:wght@400;700;900",
    "Plus+Jakarta+Sans:wght@400;700;800",
    "Manrope:wght@400;700;800",
    "Space+Grotesk:wght@400;700",
    "Rubik:wght@400;700;900",
    "Raleway:wght@400;700;900",
]


variants = [
    "aurora", "glass", "neon", "memphis", "split", "waves", "retrogrid", "soft", "spotlight", "cards"
]


niches = [
    ("ai-saas", "NeuraWave AI", "Smart automation for modern teams", "AI"),
    ("fashion-ecommerce", "Veloura Fashion", "Trend-forward apparel & accessories", "Fash"),
    ("travel-booking", "SkyTrail Travel", "Book flights, stays and adventures", "Trip"),
    ("fintech-wallet", "AuricPay", "Secure payments & digital wallet", "Pay"),
    ("health-telemed", "CareLink Health", "On-demand telemedicine appointments", "Care"),
    ("gaming-studio", "PixelForge Games", "Indie games and immersive worlds", "Game"),
    ("edtech", "StudySpark", "Micro-learning for busy minds", "Edu"),
    ("food-delivery", "DashDish", "Fast food delivery near you", "Food"),
    ("fitness-app", "PulseFit", "Train smarter, live stronger", "Fit"),
    ("music-stream", "SoundNest", "Stream limitless tracks & podcasts", "Tune"),
    ("photography", "LensCraft Studio", "Portraits, products & stories", "Lens"),
    ("digital-agency", "BrightPixel", "Creative studio & growth partners", "PX"),
    ("marketing-ads", "AdVenture", "Campaigns that convert", "Ad"),
    ("real-estate", "Brick&Beam", "Homes, rentals & spaces", "Home"),
    ("crypto-exchange", "NimbusX", "Buy, sell and stake crypto", "NX"),
    ("cloud-hosting", "StratoHost", "Fast, reliable cloud hosting", "SH"),
    ("cybersecurity", "ShieldWire", "Proactive threat defense", "SW"),
    ("legal-firm", "Lex&Co.", "Modern legal counsel", "Lex"),
    ("hr-payroll", "Payrollio", "Payroll & HR made simple", "PR"),
    ("bookstore", "Leaf&Line", "Curated reads & zines", "Book"),
    ("nonprofit", "WaterWays", "Clean water for all", "WW"),
    ("event-ticketing", "Tixly", "Discover & book events", "Tix"),
    ("interior-design", "HavenHaus", "Spaces that inspire", "HH"),
    ("coffee-roaster", "RoastLab", "Small-batch specialty coffee", "RL"),
    ("gardening", "Verdant", "Grow your urban jungle", "Leaf"),
    ("pet-care", "PawPal", "Pet grooming & care", "Paw"),
    ("auto-dealership", "ShiftDrive", "New & used cars", "SD"),
    ("barbershop", "CutCraft", "Precision cuts & shaves", "Cut"),
    ("yoga-studio", "SoulStretch", "Mindful movement & breath", "Om"),
    ("wedding-planner", "EverAfter", "Weddings & events", "EA"),
    ("architecture", "Form&Field", "Architecture & urban design", "FF"),
    ("podcast", "MicDrop", "Conversations that matter", "Mic"),
    ("writer-portfolio", "Ink&Idea", "Essays, fiction & copy", "Ink"),
    ("resume-builder", "HireCraft", "Build standout resumes", "HC"),
    ("travel-blog", "NomadNotes", "Guides for wanderers", "NN"),
    ("bakery", "Butter&Flour", "Artisan breads & pastries", "BF"),
    ("flower-shop", "BloomTheory", "Florals & decor", "BT"),
    ("spa-wellness", "Calm&Co.", "Therapy & relaxation", "Calm"),
    ("photobooth", "FlashBox", "Photo booth rentals", "FB"),
    ("kids-toys", "BrightBox Toys", "Play to learn", "Toy"),
    ("sneaker-boutique", "Kicks&Co.", "Limited drops & heat", "KK"),
    ("furniture", "Oak&Iron", "Crafted furniture", "OI"),
    ("crypto-wallet", "Vaultly", "Your web3 wallet", "VL"),
    ("ai-chatbot", "Chatterly AI", "Conversational AI agents", "CA"),
    ("startup-incubator", "SeedSprint", "Launchpad for founders", "SS"),
    ("consulting", "NorthArrow", "Strategy & ops consulting", "NA"),
    ("photoprint", "Printify Lab", "Prints & frames", "PL"),
    ("language-app", "LingoLoop", "Learn languages fast", "LL"),
    ("newsletter", "Signal&Noise", "A better daily brief", "SN"),
    ("digital-products", "PixelGoods", "Design assets & tools", "PG"),
    ("home-cleaning", "ShineBright", "Home cleaning pros", "SB"),
    ("travel-gear", "TrailKit", "Gear for explorers", "TK"),
    ("sports-club", "Northside FC", "Community football club", "NFC"),
    ("brewery", "HoppyDays", "Craft beer brewery", "HD"),
    ("art-gallery", "Canvas&Co.", "Modern art gallery", "CC"),
    ("electric-bikes", "VoltRide", "E-bikes & scooters", "VR"),
    ("green-energy", "EcoGrid", "Solar & storage", "EG"),
    ("meditation-app", "StillMind", "Meditation & sleep", "SM"),
    ("project-mgmt", "TaskFlow", "Projects & sprints", "TF"),
    ("analytics", "MetricMinds", "Dashboards & insights", "MM"),
]


def make_html(idx: int, slug: str, brand: str, tagline: str, letter: str) -> str:
    pal = palettes[idx % len(palettes)]
    primary, accent = pal
    font = google_fonts[idx % len(google_fonts)]
    variant = variants[idx % len(variants)]
    favicon_uri = inline_favicon_data_uri(primary, accent, letter[0] if letter else brand[0])
    logo_svg = inline_logo_svg(primary, accent, brand)
    # Icon CDN
    icons = [
        "https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css",
        "https://cdn.jsdelivr.net/npm/remixicon@4.3.0/fonts/remixicon.css"
    ]
    # Decorative label
    vibe = variant.capitalize()
    
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>404 — {brand}</title>
  <meta name=\"description\" content=\"{tagline}\" />
  <link rel=\"icon\" type=\"image/svg+xml\" href=\"{favicon_uri}\" />
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
  <link href=\"https://fonts.googleapis.com/css2?family={font}&display=swap\" rel=\"stylesheet\" />
  {''.join([f'<link rel="stylesheet" href="{u}" />' for u in icons])}
  <link rel=\"stylesheet\" href=\"style.css\" />
  <script defer src=\"script.js\"></script>
  <style>
    /* Variant helper for {vibe} */
  </style>
  <meta name=\"theme-color\" content=\"{primary}\" />
  <meta name=\"color-scheme\" content=\"light dark\" />
  <meta name=\"robots\" content=\"noindex\" />
  <meta property=\"og:title\" content=\"404 — {brand}\" />
  <meta property=\"og:description\" content=\"{tagline}\" />
  <meta property=\"og:type\" content=\"website\" />
</head>
<body class=\"variant-{variant}\" data-brand=\"{brand}\" data-slug=\"{slug}\">
  <header class=\"site-header\">
    <a href=\"#\" class=\"brand\" aria-label=\"{brand} home\">{logo_svg}</a>
    <nav class=\"quick\" aria-label=\"Quick links\">
      <a href=\"#\" class=\"nav-link\"><i class=\"bx bx-help-circle\"></i> Help Center</a>
      <a href=\"#\" class=\"nav-link\"><i class=\"bx bx-message-dots\"></i> Contact</a>
      <button class=\"theme-toggle\" aria-label=\"Toggle theme\"><i class=\"bx bx-moon\"></i></button>
    </nav>
  </header>

  <main class=\"hero\" role=\"main\">
    <div class=\"decor\" aria-hidden=\"true\"></div>
    <section class=\"content\">
      <div class=\"eyebrow\">{vibe} · {slug.replace('-', ' ').title()}</div>
      <h1 class=\"title\"><span class=\"num\">4</span><span class=\"num\">0</span><span class=\"num\">4</span></h1>
      <p class=\"tagline\">We can't find the page you are looking for. {tagline}</p>
      <div class=\"actions\">
        <a class=\"btn primary\" href=\"#\"><i class=\"ri-arrow-left-line\"></i> Go Back</a>
        <a class=\"btn ghost\" href=\"#\"><i class=\"ri-home-5-line\"></i> Homepage</a>
      </div>

      <div class=\"extras\">
        <div class=\"chip\"><i class=\"bx bx-time-five\"></i> Redirect in <span id=\"counter\">10</span>s</div>
        <div class=\"chip\"><i class=\"bx bx-bulb\"></i> Tip: Use search or our sitemap</div>
      </div>

      <div class=\"controls\">
        <button class=\"ctrl\" data-action=\"pause\"><i class=\"ri-pause-mini-fill\"></i> Pause</button>
        <button class=\"ctrl\" data-action=\"resume\"><i class=\"ri-play-mini-fill\"></i> Resume</button>
        <button class=\"ctrl\" data-action=\"reset\"><i class=\"ri-restart-line\"></i> Reset</button>
      </div>
    </section>
  </main>

  <footer class=\"site-footer\">
    <div class=\"cols\">
      <div>
        <h3>Need help?</h3>
        <p>Email support@{slug}.com or chat with us 24/7.</p>
      </div>
      <ul>
        <li><a href=\"#\">Status</a></li>
        <li><a href=\"#\">Docs</a></li>
        <li><a href=\"#\">Pricing</a></li>
      </ul>
      <ul>
        <li><a href=\"#\">Terms</a></li>
        <li><a href=\"#\">Privacy</a></li>
        <li><a href=\"#\">Security</a></li>
      </ul>
    </div>
  </footer>
</body>
</html>
"""
    return html


def make_css(idx: int) -> str:
    primary, accent = palettes[idx % len(palettes)]
    font_family = google_fonts[idx % len(google_fonts)].split(':')[0].replace('+', ' ')
    variant = variants[idx % len(variants)]
    return textwrap.dedent(f"""
    :root {{
      --primary: {primary};
      --accent: {accent};
      --bg: #0b0d12;
      --card: rgba(255,255,255,0.06);
      --text: #e6e7eb;
      --muted: #a2a6b3;
      --ring: color-mix(in oklab, var(--accent), white 20%);
    }}

    * {{ box-sizing: border-box; }}
    html, body {{ height: 100%; }}
    body {{
      margin: 0;
      font-family: '{font_family}', system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica Neue, Arial;
      color: var(--text);
      background: radial-gradient(1200px 800px at 85% -10%, color-mix(in oklab, var(--accent), #000 70%), transparent 60%),
                  radial-gradient(900px 700px at -10% 120%, color-mix(in oklab, var(--primary), #000 70%), transparent 60%),
                  #080a0f;
      background-attachment: fixed;
    }}

    .site-header {{
      display: flex; align-items: center; justify-content: space-between;
      padding: 20px clamp(16px, 3vw, 40px);
    }}
    .brand {{ text-decoration: none; color: inherit; display: inline-flex; align-items: center; gap: 10px; }}
    .logo-svg {{ display: block; }}
    .quick {{ display: flex; align-items: center; gap: 14px; }}
    .nav-link {{ color: var(--muted); text-decoration: none; font-weight: 600; }}
    .nav-link:hover {{ color: var(--text); }}
    .theme-toggle {{ background: transparent; border: 1px solid var(--card); color: var(--text); padding: 8px 10px; border-radius: 10px; cursor: pointer; }}

    .hero {{ position: relative; min-height: calc(100vh - 120px); display: grid; place-items: center; padding: 40px 16px; }}
    .content {{
      width: min(960px, 100%);
      background: {"backdrop-filter: blur(10px); background: color-mix(in oklab, var(--card), transparent 30%);" if variant in ['glass','soft'] else "transparent"};
      border: 1px solid color-mix(in oklab, var(--card), transparent 20%);
      border-radius: 24px;
      padding: clamp(24px, 4vw, 56px);
      position: relative;
      z-index: 2;
    }}
    .eyebrow {{ color: var(--muted); text-transform: uppercase; letter-spacing: .18em; font-size: 12px; margin-bottom: 12px; }}
    .title {{ font-size: clamp(64px, 14vw, 180px); line-height: .85; margin: 0; display: flex; gap: .1em; justify-content: center; font-weight: 900; background: linear-gradient(90deg, var(--primary), var(--accent)); -webkit-background-clip: text; background-clip: text; color: transparent; text-shadow: 0 10px 60px color-mix(in srgb, var(--accent), transparent 70%); }}
    .tagline {{ color: var(--muted); font-size: clamp(14px, 2.2vw, 18px); max-width: 60ch; margin: 16px auto 24px; text-align: center; }}
    .actions {{ display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }}
    .btn {{ appearance: none; border: 0; padding: 12px 16px; border-radius: 14px; font-weight: 700; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; }}
    .btn.primary {{ background: linear-gradient(90deg, var(--primary), var(--accent)); color: #0b0d12; box-shadow: 0 10px 30px color-mix(in srgb, var(--accent), transparent 70%); }}
    .btn.ghost {{ background: transparent; color: var(--text); border: 1px solid var(--card); }}

    .extras {{ display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 16px; }}
    .chip {{ background: rgba(255,255,255,0.06); border: 1px solid var(--card); padding: 8px 12px; border-radius: 999px; color: var(--muted); font-weight: 600; }}

    .controls {{ display: flex; justify-content: center; gap: 10px; margin-top: 18px; }}
    .ctrl {{ background: rgba(255,255,255,0.06); color: var(--text); border: 1px solid var(--card); padding: 8px 12px; border-radius: 10px; cursor: pointer; }}
    .ctrl:hover {{ border-color: var(--ring); }}

    .site-footer {{ border-top: 1px solid var(--card); padding: 24px clamp(16px, 3vw, 40px); }}
    .cols {{ display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 20px; max-width: 1200px; margin: 0 auto; }}
    .cols h3 {{ margin: 0 0 8px; }}
    .cols ul {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; }}
    .cols a {{ color: var(--muted); text-decoration: none; }}
    .cols a:hover {{ color: var(--text); }}

    .decor {{ position: absolute; inset: 0; pointer-events: none; z-index: 1; }}
    body.variant-aurora .decor {{
      background: conic-gradient(from 180deg at 70% 20%, color-mix(in oklab, var(--accent), transparent 70%), transparent),
                  radial-gradient(600px 400px at 20% 80%, color-mix(in oklab, var(--primary), transparent 75%), transparent);
      filter: blur(30px) saturate(120%);
      opacity: .9;
    }}
    body.variant-neon .title {{ text-shadow: 0 0 10px color-mix(in srgb, var(--accent), transparent 40%), 0 0 40px color-mix(in srgb, var(--accent), transparent 60%); }}
    body.variant-memphis .decor::before {{ content: ""; position: absolute; inset: 0; background-image: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.08) 2px, transparent 3px), radial-gradient(circle at 60% 70%, rgba(255,255,255,0.06) 2px, transparent 3px); background-size: 24px 24px; }}
    body.variant-waves .decor {{ background: linear-gradient(transparent 60%, rgba(255,255,255,0.06) 60%),
      url('data:image/svg+xml;utf8,{quote("""
      <svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1200 200\" preserveAspectRatio=\"none\">
        <path d=\"M0,64 C300,160 900,0 1200,96 L1200,00 L0,0 Z\" fill=\"rgba(255,255,255,0.05)\"/>
      </svg>
      """.strip())}'); background-repeat: no-repeat; background-position: bottom; background-size: cover; }}
    body.variant-retrogrid .decor {{ background-image: linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px); background-size: 40px 40px; mask-image: radial-gradient(circle at 60% 40%, #000 40%, transparent 70%); opacity: .6; }}
    body.variant-split .content {{ display: grid; grid-template-columns: 1.1fr .9fr; align-items: center; gap: clamp(16px, 3vw, 40px); }}
    body.variant-split .content::after {{ content: ""; display: block; height: 280px; border-radius: 20px; background: linear-gradient(180deg, color-mix(in oklab, var(--primary), transparent 40%), color-mix(in oklab, var(--accent), transparent 40%)); box-shadow: inset 0 0 0 1px var(--card), 0 20px 40px color-mix(in srgb, var(--accent), transparent 80%); }}
    body.variant-cards .content {{ box-shadow: 0 20px 80px color-mix(in srgb, var(--accent), transparent 85%), inset 0 0 0 1px var(--card); }}

    @media (max-width: 900px) {{
      .cols {{ grid-template-columns: 1fr; }}
      body.variant-split .content {{ grid-template-columns: 1fr; }}
    }}
    """)


def make_js() -> str:
    return textwrap.dedent(
        """
        const counterEl = document.getElementById('counter');
        let seconds = 10;
        let timer = null;

        function tick() {
          seconds -= 1;
          if (counterEl) counterEl.textContent = String(seconds);
          if (seconds <= 0) {
            clearInterval(timer);
            // Redirect target (customize):
            // location.href = '/';
          }
        }

        function start() {
          clearInterval(timer);
          timer = setInterval(tick, 1000);
        }

        function pause() { clearInterval(timer); }
        function resume() { start(); }
        function reset() { seconds = 10; if (counterEl) counterEl.textContent = '10'; }

        document.addEventListener('click', (e) => {
          const btn = e.target.closest('.ctrl');
          if (!btn) return;
          const action = btn.dataset.action;
          if (action === 'pause') pause();
          if (action === 'resume') resume();
          if (action === 'reset') reset();
        });

        // Theme toggle
        const toggle = document.querySelector('.theme-toggle');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
        function applyTheme() {
          const isDark = document.documentElement.classList.toggle('dark', prefersDark.matches);
          toggle && (toggle.innerHTML = isDark ? '<i class="bx bx-sun"></i>' : '<i class="bx bx-moon"></i>');
        }
        prefersDark.addEventListener('change', applyTheme);
        toggle && toggle.addEventListener('click', () => {
          document.documentElement.classList.toggle('dark');
        });
        applyTheme();
        reset();
        start();
        """
    )


def connector_html(entries):
    cards = []
    for i, (folder, brand, slug) in enumerate(entries):
        primary, accent = palettes[i % len(palettes)]
        cards.append(f"""
        <a class=\"card\" href=\"{folder}/index.html\">
          <div class=\"card-bg\" style=\"--p:{primary};--a:{accent}\"></div>
          <div class=\"card-body\">
            <div class=\"card-title\">{brand}</div>
            <div class=\"card-sub\">{slug.replace('-', ' ').title()}</div>
          </div>
        </a>
        """)

    head = textwrap.dedent("""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <title>404 Template Gallery (60)</title>
      <link rel="preconnect" href="https://fonts.googleapis.com"/>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
      <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap" rel="stylesheet"/>
      <style>
        :root{--bg:#0b0d12;--card:rgba(255,255,255,.06);--text:#e6e7eb;--muted:#a2a6b3}
        *{box-sizing:border-box}
        body{margin:0;background:radial-gradient(1200px 800px at 85% -10%, #1a1e2d, transparent 60%),radial-gradient(900px 700px at -10% 120%, #151824, transparent 60%),#0b0d12;color:var(--text);font-family:Outfit,system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,Helvetica Neue,Arial}
        header{display:flex;align-items:center;justify-content:space-between;padding:20px clamp(16px,3vw,40px)}
        h1{font-size:clamp(24px,3vw,34px);margin:0}
        .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;padding:20px clamp(16px,3vw,40px) 48px;max-width:1400px;margin:0 auto}
        .card{position:relative;display:block;border-radius:18px;overflow:hidden;text-decoration:none;color:var(--text);border:1px solid var(--card)}
        .card-bg{position:absolute;inset:0;background:linear-gradient(120deg,var(--p),var(--a));filter:blur(40px) saturate(120%);opacity:.4}
        .card-body{position:relative;z-index:2;padding:18px}
        .card-title{font-weight:800}
        .card-sub{color:var(--muted);font-size:12px;margin-top:2px}
        footer{padding:24px;color:var(--muted);text-align:center}
      </style>
    </head>
    <body>
      <header>
        <h1>404 Template Gallery (60)</h1>
        <nav>
          <a href="tutorial.html" style="color:var(--text);text-decoration:none;border:1px solid var(--card);padding:8px 12px;border-radius:10px">Customization Tutorial</a>
        </nav>
      </header>
      <main class="grid">
    """)

    tail = textwrap.dedent("""
      </main>
      <footer>Open any card to view the template.</footer>
    </body>
    </html>
    """)

    return head + "".join(cards) + tail


def tutorial_html() -> str:
    return textwrap.dedent(
        """
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width, initial-scale=1"/>
          <title>404 Templates — Customization Tutorial</title>
          <link rel="preconnect" href="https://fonts.googleapis.com"/>
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
          <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap" rel="stylesheet"/>
          <style>
            :root{--bg:#0b0d12;--card:rgba(255,255,255,.06);--text:#e6e7eb;--muted:#a2a6b3;--ring:#4f46e5}
            *{box-sizing:border-box}
            body{margin:0;background:radial-gradient(1200px 800px at 85% -10%, #1a1e2d, transparent 60%),radial-gradient(900px 700px at -10% 120%, #151824, transparent 60%),#0b0d12;color:var(--text);font-family:Poppins,system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,Helvetica Neue,Arial}
            header{display:flex;align-items:center;justify-content:space-between;padding:20px clamp(16px,3vw,40px)}
            h1{font-size:clamp(22px,3vw,32px);margin:0}
            main{max-width:1000px;margin:0 auto;padding:20px clamp(16px,3vw,40px) 48px;display:grid;gap:18px}
            section{border:1px solid var(--card);border-radius:16px;padding:18px;background:rgba(255,255,255,.04)}
            code,pre{background:rgba(255,255,255,.08);padding:8px 10px;border-radius:10px}
            a{color:#c4b5fd}
          </style>
        </head>
        <body>
          <header>
            <h1>404 Templates — Customization Tutorial</h1>
            <nav><a href="index.html" style="color:var(--text);text-decoration:none;border:1px solid var(--card);padding:8px 12px;border-radius:10px">Back to Gallery</a></nav>
          </header>
          <main>
            <section>
              <h2>Folder structure</h2>
              <p>Each template folder contains exactly three files:</p>
              <ul>
                <li><strong>index.html</strong> — markup with inline SVG logo and favicon (data URI)</li>
                <li><strong>style.css</strong> — all styles and background animations</li>
                <li><strong>script.js</strong> — countdown controls and interactions</li>
              </ul>
            </section>
            <section>
              <h2>Change logo (inline SVG)</h2>
              <p>Open <code>index.html</code> and find the <code>&lt;svg class="logo-svg" ...&gt;</code>. Replace the text elements or shapes. You can paste your own SVG; keep width/height reasonable (e.g., height ≈ 44px).</p>
              <p>To edit brand text, update the <code>brand</code> text inside the SVG group.</p>
            </section>
            <section>
              <h2>Use a custom favicon (SVG)</h2>
              <p>Find the favicon link in <code>&lt;head&gt;</code>:</p>
              <pre>&lt;link rel="icon" type="image/svg+xml" href="data:image/svg+xml;utf8,&lt;svg ...&gt;...&lt;/svg&gt;" /&gt;</pre>
              <p>Replace the inline SVG or point to an external <code>favicon.svg</code> file:</p>
              <pre>&lt;link rel="icon" type="image/svg+xml" href="favicon.svg" /&gt;</pre>
            </section>
            <section>
              <h2>Change colors & background</h2>
              <p>In <code>style.css</code>, adjust the CSS variables under <code>:root</code>:</p>
              <pre>:root {\n  --primary: #7F00FF;\n  --accent: #E100FF;\n  --bg: #0b0d12;\n}</pre>
              <p>For background animations, tweak the <code>.decor</code> rules per variant class on the <code>&lt;body&gt;</code>.</p>
            </section>
            <section>
              <h2>Change title, paragraph, icons</h2>
              <p>Edit the <code>.title</code> and <code>.tagline</code> in <code>index.html</code>. Icons come from CDN (Boxicons and Remix Icon). Swap classes like <code>bx bx-time-five</code> or <code>ri-home-5-line</code> to change icons.</p>
            </section>
            <section>
              <h2>Countdown counter</h2>
              <p>In <code>script.js</code>:</p>
              <ul>
                <li><strong>Change duration</strong>: set <code>let seconds = 10;</code> to your preferred number.</li>
                <li><strong>Reset</strong>: the <code>reset()</code> function sets it back to 10. Modify there.</li>
                <li><strong>Redirect</strong>: uncomment <code>location.href = '/'</code> and change the path.</li>
              </ul>
            </section>
            <section>
              <h2>Reset styles quickly</h2>
              <p>Delete or adjust any variant class on <code>&lt;body class="variant-..."&gt;</code> to switch background styling.</p>
            </section>
            <section>
              <h2>Performance tips</h2>
              <ul>
                <li>Prefer SVGs over heavy images.</li>
                <li>Keep gradients and blurs reasonable for low-end devices.</li>
                <li>Host icon CSS on your own CDN for production if needed.</li>
              </ul>
            </section>
          </main>
        </body>
        </html>
        """
    )


def main():
    entries = []
    for i, (slug, brand, tagline, letter) in enumerate(niches):
        folder = f"404-{i+1:02d}-{slug}"
        out_path = os.path.join(OUT_DIR, folder)
        ensure_dir(out_path)

        with open(os.path.join(out_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(make_html(i, slug, brand, tagline, letter))

        with open(os.path.join(out_path, "style.css"), "w", encoding="utf-8") as f:
            f.write(make_css(i))

        with open(os.path.join(out_path, "script.js"), "w", encoding="utf-8") as f:
            f.write(make_js())

        entries.append((folder, brand, slug))

    # Connector
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(connector_html(entries))

    with open(os.path.join(OUT_DIR, "tutorial.html"), "w", encoding="utf-8") as f:
        f.write(tutorial_html())

    print(f"Generated {len(entries)} templates, connector index.html and tutorial.html")


if __name__ == "__main__":
    main()

