import speech_recognition as sr
import os
import pyttsx3
import openai

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key ="your_api_key"

engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


r=sr.Recognizer()

# with sr.Microphone() as source:
#     print("Say Something")
#     audio = r.listen(source)
    # try:
    #         text = r.recognize_google(audio, language='es-ES')
    #         print("You said: " + text)
    #     except sr.UnknownValueError:
    #         print("Google Speech Recognition could not understand audio")
    #     except sr.RequestError as e:
    #         print("Could not request results from Google Speech Recognition service; {0}".format(e))
with sr.Microphone(device_index=1, sample_rate=48000) as source:
    print("Say Something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)    
    try:
        text = r.recognize_google(audio, language='es-PE')
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# completion=openai.Completion.create(engine="gpt-3.5-turbo",
#                                       prompt=text,
#                                       max_tokens="2048")


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  max_tokens=2048,
)
engine.say(response.choices[0].text)
engine.runAndWait()

engine.save_to_file(text, 'speech.mp3')
engine.runAndWait()
    # try:
    #     text=r.recognize_google(audio)
    #     print("What did you say: {}".format(text))
    # except: 
    #     print("I'm sorry! I can't understand")
