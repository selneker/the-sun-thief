#!/usr/bin/env python3
"""The Sun Thief - generative vector artwork (SVG, 1024x1024), fully deterministic.

A child on a ladder cuts a slice out of the sun with a pair of shears.
Behind the missing slice lies the night: a galaxy waits inside the wound.
The stolen slice tumbles away, still burning.
"""
import math
import random

W = H = 1024
rnd = random.Random(20261113)
out = []
A = out.append


def f(v):
    return f"{v:.2f}"


def pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


SCX, SCY, SR = 690.0, 350.0, 335.0     # sun centre and radius
MA0, MA1 = 122.0, 167.0                # the cut: a 45 degree slice
CHILD = (398.0, 540.0)                 # where the child stands

# ---------------------------------------------------------------- geometry
p0 = pt(SCX, SCY, SR + 1, MA0)
p1 = pt(SCX, SCY, SR + 1, MA1)
CUT_D = (f'M{f(SCX)} {f(SCY)} L{f(p0[0])} {f(p0[1])} '
         f'A{f(SR+1)} {f(SR+1)} 0 0 1 {f(p1[0])} {f(p1[1])} Z')


def face_y(x):
    """y of the lower cut face (centre -> lower mouth corner) at a given x."""
    return SCY + (x - SCX) * (p1[1] - SCY) / (p1[0] - SCX)


A(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0.35" y2="1">
    <stop offset="0" stop-color="#03040c"/>
    <stop offset="0.42" stop-color="#0a0820"/>
    <stop offset="0.78" stop-color="#160c2b"/>
    <stop offset="1" stop-color="#241141"/>
  </linearGradient>
  <radialGradient id="neb1" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#6a2f92" stop-opacity="0.34"/>
    <stop offset="1" stop-color="#6a2f92" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="neb2" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#0d4f6b" stop-opacity="0.32"/>
    <stop offset="1" stop-color="#0d4f6b" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="sun" cx="0.38" cy="0.32" r="0.76">
    <stop offset="0" stop-color="#fffdf2"/>
    <stop offset="0.13" stop-color="#fff6cd"/>
    <stop offset="0.36" stop-color="#ffd166"/>
    <stop offset="0.62" stop-color="#ff9f2e"/>
    <stop offset="0.84" stop-color="#ee6a15"/>
    <stop offset="1" stop-color="#c04307"/>
  </radialGradient>
  <radialGradient id="limb" cx="0.40" cy="0.34" r="0.72">
    <stop offset="0.42" stop-color="#7d2403" stop-opacity="0"/>
    <stop offset="0.82" stop-color="#7d2403" stop-opacity="0.22"/>
    <stop offset="1" stop-color="#4d1300" stop-opacity="0.62"/>
  </radialGradient>
  <radialGradient id="sunbloom" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#ffb347" stop-opacity="0.40"/>
    <stop offset="0.55" stop-color="#ff8a1e" stop-opacity="0.14"/>
    <stop offset="1" stop-color="#ff7a10" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="sunbloom2" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#ffe0a4" stop-opacity="0.38"/>
    <stop offset="1" stop-color="#ffb347" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="hole" cx="0.34" cy="0.36" r="0.9">
    <stop offset="0" stop-color="#140f2c"/>
    <stop offset="0.55" stop-color="#09071a"/>
    <stop offset="1" stop-color="#03030a"/>
  </radialGradient>
  <linearGradient id="slice" x1="0.18" y1="0.05" x2="0.82" y2="1">
    <stop offset="0" stop-color="#fffdf0"/>
    <stop offset="0.18" stop-color="#ffe9a6"/>
    <stop offset="0.46" stop-color="#ffbf4d"/>
    <stop offset="0.74" stop-color="#ff7d1c"/>
    <stop offset="0.92" stop-color="#d94c0b"/>
    <stop offset="1" stop-color="#8f2c04"/>
  </linearGradient>
  <linearGradient id="steel" x1="0.1" y1="0" x2="0.9" y2="1">
    <stop offset="0" stop-color="#ffffff"/>
    <stop offset="0.35" stop-color="#cfd9ea"/>
    <stop offset="0.72" stop-color="#8b9bb4"/>
    <stop offset="1" stop-color="#e8effc"/>
  </linearGradient>
  <linearGradient id="steel2" x1="0" y1="0" x2="0.2" y2="1">
    <stop offset="0" stop-color="#eef3fc"/>
    <stop offset="0.4" stop-color="#9dabc2"/>
    <stop offset="0.75" stop-color="#5a6880"/>
    <stop offset="1" stop-color="#b9c6da"/>
  </linearGradient>
  <linearGradient id="hill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0c0a17"/>
    <stop offset="1" stop-color="#020105"/>
  </linearGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#2a1a14"/>
    <stop offset="0.55" stop-color="#4a2c1c"/>
    <stop offset="1" stop-color="#1c110d"/>
  </linearGradient>
  <radialGradient id="vig" cx="0.50" cy="0.42" r="0.80">
    <stop offset="0.48" stop-color="#000000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000000" stop-opacity="0.70"/>
  </radialGradient>
  <radialGradient id="gcore" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#fffdf0"/>
    <stop offset="0.35" stop-color="#ffe9b8"/>
    <stop offset="0.75" stop-color="#9fb4ff" stop-opacity="0.45"/>
    <stop offset="1" stop-color="#9fb4ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="gglow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#b9c9ff" stop-opacity="0.34"/>
    <stop offset="1" stop-color="#b9c9ff" stop-opacity="0"/>
  </radialGradient>
  <filter id="blur1" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="1"/></filter>
  <filter id="blur2" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="2"/></filter>
  <filter id="blur4" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="blur8" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="8"/></filter>
  <filter id="blur14" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="14"/></filter>
  <filter id="blur26" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="26"/></filter>
  <filter id="glow2" x="-70%" y="-70%" width="240%" height="240%">
    <feGaussianBlur stdDeviation="2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow5" x="-70%" y="-70%" width="240%" height="240%">
    <feGaussianBlur stdDeviation="5" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow9" x="-70%" y="-70%" width="240%" height="240%">
    <feGaussianBlur stdDeviation="9" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="suntex" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.009 0.015" numOctaves="5" seed="11" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.66  0 0 0 0 0.28  0 0 0 0 0.04  0.75 0.75 0.75 0 0"/>
  </filter>
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="7" stitchTiles="stitch" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0.55 0.55 0.55 0 0"/>
  </filter>
  <clipPath id="sunclip"><circle cx="{f(SCX)}" cy="{f(SCY)}" r="{f(SR)}"/></clipPath>
  <clipPath id="cutclip"><path d="{CUT_D}"/></clipPath>
</defs>
''')

# ================================================================ night sky
A(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
A('<ellipse cx="230" cy="250" rx="440" ry="340" fill="url(#neb1)"/>')
A('<ellipse cx="900" cy="840" rx="440" ry="320" fill="url(#neb2)"/>')

# milky way band
A('<g opacity="0.95">')
A('<path d="M-90 150 C 190 250 330 520 530 700 C 700 856 890 940 1110 980 L1110 1130 C 830 1060 620 940 440 760 C 250 570 110 330 -90 280 Z" fill="#4a3477" opacity="0.20" filter="url(#blur26)"/>')
A('<path d="M-70 210 C 210 300 350 545 550 715 C 730 866 910 940 1110 995 L1110 1045 C 890 990 700 902 520 742 C 330 574 180 340 -70 290 Z" fill="#7c5aa8" opacity="0.11" filter="url(#blur26)"/>')
for _ in range(320):
    t = rnd.random()
    x = -70 + 1180 * t + rnd.uniform(-95, 95)
    y = 210 + 780 * t + rnd.uniform(-75, 75) - 390 * math.sin(t * 3.1)
    A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(0.3,1.15))}" fill="#e6eaff" opacity="{f(rnd.uniform(0.05,0.30))}"/>')
A('</g>')

# stars
A('<g id="stars">')
for _ in range(230):
    x, y = rnd.uniform(0, W), rnd.uniform(0, H)
    if (x - SCX) ** 2 + (y - SCY) ** 2 < (SR + 10) ** 2:
        continue
    r = rnd.choice([0.45, 0.6, 0.75, 0.9, 1.1, 1.4, 1.7])
    o = rnd.uniform(0.20, 0.95)
    col = rnd.choice(["#ffffff", "#ffe9c4", "#cfd8ff", "#ffffff", "#ffffff", "#ffd9b0"])
    A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{r}" fill="{col}" opacity="{f(o)}"/>')
for (x, y, r) in [(120, 210, 2.6), (860, 120, 2.1), (250, 690, 1.9), (975, 610, 2.3),
                  (70, 480, 1.8), (640, 70, 2.0), (170, 880, 1.6), (455, 120, 1.5)]:
    A(f'<g opacity="0.92"><circle cx="{x}" cy="{y}" r="{f(r*3.4)}" fill="#ffe9b0" opacity="0.15" filter="url(#blur4)"/>'
      f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffdf2"/>'
      f'<path d="M{f(x-r*7)} {f(y)} H{f(x+r*7)} M{f(x)} {f(y-r*7)} V{f(y+r*7)}" stroke="#fff6d8" stroke-width="0.8" opacity="0.65"/></g>')
A('</g>')

# a comet, thin and cold
A('<g opacity="0.85">')
A('<path d="M905 690 C 940 730 975 765 1010 800" stroke="#9fd0ff" stroke-width="2.2" fill="none" opacity="0.35" filter="url(#blur2)"/>')
A('<path d="M905 690 C 940 730 975 765 1010 800" stroke="#eaf4ff" stroke-width="1.1" fill="none" opacity="0.75"/>')
A('<circle cx="905" cy="690" r="3.4" fill="#ffffff"/>')
A('<circle cx="905" cy="690" r="9" fill="#cfe6ff" opacity="0.35" filter="url(#blur4)"/>')
A('</g>')

# ============================================================ solar corona
A(f'<circle cx="{f(SCX)}" cy="{f(SCY)}" r="600" fill="url(#sunbloom)"/>')
A(f'<circle cx="{f(SCX)}" cy="{f(SCY)}" r="440" fill="url(#sunbloom2)" filter="url(#blur26)"/>')

# ================================================================ the sun
A(f'<circle cx="{f(SCX)}" cy="{f(SCY)}" r="{f(SR)}" fill="url(#sun)" filter="url(#glow9)"/>')
A(f'<g clip-path="url(#sunclip)">')
A(f'<circle cx="{f(SCX)}" cy="{f(SCY)}" r="{f(SR)}" fill="url(#limb)"/>')

# convection cells
for _ in range(54):
    a = rnd.uniform(0, 360)
    rr = math.sqrt(rnd.uniform(0.02, 0.98))
    x, y = pt(SCX, SCY, SR * rr, a)
    rad = rnd.uniform(4, 13)
    col = rnd.choice(["#fff0b4", "#ffca62", "#c74a08"])
    A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rad)}" fill="{col}" opacity="{f(rnd.uniform(0.03,0.08))}" filter="url(#blur2)"/>')
# fine granulation
for _ in range(900):
    a = rnd.uniform(0, 360)
    rr = math.sqrt(rnd.uniform(0.01, 1.0))
    x, y = pt(SCX, SCY, SR * rr, a)
    col = rnd.choice(["#fff2c0", "#ffd98a", "#c04a07", "#a83406", "#ffe9ac", "#ffb45c"])
    A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(0.7,2.4))}" fill="{col}" opacity="{f(rnd.uniform(0.04,0.11))}"/>')
# supergranulation lanes
for _ in range(26):
    a = rnd.uniform(0, 360)
    rr = math.sqrt(rnd.uniform(0.05, 0.95))
    x, y = pt(SCX, SCY, SR * rr, a)
    ln = rnd.uniform(40, 110)
    da = rnd.uniform(0, 360)
    x2, y2 = x + ln * math.cos(math.radians(da)), y + ln * math.sin(math.radians(da))
    A(f'<path d="M{f(x)} {f(y)} Q{f((x+x2)/2+rnd.uniform(-10,10))} {f((y+y2)/2+rnd.uniform(-10,10))} {f(x2)} {f(y2)}" '
      f'stroke="#b8480a" stroke-width="{f(rnd.uniform(0.5,1.1))}" fill="none" opacity="{f(rnd.uniform(0.05,0.11))}"/>')
# photospheric network
for _ in range(30):
    a = rnd.uniform(0, 360)
    rr = math.sqrt(rnd.uniform(0.05, 0.95))
    x, y = pt(SCX, SCY, SR * rr, a)
    A(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rnd.uniform(50,130))}" ry="{f(rnd.uniform(18,48))}" '
      f'fill="{rnd.choice(["#ffe6a0","#b23c06"])}" opacity="{f(rnd.uniform(0.03,0.06))}" '
      f'filter="url(#blur14)" transform="rotate({f(rnd.uniform(-30,30))} {f(x)} {f(y)})"/>')
A(f'<rect x="{f(SCX-SR)}" y="{f(SCY-SR)}" width="{f(2*SR)}" height="{f(2*SR)}" filter="url(#suntex)" opacity="0.19" style="mix-blend-mode:overlay"/>')
A('</g>')

# sunspot groups: umbra, penumbra with filaments, facular ring
def sunspot(a_deg, r_frac, size):
    x, y = pt(SCX, SCY, SR * r_frac, a_deg)
    A(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(size*1.55)}" ry="{f(size*1.18)}" fill="#ffd98f" opacity="0.16" filter="url(#blur8)"/>')
    A(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(size)}" ry="{f(size*0.78)}" fill="#8c2c04" opacity="0.34" filter="url(#blur4)"/>')
    for i in range(30):
        t = i / 29 * math.tau
        fx = x + math.cos(t) * size * 0.52
        fy = y + math.sin(t) * size * 0.40
        fx2 = x + math.cos(t + rnd.uniform(-0.25, 0.25)) * size * 1.0
        fy2 = y + math.sin(t + rnd.uniform(-0.25, 0.25)) * size * 0.78
        A(f'<line x1="{f(fx)}" y1="{f(fy)}" x2="{f(fx2)}" y2="{f(fy2)}" stroke="#6b1f02" '
          f'stroke-width="{f(rnd.uniform(0.7,1.6))}" opacity="{f(rnd.uniform(0.12,0.3))}"/>')
    A(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(size*0.52)}" ry="{f(size*0.40)}" fill="#431202" opacity="0.5" filter="url(#blur2)"/>')
    A(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(size*0.27)}" ry="{f(size*0.20)}" fill="#1b0500" opacity="0.55" filter="url(#blur1)"/>')


sunspot(52, 0.56, 34)
sunspot(303, 0.42, 24)
sunspot(243, 0.68, 20)
sunspot(15, 0.74, 15)

# prominences: loops of plasma standing off the limb
def prominence(a_deg, span, height, hue):
    a0 = a_deg - span / 2
    a1 = a_deg + span / 2
    x0, y0 = pt(SCX, SCY, SR - 4, a0)
    x1, y1 = pt(SCX, SCY, SR - 4, a1)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    ox, oy = pt(SCX, SCY, SR + height, a_deg)
    c1x = x0 + (ox - x0) * 0.55
    c1y = y0 + (oy - y0) * 0.55
    c2x = x1 + (ox - x1) * 0.55
    c2y = y1 + (oy - y1) * 0.55
    d = f'M{f(x0)} {f(y0)} C {f(c1x)} {f(c1y)} {f(c2x)} {f(c2y)} {f(x1)} {f(y1)}'
    A(f'<path d="{d}" fill="none" stroke="#ff4d10" stroke-width="{f(height*0.30)}" opacity="0.55" filter="url(#blur8)"/>')
    A(f'<path d="{d}" fill="none" stroke="{hue}" stroke-width="{f(height*0.16)}" opacity="0.85" filter="url(#blur2)"/>')
    A(f'<path d="{d}" fill="none" stroke="#fff0c4" stroke-width="{f(height*0.055)}" opacity="0.9" filter="url(#blur1)"/>')
    # plasma falling back to the limb
    for k in range(6):
        t = rnd.random()
        px = x0 + (x1 - x0) * t
        py = y0 + (y1 - y0) * t
        fx, fy = pt(SCX, SCY, SR + rnd.uniform(4, height * 0.8), a_deg + rnd.uniform(-span / 2, span / 2))
        A(f'<path d="M{f(px)} {f(py)} Q{f((px+fx)/2)} {f(min(py, fy)-12)} {f(fx)} {f(fy)}" '
          f'stroke="#ff7a26" stroke-width="{f(rnd.uniform(0.8,1.8))}" fill="none" opacity="{f(rnd.uniform(0.25,0.6))}"/>')


prominence(206, 34, 74, "#ff8a3a")
prominence(252, 26, 52, "#ff9440")
prominence(28, 30, 46, "#ff7f33")
prominence(88, 22, 40, "#ff9a52")

# limb light
A(f'<circle cx="{f(SCX)}" cy="{f(SCY)}" r="{f(SR-1)}" fill="none" stroke="#ffe3a1" stroke-width="2.6" opacity="0.80"/>')
A(f'<circle cx="{f(SCX)}" cy="{f(SCY)}" r="{f(SR-9)}" fill="none" stroke="#fff4cc" stroke-width="8" opacity="0.13" filter="url(#blur4)"/>')

# solar wind: streamers off the limb
A('<g>')
for _ in range(44):
    a = rnd.uniform(0, 360)
    if MA0 - 4 < a < MA1 + 4:
        continue
    ln = rnd.uniform(10, 40)
    x0, y0 = pt(SCX, SCY, SR - 2, a)
    x1, y1 = pt(SCX, SCY, SR + ln, a + rnd.uniform(-1.8, 1.8))
    A(f'<path d="M{f(x0)} {f(y0)} Q{f((x0+x1)/2+rnd.uniform(-9,9))} {f((y0+y1)/2+rnd.uniform(-9,9))} {f(x1)} {f(y1)}" '
      f'stroke="#ffcf7a" stroke-width="{f(rnd.uniform(0.7,1.9))}" fill="none" opacity="{f(rnd.uniform(0.05,0.15))}" stroke-linecap="round"/>')
A('</g>')

# ================================================== the wound in the sun
A(f'<path d="{CUT_D}" fill="url(#hole)"/>')
A(f'<g clip-path="url(#cutclip)">')
# deep space behind the shell
A(f'<path d="{CUT_D}" fill="#2a1650" opacity="0.55" filter="url(#blur14)"/>')
A(f'<path d="{CUT_D}" fill="#081036" opacity="0.60"/>')
# nebula in the wound
A(f'<ellipse cx="520" cy="520" rx="160" ry="130" fill="#3b2a8c" opacity="0.30" filter="url(#blur26)"/>')
A(f'<ellipse cx="640" cy="440" rx="100" ry="86" fill="#7a2a6a" opacity="0.24" filter="url(#blur26)"/>')
A(f'<ellipse cx="470" cy="430" rx="80" ry="70" fill="#1d4f8c" opacity="0.20" filter="url(#blur26)"/>')
# starfield inside the wound
for _ in range(90):
    x = rnd.uniform(360, 780)
    y = rnd.uniform(330, 660)
    A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(0.5,1.5))}" fill="#eaf1ff" opacity="{f(rnd.uniform(0.35,0.95))}"/>')
# the galaxy, folded into the gap
gx, gy = 548, 500
A(f'<ellipse cx="{gx}" cy="{f(gy)}" rx="80" ry="58" fill="url(#gglow)" transform="rotate(-24 {gx} {gy})"/>')
A(f'<ellipse cx="{gx}" cy="{f(gy)}" rx="66" ry="46" fill="#8fa6ff" opacity="0.18" filter="url(#blur14)" transform="rotate(-24 {gx} {gy})"/>')
A('<g transform="rotate(-24 %d %d)">' % (gx, gy))
for arm in (0, math.pi):
    pts = []
    for i in range(64):
        t = i / 63
        ang = arm + t * 3.45
        rr = 4 + 58 * t
        pts.append((gx + rr * math.cos(ang), gy + rr * math.sin(ang) * 0.52))
    for i in range(len(pts) - 1):
        t = i / (len(pts) - 1)
        A(f'<line x1="{f(pts[i][0])}" y1="{f(pts[i][1])}" x2="{f(pts[i+1][0])}" y2="{f(pts[i+1][1])}" '
          f'stroke="#dbe6ff" stroke-width="{f(5.4*(1-t)+0.6)}" opacity="{f(0.66*(1-t*0.5))}" stroke-linecap="round"/>')
        if i % 5 == 0:
            A(f'<line x1="{f(pts[i][0])}" y1="{f(pts[i][1])}" x2="{f(pts[i+1][0])}" y2="{f(pts[i+1][1])}" '
              f'stroke="#241648" stroke-width="{f(2.8*(1-t)+0.4)}" opacity="{f(0.34*(1-t*0.5))}" stroke-linecap="round"/>')
    for i in range(0, len(pts), 4):
        px, py = pts[i]
        A(f'<circle cx="{f(px)}" cy="{f(py)}" r="{f(rnd.uniform(0.6,1.6))}" fill="#ffffff" opacity="{f(rnd.uniform(0.45,1.0))}"/>')
        if rnd.random() < 0.45:
            A(f'<circle cx="{f(px)}" cy="{f(py)}" r="{f(rnd.uniform(2.4,3.8))}" fill="#ff9ec9" opacity="{f(rnd.uniform(0.28,0.55))}" filter="url(#blur2)"/>')
A(f'<circle cx="{gx}" cy="{gy}" r="26" fill="url(#gcore)"/>')
A(f'<circle cx="{gx}" cy="{gy}" r="8" fill="#fffdf5" opacity="0.95"/>')
A(f'<circle cx="{gx}" cy="{gy}" r="3.2" fill="#ffffff"/>')
A('</g>')
A('</g>')

# the shell's thickness, seen inside the wound: a hot inner wall
A(f'<g clip-path="url(#cutclip)">')
A(f'<path d="M{f(SCX)} {f(SCY)} L{f(p1[0])} {f(p1[1])}" stroke="#ff8a2a" stroke-width="26" opacity="0.55" filter="url(#blur8)"/>')
A(f'<path d="M{f(SCX)} {f(SCY)} L{f(p0[0])} {f(p0[1])}" stroke="#ff8a2a" stroke-width="22" opacity="0.45" filter="url(#blur8)"/>')
A(f'<path d="M{f(SCX)} {f(SCY)} L{f(p1[0])} {f(p1[1])}" stroke="#ffb35c" stroke-width="9" opacity="0.55" filter="url(#blur2)"/>')
A('</g>')

# molten rim of the cut
A(f'<path d="{CUT_D}" fill="none" stroke="#ff7a10" stroke-width="30" opacity="0.22" filter="url(#blur14)"/>')
A(f'<path d="{CUT_D}" fill="none" stroke="#ff9d2e" stroke-width="14" opacity="0.48" filter="url(#blur4)"/>')
A(f'<path d="{CUT_D}" fill="none" stroke="#ffc46b" stroke-width="5.5" opacity="0.90"/>')
A(f'<path d="{CUT_D}" fill="none" stroke="#fffbe8" stroke-width="2.2" opacity="0.95"/>')
# cool galaxy-light catching the far edge of the wound
A(f'<path d="M{f(SCX)} {f(SCY)} L{f(p0[0])} {f(p0[1])}" stroke="#8fb2ff" stroke-width="4" opacity="0.35" filter="url(#blur2)"/>')
A(f'<path d="M{f(SCX)} {f(SCY)} L{f(p1[0])} {f(p1[1])}" stroke="#8fb2ff" stroke-width="3" opacity="0.22" filter="url(#blur2)"/>')

# molten drips running out of the wound, along the upper cut face
A('<g filter="url(#glow2)">')
_fx, _fy = p1[0] - SCX, p1[1] - SCY
_fl = math.hypot(_fx, _fy)
_ux, _uy = _fx / _fl, _fy / _fl
_px, _py = _uy, -_ux           # perpendicular, into the wound
for _ in range(16):
    t = rnd.uniform(0.25, 0.98)
    x = SCX + _ux * _fl * t
    y = SCY + _uy * _fl * t
    ln = rnd.uniform(5, 19)
    A(f'<path d="M{f(x)} {f(y)} q {f(_px*3)} {f(_py*3)} {f(_px*ln*0.6)} {f(_py*ln)}" stroke="#ffcf6e" '
      f'stroke-width="{f(rnd.uniform(0.9,1.9))}" fill="none" stroke-linecap="round" opacity="{f(rnd.uniform(0.3,0.75))}"/>')
A('</g>')

# ============================================ the stolen slice, drifting away
SX, SY = 208.0, 208.0
SRAD = 152.0
_sa = math.atan2(SY - SCY, SX - SCX)          # away from the sun
sa = _sa
sw = math.radians(45)
q0 = (SX + SRAD * math.cos(sa - sw / 2), SY + SRAD * math.sin(sa - sw / 2))
q1 = (SX + SRAD * math.cos(sa + sw / 2), SY + SRAD * math.sin(sa + sw / 2))
SL_D = f'M{f(SX)} {f(SY)} L{f(q0[0])} {f(q0[1])} A{f(SRAD)} {f(SRAD)} 0 0 1 {f(q1[0])} {f(q1[1])} Z'
A(f'<circle cx="{f(SX)}" cy="{f(SY)}" r="230" fill="#ff8f2e" opacity="0.16" filter="url(#blur26)"/>')
A(f'<circle cx="{f(SX)}" cy="{f(SY)}" r="120" fill="#ffc46b" opacity="0.13" filter="url(#blur14)"/>')
A(f'<g transform="rotate(27 {f(SX)} {f(SY)})">')
A(f'<g transform="translate(7 9)"><path d="{SL_D}" fill="#4a1501" opacity="0.85"/></g>')
A(f'<path d="{SL_D}" fill="url(#slice)" filter="url(#glow9)"/>')
A(f'<clipPath id="sliceclip"><path d="{SL_D}"/></clipPath>')
A('<g clip-path="url(#sliceclip)">')
for k in range(10):
    A(f'<path d="M{f(SX-70+k*14)} {f(SY-90)} L{f(SX-140+k*28)} {f(SY+150)}" stroke="#fff0b4" '
      f'stroke-width="{f(rnd.uniform(0.9,2.4))}" opacity="{f(rnd.uniform(0.07,0.22))}" stroke-linecap="round"/>')
for _ in range(90):
    x = rnd.uniform(SX - SRAD, SX + SRAD)
    y = rnd.uniform(SY - SRAD, SY + SRAD)
    if (x - SX) ** 2 + (y - SY) ** 2 < SRAD ** 2:
        A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(0.7,2.3))}" fill="{rnd.choice(["#fff2c0","#c04a07"])}" opacity="{f(rnd.uniform(0.05,0.13))}"/>')
A(f'<ellipse cx="{f(SX-40)}" cy="{f(SY-20)}" rx="46" ry="30" fill="#fff8dc" opacity="0.30" filter="url(#blur14)"/>')
A('</g>')
# the two cut faces, white hot
A(f'<line x1="{f(SX)}" y1="{f(SY)}" x2="{f(q0[0])}" y2="{f(q0[1])}" stroke="#fff4d6" stroke-width="3.4" opacity="0.92"/>')
A(f'<line x1="{f(SX)}" y1="{f(SY)}" x2="{f(q1[0])}" y2="{f(q1[1])}" stroke="#fff4d6" stroke-width="3.4" opacity="0.92"/>')
A(f'<line x1="{f(SX)}" y1="{f(SY)}" x2="{f(q0[0])}" y2="{f(q0[1])}" stroke="#ffb35c" stroke-width="9" opacity="0.45" filter="url(#blur2)"/>')
# the crust, along the outer arc
A(f'<path d="M{f(q0[0])} {f(q0[1])} A{f(SRAD)} {f(SRAD)} 0 0 1 {f(q1[0])} {f(q1[1])}" fill="none" stroke="#6b1d02" stroke-width="20" opacity="0.78"/>')
A(f'<path d="M{f(q0[0])} {f(q0[1])} A{f(SRAD)} {f(SRAD)} 0 0 1 {f(q1[0])} {f(q1[1])}" fill="none" stroke="#ffcf7a" stroke-width="2.4" opacity="0.8"/>')
A(f'<path d="M{f(q0[0])} {f(q0[1])} A{f(SRAD)} {f(SRAD)} 0 0 1 {f(q1[0])} {f(q1[1])}" fill="none" stroke="#ffd79a" stroke-width="1.2" opacity="0.45"/>')
# embers still falling off the crust
for (dx, dy, dl) in [(-96, -26, 22), (-70, -70, 30), (-30, -104, 18)]:
    A(f'<path d="M{f(SX+dx)} {f(SY+dy)} q2 {f(dl*0.6)} 0 {f(dl)}" stroke="#ffbe5c" stroke-width="2.6" fill="none" stroke-linecap="round" opacity="0.8"/>')
A('</g>')

# ember trail from the wound up to the drifting slice
A('<g filter="url(#glow2)">')
P0, P1, P2 = (515, 385), (420, 280), (SX + 14, SY + 6)
for i in range(80):
    t = i / 79
    bx = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
    by = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
    x = bx + math.sin(t * 7.1 + 1.2) * 16 * (1 - t * 0.3)
    y = by + math.cos(t * 4.8) * 12 * (1 - t * 0.4)
    r = rnd.uniform(0.5, 2.3) * (1 - 0.35 * t)
    o = rnd.uniform(0.3, 0.95) * (1 - 0.25 * t)
    A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{rnd.choice(["#ffe9b0","#ffd166","#ff9d2e","#fff6d8"])}" opacity="{f(o)}"/>')
A('</g>')
for (cx0, cy0, cr) in [(452, 452, 3.2), (410, 494, 2.2), (486, 508, 2.4), (388, 424, 1.8), (520, 560, 1.6)]:
    A(f'<path d="M{f(cx0)} {f(cy0-cr)} L{f(cx0+cr)} {f(cy0+cr*0.7)} L{f(cx0-cr*0.9)} {f(cy0+cr*0.5)} Z" '
      f'fill="#ffcf6e" opacity="0.85" transform="rotate({f(rnd.uniform(0,360))} {f(cx0)} {f(cy0)})"/>')

# ================================================================ the ground
# blurred grass in the near foreground, for depth
A('<g opacity="0.92" filter="url(#blur4)">')
for _ in range(26):
    x = rnd.uniform(690, 1040)
    y = rnd.uniform(1010, 1040)
    h = rnd.uniform(60, 190)
    lean = rnd.uniform(-40, 30)
    A(f'<path d="M{f(x)} {f(y)} q {f(lean*0.35)} {f(-h*0.55)} {f(lean)} {f(-h)}" stroke="#03020a" '
      f'stroke-width="{f(rnd.uniform(4,9))}" fill="none" stroke-linecap="round"/>')
A('</g>')
A(f'<path d="M0 1024 L0 962 C 110 928 205 940 292 922 C 380 904 462 940 556 958 C 700 984 848 970 1024 992 L1024 1024 Z" fill="url(#hill)"/>')
A('<path d="M0 962 C 110 928 205 940 292 922 C 380 904 462 940 556 958 C 700 984 848 970 1024 992" '
  'fill="none" stroke="#7a3b5e" stroke-width="1.6" opacity="0.5"/>')
# grass along the ridge
for _ in range(120):
    x = rnd.uniform(0, W)
    y = 960 + rnd.uniform(-6, 36)
    h = rnd.uniform(7, 30)
    lean = rnd.uniform(-9, 9)
    A(f'<path d="M{f(x)} {f(y)} q {f(lean*0.4)} {f(-h*0.6)} {f(lean)} {f(-h)}" stroke="#050410" '
      f'stroke-width="{f(rnd.uniform(1.1,2.5))}" fill="none" stroke-linecap="round"/>')

# bare trees on the far ridge, for depth
def tree(x, y, h, seed):
    r = random.Random(seed)
    A(f'<path d="M{f(x)} {f(y)} C {f(x+r.uniform(-2,2))} {f(y-h*0.35)} {f(x+r.uniform(-4,4))} {f(y-h*0.7)} {f(x+r.uniform(-6,6))} {f(y-h)}" '
      f'stroke="#03020a" stroke-width="{f(h*0.055)}" fill="none" stroke-linecap="round"/>')
    def limb(x0, y0, ang, ln, depth):
        if depth == 0:
            return
        x1 = x0 + math.cos(math.radians(ang)) * ln
        y1 = y0 - math.sin(math.radians(ang)) * ln
        A(f'<path d="M{f(x0)} {f(y0)} Q {f((x0+x1)/2+r.uniform(-3,3))} {f((y0+y1)/2)} {f(x1)} {f(y1)}" '
          f'stroke="#03020a" stroke-width="{f(max(1.0, depth*0.9))}" fill="none" stroke-linecap="round"/>')
        for s in (-1, 1):
            limb(x1, y1, ang + s * r.uniform(16, 40), ln * r.uniform(0.55, 0.75), depth - 1)
    for s in (-1, 1):
        limb(x, y - h * 0.72, 90 + s * r.uniform(22, 42), h * 0.26, 3)


tree(52, 936, 104, 5)
tree(108, 938, 82, 9)
tree(146, 934, 62, 13)
tree(908, 984, 68, 21)
tree(950, 986, 52, 33)

# the cottage with one lit window
A('<g transform="translate(112 918)">')
A('<path d="M0 46 L0 10 L23 -10 L46 10 L46 46 Z" fill="#050410"/>')
A('<path d="M-4 12 L23 -14 L50 12 L50 8 L23 -18 L-4 8 Z" fill="#0a0614"/>')
A('<rect x="9" y="25" width="11" height="12" fill="#ffb347" opacity="0.95"/>')
A('<rect x="9" y="25" width="11" height="12" fill="#ffb347" opacity="0.38" filter="url(#blur4)"/>')
A('<path d="M14.5 25 V37 M9 31 H20" stroke="#7a3c10" stroke-width="0.8" opacity="0.6"/>')
A('<path d="M23 -10 L23 3" stroke="#ffb35c" stroke-width="1.4" opacity="0.45"/>')
A('</g>')
A('<ellipse cx="127" cy="962" rx="70" ry="16" fill="#ff9d2e" opacity="0.10" filter="url(#blur14)"/>')

# ================================================================ the ladder
BX, BY = 168.0, 1004.0
TX, TY = 424.0, 500.0
A('<g stroke-linecap="round">')
A(f'<line x1="{f(BX)}" y1="{f(BY)}" x2="{f(TX)}" y2="{f(TY)}" stroke="#0b0813" stroke-width="14"/>')
A(f'<line x1="{f(BX+36)}" y1="{f(BY)}" x2="{f(TX+36)}" y2="{f(TY)}" stroke="#0b0813" stroke-width="14"/>')
A('</g>')
for i in range(1, 12):
    t = i / 12
    x0 = BX + (TX - BX) * t
    y0 = BY + (TY - BY) * t
    A(f'<line x1="{f(x0+3)}" y1="{f(y0)}" x2="{f(x0+35)}" y2="{f(y0-1)}" stroke="#0b0813" stroke-width="7.5"/>')
A('</g>' if False else '')
# sun-side highlight on the ladder
A(f'<line x1="{f(BX+36)}" y1="{f(BY)}" x2="{f(TX+36)}" y2="{f(TY)}" stroke="#ffb35c" stroke-width="1.8" opacity="0.5"/>')
for i in range(1, 12):
    t = i / 12
    x0 = BX + (TX - BX) * t + 35
    y0 = BY + (TY - BY) * t
    A(f'<line x1="{f(x0)}" y1="{f(y0)}" x2="{f(x0-1)}" y2="{f(y0-1)}" stroke="#ffb35c" stroke-width="1.5" opacity="0.36"/>')

# ================================================================= the child
A(f'<g transform="translate({f(CHILD[0])} {f(CHILD[1])}) scale(1.25) rotate(-4)">')
A('<g fill="#07060d">')
# back leg and boot
A('<path d="M-6 -46 L-15 -10 L-8 -8 L-1 -44 Z"/>')
A('<path d="M-16 -10 L-5 -8 L-4 2 L-18 2 Z"/>')
# front leg and boot
A('<path d="M3 -44 L11 -11 L18 -9 L11 -47 Z"/>')
A('<path d="M10 -11 L20 -8 L22 2 L8 2 Z"/>')
# the coat, flaring at the hem
A('<path d="M-10 -91 C -17 -73 -23 -53 -27 -38 L 21 -38 C 18 -54 15 -73 8 -92 C 2 -97 -3 -97 -10 -91 Z"/>')
# the hood, a smooth rounded cowl
A('<ellipse cx="1" cy="-115" rx="19" ry="21" transform="rotate(-10 1 -115)"/>')
# the cowl brim, folded forward
A('<path d="M11 -131 C 19 -127 24 -116 22 -106 C 17 -112 12 -118 7 -120 Z"/>')
# the scarf, blown away from the sun, hanging off the shoulder
A('<path d="M-12 -101 C -24 -97 -30 -86 -31 -72 C -33 -85 -26 -96 -14 -99 Z"/>')
A('<path d="M-30 -74 C -38 -71 -45 -73 -50 -80 C -43 -76 -36 -76 -29 -77 Z"/>')
# a satchel on the back
A('<path d="M-23 -85 C -33 -81 -35 -67 -29 -59 C -23 -53 -14 -55 -14 -62 L -16 -83 Z"/>')
A('<path d="M-9 -89 C -19 -77 -23 -67 -21 -59" stroke="#07060d" stroke-width="3.4" fill="none"/>')
# the left arm, down on the ladder
A('<path d="M-5 -88 C -13 -75 -17 -62 -17 -47 L -11 -46 C -11 -60 -7 -72 1 -80 Z"/>')
# the right arm, raised to the cut
A('<path d="M8 -93 C 20 -90 30 -84 38 -77 L 48 -88 C 38 -99 24 -105 10 -105 Z"/>')
A('</g>')
# a sliver of lit cheek inside the hood
A('<path d="M14 -123 C 19 -118 20 -111 18 -105 C 14 -109 12 -115 11 -120 Z" fill="#ffc46b" opacity="0.32"/>')
# the shears, biting the edge of the cut
A('<g transform="translate(50 -80) rotate(-45)">')
A('<path d="M2 -2 L54 -4.8 L56 -1.4 L3 2 Z" fill="url(#steel2)"/>')
A('<path d="M2 2 L54 4.8 L56 1.4 L3 -2 Z" fill="url(#steel2)" opacity="0.8"/>')
A('<path d="M54 -4.8 L62 -5.8 L63 -2.2 L56 -1.4 Z" fill="#dfe8f6"/>')
A('<path d="M54 4.8 L62 5.8 L63 2.2 L56 1.4 Z" fill="#93a1b6"/>')
A('<path d="M8 -1.8 L52 -4.2" stroke="#ffffff" stroke-width="0.9" opacity="0.8"/>')
A('<circle cx="2" cy="0" r="3.4" fill="#0a0812" stroke="#ffcf6e" stroke-width="1.1"/>')
A('<path d="M0 4 L-11 15" stroke="#0a0812" stroke-width="4.6" stroke-linecap="round"/>')
A('<path d="M4 -4 L-5 22" stroke="#0a0812" stroke-width="4.6" stroke-linecap="round"/>')
A('<circle cx="-16" cy="20" r="6" fill="none" stroke="#0a0812" stroke-width="3.6"/>')
A('<circle cx="-8" cy="31" r="6" fill="none" stroke="#0a0812" stroke-width="3.6"/>')
A('</g>')
# rim light from the sun along the child's warm side
A('<g fill="none" stroke="#ffc46b" stroke-linecap="round">')
A('<path d="M8 -92 C 15 -73 18 -54 21 -38" stroke-width="2.4" opacity="0.92"/>')
A('<path d="M18 -131 A 19 21 0 0 1 19 -99" stroke-width="1.5" opacity="0.62"/>')
A('<path d="M22 -114 C 24 -110 24 -106 22 -102" stroke-width="1.6" opacity="0.7"/>')
A('<path d="M10 -105 C 24 -105 38 -99 48 -88" stroke-width="2.2" opacity="0.85"/>')
A('<path d="M11 -47 L18 -9" stroke-width="1.4" opacity="0.45"/>')
A('<path d="M21 -38 L22 -8" stroke-width="1.2" opacity="0.4"/>')
A('</g>')
# cold fill light from the night sky
A('<g fill="none" stroke="#5f7ec4" stroke-linecap="round" opacity="0.35">')
A('<path d="M-10 -91 C -17 -73 -23 -53 -27 -38" stroke-width="1.6"/>')
A('<path d="M-18 -118 A 19 21 0 0 1 -14 -133" stroke-width="1.2" opacity="0.8"/>')
A('<path d="M-12 -101 C -24 -97 -30 -86 -31 -72" stroke-width="1" opacity="0.8"/>')
A('</g>')
A('</g>')

# sparks around the shears
A('<g filter="url(#glow2)">')
for _ in range(26):
    x = rnd.uniform(470, 610)
    y = rnd.uniform(320, 450)
    A(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(0.5,1.9))}" fill="#ffe6a8" opacity="{f(rnd.uniform(0.3,0.9))}"/>')
A('</g>')

# ============================================================== atmosphere
# god rays from the sun across the sky
A('<g opacity="0.30">')
for i in range(9):
    a = rnd.uniform(150, 215)
    ln = rnd.uniform(240, 620)
    x0, y0 = pt(SCX, SCY, SR * 0.96, a)
    x1, y1 = pt(SCX, SCY, SR + ln, a + rnd.uniform(-4, 4))
    A(f'<path d="M{f(x0)} {f(y0)} L{f(x1)} {f(y1)}" stroke="#ffbe6e" stroke-width="{f(rnd.uniform(8,26))}" '
      f'opacity="{f(rnd.uniform(0.03,0.09))}" filter="url(#blur14)"/>')
A('</g>')
A('<g opacity="0.45">')
A('<path d="M0 754 C 220 714 420 742 640 720 C 800 704 930 720 1024 710 L1024 754 C 900 766 780 748 620 760 C 420 776 210 762 0 794 Z" fill="#1a1030" opacity="0.55" filter="url(#blur14)"/>')
A('<path d="M90 606 C 240 592 350 602 470 592 L470 604 C 350 616 240 610 90 622 Z" fill="#221436" opacity="0.5" filter="url(#blur14)"/>')
A('</g>')

# ================================================================ finishing
A(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
A(f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.05" style="mix-blend-mode:overlay"/>')
A('</svg>')

svg = "\n".join(out)
with open("sun-thief.svg", "w") as fh:
    fh.write(svg)
print("wrote sun-thief.svg", len(svg), "bytes")
