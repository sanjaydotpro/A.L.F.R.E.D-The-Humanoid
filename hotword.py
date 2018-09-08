import snowboydecoder
import importlib


def detected_callback():
    print "hotword detected"
    importlib.import_module("alfred")
    import alfred
    alfred.order_for_alfred()
detector = snowboydecoder.HotwordDetector("hey_alfred.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
