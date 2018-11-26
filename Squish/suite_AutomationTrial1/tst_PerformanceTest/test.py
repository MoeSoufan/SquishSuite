import login, studyFunctions, short3d, biplanarLAX, ctModules, cvi42Objects, drawContours
import sys, os, subprocess

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)

def the_test():
    
    startApplication("cvi42")
#     attachToApplication("MyApplicationAttachable")
    
    # Login
    login.login("moeadmin", "absinthe")
    
    # Anonymize and load Function-Flow-Perfusion
    study_mr = studyFunctions.anonymize_study("Function-Flow-Perfusion", "Automation-FuncFlow")
    loadStudy.load(study_mr)
    
    # Short3D entire stack ML 
    studyFunctions.click_module("Short\n 3D")
    studyFunctions.load_series("short3d", 1)
    short3d.click_ml("Detect LV Endo/Epi Contours Entire Stack")

    # BiplanarLAX entire stack ML
    studyFunctions.click_module("Biplanar\n LAX")
    studyFunctions.load_series("2cv", 2)
    studyFunctions.load_series("4cv", 3)
    biplanarLAX.ml_button()
    
    # Close MR study
    studyFunctions.close_study()
    
    # Anonymize and load Annulus-016
    study_ct = studyFunctions.anonymize_study("Annulus-016 (Anonymize This for Load Tests)", "Automation-Annulus")
    loadStudy.load(study_ct, True)
    
    # Click and load ct study in 4D viewer
    studyFunctions.click_module("4D\n Viewer", True)
    studyFunctions.load_series("4d", 1)
    studyFunctions.close_study()
    
    # Anonymize and load 4d flow study
    study_4d = studyFunctions.anonymize_study("4D\\_066", "Automation-4DFlow")
    loadStudy.load(study_4d)
    studyFunctions.click_module("4D\n Flow")
    studyFunctions.load_series("4d flow", 1)
    studyFunctions.close_study()
    
    # Delete anon studies
    studyFunctions.delete_study(study_mr)
    studyFunctions.delete_study(study_ct)
    studyFunctions.delete_study(study_4d)

def main():
    counter = 0
    while True:
        try:
            the_test()
            counter += 1
            
            if counter == 1:
                raise
            
            if counter == 100:
                break
            
        except Exception, E:
            test.log("Error: %s" % E)
            counter -= 1
            os.system("taskkill /im cvi42.exe")
            os.system("taskkill /im startaut.exe")
            snooze(10)
            os.system("taskkill /im cvi42.exe")
            os.system("taskkill /im startaut.exe")
            snooze(10)
            
    