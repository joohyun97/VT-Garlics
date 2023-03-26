# import streamlit as st
import azure.cognitiveservices.speech as acs


def audio_output(text):
    #  https://stackoverflow.com/questions/72147776/how-to-integrate-azure-text-to-speech-with-streamlit
    speech_config = acs.SpeechConfig(subscription="9b1677e9472e4b1c8f6b235b8b1d9bf2", region="eastus")
    audio_config = acs.audio.AudioOutputConfig(use_default_speaker=True, filename="file.wav")

    #https://stackoverflow.com/questions/74376903/azure-text-to-speech-and-play-it-in-virtual-microphone-using-python
    speech_synthesizer = acs.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    stream = acs.AudioDataStream(speech_synthesis_result)
    stream.save_to_wav_file("file.wav")

    # mixer.init(devicename = 'Line 1 (Virtual Audio Cable)')
    # mixer.music.load("file.wav")
    # mixer.music.play()

    # if speech_synthesis_result.reason == acs.ResultReason.SynthesizingAudioCompleted:
    #     st.write("Speech synthesized for text [{}]".format(text))
    # elif speech_synthesis_result.reason == acs.ResultReason.Canceled:
    #     cancellation_details = speech_synthesis_result.cancellation_details
    #     st.write("Speech synthesis canceled: {}".format(cancellation_details.reason))
    #     if cancellation_details.reason == acs.CancellationReason.Error:
    #         if cancellation_details.error_details:
    #             st.write("Error details: {}".format(cancellation_details.error_details))
    #             st.write("Did you set the speech resource key and region values?")
       
         
# st.title("Let's learn Math!")
# text = st.text_input("Enter text", value="Hi")
