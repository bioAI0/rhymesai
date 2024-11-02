from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

# Load your video file
video = VideoFileClip("video0.mp4")

# Define your text properties
title_text = "Your Title Here"
fontsize = 70  # Adjust font size for largeness
color = 'white'  # Main text color
stroke_color = 'black'  # Outline color
stroke_width = 2  # Outline width
duration = 5  # Duration for which title is displayed, in seconds

# Create a TextClip for the title with outline
text_clip = TextClip(
    title_text,
    font='Amiri-Bold',  # Ensure this font is available
    fontsize=fontsize,
    color=color,
    stroke_color=stroke_color,
    stroke_width=stroke_width,
    method='caption'  # This method makes multiline text behave properly
)

# Add a drop shadow (optional)
shadow_clip = text_clip.on_color(
    size=(text_clip.w + 5, text_clip.h + 5),
    color=(0, 0, 0),  # Shadow color
    pos=(3, 3),  # Shadow offset
    col_opacity=0.6  # Shadow opacity
).set_position('center').set_duration(duration)

# Place the shadow and then the text
final_text = CompositeVideoClip([shadow_clip, text_clip.set_position('center')])

# Concatenate title clips and original video
video_with_title = CompositeVideoClip([video, final_text])

# Write the result into a file
video_with_title.write_videofile("output_video.mp4", codec="libx264", fps=24)
