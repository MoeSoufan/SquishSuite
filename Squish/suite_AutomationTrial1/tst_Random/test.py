import login, studyFunctions, loadStudy, cvi42Objects, report42, sys, biplanarLAX, short3d, flowModule, drawContours
import random
import time

def main():
    
    attachToApplication("MyApplicationAttachable")
    login.login("moe", "moonshine")
#     snooze(3)
    
#     loadStudy.load("Function-Flow-Perfusion")         

    
    for x in range(1000):
        studyFunctions.load_series("short3d", 1)
        studyFunctions.reset_workspace()
        
#         drawContours.lineContour("viewer1")
        
#         start = time.time()
#         studyFunctions.click_module("Short\n 3D")
#         end = time.time()
#         test.log("Time %.2f" %(end - start))
#         studyFunctions.click_module("Viewer")
    
#     for x in range(2):
#         loadStudy.load("Function-Flow-Perfusion")
#         
#         start = time.time()
#         studyFunctions.click_module("Short\n 3D")
#         end = time.time()
#         test.log("Time to load module %.2f" %(end-start))
#         
#         studyFunctions.load_series("short3d", 1)
#         short3d.click_ml("Detect LV Endo/Epi Contours Entire Stack")
#         studyFunctions.reset_workspace()
#         
#         studyFunctions.load_series("short3d", 1)
#         short3d.click_ml("Detect LV Endo/Epi Contours Entire Stack")
#         studyFunctions.reset_workspace()
#         studyFunctions.close_study()