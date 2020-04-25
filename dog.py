import time
import speech_recognition as sr
from googletrans import Translator
from monkeylearn import MonkeyLearn
monkeylearn_key = MonkeyLearn('<my_key')


def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration = 0.5)
        audio = recognizer.record(source,  duration = 4)
    try:
        transcription = recognizer.recognize_google(audio, language= 'he-IL')
    except:
        transcription = '-'

    return (transcription)

def translator(original_text,translator):
    return translator.translate(original_text, src='iw', dest='en')

def sentiment_analysis(speech_to_text,ml_k):
    analysis = ml_k.classifiers.classify(model_id='cl_Jx8qzYJh', data=[speech_to_text])
    return analysis.body[0]['classifications'][0]['tag_name']

def print_happy():
    print('\n'*100)
    print ('שמח!')
    print ('')
    print('')
    print ('╭━┳━╭━╭━╮╮')
    print ('┃┈┈┈┣▉╋▉┫┃')
    print ('┃┈┃┈╰━╰━━━━━━╮')
    print ('╰┳╯┈┈┈┈┈┈┈┈◢▉◣')
    print ('╲┃┈┈┈┈┈┈┈┈┈▉▉▉')
    print ('╲┃┈┈┈┈┃┈┈┈┈◥▉◤')
    print ('╲┃┈┈┈┈╰━┳━━━━╯')
    time.sleep(3)


def print_sad():
    print('\n'*100)
    print('עצוב')
    print('')
    print('')
    print('╭━┳━╭━╭━╮╮')
    print('┃┈┈┈┣▅╋▅┫┃')
    print('┃┈┃┈╰━╰━━━━━━╮')
    print('╰┳╯┈┈┈┈┈┈┈┈◢▉◣')
    print('╲┃┈┈┈┈┈┈┈┈┈▉▉▉')
    print('╲┃┈┈┈┈┈┈┈┈┈◥▉◤')
    print('╲┃┈┈┈┈╭━┳━━━━╯')
    time.sleep(3)


def print_listening():
    print('\n'*100)
    print('מקשיב')
    print('╭━┳    ╭━┳  ')
    print('┃┈┃    ┃┈┃  ')
    print('┃┈┳━╭━╭━╮╮')
    print('╰━╯┈┣▉╋▉┫┃')
    print('┃┈┃┈╰━╰━━━━━━╮')
    print('╰┳╯┈┈┈┈┈┈┈┈◢▉◣')
    print('╲┃┈┈┈┈┈┈┈┈┈▉▉▉')
    print('╲┃┈┈┈┈┈┈┈┈┈◥▉◤')
    print('╲┃┈┈┈┈━━┳━━━━╯')


def print_thinking():
    print('\n'*100)
    print('חושב')
    print('')
    print('')
    print('╭━┳━╭━╭━╮╮')
    print('┃┈┈┈┣━╋━┫┃')
    print('┃┈┃┈╰━╰━━━━━━╮')
    print('╰┳╯┈┈┈┈┈┈┈┈◢▉◣')
    print('╲┃┈┈┈┈┈┈┈┈┈▉▉▉')
    print('╲┃┈┈┈┈┈┈┈┈┈◥▉◤')
    print('╲┃┈┈┈┈━━┳━━━━╯')



dog_mood = 0
dog_awake = True
while dog_awake == True:
    print_listening()
    speech_to_text = recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
    print_thinking()

    translation = translator(speech_to_text, Translator()).text


    if "sleep" in translation:
        dog_awake = False

    sentiment = (sentiment_analysis(translation, monkeylearn_key))
    print('sentiment:' ,sentiment)
    if sentiment == 'Positive':
        print_happy()
        dog_mood = dog_mood + 1
    elif sentiment == 'Negative':
        print_sad()
        dog_mood = dog_mood - 1
    else:
        if dog_mood > 0:
            print_happy()
            dog_mood = dog_mood - 0.5
        elif dog_mood < 0:
            print_sad()
            dog_mood = dog_mood + 0.5


print ('Good night')
print('\n' * 100)
print('ישן')
print('')
print('')
print('╭━┳━╭━╭━╮╮  z   z   z')
print('┃┈┈┈┣━╋━┫┃    z   z   z')
print('┃┈┃┈╰━╰━━━━━━╮')
print('╰┳╯┈┈┈┈┈┈┈┈◢▉◣')
print('╲┃┈┈┈┈┈┈┈┈┈▉▉▉')
print('╲┃┈┈┈┈┈┈┈┈┈◥▉◤')
print('╲┃┈┈┈┈━━┳━━━━╯')
