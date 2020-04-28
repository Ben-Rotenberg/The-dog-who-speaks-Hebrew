import time
import speech_recognition as sr
from googletrans import Translator
from monkeylearn import MonkeyLearn
monkeylearn_key = MonkeyLearn('500b6a2c68c8fef2679991a11402e281bcfaef2f')

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        audio = recognizer.record(source,  duration = 3)
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

def print_dog(mood):
    print('\n' * 100)
    if mood == 'happy':
        print('שמח!')
        print('')
        print('')
        print('╭━┳━╭━╭━╮╮')
        print('┃┈┈┈┣▉╋▉┫┃')
        print('┃┈┃┈╰━╰━━━━━━╮')
        print('╰┳╯┈┈┈┈┈┈┈┈◢▉◣')
        print('╲┃┈┈┈┈┈┈┈┈┈▉▉▉')
        print('╲┃┈┈┈┈┃┈┈┈┈◥▉◤')
        print('╲┃┈┈┈┈╰━┳━━━━╯')
        time.sleep(3)

    elif mood == 'sad':
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

    elif mood == 'neutral':
        print('ניטרלי')
        print('')
        print('')
        print('╭━┳━╭━╭━╮╮')
        print('┃┈┈┈┣▉╋▉┫┃')
        print('┃┈┃┈╰━╰━━━━━━╮')
        print('╰┳╯┈┈┈┈┈┈┈┈◢▉◣')
        print('╲┃┈┈┈┈┈┈┈┈┈▉▉▉')
        print('╲┃┈┈┈┈┈┈┈┈┈◥▉◤')
        print('╲┃┈┈┈┈┈━┳━━━━╯')
        time.sleep(3)

    elif mood == 'listening':
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

    elif mood == 'thinking':
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

    elif mood == 'sleeping':
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

dog_awake = True
while dog_awake == True:
    print_dog('listening')
    speech_to_text = recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
    print_dog('thinking')

    translation = translator(speech_to_text, Translator()).text

    if "sleep" in translation:
        dog_awake = False
        break

    sentiment = (sentiment_analysis(translation, monkeylearn_key))

    if sentiment == 'Positive':
        print_dog('happy')
    elif sentiment == 'Negative':
        print_dog('sad')
    else:
        print_dog('neutral')

print_dog('sleeping')
