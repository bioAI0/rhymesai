from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx.all import resize

# Load your video file
video = VideoFileClip("video0.mp4")

# Define your text properties
title_text = "Your Title Here"
initial_fontsize = 50  # Starting font size for animation
final_fontsize = 144  # Final font size after growth
color = 'white'  # Color of the text
duration = 5  # Duration for which title is displayed, in seconds
stroke_color = 'black'  # Outline color
stroke_width = 2  # Outline width

# Create a TextClip for the title with the initial font size
text_clip = TextClip(
    title_text, font='Helvetica-Bold', fontsize=initial_fontsize,
    color=color, stroke_color=stroke_color, stroke_width=stroke_width,
).set_duration(duration)

# Apply a resizing effect over time to simulate growth
size_factor = final_fontsize / initial_fontsize
text_clip = text_clip.fx(resize, lambda t: 1 + (size_factor - 1) * (t / duration))

# Position the text in the center of the video
text_clip = text_clip.set_position('center')

# Overlay the text clip on the video
video_with_title = CompositeVideoClip([video, text_clip])

# Write the result into a file
video_with_title.write_videofile("output_video.mp4", codec="libx264", fps=24)
