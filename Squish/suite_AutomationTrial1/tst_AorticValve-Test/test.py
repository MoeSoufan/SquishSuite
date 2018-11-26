import studyFunctions, ctModules
import sys 

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)
    
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
    
    studyFunctions.click_module("Aortic\n Valve", True)
     
    studyFunctions.load_series("aortic1", 1)

    ctModules.aortic_tricuspid()
    ctModules.aortic_annulus()
    
    
