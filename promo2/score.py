#!/usr/bin/env python3
"""score.py — sound for promo2/comp.html (Satu borang). Events come from the comp (window.__events), so a retimed beat takes its sound with it.
Materials: onetake's sfx_palette (one room). Music: an original synthesised bed at 112 BPM, F major pentatonic, ducked under hits.
Master: -16 LUFS integrated, peak ceiling -4 dBFS (so the AAC render stays under -3)."""
import asyncio, json, os, sys
import numpy as np, pyloudnorm as pyln
sys.path.insert(0, os.path.expanduser("~/.claude/skills/onetake/scripts"))
from sfx_palette import SR, Score, air, glass, wood, sub, bubble, lp, hp, sat, _t
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))

async def dump():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto("file://" + os.path.join(HERE, "comp.html")); await pg.evaluate("window.__ready")
        ev = await pg.evaluate("window.__events()"); await b.close(); return ev
EV = asyncio.run(dump()); json.dump(EV, open(os.path.join(HERE, "out/events.json"), "w"), indent=1)
DUR = EV["dur"]; T = EV["T"]
PENTA = [440.0, 523.25, 587.33, 659.25, 783.99, 880.0, 1046.5, 1174.66, 1318.5]   # A minor pentatonic

s = Score(dur=DUR, T60=1.1)
A = [440.0, 523.25, 587.33, 659.25, 783.99, 880.0, 1046.5, 1174.66]   # A minor pentatonic, A4 up
for e in EV["events"]:
    t, k, pan, v = e["t"], e["kind"], e["pan"] * 0.6, e["v"]
    if k == "word":   s.place(wood(220, 0.09), t, 0.32 * v, pan, 0.2)
    elif k == "hit":  s.place(sub(56, 0.7), t, 0.5 * v, 0, 0.3); s.place(glass(659.25, 1.0, 0.5), t, 0.12, pan, 0.5)
    elif k == "ping": s.place(glass(A[4 + e["i"] % 3] * 1.0, 0.35, 1.0), t, 0.16, pan, 0.25); s.place(bubble(900, 0.12), t + 0.02, 0.12, pan, 0.2)
    elif k == "tap":  s.place(wood(300, 0.07), t, 0.4 * v, pan, 0.15); s.place(wood(240, 0.06), t + 0.06, 0.25 * v, pan, 0.15)
    elif k == "suck": s.place(air(0.4, 3000, 300, 1.2, 0.8), t, 0.35, 0, 0.4)
    elif k == "fold": s.place(air(0.6, 250, 2200, 1.3, 0.6), t, 0.4, 0, 0.45)
    elif k == "land": s.place(sub(60, 0.5), t, 0.4 * v, 0, 0.25); s.place(wood(160, 0.1), t, 0.25, 0, 0.2)
    elif k == "key":  s.place(wood(260, 0.04), t, 0.16, pan, 0.1)
    elif k == "pop":  s.place(bubble(480, 0.2), t, 0.3 * v, pan, 0.3)
    elif k == "scan":
        n = int(SR * e["dur"]); tt = _t(n); f = 900 + 700 * tt / e["dur"]
        s.place(np.sin(np.cumsum(2 * np.pi * f / SR)) * 0.3 * np.sin(np.pi * tt / e["dur"]), t, 0.1, 0, 0.3)
    elif k == "ok":   s.place(glass(A[2 + e["i"]], 0.7, 0.6), t, 0.15, pan, 0.45); s.place(glass(A[4 + e["i"]], 0.7, 0.6), t + 0.06, 0.12, pan, 0.45)
    elif k == "shrink": s.place(air(0.35, 2400, 600, 1.4, 0.3), t, 0.3, 0, 0.3)
    elif k == "whoosh": s.place(air(e["dur"], 2400, 220, 1.1, 0.35), t, 0.45 * v, 0.3, 0.5, pan_to=-0.3)
    elif k == "node": s.place(glass(A[1 + e["i"]], 0.8, 0.7), t, 0.17, pan, 0.45); s.place(wood(170, 0.1), t, 0.3, pan, 0.2)
    elif k == "win":
        for j, fr in enumerate([523.25, 659.25, 783.99]): s.place(glass(fr, 1.2, 0.5), t + 0.03 * j, 0.13, -0.2 + 0.2 * j, 0.6)
    elif k == "rise": s.place(air(e["dur"], 200, 1800, 0.9, 0.9), t, 0.4, 0, 0.6)
    elif k == "chip": s.place(wood(200 + 25 * e["i"], 0.08), t, 0.35, pan, 0.2); s.place(glass(A[e["i"] % 8], 0.4, 0.5), t, 0.1, pan, 0.35)
    elif k == "count":
        n = int(SR * e["dur"]); tt = _t(n); tick = (np.sin(2 * np.pi * 40 * tt * (1 + tt)) > 0.97).astype(float)
        s.place(hp(tick, 3000) * 0.5, t, 0.2, 0, 0.2)
    elif k == "iris": s.place(air(e["dur"], 300, 3400, 1.2, 0.5), t, 0.45, 0, 0.5)
    elif k == "letter": s.place(wood(200, 0.06), t, 0.18, pan, 0.2)
    elif k == "final": s.place(sub(44, 1.6), t, 0.6, 0, 0.45); s.place(glass(523.25, 2.2, 0.4), t, 0.2, 0, 0.7); s.place(glass(783.99, 2.2, 0.4), t + 0.02, 0.14, 0, 0.7)
fx = s.mix(peak_db=-1.0)

# ── music bed (original): soft kick, offbeat hats, a plucked ostinato, a pad; out for the hard cuts' accents ──
n = int(SR * DUR); bed = np.zeros((n, 2)); beat = 60 / 100
def add(sig, t, g=1.0, pan=0.0):
    i = int(t * SR); m = min(len(sig), n - i)
    if m > 0: bed[i:i + m, 0] += sig[:m] * g * np.sqrt(0.5 * (1 - pan)); bed[i:i + m, 1] += sig[:m] * g * np.sqrt(0.5 * (1 + pan))
rng = np.random.default_rng(3)
def pluck(f, d=0.35):
    m = int(SR * d); tt = _t(m); return lp(np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(4 * np.pi * f * tt), 2600) * np.exp(-tt * 9)
def hat():
    m = int(SR * 0.05); return hp(rng.standard_normal(m), 7000) * np.exp(-_t(m) * 90)
def kick():
    m = int(SR * 0.3); tt = _t(m); return sat(np.sin(np.cumsum(2 * np.pi * (50 + 90 * np.exp(-tt * 35)) / SR)) * np.exp(-tt * 9), 1.5)
seq = [0, 2, 4, 2, 3, 2, 5, 4]   # pentatonic index pattern on 8ths
nb = int(DUR / beat)
for b in range(nb):
    tb = b * beat
    quiet = (EV["rest"][0] < tb < EV["rest"][1]) or tb > T["end"] + 1.4
    if tb < 0.05: continue
    if not quiet:
        add(kick(), tb, 0.55 if b % 2 == 0 else 0.35)
        add(hat(), tb + beat / 2, 0.12, 0.3)
    for h in (0, 1):
        f = PENTA[seq[(2 * b + h) % 8]] / 2 * (2 if T["hop"] < tb < T["push"] else 1)
        add(pluck(f), tb + h * beat / 2, 0.10 if not quiet else 0.05, -0.25 if h else 0.25)
# pad: F – Dm – Bb – C, two bars each
chords = [[220.0, 261.63, 329.63], [174.61, 220.0, 261.63], [130.81, 164.81, 196.0], [196.0, 246.94, 293.66]]   # Am F C G
bar = 4 * beat
for c in range(int(DUR / bar) + 1):
    m = int(SR * bar); tt = _t(m); env = np.minimum(1, tt / 0.4) * np.minimum(1, (bar - tt) / 0.4)
    sig = sum(np.sin(2 * np.pi * f * tt + j) + 0.3 * np.sin(2 * np.pi * 2.003 * f * tt) for j, f in enumerate(chords[c % 4]))
    add(lp(sig, 900) * env, c * bar, 0.05, 0)
# duck the bed under the effects (sidechain from the fx envelope)
envfx = np.abs(fx).max(1); k = int(SR * 0.08); envfx = np.convolve(envfx, np.ones(k) / k, mode="same")
duck = 1 / (1 + 6 * envfx / (envfx.max() + 1e-9)); bed *= duck[:, None]
bed *= np.minimum(1, _t(n) / 0.05)[:, None] * np.minimum(1, (DUR - _t(n)) / 0.6)[:, None]
mix = fx * 0.85 + bed / (np.abs(bed).max() + 1e-9) * 0.42
# breaths: the hold, a gasp before the burst, the end card ringing out
gate = np.ones(n); tt = _t(n)
for a, b, ra in [(EV['rest'][0], EV['rest'][1] + 0.05, 0.08), (12.3, 12.55, 0.05), (16.55, 16.8, 0.05), (19.45, DUR + 1, 0.6)]:
    gate *= 1 - np.clip(np.minimum((tt - a) / ra, (b - tt) / 0.04), 0, 1)
mix *= gate[:, None]
meter = pyln.Meter(SR); L = meter.integrated_loudness(mix); mix = pyln.normalize.loudness(mix, L, -16.0)
pk = np.abs(mix).max(); ceil = 10 ** (-4 / 20)
if pk > ceil: mix = np.tanh(mix / ceil * 0.95) * ceil   # soft ceiling
import wave
with wave.open(os.path.join(HERE, "out/mix.wav"), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix, -1, 1) * 32767).astype(np.int16).tobytes())
print(f"mix.wav: {len(EV['events'])} events · {meter.integrated_loudness(mix):.1f} LUFS · peak {20*np.log10(np.abs(mix).max()):.1f} dBFS")
