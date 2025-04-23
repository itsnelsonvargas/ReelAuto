# core/video_gen.py

import os
from elevenlabs.client import ElevenLabs
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
from dotenv import load_dotenv

from elevenlabs import generate, save
# Load API key from .env
load_dotenv()
eleven = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))



def text_to_speech(script, audio_path="output/audio.wav"):
    # Ensure you replace 'your_voice_id' with a valid Eleven Labs voice ID
    audio = generate(script, voice="your_voice_id")  # Replace with a valid voice ID
    save(audio, audio_path)  # Save the audio to a file (e.g., 'output/audio.wav')
    return audio_path


def generate_video_from_script(script, output_path="output/generated_video.mp4"):
    os.makedirs("output", exist_ok=True)

    # Step 1: Generate audio from script
    audio_path = text_to_speech(script)

    # Step 2: Create a text clip (centered)
    text_clip = TextClip(script, fontsize=32, color='white', size=(720, 1280), method='caption')
    text_clip = text_clip.set_duration(60).set_position('center')

    # Step 3: Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Step 4: Combine text and audio into a video
    video = CompositeVideoClip([text_clip.set_audio(audio_clip)])
    video.write_videofile(output_path, fps=24)

    return output_path
