# import streamlit as st
import azure.cognitiveservices.speech as acs


def audio_output(title, text):
    wav_file = f"resources/tales/{title}.wav"
    # can find diff langs here:
    # https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt
    
    #  https://stackoverflow.com/questions/72147776/how-to-integrate-azure-text-to-speech-with-streamlit
    speech_config = acs.SpeechConfig(subscription="ea5e1d6756c54c349a1b40e5eb18c436", region="eastus")
    speech_config.speech_synthesis_voice_name='en-US-JasonNeural'
    audio_config = acs.audio.AudioOutputConfig(use_default_speaker=True, filename=wav_file)

    # https://stackoverflow.com/questions/74376903/azure-text-to-speech-and-play-it-in-virtual-microphone-using-python
    speech_synthesizer = acs.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    stream = acs.AudioDataStream(speech_synthesis_result)
    stream.save_to_wav_file(wav_file)
         
