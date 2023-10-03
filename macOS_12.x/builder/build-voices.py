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

current_country = ""

counter = 0

for voice in voice_list:
    counter += 1

    print(voice)

    # print(f"aiff: {voice[2]}")
    # aiff_command = [
    #     "say",
    #     "--voice",
    #     voice[1],
    #     voice[3],
    #     "-o",
    #     f"../aiffs/{voice[2]}.aiff"
    # ]
    # subprocess.run(aiff_command)

    # print(f"mp3:  {voice[2]}")
    # mp3_command = [
    #     "ffmpeg",
    #     "-i",
    #     f"../aiffs/{voice[2]}.aiff",
    #     "-y",
    #     f"../mp3s/{voice[2]}.mp3",
    # ]
    # subprocess.run(mp3_command)

    # if current_country != voice[0]:
    #     output += f"""
# <div class="lang_wrapper">
    # <div class="lang_line">{voice[0]}</div>"""

    output += f"""
    <div class="voice_sample">
        <audio id="audio_bravo{counter}" preload="none">
            <source src="https://github.com/alanwsmith/text-to-speech-voices/blob/main/macOS_12.x/mp3s/{voice[2]}.mp3?raw=true" type="audio/mpeg" />
        </audio>
        <button class="voice_name_play_button" data-audioidbravo="{counter}">{voice[2]} ({voice[0]})</button>
    </div>
"""

    # if current_country != voice[0]:
    #     output += f"""</div>"""
    #     current_country = voice[0]

output += """
<script>
const init = () => {
    audioWrapper.addEventListener("click", (event) => {
        let audioId = event.target.dataset.audioidbravo
        window[`audio_bravo${audioId}`].play()
    }) 
}
document.addEventListener("DOMContentLoaded", init)
</script>

"""


with open("../links.html", "w") as _out:
    _out.write("""<div id="audioWrapper">""")
    _out.write(output)
    _out.write("""</div>""")
