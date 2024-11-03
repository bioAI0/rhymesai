from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Define the single title
title = "Welcome to Rhymes.ai"

# Specify your video file
video_file = 'video0.mp4'
output_file = 'output_video_with_title.mp4'

# Load the video clip
video_clip = VideoFileClip(video_file)

# Parameters for text animation
text_duration = 5  # duration for the text clip in seconds
font_size_start = 20  # starting font size
font_size_end = 60  # ending font size

# Create a growing text clip
text_clip = (TextClip(title, fontsize=font_size_start, color='white', font='Amiri-Bold')
             .set_position('center')
             .set_duration(text_duration)
             .set_start(0)  # text appears at the start of the video
             .crossfadein(1)  # Crossfade for smooth appearance
             .crossfadeout(1)  # Crossfade for smooth disappearance
             .resize(lambda t: 1 + (font_size_end-font_size_start)/font_size_start * (t/text_duration)))

# Combine video and text clips
final_clip = CompositeVideoClip([video_clip, text_clip])

# Write the result into a file
final_clip.write_videofile(output_file, codec='libx264', fps=24)

# Clean up
video_clip.close()
final_clip.close()
