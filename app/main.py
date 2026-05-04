# app/main.py
from flask import Flask, jsonify, render_template_string
import datetime

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>My App</title>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:       #0a0a0f;
      --surface:  #13131a;
      --border:   #22222e;
      --accent:   #c8f135;
      --accent2:  #5c5cf9;
      --text:     #e8e8f0;
      --muted:    #6b6b80;
      --ok:       #39d98a;
      --radius:   14px;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Syne', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      overflow-x: hidden;
    }

    /* Decorative background grid */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(var(--border) 1px, transparent 1px),
        linear-gradient(90deg, var(--border) 1px, transparent 1px);
      background-size: 48px 48px;
      opacity: 0.35;
      pointer-events: none;
      z-index: 0;
    }

    .wrapper {
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 680px;
      animation: fadeUp 0.6s cubic-bezier(.16,1,.3,1) both;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(28px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* ── Header ── */
    header {
      margin-bottom: 2.5rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'DM Mono', monospace;
      font-size: 0.7rem;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--accent);
      background: rgba(200,241,53,.08);
      border: 1px solid rgba(200,241,53,.2);
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 1.2rem;
    }

    .badge::before {
      content: '';
      width: 7px; height: 7px;
      border-radius: 50%;
      background: var(--accent);
      animation: pulse 2s ease-in-out infinite;
    }

    @keyframes pulse {
      0%,100% { opacity:1; transform:scale(1); }
      50%      { opacity:.4; transform:scale(.8); }
    }

    h1 {
      font-size: clamp(2.4rem, 6vw, 3.6rem);
      font-weight: 800;
      letter-spacing: -.03em;
      line-height: 1.05;
      background: linear-gradient(135deg, #fff 30%, var(--muted));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .subtitle {
      margin-top: .75rem;
      color: var(--muted);
      font-size: .95rem;
      font-weight: 400;
    }

    /* ── Cards ── */
    .cards {
      display: grid;
      gap: 1rem;
      grid-template-columns: 1fr 1fr;
    }

    @media (max-width: 480px) {
      .cards { grid-template-columns: 1fr; }
    }

    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.5rem;
      position: relative;
      overflow: hidden;
      transition: border-color .2s, transform .2s;
      animation: fadeUp 0.6s cubic-bezier(.16,1,.3,1) both;
    }

    .card:nth-child(1) { animation-delay: .1s; }
    .card:nth-child(2) { animation-delay: .2s; }
    .card:nth-child(3) { animation-delay: .3s; grid-column: 1 / -1; }

    .card:hover {
      border-color: rgba(255,255,255,.12);
      transform: translateY(-2px);
    }

    /* accent glow strip at top */
    .card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: var(--card-accent, var(--accent2));
      opacity: 0;
      transition: opacity .2s;
    }
    .card:hover::before { opacity: 1; }

    .card--home  { --card-accent: var(--accent); }
    .card--health{ --card-accent: var(--ok); }
    .card--time  { --card-accent: var(--accent2); }

    .card-icon {
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    .card-label {
      font-family: 'DM Mono', monospace;
      font-size: .68rem;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: .4rem;
    }

    .card-value {
      font-size: 1.05rem;
      font-weight: 700;
      word-break: break-all;
    }

    .card-value.mono {
      font-family: 'DM Mono', monospace;
      font-size: .9rem;
      font-weight: 500;
      color: var(--accent);
    }

    .status-dot {
      display: inline-block;
      width: 8px; height: 8px;
      border-radius: 50%;
      background: var(--ok);
      margin-right: 6px;
      animation: pulse 2s ease-in-out infinite;
    }

    /* ── Endpoint list ── */
    .endpoints {
      margin-top: 2rem;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      background: var(--surface);
      overflow: hidden;
      animation: fadeUp 0.6s cubic-bezier(.16,1,.3,1) .4s both;
    }

    .endpoints-header {
      padding: 1rem 1.5rem;
      border-bottom: 1px solid var(--border);
      font-family: 'DM Mono', monospace;
      font-size: .72rem;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .endpoint-row {
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: .9rem 1.5rem;
      border-bottom: 1px solid var(--border);
      transition: background .15s;
      cursor: default;
    }

    .endpoint-row:last-child { border-bottom: none; }
    .endpoint-row:hover { background: rgba(255,255,255,.03); }

    .method {
      font-family: 'DM Mono', monospace;
      font-size: .72rem;
      font-weight: 500;
      padding: 3px 9px;
      border-radius: 6px;
      background: rgba(92,92,249,.15);
      color: #8888ff;
      flex-shrink: 0;
    }

    .path {
      font-family: 'DM Mono', monospace;
      font-size: .85rem;
      color: var(--text);
      flex: 1;
    }

    .desc {
      font-size: .8rem;
      color: var(--muted);
    }

    /* ── Footer ── */
    footer {
      margin-top: 2.5rem;
      text-align: center;
      font-family: 'DM Mono', monospace;
      font-size: .7rem;
      color: var(--muted);
      letter-spacing: .05em;
      animation: fadeUp 0.6s cubic-bezier(.16,1,.3,1) .5s both;
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <header>
      <div class="badge">live</div>
      <h1>My App</h1>
      <p class="subtitle">Flask · Python · Running on port 5000</p>
    </header>

    <div class="cards">
      <div class="card card--home">
        <div class="card-icon">👋</div>
        <div class="card-label">Message</div>
        <div class="card-value">Hello from my app!</div>
      </div>

      <div class="card card--health">
        <div class="card-icon">💚</div>
        <div class="card-label">Health</div>
        <div class="card-value">
          <span class="status-dot"></span>OK
        </div>
      </div>

      <div class="card card--time">
        <div class="card-icon">🕐</div>
        <div class="card-label">Server Time</div>
        <div class="card-value mono" id="clock">{{ time }}</div>
      </div>
    </div>

    <div class="endpoints">
      <div class="endpoints-header">Available Endpoints</div>
      <div class="endpoint-row">
        <span class="method">GET</span>
        <span class="path">/</span>
        <span class="desc">Home — returns greeting message</span>
      </div>
      <div class="endpoint-row">
        <span class="method">GET</span>
        <span class="path">/health</span>
        <span class="desc">Health check — returns status</span>
      </div>
    </div>

    <footer>Flask · {{ year }} · My App</footer>
  </div>

  <script>
    // Live clock ticking
    const el = document.getElementById('clock');
    function tick() {
      el.textContent = new Date().toLocaleTimeString('en-US', { hour12: false });
    }
    tick();
    setInterval(tick, 1000);
  </script>
</body>
</html>"""


@app.route("/")
def home():
    now = datetime.datetime.now()
    return render_template_string(
        HTML,
        time=now.strftime("%H:%M:%S"),
        year=now.year,
    )


@app.route("/api")
def api_home():
    return jsonify({"message": "Hello from my app!"}), 200


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)