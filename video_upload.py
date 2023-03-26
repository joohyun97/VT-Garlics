import streamlit as st
# from moviepy.editor import 
import video_converter as vc

def video_uploader():
    # converting from video extension to .wav
    video_file = st.file_uploader("Upload video file", type=["mp4", "avi", "mov"])

    # convert video to wav file
    if video_file is not None:
        if video_file.name.endswith(("mp4", "avi", "mov")):
            upload_voice = st.button(label='Upload Voice')
            
            if upload_voice:
                path_to_file = 'resources/video/'
                file_name = f'{path_to_file}{video_file.name}'
                with open(file_name, 'wb') as f:
                    f.write(video_file.getbuffer())
                    f.close()
                    
                    
            # extract the video to a wav file
                vc.video_to_wav(path_to_file, video_file.name)
        else:
            st.warning("Invalid file type. Please upload an MP4, AVI, or MOV")