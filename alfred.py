# A.L.F.R.E.D main libraries and modules 
import speech_recognition as sr 
import pyttsx3 as px

# A.L.F.R.E.D supporting modules


#for text to speech
engine = px.init()
engine.setProperty('rate', 125)  # 125 words per minute
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')



rs = sr.Recognizer()
with sr.Microphone() as source:
    print("######### CALIBARATING NOISE LEVEL #############")
    rs.adjust_for_ambient_noise(source,duration=float(2))
    # Conversation loop
    while True:
        print("######### CALIBARATING NOISE LEVEL #############")
        rs.adjust_for_ambient_noise(source,duration=float(5))
        print('Speak ALFRED is listening......')
        #for female voice uncomment these below 2 lines
        #for voice in voices:
        #    engine.setProperty('voice', voice.id)
        engine.say("I am Listening")
        engine.runAndWait()
        spoken_text = rs.listen(source)
        print('Done Recording')

        try:
            print('Sending the data to the API')
            text_recieved = rs.recognize_google(spoken_text)
            print("You have said :",text_recieved.lower())
            engine.say("You have said ")
            engine.runAndWait()
            engine.say(text_recieved)
            engine.runAndWait()

        except:
            print('A.L.F.R.E.D could\'t understand what you said')
            engine.say("Sorry,I couldnot understand what you have said")
            engine.runAndWait()
            spoken_text = rs.listen(source)
