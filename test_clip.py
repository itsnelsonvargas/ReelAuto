from moviepy.config import change_settings
from moviepy.editor import TextClip

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

clip = TextClip("Test", fontsize=50, color='white', size=(720, 1280), method='caption')
clip = clip.set_duration(5)
clip.write_videofile("test.mp4", fps=24)
