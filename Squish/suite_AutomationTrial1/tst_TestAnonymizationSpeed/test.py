import login, studyFunctions, loadStudy, cvi42Objects, report42, sys, biplanarLAX, short3d, flowModule, drawContours, flowAnalysisModule
import random
import time

def main():
    
    attachToApplication("MyApplicationAttachable")
    login.login("moe", "moonshine")
    
    for x in range(10):
        # Anonymize study
        anon_study = studyFunctions.anonymize_study("Concurrency-Test1", "Concurrency-Test2")
        
        login.login("moe", "moonshine")
#         # Delete study
#         studyFunctions.delete_study(anon_study)
#         
#         snooze(2)

