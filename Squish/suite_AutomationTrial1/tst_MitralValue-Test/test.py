import studyFunctions, ctModules
import sys 

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)
    
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
     
    studyFunctions.click_module("Mitral\n Valve", True)
    ctModules.mitral_define_annulus()
     
    ctModules.mitral_measurement_capture()