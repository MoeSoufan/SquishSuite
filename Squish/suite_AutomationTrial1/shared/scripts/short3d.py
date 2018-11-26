# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish
import studyFunctions

def click_ml(button):
    
    toolBarObject = ":cmr42MainWindow.ToolBar_QToolBar"
    contextWindow = ":cmr42MainWindow_QMenu"
    
#     # If button exists in toolbar, clicks otherwise, find button
#     children = find_children_by_text(squish.waitForObject(toolBarObject), button)
    
    contextButton = find_context_menu(button)
    squish.openContextMenu(squish.waitForObject(contextButton), 30, 20, 0)
    squish.activateItem(squish.waitForObjectItem(contextWindow, button))
#         squish.snooze(1)
    
    squish.clickButton(squish.waitForObject(contextButton))

    # Wait for progress bar 
    time = studyFunctions.loading_time()
 
    test.log("Short3d %s: %.2f "% (button, time))
    return
    
    
def find_context_menu(button):
    
    machine_butto = {"Detect Endo/Epi Contours Current Phase"   : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Endo/Epi Contours Current Slice"   : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Endo/Epi Contours Entire Stack"    : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Endo/Epi Contours Current Image"   : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Endo Contours Current Phase"       : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Endo Contours Current Slice"       : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Endo Contours Entire Stack"        : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Epi Contours Current Phase"        : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Epi Contours Current Slice"        : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect Epi Contours Entire Stack"         : ":mContourDetectionMrTools.MrButton_SwitchingToolButton",
                     "Detect RV Contours Current Phase"         : ":mContourDetectionMrTools.RvButton_SwitchingToolButton",
                     "Detect RV Contours Current Slice"         : ":mContourDetectionMrTools.RvButton_SwitchingToolButton",
                     "Detect RV Contours Entire Stack"          : ":mContourDetectionMrTools.RvButton_SwitchingToolButton",
                     "Detect LV/RV Contours at ED/ES Phases"    : ":mContourDetectionMrMlTools.mlButton_SwitchingToolButton",
                     "Detect LV/RV Contours Current Phase"      : ":mContourDetectionMrMlTools.mlButton_SwitchingToolButton",
                     "Detect LV/RV Contours Entire Stack"       : ":mContourDetectionMrMlTools.mlButton_SwitchingToolButton",
                     "Detect LV/RV Contours Current Slice"      : ":mContourDetectionMrMlTools.mlButton_SwitchingToolButton",
                     "Detect LV/RV Contours Current Image"      : ":mContourDetectionMrMlTools.mlButton_SwitchingToolButton",
                     "Detect LV Endo/Epi Contours Current Phase": ":mContourDetectionMrMlTools.mlLvButton_SwitchingToolButton",
                     "Detect LV Endo Contours Current Phase"    : ":mContourDetectionMrMlTools.mlLvButton_SwitchingToolButton",
                     "Detect LV Endo/Epi Contours Entire Stack" : ":mContourDetectionMrMlTools.mlLvButton_SwitchingToolButton",
                     "Detect LV Endo Contours Entire Stack"     : ":mContourDetectionMrMlTools.mlLvButton_SwitchingToolButton",
                     "Detect RV Contours Current Phase"         : ":mContourDetectionMrMlTools.mlRvButton_SwitchingToolButton",
                     "Detect RV Contours Entire Stack"          : ":mContourDetectionMrMlTools.mlRvButton_SwitchingToolButton"}
    
    for key, value in machine_butto.iteritems():
        if key == button:
            return value
#     for filtered_button in [k for k, v in machine_butto.items() if v == machine_butto[button]]:
#          test.log("%s ,%s" % (k,v))
         
            
    
def find_children_by_text(obj, text, max_count=1):
    children = object.children(obj)
    found_children=[]
 
    # Add immediate children:
    for c in children:
        if hasattr(c, "text") and c.text == text:
            found_children.append(c)
            if max_count is not None and len(found_children) >= max_count:
                return found_children
 
    # Add grand children:
    for c in children:
        found_children.extend(find_children_by_text(c, text))
        if max_count is not None and len(found_children) >= max_count:
            found_children = found_children[:max_count]
            break
    return found_children