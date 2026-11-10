#!/usr/bin/env python3
"""vstills.py — vertical contact sheet (1080×1920 comps). --safe draws the TikTok/Reels safe-zone overlay."""
import argparse, asyncio, io, os
from PIL import Image, ImageDraw
from playwright.async_api import async_playwright
async def main():
    ap = argparse.ArgumentParser(); ap.add_argument("comp"); ap.add_argument("--times", required=True); ap.add_argument("--out", default="stills.png")
    ap.add_argument("--cols", type=int, default=6); ap.add_argument("--tw", type=int, default=360); ap.add_argument("--safe", action="store_true")
    a = ap.parse_args(); ts = [float(x) for x in a.times.split(",")]; th = a.tw * 16 // 9
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
        await pg.goto("file://" + os.path.abspath(a.comp) + ("?safe=1" if a.safe else "")); await pg.evaluate("window.__ready")
        tiles = []
        for t in ts:
            await pg.evaluate(f"window.__seek({t})")
            im = Image.open(io.BytesIO(await pg.screenshot())).resize((a.tw, th)); ImageDraw.Draw(im).text((6, 6), f"t={t}", fill=(200, 0, 0)); tiles.append(im)
        await b.close()
    rows = (len(tiles) + a.cols - 1) // a.cols; sheet = Image.new("RGB", (a.tw * a.cols, th * rows), (0, 0, 0))
    for i, im in enumerate(tiles): sheet.paste(im, ((i % a.cols) * a.tw, (i // a.cols) * th))
    sheet.save(a.out); print("wrote", a.out, "| page errors:", errs[:5] or "none")
asyncio.run(main())
