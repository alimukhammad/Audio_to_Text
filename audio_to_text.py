
import speech_recognition as sr # importing required library

r = sr.Recognizer() #creating a class to recognize the speech

with sr.AudioFile('audio_files_harvard.wav') as source: #open the audio_files_harvard.wav -> assign it to sourse
    audio_text = r.listen(source) # listen to the audio file and store the audio data in the audio_text variable

    try:
        text = r.recognize_google(audio_text) #google speech recognition service to convert to the audio data then assign to text
        print('Converting audio transcripts into text ') # print
        print('--' + text) #print
    except:
        print('Pardon... Can you repeat') # if try fails -> print
