#!/usr/bin/python
from gtts import gTTS
import speech_recognition as sr
import pyttsx3             # use pyttsx3 instead 
from nltk.tokenize import word_tokenize as wtk
from nltk.tokenize import sent_tokenize as srtk
import random as ran
import os


# A.L.F.R.E.D Modules
import random_music_play_feature as rmpf
import wolframalpha_feature as wf
import wikipedia_feature as wkf
import news_api as nap
import browser_feature as bf
import youtube_feature as yf
import book_api as bap




# Global list
opening_phrases = ['Welcome','How May I help You','Welcome, How may I help You','At your service, sir']
exit_when_done = ['thats all alfred','exit','exit now alfred','close alfred','thank you alfred']
command_acknowledgement = ['Sure, sir','give me a second','anything for you, sir']


# this function takes recived sentence as an input and returns the task performing word as an output
def task_performing_word(input_sent):
    input_list = wtk(input_sent)
    task_word = ''
    
    if 'book' in input_list:
        task_word = 'book'
    elif 'news' in input_list:
        task_word = 'news'
    elif ('search' in input_list or 'look' in input_list) and ('wikipedia' in input_list) :
        task_word = 'wikipedia'
    elif ( 'song' in input_list )or ( 'bored' in input_list):
        task_word = 'song'
    elif ( 'search' in input_list ) and ('youtube' in input_list):
        task_word = 'youtube'
    elif ('search' in input_list) or ('look' in input_list):
        task_word = 'browser'
    else:
        task_word = 'wolf'
    return task_word

def order_for_alfred():
    rs = sr.Recognizer()
    with sr.Microphone() as source:
    # Conversation loop
        while True:
            print("######### CALIBARATING NOISE LEVEL #############")
            rs.adjust_for_ambient_noise(source,duration=float(2))
	    os.system("aplay /home/adhanai1419/Documents/Pythonprojects/A.L.F.R.E.D-THEHUMANOIDROBOT/resources/ding.wav")
	    #GTTS
	    tts = gTTS(ran.choice(opening_phrases))	
	    tts.save("GTTSAudio.mp3")
	    os.system('mpg321 GTTSAudio.mp3 -quiet')	

            audi = rs.listen(source)

            #GTTS
	    tts = gTTS(ran.choice(command_acknowledgement))	
	    tts.save("GTTSAudio.mp3")
	    os.system('mpg321 GTTSAudio.mp3 -quiet')

            try:
                print('Sending data to API')
                text_recieved = rs.recognize_google(audi)
                text_recieved = text_recieved.lower()
                print(text_recieved)
            except sr.UnknownValueError:
		#GTTS
		tts = gTTS("Beg your pardon, sir")	
		tts.save("GTTSAudio.mp3")
		os.system('mpg321 GTTSAudio.mp3 -quiet')
                continue
            except sr.RequestError:
		#GTTS
		tts = gTTS("Unable to make request to google check your internet connection")	
		tts.save("GTTSAudio.mp3")
		os.system('mpg321 GTTSAudio.mp3 -quiet')
                continue
            
            if text_recieved.lower() in exit_when_done:
		#GTTS
		tts = gTTS("Exiting Now")	
		tts.save("GTTSAudio.mp3")
		os.system('mpg321 GTTSAudio.mp3 -quiet')
                break
            else:
                finl_task = task_performing_word(text_recieved)
            
            if finl_task == 'song':
                ctr = rmpf.play_random_music()
                if ctr == 1:
		    #GTTS
		    tts = gTTS("Hope You like it")	
		    tts.save("GTTSAudio.mp3")
		    os.system('mpg321 GTTSAudio.mp3 -quiet')
                    break
                else:
                    print("Enter the correct path to your music directory in random_music_play_feature.py file")
                    break

            elif finl_task == 'wolf':
                answer = wf.wolframalpha_questions(text_recieved)
                if answer == 0 or answer == 'none':
		    #GTTS
		    tts = gTTS("Sorry, I dont know about it.")	
		    tts.save("GTTSAudio.mp3")
		    os.system('mpg321 GTTSAudio.mp3 -quiet')
                    break
                else:
		    #GTTS
		    tts = gTTS(answer)	
		    tts.save("GTTSAudio.mp3")
		    os.system('mpg321 GTTSAudio.mp3 -quiet')
                    break

            elif finl_task == 'wikipedia':
                topic = wkf.give_me_topic_name(text_recieved)
                short_summary = wkf.get_short_summary(topic)
                print(short_summary)
		#GTTS
		tts = gTTS("Showing results on your screen,Sir")	
		tts.save("GTTSAudio.mp3")
		os.system('mpg321 GTTSAudio.mp3 -quiet')
                break
                    

            elif finl_task == 'browser':
                bf.browser_search(text_recieved)
		#GTTS
		tts = gTTS("Showing search result on the browser,Sir")	
		tts.save("GTTSAudio.mp3")
		os.system('mpg321 GTTSAudio.mp3 -quiet')
                break

            elif finl_task == 'youtube':
                yf.open_video_youtube(text_recieved)
		#GTTS
		tts = gTTS("Opening the results on your browser,Sir.")	
		tts.save("GTTSAudio.mp3")
		os.system('mpg321 GTTSAudio.mp3 -quiet')
                break

            elif finl_task == 'news':
                news_cat,news_name = nap.give_me_news_name(text_recieved)
                if news_cat == 'category':         # Not working properly
                    nap.get_by_category(news_name)
                elif news_cat == 'from':
                    nap.get_by_source(news_name)
                elif news_cat == 'on' or news_cat == 'of':
                    nap.get_by_query(news_name)
                else:
		    #GTTS
		    tts = gTTS("Sorry, Sir I couldn\'t find any relevant news")	
		    tts.save("GTTSAudio.mp3")
		    os.system('mpg321 GTTSAudio.mp3 -quiet')
                break
    return 


