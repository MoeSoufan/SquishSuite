import sys
import studyFunctions, drawContours, short3d

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)
    
def main():
    
#     startApplication("cvi42")
    attachToApplication("MyApplicationAttachable")
    
    studyFunctions.click_module("Short\n 3D")
    studyFunctions.load_series("short3d", 1)
    
    ml_button_list = ["Detect LV Endo/Epi Contours Current Phase", 
                      "Detect LV Endo Contours Current Phase",
                      "Detect LV Endo/Epi Contours Entire Stack",
                      "Detect LV Endo Contours Entire Stack",
                      "Detect RV Contours Current Phase",
                      "Detect RV Contours Entire Stack"]
    
    for item in ml_button_list:
        short3d.click_ml(item)
        studyFunctions.reset_workspace()
