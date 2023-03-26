import subprocess
import os

# https://you.com/search?q=mp4+to+wav+python&tbm=youchat&cfr=chatb&cid=c2_78723c07-236e-4daf-8023-333969648460

def video_to_wav(path_to_input, input_vid):
# set the path to the input MP4 file and output WAV file
    name, ext = os.path.splitext(input_vid)
    output_audio = f'{name}.wav'
    # output_audio = f'resources/video_to_wav/{name}.wav'
    input_video = f'{path_to_input}{input_vid}'

    # use FFmpeg to convert MP4 to WAV
    subprocess.run(['ffmpeg', '-i', input_video, '-acodec', 'pcm_s16le', '-ar', '44100', output_audio])
    
    
