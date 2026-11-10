# Rungkai Kusut — "Satu benang" (TikTok / Reels promo)

21 s · 1080×1920 · made with the [onetake](https://github.com/feitangyuan/onetake) method: one HTML composition
(`comp.html`), every value a pure function of time, moves from `motion.js`, rendered frame by frame with shutter motion blur.

| file | what |
|---|---|
| `out/rungkaikusut-tiktok.mp4` | the film with sound, 1080×1920 30 fps (upload this) |
| `out/rungkaikusut-tiktok-60fps.mp4` | the same at 60 fps, if made |
| `out/mix.wav` | the sound mix alone (−17 LUFS) |
| `review/safe-zone.png` | key frames with the TikTok + Reels safe zone drawn on |
| `caption.txt` | post caption and hashtags (BM) |
| `comp.html` | the composition: `?play` plays it, `?t=6.4` pins a frame, `?safe` shows the safe zone |
| `score.py` | the sound, built from the comp's own `__events()` |
| `ref/` | the benchmark TikTok and its measurements (`ref/ana/`) |

## The concept round

1. **Satu benang (picked).** A single tangled thread *is* the film. The brand name made literal: *rungkai* = untangle, *kusut* = tangled.
2. **Rambut dalam tepung.** The site's proverb as a macro dive: one hair lifted out of a flour-white spreadsheet without scattering it.
3. **Kusut | Jelas split.** One SME's week as chaos on the left and clean on the right, until the right swallows the left.

## Beat sheet: what carries every boundary

| t | beat | the thread | carries into the next beat |
|---|---|---|---|
| 0.1–1.3 | hook: *Excel bersepah. PDF berlambak. WhatsApp tak henti.* → **Data anda kusut?** | a breathing tangle with messy values riding it (`12/3/24`, `SHAH ALAM`, `#N/A`) | the tangle |
| 2.75–4.3 | a finger grabs the loose end and pulls; "kusut?" shatters; rubbish falls off | straightens from the pulled end, twangs taut | the straight line |
| 4.2–6.2 | **Kami rungkaikan.** The messy values hop into a clean table and come out normalised | it is the table's top rule; the rows drop out of it | the line + the card |
| 6.25–8.4 | **Dashboard yang jelas.** *Setiap cawangan. / Setiap invois. / Setiap akaun. → satu dashboard.* | bends into the 7-day sales line; the card morphs into the dashboard | the chart line |
| 8.4–9.95 | a hold (the one breath) | still | — |
| 9.95–12.5 | **Proses manual? Kami digitalkan.** Paper → digital form, WhatsApp → workflow, retyping → connected systems | peels off the chart and pours down; the camera whips with it; each node lights as it passes | the stepper line |
| 12.55–14.0 | burst of hard cuts: **Data. Dashboard. Automasi. Apps. AI.** | the underline of each word, snapping to its width | the underline |
| 14.0–17.0 | **Excel anda sekusut mana?** Data Kusut Checker: 41/100 *Sangat kusut* → tap **Semak data saya: PERCUMA** → 98 *Jelas ✓* | curls into the gauge's track | the arc |
| 17.0–21.0 | **Rungkai Kusut** · *Yang kusut, kami rungkai.* · `rungkaikusut.com` · Data · Dashboard · Digital · AI untuk PKS Malaysia | unrolls into the line under the name | end |

## Safe zone (TikTok + Instagram Reels, 1080×1920)

All text, numbers and the URL stay inside **x 72–930, y 250–1440**:

- top 250 px: status bar, the For You / Following tabs, the IG header;
- bottom 480 px: caption, sound ticker, nav bar;
- right 150 px: the like / comment / share / profile rail;
- left 72 px.

Headlines are drawn in screen space, so a camera move can never push them out. Only the thread, the finger and scrolling
cards cross the edge while they move. Open `comp.html?safe&t=<time>` to check any frame.

## Benchmark: @damianodesu TikTok (`ref/ref.mp4`)

The reference is a phone filming a laptop that plays a motion promo. Measured with `analyze_ref.py`: 53 s, 24 fps,
1.4 % dead-still, longest quiet 1.42 s, cuts in bursts (~19 s, 42 s, 47 s), soft curves (median t80 0.74), no motion blur.
Taken from it:

- the **shattering word** ("LYING." → here "kusut?" breaks apart as the thread is pulled out of it);
- the **"Every store. Every payout. Every ad account. → melted into one number"** staccato pill (here *Setiap cawangan. /
  Setiap invois. / Setiap akaun. → satu dashboard.*), which is exactly Rungkai Kusut's "1 sumber data" pitch;
- **nearly constant energy**: one short hold (≈1.5 s) instead of onetake's usual quarter of the film at rest;
- a short native caption on top. Add it in TikTok's own text tool (see `caption.txt`), so it stays editable and sits in the app's font.

Not taken: the filmed-laptop framing (it needs a real camera take) and the 53 s length (15–25 s is the sweet spot for a promo).

## Re-render

```bash
python3 ~/.claude/skills/onetake/scripts/render.py comp.html --out out/draft.mp4 --width 1080 --height 1920 --workers 3
python3 score.py   # → out/mix.wav
ffmpeg -i out/draft.mp4 -i out/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest out/rungkaikusut-tiktok.mp4
```

Fonts: Plus Jakarta Sans and Instrument Serif (SIL OFL 1.1, the site's own faces), inlined in `fonts.css`.
Music: an original synthesised bed in `score.py`. There are no third-party audio licences to clear. You can also swap
it for a trending sound inside TikTok.
