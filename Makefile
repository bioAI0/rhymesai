all: video0.mp4

video0.mp4: generate_video.py input0.txt
	python generate_video.py input0.txt video0.mp4

clean:
	rm -f video0.mp4
