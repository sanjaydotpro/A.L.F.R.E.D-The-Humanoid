#!/usr/bin/python

print()
print("checking for nltk")
try:
    import nltk
except ImportError:
    print("you should install nltk before continuing")

print("checking for speech_recognition")
try:
    import speech_recognition
except ImportError:
    print("you should install speech_recognition before continuing")

print("checking for scipy")
try:
    import scipy
except:
    print("you should install scipy before continuing")

print("checking for sklearn")
try:
    import sklearn
except:
    print("you should install sklearn before continuing")