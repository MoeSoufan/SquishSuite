import login, studyFunctions, loadStudy, cvi42Objects, report42, sys, biplanarLAX, short3d, flowModule, drawContours
import random
import time
        
# def for_each_call(frame, event, arg):
#     snooze(0.01)
#      
# def init():
#     sys.setprofile(for_each_call)
#     
def main():
    attachToApplication("MyApplicationAttachable")
    login.login("moe", "moonshine")
    list = ["4D\n Flow", "4D\n Viewer", "Biplanar\n LAX", "Flow", "Patient\n Data", 
            "Report", "MPR", "Multiple\n Long LAX", "Perfusion", "T1",
            "T2", "Tissue\n Char", "Tissue\n Tracking", "Vascular", "Viewer", "Series\n Overview"]
    
#     loadStudy.load("Functions1")
    studyFunctions.reset_workspace()
    
    i = 0
    for x in range(50000):
        module = random.choice(list)

        start = time.time()
        studyFunctions.click_module(module)
        end = time.time()
         
        if i == 0:
            module = module.replace('\n', ' ')
            if end-start > 1.0:
                test.log("%s module load time = %.2f" %(module, end-start)) 
            oldModule = module
        else:
            oldModule = oldModule.replace('\n', ' ')
            module = module.replace('\n', ' ')
            if end-start > 1.0:
                test.log("From %s -> %s = %.2f " %(oldModule, module, end-start))
            oldModule = module
        i += 1

            
#     for child in object.children(waitForObject(":Primary Study.blackBackground_QWidget")):
#         for kid in child:
#             test.log("%s"%kid)
    
#     clickButton(waitForObject(":Primary Study.seriesPreview_SeriesPreview")
#     :Primary Study.seriesPreview_SeriesPreview_2
    
    
#     status = ":cmr42MainWindow.cmr42StatusBar_QStatusBar"
#     if object.exists(status) is True:
#         test.log("yes")
#     else:
#         activateItem(waitForObjectItem(":cmr42MainWindow.appMenuBar_QMenuBar", "View"))
#         activateItem(waitForObjectItem(":cmr42MainWindow.viewMenu_QMenu", "Hide Status Bar"))
#     user = ":cmr42MainWindow.mLicenseStatusLabel_QLabel"
#     server = ":cmr42MainWindow.connectionStatusLabel_QLabel"
    
#     for name, value in object.properties(waitForObject(user)).iteritems():
#         if name == "text":
#             test.log("Users = %s"%value)
#             break
#     for name, value in object.properties(waitForObject(server)).iteritems():
#         if name == "text":
#             test.log("Users = %s"%value)
#             break