# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish

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


def click_ml(button):
    
    toolBarObject = ":cmr42MainWindow.ToolBar_QToolBar"
    contextWindow = "cmr42MainWindow_QMenu"
    
    # If button exists in toolbar, clicks otherwise, find button
    children = find_children_by_text(squish.waitForObject(toolBarObject), button)
#     
    try:
        squish.mouseClick(children[0])
    except RuntimeError:
        contextButton = find_context_menu(button)
#         squish.openContextMenu(squish.waitForObject(":mContourDetectionMrMlTools.mlLvButton_SwitchingToolButton")
        # activateItem(waitForObjectItem(":cmr42MainWindow_QMenu", "Detect LV Endo/Epi Contours Entire Stack"))

        test.log("no")
        
        
    return
    
    
def find_context_menu(button):
    
    machine_butto = {"Detect Endo/Epi Contours Current Phase": 1,
                     "Detect Endo/Epi Contours Current Slice": 1,
                     "Detect Endo/Epi Contours Entire Stack": 1,
                     "Detect Endo/Epi Contours Current Image": 1,
                     "Detect Endo Contours Current Phase": 1,
                     "Detect Endo Contours Current Slice": 1,
                     "Detect Endo Contours Entire Stack": 1,
                     "Detect Epi Contours Current Phase": 1,
                     "Detect Epi Contours Current Slice": 1,
                     "Detect Epi Contours Entire Stack": 1,
                     "Detect RV Contours Current Phase": 2,
                     "Detect RV Contours Current Slice": 2,
                     "Detect RV Contours Entire Stack": 2,
                     "Detect LV/RV Contours at ED/ES Phases": 3,
                     "Detect LV/RV Contours Current Phase": 3,
                     "Detect LV/RV Contours Entire Stack": 3,
                     "Detect LV/RV Contours Current Slice": 3,
                     "Detect LV/RV Contours Current Image": 3,
                     "Detect LV Endo/Epi Contours Current Phase": 4,
                     "Detect LV Endo Contours Current Phase": 4,
                     "Detect LV Endo/Epi Contours Entire Stack": 4,
                     "Detect LV Endo Contours Entire Stack": 4,
                     "Detect RV Contours Current Phase": 5,
                     "Detect RV Contours Entire Stack": 5}
    
#     if object.exists(waitF)
# 
# openContextMenu(waitForObject(":mContourDetectionMrMlTools.mlLvButton_SwitchingToolButton"), 25, 20, 0)
# activateItem(waitForObjectItem(":cmr42MainWindow_QMenu", "Detect LV Endo/Epi Contours Entire Stack"))


# :mContourDetectionMrMlTools.mlLvButton_SwitchingToolButton