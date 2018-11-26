import sys
import studyFunctions, loadStudy

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)
    
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
     
    studyFunctions.anonymize_study("4D\\_066", "Automation-4DFlow")
     
    loadStudy.load("Automation-4DFlow")
    
    studyFunctions.click_module("4D\n Flow")
#     
    studyFunctions.load_series("4d flow", 1)
    
#     mouseClick(waitForObject(":Flow4dPrepOptionsFrame.mConfirmRoiPushButton_QPushButton"))
#     time = studyFunctions.loading_time()
#     test.log("4D Flow %.2f" % time)
#     
    studyFunctions.close_study()