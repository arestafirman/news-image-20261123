#!/usr/bin/env python3
"""Render THE WORLD IN ONE DAY — Monday 23 November 2026.

Draws the 1024x1024 news poster from data.py with Pillow only.
Every illustration is procedural (geometric shapes drawn in code);
no photos, no external assets, no network. Output is deterministic:
the same code always writes the same bytes.

Run:  python3 generate_image.py   (writes entry.png next to this file)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data

W, H = 1024, 1024

# --- palette ---------------------------------------------------------------
NAVY = "#0e1e3e"
NAVY2 = "#16294d"
GOLD = "#e8b64c"
PAPER = "#f7f4ec"
INK = "#14181f"
MUTED = "#5a6472"
LINE = "#c9c2b2"
WHITE = "#ffffff"
RED = "#b91c1c"
GREEN = "#15803d"
AMBER = "#b45309"
STATUS_COLOUR = {"CONFIRMED": GREEN, "REPORTED": AMBER, "ONGOING": RED}

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except OSError:
        return ImageFont.load_default()


F_TITLE = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
F_REG = lambda s: font("DejaVuSans.ttf", s)
F_OBLIQUE = lambda s: font("DejaVuSans-Oblique.ttf", s)


def text_w(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if text_w(draw, trial, fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def status_pill(draw, x, y, status):
    """Small coloured status pill; returns its right edge."""
    col = STATUS_COLOUR.get(status, MUTED)
    fnt = F_BOLD(8)
    w = text_w(draw, status, fnt) + 10
    draw.rounded_rectangle([x, y, x + w, y + 13], radius=6, fill=col)
    draw.text((x + 5, y + 2), status, font=fnt, fill=WHITE)
    return x + w


def num_chip(draw, x, y, n, r=11, fill=RED):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=WHITE, width=2)
    label = str(n)
    size = 12 if r >= 11 else 9
    if len(label) > 1:
        size -= 2
    fnt = F_BOLD(size)
    tw = text_w(draw, label, fnt)
    draw.text((x - tw / 2, y - size / 2 - 1), label, font=fnt, fill=WHITE)


# --- procedural scene art --------------------------------------------------
def scene_tanker(draw, box):
    x0, y0, x1, y1 = box
    # dusk sky
    for i in range(y1 - y0):
        t = i / max(1, y1 - y0)
        r = int(232 - 120 * t)
        g = int(150 - 60 * t)
        b = int(80 + 60 * t)
        draw.line([(x0, y0 + i), (x1, y0 + i)], fill=(r, g, b))
    # sun
    cx, cy = x0 + (x1 - x0) * 0.72, y0 + 34
    draw.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill="#fde68a")
    # sea
    draw.rectangle([x0, y0 + 78, x1, y1], fill="#123a5c")
    for k in range(4):
        yy = y0 + 86 + k * 9
        draw.line([(x0 + 6, yy), (x1 - 6, yy)], fill="#2f6ea5", width=2)
    # three tankers, near to far
    for tx, tw, th, col in [(x0 + 18, 96, 26, "#1f2937"),
                            (x0 + 132, 74, 20, "#374151"),
                            (x0 + 228, 58, 16, "#4b5563")]:
        ty = y0 + 78 - th
        draw.rectangle([tx, ty, tx + tw, ty + th], fill=col)
        draw.rectangle([tx + tw - 18, ty - 12, tx + tw - 6, ty], fill=col)
        draw.rectangle([tx + 4, ty - 8, tx + 12, ty], fill=col)
    # dashed blockade line
    yy = y0 + 62
    for xx in range(x0 + 8, x1 - 8, 16):
        draw.line([(xx, yy), (xx + 9, yy)], fill="#fca5a5", width=2)
    draw.text((x0 + 10, y0 + 6), "KHARG  ·  14+ TANKERS WAITING",
              font=F_BOLD(10), fill="#fff7ed")


def scene_kyiv(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill="#0b1026")
    # stars
    for sx, sy in [(30, 14), (80, 26), (150, 10), (210, 22), (270, 12),
                   (55, 40), (180, 42), (240, 48), (310, 30), (120, 52)]:
        draw.ellipse([x0 + sx - 1, y0 + sy - 1, x0 + sx + 1, y0 + sy + 1],
                     fill="#e5e7eb")
    # searchlight beams
    draw.polygon([(x0 + 40, y1), (x0 + 150, y0 + 8), (x0 + 190, y0 + 8),
                  (x0 + 90, y1)], fill="#26355e")
    draw.polygon([(x1 - 60, y1), (x1 - 180, y0 + 14), (x1 - 150, y0 + 14),
                  (x1 - 20, y1)], fill="#1e2c4e")
    # drones with red lights
    for dx, dy in [(120, 26), (200, 18), (260, 34)]:
        draw.ellipse([x0 + dx - 3, y0 + dy - 3, x0 + dx + 3, y0 + dy + 3],
                     fill="#111827", outline="#f87171", width=1)
        draw.ellipse([x0 + dx - 1, y0 + dy - 1, x0 + dx + 1, y0 + dy + 1],
                     fill="#ef4444")
    # skyline, one block collapsed in the middle
    base = y1
    draw.rectangle([x0 + 8, base - 52, x0 + 118, base], fill="#1f2937")
    draw.rectangle([x0 + 210, base - 64, x0 + 320, base], fill="#1f2937")
    draw.polygon([(x0 + 118, base - 52), (x0 + 150, base - 30),
                  (x0 + 168, base - 44), (x0 + 210, base - 64),
                  (x0 + 210, base), (x0 + 118, base)], fill="#111827")
    # lit windows
    for wx in range(x0 + 18, x0 + 112, 16):
        for wy in range(base - 46, base - 6, 14):
            draw.rectangle([wx, wy, wx + 6, wy + 7], fill="#fbbf24")
    for wx in range(x0 + 220, x0 + 312, 16):
        for wy in range(base - 58, base - 6, 14):
            draw.rectangle([wx, wy, wx + 6, wy + 7], fill="#fbbf24")
    # fire glow at the collapse
    draw.polygon([(x0 + 140, base), (x0 + 156, base - 26), (x0 + 168, base - 8),
                  (x0 + 182, base - 22), (x0 + 196, base)],
                 fill="#f97316")
    draw.ellipse([x0 + 152, base - 34, x0 + 186, base - 6], fill="#f59e0b")


def scene_chip(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill="#052e16")
    # circuit traces
    for tx in range(x0 + 12, x1 - 12, 26):
        draw.line([(tx, y0 + 6), (tx, y1 - 6)], fill="#166534", width=2)
        draw.ellipse([tx - 3, y0 + 10, tx + 3, y0 + 16], fill="#22c55e")
        draw.ellipse([tx - 3, y1 - 16, tx + 3, y1 - 10], fill="#22c55e")
    for ty in range(y0 + 14, y1 - 10, 30):
        draw.line([(x0 + 6, ty), (x1 - 6, ty)], fill="#14532d", width=2)
    # rising chart arrow
    pts = [(x0 + 22, y1 - 30), (x0 + 90, y1 - 52), (x0 + 150, y1 - 44),
           (x0 + 220, y1 - 78), (x0 + 300, y1 - 96)]
    draw.line(pts, fill="#4ade80", width=4)
    draw.polygon([(x0 + 300, y1 - 96), (x0 + 284, y1 - 92), (x0 + 296, y1 - 78)],
                 fill="#4ade80")
    # chip
    cx0, cy0, cx1, cy1 = x0 + 118, y0 + 34, x0 + 210, y0 + 96
    draw.rectangle([cx0, cy0, cx1, cy1], fill="#16a34a", outline="#bbf7d0",
                   width=3)
    for px in range(cx0 + 12, cx1 - 8, 16):
        draw.line([(px, cy0 - 8), (px, cy0)], fill="#bbf7d0", width=3)
        draw.line([(px, cy1), (px, cy1 + 8)], fill="#bbf7d0", width=3)
    for py in range(cy0 + 12, cy1 - 8, 16):
        draw.line([(cx0 - 8, py), (cx0, py)], fill="#bbf7d0", width=3)
        draw.line([(cx1, py), (cx1 + 8, py)], fill="#bbf7d0", width=3)
    draw.text((cx0 + 26, cy0 + 20), "NVDA", font=F_BOLD(15), fill=WHITE)
    draw.text((x0 + 12, y0 + 8), "+30% PREMARKET", font=F_BOLD(10),
              fill="#bbf7d0")


SCENES = {"tanker": scene_tanker, "kyiv": scene_kyiv, "chip": scene_chip}


def tile_art(draw, box, kind, colour):
    """Small illustrated strip for a tile: tinted ground + simple icon."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=colour)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    white, dark = "#ffffff", "#1f2937"
    if kind == "gavel":  # COP31: gavel over a broken deal
        draw.rectangle([cx - 34, cy - 4, cx + 10, cy + 6], fill=dark)
        draw.line([(cx + 8, cy - 2), (cx + 34, cy - 12)], fill=dark, width=4)
        draw.line([(cx - 30, cy + 10), (cx + 30, cy + 10)], fill=white, width=3)
    elif kind == "ship":
        draw.polygon([(cx - 36, cy + 2), (cx + 36, cy + 2), (cx + 26, cy + 12),
                      (cx - 26, cy + 12)], fill=dark)
        draw.rectangle([cx - 8, cy - 12, cx + 2, cy + 2], fill=dark)
        draw.line([(x0 + 6, cy + 15), (x1 - 6, cy + 15)], fill=white, width=2)
    elif kind == "flame":
        draw.polygon([(cx, cy - 14), (cx + 12, cy + 2), (cx + 6, cy + 12),
                      (cx - 6, cy + 12), (cx - 12, cy + 2)], fill="#ea580c")
        draw.polygon([(cx, cy - 4), (cx + 6, cy + 6), (cx - 6, cy + 6)],
                     fill="#fde68a")
    elif kind == "capitol":
        draw.pieslice([cx - 14, cy - 16, cx + 14, cy + 4], 180, 360, fill=dark)
        draw.rectangle([cx - 20, cy + 2, cx + 20, cy + 6], fill=dark)
        for ox in (-16, -6, 4, 14):
            draw.rectangle([cx + ox, cy + 6, cx + ox + 4, cy + 14], fill=dark)
        draw.rectangle([cx - 24, cy + 14, cx + 24, cy + 16], fill=dark)
    elif kind == "handshake":  # agreement document + check
        draw.rectangle([cx - 22, cy - 13, cx + 22, cy + 13], fill=white,
                       outline=dark, width=2)
        draw.line([(cx - 14, cy - 6), (cx + 6, cy - 6)], fill=dark, width=2)
        draw.line([(cx - 14, cy), (cx + 2, cy)], fill=dark, width=2)
        draw.line([(cx + 2, cy + 8), (cx + 8, cy + 12)], fill="#15803d",
                  width=3)
        draw.line([(cx + 8, cy + 12), (cx + 18, cy - 2)], fill="#15803d",
                  width=3)
    elif kind == "aid":
        draw.rectangle([cx - 24, cy - 10, cx + 24, cy + 12], fill=white,
                       outline=dark, width=2)
        draw.rectangle([cx - 4, cy - 7, cx + 4, cy + 9], fill=RED)
        draw.rectangle([cx - 11, cy, cx + 11, cy + 2], fill=RED)
    elif kind == "court":
        draw.line([(cx, cy - 13), (cx, cy + 13)], fill=dark, width=3)
        draw.line([(cx - 20, cy - 10), (cx + 20, cy - 10)], fill=dark, width=3)
        draw.polygon([(cx - 26, cy - 8), (cx - 14, cy - 8), (cx - 20, cy + 2)],
                     fill=dark)
        draw.polygon([(cx + 14, cy - 8), (cx + 26, cy - 8), (cx + 20, cy + 2)],
                     fill=dark)
    elif kind == "constitution":
        draw.rectangle([cx - 18, cy - 13, cx + 18, cy + 13], fill=white,
                       outline=dark, width=2)
        for ly in (-7, -1, 5):
            draw.line([(cx - 12, cy + ly), (cx + 12, cy + ly)], fill=dark,
                      width=2)
        draw.ellipse([cx + 8, cy + 6, cx + 18, cy + 16], fill=GOLD,
                     outline=dark, width=1)
    elif kind == "phone":
        draw.rounded_rectangle([cx - 12, cy - 14, cx + 12, cy + 14], radius=4,
                               fill=dark)
        draw.rectangle([cx - 7, cy - 9, cx + 7, cy + 8], fill=white)
        draw.line([(cx - 18, cy + 14), (cx + 18, cy - 14)], fill=RED, width=4)
    elif kind == "virus":
        draw.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill="#7c3aed")
        for ang in range(0, 360, 45):
            import math
            dx = math.cos(math.radians(ang)) * 14
            dy = math.sin(math.radians(ang)) * 14
            draw.line([(cx, cy), (cx + dx, cy + dy)], fill="#7c3aed", width=3)


# --- world map ---------------------------------------------------------------
CONTINENTS = [
    # North America
    [(-168, 66), (-150, 70), (-130, 71), (-110, 72), (-95, 80), (-82, 73),
     (-65, 62), (-55, 47), (-65, 44), (-75, 35), (-81, 31), (-90, 21),
     (-97, 16), (-105, 20), (-112, 29), (-120, 34), (-125, 42), (-125, 49),
     (-140, 60), (-158, 58), (-168, 66)],
    # Greenland
    [(-55, 60), (-42, 64), (-30, 68), (-22, 74), (-32, 78), (-55, 80),
     (-60, 74), (-55, 60)],
    # South America
    [(-80, 10), (-62, 11), (-52, 5), (-44, -3), (-35, -8), (-38, -15),
     (-41, -23), (-48, -28), (-57, -35), (-65, -41), (-70, -52), (-73, -44),
     (-73, -30), (-77, -18), (-80, -5), (-80, 10)],
    # Africa
    [(-17, 15), (-10, 31), (-5, 35), (10, 37), (20, 32), (30, 31), (35, 28),
     (43, 12), (51, 11), (48, 1), (40, -10), (35, -18), (32, -26), (26, -34),
     (19, -35), (15, -27), (12, -18), (9, 4), (-8, 5), (-17, 15)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 48), (2, 51), (5, 53), (8, 57), (10, 59),
     (6, 62), (12, 56), (18, 56), (21, 55), (24, 59), (28, 60), (25, 65),
     (30, 70), (40, 68), (44, 64), (40, 58), (35, 54), (30, 50), (28, 46),
     (23, 40), (19, 42), (13, 44), (8, 44), (3, 43), (-2, 37), (-10, 36)],
    # Asia
    [(30, 70), (45, 69), (60, 70), (75, 72), (90, 75), (105, 77), (120, 74),
     (135, 72), (150, 70), (162, 66), (170, 66), (178, 65), (170, 60),
     (162, 56), (156, 52), (150, 59), (142, 50), (140, 40), (135, 35),
     (130, 33), (127, 36), (122, 39), (120, 32), (115, 23), (110, 20),
     (108, 12), (103, 8), (100, 6), (97, 10), (94, 16), (92, 21), (89, 22),
     (86, 20), (80, 14), (77, 8), (75, 13), (72, 20), (68, 23), (64, 25),
     (60, 25), (56, 27), (52, 28), (50, 30), (46, 30), (42, 31), (39, 33),
     (36, 36), (33, 36), (30, 36), (28, 38), (27, 41), (28, 45), (30, 50),
     (30, 60), (30, 70)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (120, -34), (125, -32), (130, -32),
     (135, -35), (140, -38), (145, -38), (150, -37), (153, -32), (153, -27),
     (150, -23), (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
     (132, -12), (130, -13), (126, -14), (122, -17), (118, -20), (113, -22)],
    # New Zealand
    [(167, -45), (170, -43), (174, -41), (177, -38), (175, -37), (173, -35),
     (170, -40), (167, -45)],
]

PIN_OFFSETS = {4: (-24, -14), 5: (-26, -13), 9: (18, 14), 11: (17, 12)}


def project(lon, lat, mx0, my0, mx1, my1):
    x = mx0 + (lon + 180.0) / 360.0 * (mx1 - mx0)
    y = my0 + (75.0 - lat) / 135.0 * (my1 - my0)
    return x, y


# --- poster ------------------------------------------------------------------
def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead -----------------------------------------------------------
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.rectangle([0, 97, W, 100], fill=GOLD)
    d.text((14, 8), "THE WORLD IN ONE DAY", font=F_TITLE(40), fill=WHITE)
    d.text((14, 58), "MONDAY  23  NOVEMBER  2026", font=F_BOLD(21),
           fill=GOLD)
    right = "36 STORIES  ·  9 REGIONS  ·  EVERY ONE DATED"
    tw = text_w(d, right, F_BOLD(13))
    d.text((W - 14 - tw, 16), right, font=F_BOLD(13), fill="#cbd5e1")
    right2 = "MONDAY 23 NOVEMBER 2026"
    tw2 = text_w(d, right2, F_REG(12))
    d.text((W - 14 - tw2, 62), right2, font=F_REG(12), fill="#cbd5e1")

    # ---- subtitle strip: the three hero headlines ---------------------------
    d.rectangle([0, 100, W, 122], fill="#e9e2d2")
    heroes_line = "  ·  ".join(
        "%d  %s" % (n, h) for n, _p, _r, _k, h, _b, _s, _st, _a in data.HEROES)
    # shorten: use headline text only, wrapped to one line at 12px
    f_sub = F_BOLD(12)
    parts = []
    for n, _p, _r, _k, h, _b, _s, _st, _a in data.HEROES:
        parts.append("%d %s" % (n, h))
    line = "   ·   ".join(parts)
    while text_w(d, line, f_sub) > W - 24 and len(parts) > 0:
        # trim the longest headline word by word from the end
        longest = max(range(len(parts)), key=lambda i: len(parts[i]))
        words = parts[longest].split()
        parts[longest] = " ".join(words[:-1]) + "…"
        line = "   ·   ".join(parts)
    d.text((12, 105), line, font=f_sub, fill=NAVY)

    # ---- six big numbers ------------------------------------------------------
    y0, y1 = 122, 172
    cw = W / 6
    for i, (num, label) in enumerate(data.BIG_NUMBERS):
        x = i * cw
        d.rectangle([x, y0, x + cw, y1], outline=LINE, width=1)
        d.text((x + cw / 2 - text_w(d, num, F_BOLD(28)) / 2, y0 + 2),
               num, font=F_BOLD(28), fill=NAVY)
        for j, lab in enumerate(label.split("\n")):
            d.text((x + cw / 2 - text_w(d, lab, F_REG(8)) / 2, y0 + 31 + j * 9),
                   lab, font=F_REG(8), fill=MUTED)

    # ---- region strip ---------------------------------------------------------
    y0, y1 = 172, 200
    total_w = W
    # widths proportional to count, min 60
    raw = [c for _n, c, _col in data.REGIONS]
    widths = [max(64, total_w * c / data.TOTAL_STORIES) for c in raw]
    scale = total_w / sum(widths)
    widths = [w * scale for w in widths]
    x = 0
    for (name, count, colour), w in zip(data.REGIONS, widths):
        d.rectangle([x, y0, x + w, y1], fill=colour)
        label = "%s %d" % (name, count)
        fnt = F_BOLD(11)
        while text_w(d, label, fnt) > w - 8 and fnt.size > 8:
            fnt = F_BOLD(fnt.size - 1)
        d.text((x + w / 2 - text_w(d, label, fnt) / 2, y0 + 9),
               label, font=fnt, fill=WHITE)
        x += w

    # ---- heroes ---------------------------------------------------------------
    hx0, hy0, hy1 = 10, 206, 428
    hgap = 8
    hw = (W - 20 - 2 * hgap) / 3
    for i, (n, place, region, kicker, headline, body, src, status,
            art) in enumerate(data.HEROES):
        x = hx0 + i * (hw + hgap)
        col = data.REGION_COLOUR[region]
        d.rectangle([x, hy0, x + hw, hy1], outline=col, width=2)
        d.rectangle([x, hy0, x + hw, hy0 + 22], fill=col)
        d.text((x + 8, hy0 + 4), kicker, font=F_BOLD(11), fill=WHITE)
        num_chip(d, x + hw - 18, hy0 + 118, n, r=13)
        SCENES[art](d, (int(x + 2), hy0 + 22, int(x + hw - 2), hy0 + 118))
        d.text((x + 8, hy0 + 122), place, font=F_BOLD(10), fill=MUTED)
        hl = wrap(d, headline, F_BOLD(15), hw - 16)
        y = draw_lines(d, hl[:2], x + 8, hy0 + 136, F_BOLD(15), INK, 17)
        bl = wrap(d, body, F_REG(10), hw - 16)
        draw_lines(d, bl[:3], x + 8, y + 2, F_REG(10), "#2b3442", 12)
        d.text((x + 8, hy1 - 14), "Source: " + src, font=F_REG(9),
               fill=MUTED)
        status_pill(d, x + hw - 78, hy1 - 15, status)

    # ---- tiles 4-13 -------------------------------------------------------------
    tx0, ty0 = 10, 436
    tgap = 6
    tw = (W - 20 - 4 * tgap) / 5
    th = 102
    for i, (n, place, region, headline, body, src, status,
            art) in enumerate(data.TILES):
        row, col_i = divmod(i, 5)
        x = tx0 + col_i * (tw + tgap)
        y = ty0 + row * (th + 6)
        colour = data.REGION_COLOUR[region]
        d.rectangle([x, y, x + tw, y + th], outline=LINE, width=1,
                    fill=WHITE)
        tile_art(d, (x + 1, y + 1, x + tw - 1, y + 33), art,
                 "#eef2f7" if region != "GLOBAL" else "#eceff4")
        num_chip(d, x + 16, y + 17, n, r=10)
        d.text((x + 30, y + 4), place, font=F_BOLD(8), fill=MUTED)
        hl = wrap(d, headline, F_BOLD(11), tw - 12)
        yy = draw_lines(d, hl[:2], x + 6, y + 37, F_BOLD(11), INK, 13)
        bl = wrap(d, body, F_REG(9), tw - 12)
        draw_lines(d, bl[:2], x + 6, yy + 1, F_REG(9), "#2b3442", 11)
        d.text((x + 6, y + th - 13), src, font=F_REG(8), fill=MUTED)
        status_pill(d, x + tw - 66, y + th - 14, status)

    # ---- timeline ---------------------------------------------------------------
    y0, y1 = 650, 676
    d.rectangle([0, y0, W, y1], fill=NAVY2)
    d.text((10, y0 + 7), "THE DAY IN UTC", font=F_BOLD(11), fill=GOLD)
    seg_w = (W - 150) / len(data.TIMELINE)
    for i, (when, what) in enumerate(data.TIMELINE):
        x = 150 + i * seg_w
        d.text((x + 4, y0 + 3), when, font=F_BOLD(9), fill=GOLD)
        d.text((x + 4, y0 + 14), what, font=F_REG(8), fill=WHITE)
        if i:
            d.line([(x, y0 + 3), (x, y1 - 3)], fill="#3b4a6b", width=1)

    # ---- world map ---------------------------------------------------------------
    y0, y1 = 676, 788
    d.rectangle([0, y0, W, y1], fill="#f1ecdd")
    d.text((10, y0 + 4), "WHERE IT HAPPENED", font=F_BOLD(12), fill=NAVY)
    d.text((W - 10 - text_w(d, "Pin colour = region  ·  number = story",
                            F_REG(9)), y0 + 5),
           "Pin colour = region  ·  number = story", font=F_REG(9),
           fill=MUTED)
    mx0, my0, mx1, my1 = 14, y0 + 22, W - 14, y1 - 4
    for poly in CONTINENTS:
        pts = [project(lon, lat, mx0, my0, mx1, my1) for lon, lat in poly]
        d.polygon(pts, fill="#cfe0c0", outline="#8aa87a")
    for n, lon, lat in data.PINS:
        px, py = project(lon, lat, mx0, my0, mx1, my1)
        region = data.STORY_REGION[n]
        col = data.REGION_COLOUR[region]
        ox, oy = PIN_OFFSETS.get(n, (0, 0))
        bx, by = px + ox, py + oy
        if (ox, oy) != (0, 0):
            d.line([(px, py), (bx, by)], fill=col, width=2)
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=col)
        num_chip(d, bx, by, n, r=8, fill=col)

    # ---- ALSO ON ------------------------------------------------------------------
    y0, y1 = 788, 908
    d.rectangle([0, y0, W, y1], fill=WHITE)
    d.text((10, y0 + 4), "ALSO ON MONDAY 23 NOVEMBER — 23 MORE STORIES",
           font=F_BOLD(12), fill=NAVY)
    cols = [data.BRIEFS[i::3] for i in range(3)]
    # regroup into 3 columns of 8/8/7 in order
    cols = [data.BRIEFS[0:8], data.BRIEFS[8:16], data.BRIEFS[16:23]]
    col_w = (W - 20) / 3
    for ci, items in enumerate(cols):
        x = 10 + ci * col_w
        y = y0 + 22
        for n, region, text in items:
            col = data.REGION_COLOUR[region]
            d.ellipse([x, y + 1, x + 8, y + 9], fill=col)
            d.text((x + 12, y), "%d. %s" % (n, text), font=F_REG(9),
                   fill=INK)
            y += 12

    # ---- DATE CHECK -----------------------------------------------------------------
    y0, y1 = 908, 984
    d.rectangle([0, y0, W, y1], fill="#fdf3e3")
    d.line([(0, y0), (W, y0)], fill=AMBER, width=2)
    d.text((10, y0 + 4), "DATE CHECK — LEFT OUT ON PURPOSE",
           font=F_BOLD(11), fill="#92400e")
    left = "  ·  ".join("%s (%s)" % (name, when)
                        for name, when in data.DATE_CHECK_LEFT_OUT)
    ll = wrap(d, left, F_REG(9), 600)
    draw_lines(d, ll[:3], 10, y0 + 20, F_REG(9), "#44403c", 12)
    d.line([(640, y0 + 6), (640, y1 - 6)], fill=AMBER, width=1)
    d.text((652, y0 + 4), "NOT YET", font=F_BOLD(11), fill="#92400e")
    ny = "  ·  ".join(data.DATE_CHECK_NOT_YET)
    nl = wrap(d, ny, F_REG(9), W - 652 - 12)
    draw_lines(d, nl[:3], 652, y0 + 20, F_REG(9), "#44403c", 12)

    # ---- footer -----------------------------------------------------------------------
    y0 = 984
    d.rectangle([0, y0, W, H], fill=NAVY)
    d.text((W / 2 - text_w(d, "Every story here happened, or was first "
                            "reported, on Monday 23 November 2026",
                            F_BOLD(12)) / 2, y0 + 6),
           "Every story here happened, or was first reported, on Monday "
           "23 November 2026", font=F_BOLD(12), fill=WHITE)
    d.text((W / 2 - text_w(d, "Sources named beside each story  ·  "
                            "Original drawings", F_REG(10)) / 2, y0 + 23),
           "Sources named beside each story  ·  Original drawings",
           font=F_REG(10), fill="#cbd5e1")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    build()
