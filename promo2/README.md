# Rungkai Kusut: "Satu borang" (process digitalisation, TikTok / Reels)

22 s · 1080×1920 · 60 fps sharp master (rendered at 2160×3840, Lanczos down) · onetake method, like `../promo`.

| file | what |
|---|---|
| `out/rungkaikusut-digital-sharp.mp4` | the film with sound: upload this |
| `out/mix.wav` | the sound alone (−17 LUFS) |
| `caption.txt` | hook text, post caption, hashtags |
| `comp.html` | composition: `?play`, `?t=6.4`, `?safe` |
| `score.py` | sound from the comp's `__events()` |
| `tools/render_sharp.sh` | the sharp master pipeline |

## Concepts

1. **Satu borang (picked).** One paper claim form is the whole film: it becomes the app, then the claim itself travels
   through approval into the system, and the system connects to everything.
2. **Group chat meletup.** A WhatsApp group bursting with "Boss, dah approve?" messages, each bubble caught and turned into a
   workflow step. Its hook is used in 1.
3. **Pejabat dua dunia.** A split desk: stamps and paper on one side, phone and app on the other.

Look: chosen fresh, not video 1's. A night-navy ground, cream cards, amber and mint accents; three stations side by side
with horizontal camera whips, a pull-back reveal, and an iris into the end card.

## Beat sheet: what carries

| t | beat | carries into the next |
|---|---|---|
| 0–2.2 | **Masih approve guna kertas & WhatsApp?** A paper form, stamp MENUNGGU, chat bubbles piling on, unread count racing to 99+ | the paper |
| 2.2–3.0 | the finger taps the form; the bubbles are swept into it; the paper **becomes a phone** (`morphRect`) | the phone |
| 3.0–6.1 | **Kami jadikan apps.** The camera leans in; the finger picks *Perjalanan*, types RM 86.40, snaps the receipt, *AI baca: RM 86.40*, *Hantar* | the form |
| 6.1–7.15 | the form shrinks into the claim token (`#0142 · RM 86.40`) and hops out; the camera whips with it | the token |
| 7.15–9.35 | **Kelulusan automatik.** Staf → Pengurus → Kewangan → Dibayar, each node lights as the bead lands; **3 hari → 3 minit** | the token |
| 9.35–10.3 | the one held breath | — |
| 10.3–12.55 | **Masuk terus ke sistem anda.** The token flies into the admin panel and becomes its newest row; the old rows shift down | the panel |
| 12.55–14.3 | **Semua sistem bersambung.** Pull back to see phone, workflow and panel on one road; *Akaun, Gaji, Bank, Stok, CRM, Kedai online* plug in | the camera |
| 14.3–17.0 | **Berapa kos kerja manual?** Calculator: 5 staf × 2 jam × RM 25 → **RM 65,000** setahun; tap *Kira kos saya: PERCUMA* | the button |
| 17.0–22 | an iris opens from the button: **Rungkai Kusut** · *Proses kusut? Kami digitalkan.* · rungkaikusut.com · Apps iOS & Android · Portal · Panel admin | end |

## Checks

- `verify_promo.py` vs the benchmark TikTok: cadence, rest, burst, not-flat and audio all PASS.
- `probe.py --width 1080 --height 1920`: continuity 0.83, 5 of 6 boundaries carried. The bare one is the iris into the end card.
- Safe zone: x 72–930, y 250–1440 for every word, number and the URL (`?safe` to check any frame).

The RM 65,000 figure is an illustration (5 × 2 h × RM 25 × 260 working days), the same sum the site's calculator does.
Names and claims in the UI are made up.
