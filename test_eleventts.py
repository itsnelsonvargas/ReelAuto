# test_eleventts.py

from dotenv import load_dotenv
import os

# 1) Import the client and helper
from elevenlabs.client import ElevenLabs
from elevenlabs import save

# 2) Load your API key from .env
load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise RuntimeError("ELEVENLABS_API_KEY not set in .env")

# 3) Instantiate the client
#    If you omit api_key here, it will still read from ELEVENLABS_API_KEY
client = ElevenLabs(api_key=api_key)

# 4) (Optional) List your available voices so you can pick one by name or id
voices = client.voices.get_all().voices
print("Available voices:")
for v in voices:
    print(f" • {v.name!r} (voice_id={v.voice_id})")

# 5) Choose a voice (by voice_id). E.g., take the first one:
voice_id = voices[0].voice_id

# 6) Generate speech via the text_to_speech converter
audio = client.text_to_speech.convert(
    text="Hello! This is a test of the ElevenLabs Python SDK.",
    voice_id=voice_id,
    model_id="eleven_monolingual_v1",     # or "eleven_multilingual_v2"
    output_format="mp3_44100_128"          # mp3 @44.1kHz
)

# 7) Save it to disk
out_path = "elevenlabs_test.mp3"
save(audio, out_path)

print(f"✅ Audio saved to {out_path}")
