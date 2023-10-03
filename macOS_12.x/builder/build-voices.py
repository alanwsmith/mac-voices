#!/usr/bin/env python3

import re
import subprocess

with open("../voices.txt") as _voices:
    voices = _voices.read().split("\n")

output = ""

voice_list = []

for line in voices:
    matches = re.search(r'(.*?)\s+(\S+)\s+#\s+(.*)', line)
    if matches:
        name = matches.group(1)
        name_lc = name.lower()
        lang = matches.group(2)
        text = matches.group(3)
        voice_list.append((lang, name, name_lc, text))

voice_list.sort(key=lambda x: x[0])

for voice in voice_list:
    print(voice)

    print(f"aiff: {voice[2]}")
    aiff_command = [
        "say",
        "--voice",
        voice[1],
        voice[3],
        "-o",
        f"../aiffs/{voice[2]}.aiff"
    ]
    subprocess.run(aiff_command)

    print(f"mp3:  {voice[2]}")
    mp3_command = [
        "ffmpeg",
        "-i",
        f"../aiffs/{voice[2]}.aiff",
        "-y",
        f"../mp3s/{voice[2]}.mp3",
    ]
    subprocess.run(mp3_command)

    output += f"""<div class="voice_wrapper">
  <div class="voice_name">{voice[0]} - {voice[2]}</div>
  <div class="voice_sample">
    <audio controls preload="none">
    <source src="https://github.com/alanwsmith/text-to-speech-voices/blob/main/macOS_12.x/mp3s/{voice[2]}.mp3?raw=true" type="audio/mpeg" />
    </audio>
  </div>
</div>
"""


with open("../links.html", "w") as _out:
    _out.write(output)
