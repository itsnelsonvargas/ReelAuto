import os
from dotenv import load_dotenv
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
from moviepy.config import get_setting, change_settings

# Load environment variables
load_dotenv()

# Set ImageMagick binary path
change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"
})
print("✅ ImageMagick path set to:", get_setting("IMAGEMAGICK_BINARY"))

# ElevenLabs imports
from elevenlabs.client import ElevenLabs
from elevenlabs import save

def text_to_speech(script, audio_path="output/audio.wav"):
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    # Initialize ElevenLabs client
    client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    # Generate audio
    audio = client.generate(
        text=script,
        voice="Rachel",  # Change to any supported voice name or ID
        model="eleven_monolingual_v1"
    )

    save(audio, audio_path)
    return audio_path


def generate_video_from_script(script, output_path="output/generated_video.mp4"):
    print("🔍 Using ImageMagick from:", get_setting("IMAGEMAGICK_BINARY"))
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
