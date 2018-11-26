import sys
import studyFunctions, drawContours, biplanarLAX

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)
    
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
    
    studyFunctions.click_module("Biplanar\n LAX")
    
    studyFunctions.load_series("2cv", 2)
    studyFunctions.load_series("4cv", 3)

    biplanarLAX.ml_button()
    studyFunctions.reset_workspace()