import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *

video = VideoFileClip("orijinal.mp4").subclip(0,10)

 

result = CompositeVideoClip([video]) # Overlay text on video
result.write_videofile("encrypted.webm",fps=25) # Many options...