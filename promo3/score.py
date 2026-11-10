#!/usr/bin/env python3
"""score.py — sound for promo3/comp.html (Cahaya imbasan). Events come from the comp (window.__events), so a retimed beat takes its sound with it.
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
PENTA = [293.66, 349.23, 392.0, 440.0, 523.25, 587.33, 698.46, 783.99, 880.0]   # D minor pentatonic

s = Score(dur=DUR, T60=0.9)
Dd = [293.66, 329.63, 349.23, 392.0, 440.0, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99, 880.0]   # D dorian
def hum(d, f0=120):
    n = int(SR * d); tt = _t(n); x = np.sin(2 * np.pi * f0 * tt) + 0.5 * np.sin(2 * np.pi * f0 * 2.01 * tt) + 0.2 * np.sin(2 * np.pi * f0 * 6.02 * tt)
    return lp(x, 2400) * np.sin(np.pi * np.clip(tt / d, 0, 1)) ** 0.5
for e in EV["events"]:
    t, k, pan, v = e["t"], e["kind"], e["pan"] * 0.6, e["v"]
    if k == "word":   s.place(wood(220, 0.09), t, 0.32 * v, pan, 0.2)
    elif k == "hit":  s.place(sub(56, 0.7), t, 0.5 * v, 0, 0.3); s.place(glass(587.33, 1.0, 0.5), t, 0.12, pan, 0.5)
    elif k == "paper": s.place(air(0.18, 2600, 900, 1.6, 0.2), t - 0.06, 0.3 * v, pan, 0.2); s.place(wood(130, 0.09), t, 0.4 * v, pan, 0.2)
    elif k == "beamOn": s.place(glass(1174.66, 1.2, 1.0), t, 0.14, 0, 0.6); s.place(hum(0.5, 180), t, 0.12, 0, 0.3)
    elif k == "scan": s.place(hum(e["dur"], 120), t, 0.18, 0, 0.25)
    elif k == "blip": s.place(glass(Dd[6 + e["i"] % 5], 0.25, 0.8), t, 0.13, pan, 0.25)
    elif k == "stamp": s.place(sub(70, 0.35), t, 0.45, pan, 0.2); s.place(wood(180, 0.1), t, 0.45, pan, 0.2)
    elif k == "swipe": s.place(air(0.22, 3200, 700, 1.4, 0.25), t, 0.32, -0.2, 0.25, pan_to=-0.7); s.place(glass(Dd[4 + e["i"]], 0.2, 0.8), t + 0.1, 0.09, -0.4, 0.2)
    elif k == "done":
        for j, fr in enumerate([587.33, 739.99, 880.0]): s.place(glass(fr, 1.0, 0.5), t + 0.03 * j, 0.13, -0.2 + 0.2 * j, 0.55)
        s.place(sub(58, 0.5), t, 0.4, 0, 0.2)
    elif k == "whoosh": s.place(air(e["dur"], 2400, 220, 1.1, 0.35), t, 0.45 * v, 0.2, 0.5, pan_to=-0.2)
    elif k == "key":  s.place(wood(280, 0.035), t, 0.14, pan, 0.08)
    elif k == "send": s.place(bubble(700, 0.16), t, 0.35, pan, 0.2)
    elif k == "reply": s.place(bubble(460, 0.2), t, 0.35, pan, 0.25); s.place(glass(Dd[3 + 2 * e["i"]], 0.6, 0.5), t + 0.05, 0.12, pan, 0.4)
    elif k == "dive": s.place(air(e["dur"] + 0.2, 200, 3200, 1.0, 0.85), t, 0.5, 0, 0.55)
    elif k == "sweep":
        n = int(SR * e["dur"]); tt = _t(n); f = 220 * 2 ** (tt / e["dur"] * 1.0)
        s.place(lp(np.sin(np.cumsum(2 * np.pi * f / SR)), 1800) * np.sin(np.pi * tt / e["dur"]) * 0.5, t, 0.16, 0, 0.4)
    elif k == "warn": s.place(glass(880.0, 0.5, 0.8), t, 0.15, pan, 0.3); s.place(glass(880.0, 0.5, 0.8), t + 0.14, 0.12, pan, 0.3)
    elif k == "slam": s.place(sub(54 - 3 * e["i"], 0.5), t, 0.55 + 0.05 * e["i"], 0, 0.25); s.place(wood(150 + 20 * e["i"], 0.1), t, 0.45, 0, 0.2); s.place(air(0.2, 3000, 600, 1.4, 0.8), t - 0.2, 0.25, 0, 0.2)
    elif k == "morph": s.place(air(0.5, 300, 2400, 1.3, 0.5), t, 0.3, 0, 0.45)
    elif k == "tap":  s.place(wood(300, 0.07), t, 0.4 * v, pan, 0.15); s.place(wood(240, 0.06), t + 0.06, 0.25 * v, pan, 0.15)
    elif k == "letter": s.place(wood(200, 0.06), t, 0.18, pan, 0.2)
    elif k == "final": s.place(sub(44, 1.6), t, 0.6, 0, 0.45); s.place(glass(587.33, 2.2, 0.4), t, 0.2, 0, 0.7); s.place(glass(880.0, 2.2, 0.4), t + 0.02, 0.14, 0, 0.7)
fx = s.mix(peak_db=-1.0)

# ── music bed (original): soft kick, offbeat hats, a plucked ostinato, a pad; out for the hard cuts' accents ──
n = int(SR * DUR); bed = np.zeros((n, 2)); beat = 60 / 118
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
        f = PENTA[seq[(2 * b + h) % 8]] / 2 * (2 if T["toChat"] < tb < T["toD"] else 1)
        add(pluck(f), tb + h * beat / 2, 0.10 if not quiet else 0.05, -0.25 if h else 0.25)
# pad: F – Dm – Bb – C, two bars each
chords = [[146.83, 174.61, 220.0], [196.0, 246.94, 293.66], [174.61, 220.0, 261.63], [130.81, 164.81, 196.0]]   # Dm G F C (dorian)
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
for a, b, ra in [(EV['rest'][0], EV['rest'][1] + 0.05, 0.08), (12.55, 12.8, 0.05), (16.25, 16.5, 0.05), (18.65, DUR + 1, 0.5)]:
    gate *= 1 - np.clip(np.minimum((tt - a) / ra, (b - tt) / 0.04), 0, 1)
mix *= gate[:, None]
meter = pyln.Meter(SR); L = meter.integrated_loudness(mix); mix = pyln.normalize.loudness(mix, L, -16.0)
pk = np.abs(mix).max(); ceil = 10 ** (-4 / 20)
if pk > ceil: mix = np.tanh(mix / ceil * 0.95) * ceil   # soft ceiling
import wave
with wave.open(os.path.join(HERE, "out/mix.wav"), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix, -1, 1) * 32767).astype(np.int16).tobytes())
print(f"mix.wav: {len(EV['events'])} events · {meter.integrated_loudness(mix):.1f} LUFS · peak {20*np.log10(np.abs(mix).max()):.1f} dBFS")
