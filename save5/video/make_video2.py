from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Load your video file
video = VideoFileClip("video0.mp4")

# Define your text properties
title_text = "Your Title Here"
fontsize = 70  # Adjust the font size for largeness
color = 'white'  # Color of the text
duration = 5  # Duration for which title is displayed, in seconds

# Create a TextClip for the title
text_clip = TextClip(title_text, font='Amiri-Bold', fontsize=fontsize, color=color)

# Position the text in the center of the video
text_clip = text_clip.set_position('center').set_duration(duration)

# Overlay the text clip on the video
video_with_title = CompositeVideoClip([video, text_clip])

# Write the result into a file
video_with_title.write_videofile("output_video.mp4", codec="libx264", fps=24)
