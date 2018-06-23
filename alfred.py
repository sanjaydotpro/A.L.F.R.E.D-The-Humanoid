# A.L.F.R.E.D main libraries and modules 
import speech_recognition as sr 

# A.L.F.R.E.D supporting modules 


rs = sr.Recognizer()
with sr.Microphone() as source:
    print("######### CALIBARATING NOISE LEVEL #############")
    rs.adjust_for_ambient_noise(source,duration=float(2))
    # Conversation loop
    while True:
        print("######### CALIBARATING NOISE LEVEL #############")
        rs.adjust_for_ambient_noise(source,duration=float(2))
        print('Speak ALFRED is listening......')
        spoken_text = rs.listen(source)
        print('Done Recording')

        try:
            print('Sending the data to the API')
            text_recieved = rs.recognize_google(spoken_text)
            print("You said :",text_recieved.lower())
        except:
            print('A.L.F.R.E.D could\'t understand what you said')