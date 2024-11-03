all: results9.txt

# 0

input0.txt: prompt.txt
	cp prompt.txt input0.txt

generate0.json: input0.txt
	python catception_generate_video.py input0.txt video0.mp4 | tee generate0.json

get0.json: generate0.json
	python catception_get_video.py generate0.json | tee get0.json

video0.mp4: get0.json
	cut -f 3 -d " " get0.json | xargs wget -O video0.mp4
	touch video0.mp4

image00.jpg: video0.mp4
	ffmpeg -i video0.mp4 -ss 0 -vframes 1 image00.jpg

image01.jpg: video0.mp4
	ffmpeg -i video0.mp4 -ss 1 -vframes 1 image01.jpg

results0.txt: input0.txt image00.jpg image01.jpg
	python catception_analyze_video.py input0.txt image00.jpg image01.jpg | tee results0.txt

input1.txt: input0.txt image00.jpg image01.jpg results0.txt
	python catception_new_prompt.py input0.txt image00.jpg image01.jpg | tee input1.txt

# 1

generate1.json: input1.txt
	python catception_generate_video.py input1.txt video1.mp4 | tee generate1.json

get1.json: generate1.json
	python catception_get_video.py generate1.json | tee get1.json

video1.mp4: get1.json
	cut -f 3 -d " " get1.json | xargs wget -O video1.mp4
	touch video1.mp4

image10.jpg: video1.mp4
	ffmpeg -i video1.mp4 -ss 0 -vframes 1 image10.jpg

image11.jpg: video1.mp4
	ffmpeg -i video1.mp4 -ss 1 -vframes 1 image11.jpg

results1.txt: input1.txt image10.jpg image11.jpg
	python catception_analyze_video.py input1.txt image10.jpg image11.jpg | tee results1.txt

input2.txt: input1.txt image10.jpg image11.jpg results1.txt
	python catception_new_prompt.py input1.txt image10.jpg image11.jpg | tee input2.txt

# 2

generate2.json: input2.txt
	python catception_generate_video.py input2.txt video2.mp4 | tee generate2.json

get2.json: generate2.json
	python catception_get_video.py generate2.json | tee get2.json

video2.mp4: get2.json
	cut -f 3 -d " " get2.json | xargs wget -O video2.mp4
	touch video2.mp4

image20.jpg: video2.mp4
	ffmpeg -i video2.mp4 -ss 0 -vframes 1 image20.jpg

image21.jpg: video2.mp4
	ffmpeg -i video2.mp4 -ss 1 -vframes 1 image21.jpg

results2.txt: input2.txt image20.jpg image21.jpg
	python catception_analyze_video.py input2.txt image20.jpg image21.jpg | tee results2.txt

input3.txt: input2.txt image20.jpg image21.jpg results2.txt
	python catception_new_prompt.py input2.txt image20.jpg image21.jpg | tee input3.txt

# 3

generate3.json: input3.txt
	python catception_generate_video.py input3.txt video3.mp4 | tee generate3.json

get3.json: generate3.json
	python catception_get_video.py generate3.json | tee get3.json

video3.mp4: get3.json
	cut -f 3 -d " " get3.json | xargs wget -O video3.mp4
	touch video3.mp4

image30.jpg: video3.mp4
	ffmpeg -i video3.mp4 -ss 0 -vframes 1 image30.jpg

image31.jpg: video3.mp4
	ffmpeg -i video3.mp4 -ss 1 -vframes 1 image31.jpg

results3.txt: input3.txt image30.jpg image31.jpg
	python catception_analyze_video.py input3.txt image30.jpg image31.jpg | tee results3.txt

input4.txt: input3.txt image30.jpg image31.jpg results3.txt
	python catception_new_prompt.py input3.txt image30.jpg image31.jpg | tee input4.txt


# 4

generate4.json: input4.txt
	python catception_generate_video.py input4.txt video4.mp4 | tee generate4.json

get4.json: generate4.json
	python catception_get_video.py generate4.json | tee get4.json

video4.mp4: get4.json
	cut -f 3 -d " " get4.json | xargs wget -O video4.mp4
	touch video4.mp4

image40.jpg: video4.mp4
	ffmpeg -i video4.mp4 -ss 0 -vframes 1 image40.jpg

image41.jpg: video4.mp4
	ffmpeg -i video4.mp4 -ss 1 -vframes 1 image41.jpg

results4.txt: input4.txt image40.jpg image41.jpg
	python catception_analyze_video.py input4.txt image40.jpg image41.jpg | tee results4.txt

input5.txt: input4.txt image40.jpg image41.jpg results4.txt
	python catception_new_prompt.py input4.txt image40.jpg image41.jpg | tee input5.txt

# 5

generate5.json: input5.txt
	python catception_generate_video.py input5.txt video5.mp4 | tee generate5.json

get5.json: generate5.json
	python catception_get_video.py generate5.json | tee get5.json

video5.mp4: get5.json
	cut -f 3 -d " " get5.json | xargs wget -O video5.mp4
	touch video5.mp4

image50.jpg: video5.mp4
	ffmpeg -i video5.mp4 -ss 0 -vframes 1 image50.jpg

image51.jpg: video5.mp4
	ffmpeg -i video5.mp4 -ss 1 -vframes 1 image51.jpg

results5.txt: input5.txt image50.jpg image51.jpg
	python catception_analyze_video.py input5.txt image50.jpg image51.jpg | tee results5.txt

input6.txt: input5.txt image50.jpg image51.jpg results5.txt
	python catception_new_prompt.py input5.txt image50.jpg image51.jpg | tee input6.txt

# 6

generate6.json: input6.txt
	python catception_generate_video.py input6.txt video6.mp4 | tee generate6.json

get6.json: generate6.json
	python catception_get_video.py generate6.json | tee get6.json

video6.mp4: get6.json
	cut -f 3 -d " " get6.json | xargs wget -O video6.mp4
	touch video6.mp4

image60.jpg: video6.mp4
	ffmpeg -i video6.mp4 -ss 0 -vframes 1 image60.jpg

image61.jpg: video6.mp4
	ffmpeg -i video6.mp4 -ss 1 -vframes 1 image61.jpg

results6.txt: input6.txt image60.jpg image61.jpg
	python catception_analyze_video.py input6.txt image60.jpg image61.jpg | tee results6.txt

input7.txt: input6.txt image60.jpg image61.jpg results6.txt
	python catception_new_prompt.py input6.txt image60.jpg image61.jpg | tee input7.txt

# 7

generate7.json: input7.txt
	python catception_generate_video.py input7.txt video7.mp4 | tee generate7.json

get7.json: generate7.json
	python catception_get_video.py generate7.json | tee get7.json

video7.mp4: get7.json
	cut -f 3 -d " " get7.json | xargs wget -O video7.mp4
	touch video7.mp4

image70.jpg: video7.mp4
	ffmpeg -i video7.mp4 -ss 0 -vframes 1 image70.jpg

image71.jpg: video7.mp4
	ffmpeg -i video7.mp4 -ss 1 -vframes 1 image71.jpg

results7.txt: input7.txt image70.jpg image71.jpg
	python catception_analyze_video.py input7.txt image70.jpg image71.jpg | tee results7.txt

input8.txt: input7.txt image70.jpg image71.jpg results7.txt
	python catception_new_prompt.py input7.txt image70.jpg image71.jpg | tee input8.txt

# 8

generate8.json: input8.txt
	python catception_generate_video.py input8.txt video8.mp4 | tee generate8.json

get8.json: generate8.json
	python catception_get_video.py generate8.json | tee get8.json

video8.mp4: get8.json
	cut -f 3 -d " " get8.json | xargs wget -O video8.mp4
	touch video8.mp4

image80.jpg: video8.mp4
	ffmpeg -i video8.mp4 -ss 0 -vframes 1 image80.jpg

image81.jpg: video8.mp4
	ffmpeg -i video8.mp4 -ss 1 -vframes 1 image81.jpg

results8.txt: input8.txt image80.jpg image81.jpg
	python catception_analyze_video.py input8.txt image80.jpg image81.jpg | tee results8.txt

input9.txt: input8.txt image80.jpg image81.jpg results8.txt
	python catception_new_prompt.py input8.txt image80.jpg image81.jpg | tee input9.txt

# 9

generate9.json: input9.txt
	python catception_generate_video.py input9.txt video9.mp4 | tee generate9.json

get9.json: generate9.json
	python catception_get_video.py generate9.json | tee get9.json

video9.mp4: get9.json
	cut -f 3 -d " " get9.json | xargs wget -O video9.mp4
	touch video9.mp4

image90.jpg: video9.mp4
	ffmpeg -i video9.mp4 -ss 0 -vframes 1 image90.jpg

image91.jpg: video9.mp4
	ffmpeg -i video9.mp4 -ss 1 -vframes 1 image91.jpg

results9.txt: input9.txt image90.jpg image91.jpg
	python catception_analyze_video.py input9.txt image90.jpg image91.jpg | tee results9.txt

clean:
	mv video*.mp4 input*.txt generate*.json get*.json image* results* save
