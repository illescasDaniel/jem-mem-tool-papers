"""Render images/memory-growth.png|svg: memory-bank file sizes over time on SpaceMaker (stdlib only)."""
from math import log10
from pathlib import Path

DATES = ["09-22", "09-24", "09-27", "09-29", "10-03"]
SERIES = [("decisions.md", "#0EA5E9", [9180, 51262, 79190, 155696, 175966]),
          ("progress.md", "#16A34A", [2267, 682, 1408, 31229, 40358]),
          ("activeContext.md", "#EA580C", [772, 3103, 862, 2856, 887])]
W, H, x0, y0, pw, ph = 760, 340, 80, 50, 640, 210
lo, hi = 2.5, 5.5  # log10 bytes
def X(i): return x0 + 40 + i * (pw - 80) / (len(DATES) - 1)
def Y(v): return y0 + ph - (log10(v) - lo) / (hi - lo) * ph
o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
     f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
     f'<text x="{W/2}" y="26" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">Memory-bank files on SpaceMaker (bytes, log scale)</text>']
for e, label in [(3, "1 KB"), (4, "10 KB"), (5, "100 KB")]:
    y = Y(10 ** e)
    o.append(f'<line x1="{x0}" x2="{x0+pw}" y1="{y:.1f}" y2="{y:.1f}" stroke="#E2E8F0"/>')
    o.append(f'<text x="{x0-8}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="#475569">{label}</text>')
for i, d in enumerate(DATES):
    o.append(f'<text x="{X(i):.1f}" y="{y0+ph+20}" text-anchor="middle" font-size="12" fill="#334155">{d}</text>')
for li, (name, col, vals) in enumerate(SERIES):
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.5"/>')
    for i, v in enumerate(vals):
        o.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="4" fill="{col}"/>')
    o.append(f'<text x="{X(4)+8:.1f}" y="{Y(vals[-1])+4:.1f}" font-size="11" fill="{col}">{vals[-1]/1000:.1f} KB</text>')
    lx = x0 + li * 190
    o.append(f'<rect x="{lx}" y="{H-24}" width="12" height="12" rx="2" fill="{col}"/>')
    o.append(f'<text x="{lx+18}" y="{H-14}" font-size="12" fill="#334155">{name}</text>')
o.append("</svg>")
out = Path(__file__).resolve().parent.parent / "images"
(out / "memory-growth.svg").write_text("\n".join(o))
