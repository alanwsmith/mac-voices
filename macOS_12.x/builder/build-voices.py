#!/usr/bin/env python3

import re
import subprocess

with open("../voices.txt") as _voices:
    voices = _voices.read().split("\n")

output = ""

for voice in voices:
    matches = re.search(r'(.*?)\s+\S+\s+#\s+(.*)', voice)
    if matches:
        name = matches.group(1)
        name_lc = name.lower()
        text = matches.group(2)

        print(f"aiff: {name_lc}")
        aiff_command = [
            "say", 
            "--voice", 
            name,
            text,
            "-o", 
            f"../aiffs/{name_lc}.aiff"
        ]
        subprocess.run(aiff_command)

        print(f"mp3:  {name_lc}")
        mp3_command = [
            "ffmpeg",
            "-i",
            f"../aiffs/{name_lc}.aiff",
            "-y",
            f"../mp3s/{name_lc}.mp3",
        ]
        subprocess.run(mp3_command)

        output += f"""<div class="voice_wrapper>
  <div class="voice_name">{name_lc}</div>
  <div class="voice_sample">
    <audio controls preload="none">
      <source src="https://github.com/alanwsmith/text-to-speech-voices/blob/main/macOS_12.x/mp3s/{name_lc}.mp3?raw=true" type="audio/mpeg" />
    </audio>
  </div>
</div>
"""


with open("../links.html", "w") as _out:
    _out.write(output)

            
