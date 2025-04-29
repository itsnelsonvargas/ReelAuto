import os
from dotenv import load_dotenv
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
from elevenlabs import ElevenLabs

# Load API key from .env
load_dotenv()
eleven = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def text_to_speech(script, audio_path="output/audio.wav"):
    voice_id = "EiNlNiXeDU1pqqOPrYMO"  # Your actual voice ID

    # Generate audio using ElevenLabs (returns a generator)
    audio_stream = eleven.generate(
        text=script,
        voice=voice_id,
        model="eleven_monolingual_v1",  # Adjust if needed
        stream=True
    )

    # Save audio stream to file
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    with open(audio_path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    return audio_path

def generate_video_from_script(script, output_path="output/generated_video.mp4"):
    os.makedirs("output", exist_ok=True)

    # Step 1: Generate audio from script
    audio_path = text_to_speech(script)

    # Step 2: Create a text clip
    text_clip = TextClip(script, fontsize=32, color='white', size=(720, 1280), method='caption')
    text_clip = text_clip.set_duration(60).set_position('center')

    # Step 3: Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Step 4: Combine video and audio
    video = CompositeVideoClip([text_clip.set_audio(audio_clip)])
    video.write_videofile(output_path, fps=24)

    return output_path
