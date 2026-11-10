#!/bin/bash
# Sharp master: render at 2x (2160x3840), 60 fps, 90° shutter, then Lanczos down to 1080x1920 and mux the mix.
set -e
cd "$(dirname "$0")/.."
python3 ~/.claude/skills/onetake/scripts/render.py comp.html --out out/sharp-2x.mp4 --width 1080 --height 1920 --scale 2 --fps 60 --shutter 90 --workers ${WORKERS:-4} --crf 12
ffmpeg -v error -y -i out/sharp-2x.mp4 -i out/mix.wav -map 0:v -map 1:a -vf "scale=1080:1920:flags=lanczos+accurate_rnd+full_chroma_int" \
  -c:v libx264 -preset slow -crf 14 -profile:v high -pix_fmt yuv420p -c:a aac -b:a 256k -movflags +faststart -shortest out/rungkaikusut-digital-sharp.mp4
