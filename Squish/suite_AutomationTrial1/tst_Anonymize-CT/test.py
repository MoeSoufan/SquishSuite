import studyFunctions
import sys 

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)
    
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
    
    study = studyFunctions.anonymize_study("Annulus-016 (Anonymize This for Load Tests)", "Automation-Annulus")
    
    loadStudy.load(study, True)