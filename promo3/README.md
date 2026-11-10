# Rungkai Kusut: "Cahaya imbasan" (practical AI, TikTok / Reels)

21.5 s · 1080×1920 · 60 fps sharp master (rendered at 2160×3840, Lanczos down) · onetake method, like `../promo` and `../promo2`.

| file | what |
|---|---|
| `out/rungkaikusut-ai-sharp.mp4` | the film with sound: upload this |
| `out/mix.wav` | the sound alone |
| `caption.txt` | hook text, description, pinned comment |
| `comp.html` | composition: `?play`, `?t=6.4`, `?safe` |
| `score.py` | sound from the comp's `__events()` |

## Concepts

1. **Cahaya imbasan (picked).** One mint scan light carries the whole film.
2. **Tanya data anda.** The film as one chat with an AI assistant, each answer opening into a chart. Folded into 1 as its middle.
3. **Perlumbaan.** A staff member typing invoices against the AI, with a race timer.

Look: chosen fresh. A deep-teal ground with mint light; the camera dives *into* a chart (nested units, as in onetake's
clearing case) instead of whipping sideways; the ending zooms through the mint button into a mint end card.

## Beat sheet: the beam carries every boundary

| t | beat | the beam |
|---|---|---|
| 0–2.1 | **Staf anda masih taip invois satu-satu?** Seven invoices slam into a pile; the backlog counts up to 1,247 | — |
| 2.15–3.6 | **AI baca invois dalam 2 saat.** The beam appears and reads the top invoice; Pembekal, No. invois, Tarikh and Jumlah light up and pop out; ✓ DIREKOD | scans the invoice |
| 3.7–5.2 | five more invoices scanned and flung away; the counter runs down to **✓ 1,247 invois siap** | sweeps, one per invoice |
| 5.3–9.9 | **Tanya data anda macam WhatsApp.** "Berapa belanja pembekal bulan lepas?" → RM 182,400 ▲12% with a chart; "Pembekal paling mahal?" → Syarikat Maju Jaya | the input line under the chat |
| 9.9–12.85 | **Ramal jualan & stok sebelum terlambat.** The camera dives into the chart in the answer; the beam stands up as *HARI INI* and sweeps right, revealing the forecast; *Disember: +35% ▲* | the "today" line |
| 12.85–14.75 | **AI praktikal, bukan gimik.** Four capability cards slam onto the beam: baca invois, chatbot, ramalan, laporan automatik | the shelf |
| 14.75–16.75 | **Mula dengan satu proses.** The top card becomes the CTA: Semakan Kesediaan AI, 45 minit, PERCUMA, data kekal milik anda, patuh PDPA | the glowing outline of the button |
| 16.75–21.5 | the finger taps; the camera zooms through the mint button: **Rungkai Kusut** · *AI praktikal untuk PKS Malaysia.* · rungkaikusut.com | the underline (in ink) |

## Checks

- `verify_promo.py` vs the benchmark TikTok: cadence, rest, burst, not-flat and audio all PASS.
- `probe.py --width 1080 --height 1920`: continuity 0.80, 4 of 5 carried. The bare one is the zoom into the end card.
- Safe zone x 72–930, y 250–1440 for all text.

Company names, invoice numbers and figures are illustrations.
