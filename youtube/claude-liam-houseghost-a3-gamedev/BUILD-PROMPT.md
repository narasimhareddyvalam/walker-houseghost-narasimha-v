# BUILD-PROMPT — how this film is rebuilt

From the repository root, with the course toolkit at `~/Desktop/brutalist.art`:

```bash
python3 youtube/claude-liam-houseghost-a3-gamedev/build_beats.py      # beat sheet from SCRIPT.md
python3 youtube/claude-liam-houseghost-a3-gamedev/prepare_clips.py    # fit captures to 4K, labelled
cd ~/Desktop/brutalist.art
.venv/bin/python3 runtime/scripts/generate_audio_kokoro.py <reel>     # narration (local, $0.00)
.venv/bin/python3 runtime/scripts/remotion_scenes.py <reel>           # render the compositions
python3 <repo>/youtube/claude-liam-houseghost-a3-gamedev/build_evidence.py
./art godot-gamedev --check <reel> --game <repo>/godot                # evidence ledger
./art run <reel> --height 1080                                        # review cut
./art final <reel> --height 2160 --out <reel>/exports/landscape       # 4K master
```

Recordings are made once and hashed in `CAPTURE.md`; images used by the compositions are copied
to `runtime/remotion/public/houseghost-a3/`.
