import json
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Load the JSON file
with open('videos_and_titles.json', 'r') as f:
    video_data = json.load(f)

# Define text properties
fontsize = 144  # Adjust the font size for largeness
color = 'white'  # Color of the text
stroke_color = 'black'  # Outline color
stroke_width = 2  # Outline width
duration = 5  # Duration for which title is displayed, in seconds

# Process each video
for entry in video_data:
    video_file = entry['video']
    title_text = entry['title']
    
    # Load the video file
    video = VideoFileClip(video_file)
    
    # Create a TextClip for the title
    text_clip = TextClip(title_text, font='Helvetica-Bold',
                         fontsize=fontsize, color=color, 
                         stroke_color=stroke_color, stroke_width=stroke_width)
    
    # Position the text in the center of the video
    text_clip = text_clip.set_position('center').set_duration(duration)
    
    # Overlay the text clip on the video
    video_with_title = CompositeVideoClip([video, text_clip])
    
    # Define the output video filename
    output_file = f"output_{video_file}"
    
    # Write the result into a file
    video_with_title.write_videofile(output_file, codec="libx264", fps=24)
