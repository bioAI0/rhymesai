import json
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

titles = [
    "Welcome to Rhymes.ai", "Catception", "Video Optimizer", "Aria & Allegro", "Cutest Cat Videos", "Creative Journey", "Adorable Prompt", "Cute Cat Wizard", "Allegro Model", "Concept Materializes", "Allegro Magic", "Whimsical Essence", "Initial Creation", "Uncover More Charm", "Starting Point", "Introducing Aria", "Multimodal Power", "Cuteness Judgment", "Analyzing Video", "Keen Eye", "Cuteness Score", "Delve Deeper", "Extracted Frames", "Wizardly Charm", "Foundation Step", "Feed Back to Aria", "Creative Enhancements", "Vibrant Colors",
    "Enchanting Backdrops", "Playful Expressions", "Imaginative Suggestions",
    "New Video Iteration", "Iterative Loop", "Charming Content", "Captivating Wizard",
    "Reinforcement Learning", "Reward Signals", "Refine & Optimize", "Creative Brains",
    "Adorable Progress", "Careful Analysis", "Kitty Wizardry", "Iterative Creativity",
    "Art & Technology", "Harmonious Blend", "Culmination", "Catception",
    "Harmony & Creativity", "Endless Possibilities", "AI Wizardry", "Thank You",
    "Enchanting Adventure", "Stay Tuned", "Rhymes.ai Hackathon", "Creative Boundaries"
]

# Specify your video file
video_file = 'your_video.mp4'
output_file = 'output_video_with_titles.mp4'

# Load the video clip
video_clip = VideoFileClip(video_file)
video_duration = video_clip.duration

# Parameters for text animation
text_duration = 5  # duration for each text clip in seconds
font_size_start = 20  # starting font size
font_size_end = 60  # ending font size

# Helper function to create a growing text animation
def create_growing_text_clip(title, start_time):
    text_clip = (TextClip(title, fontsize=font_size_start, color='white', font='Amiri-Bold')
                 .set_position('center')
                 .set_duration(text_duration)
                 .set_start(start_time)
                 .crossfadein(1)  # Crossfade for smooth appearance
                 .crossfadeout(1)  # Crossfade for smooth disappearance
                 .resize(lambda t: 1 + (font_size_end-font_size_start)/font_size_start * (t/text_duration)))
    return text_clip

# Create a list of text clips with growing sizes
text_clips = []
total_time = 0
for title in titles:
    text_clips.append(create_growing_text_clip(title, total_time))
    total_time += text_duration

# Combine video and text clips
final_clip = CompositeVideoClip([video_clip] + text_clips)

# Write the result into a file
final_clip.write_videofile(output_file, codec='libx264', fps=24)

# Clean up
video_clip.close()
final_clip.close()

