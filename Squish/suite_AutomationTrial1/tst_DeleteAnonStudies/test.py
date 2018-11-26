import sys
import studyFunctions, loadStudy

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)
    
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
     
    studyFunctions.delete_study("Automation-Annulus")
    studyFunctions.delete_study("Automation-4DFlow")
    studyFunctions.delete_study("Automation-FuncFlow")