import sys
import studyFunctions

def for_each_call(frame, event, arg):
    snooze(0.1)
  
def init():
    sys.setprofile(for_each_call)
#     
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
    
    study = studyFunctions.anonymize_study("Function-Flow-Perfusion", "Automation-FuncFlow")
 
    loadStudy.load(study)
