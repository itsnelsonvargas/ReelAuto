import os
import pyttsx3
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip

def text_to_speech(script, audio_path="output/audio.wav"):
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speaking speed if needed
    engine.save_to_file(script, audio_path)
    engine.runAndWait()
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
