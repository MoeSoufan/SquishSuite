# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish

def click_module(module, ct=False):
    
    counter = 0 
    
    toolbarModuleButton = ":cmr42MainWindow.mCurrentProtocolStepButton_QToolButton"
    moduleListItem = "{container=':mWorkflowDockWidget.protocolSteps_Workflow::ProtocolStepListWidget' text='%s' type='QModelIndex'}" % module
    moduleListScrollbar = ":protocolSteps_QScrollBar"
    addProtocolButton = ":mWorkflowDockWidget.insertStep_QPushButton"
    addProtocolWindow = ":cmr42MainWindow.mModuleMenu_QMenu"

    # If the study is MR, the icon of the selected module is available in the toolbar. Checks if module already selected
    if ct == False:
        if object.exists(toolbarModuleButton) is True:
            if squish.waitForObject(toolbarModuleButton).text == module:
                test.log("Module Already Loaded")
                return
        
    while True:
        # If module not in the module list, search for it    
        if object.exists(moduleListItem) is False:
            
            if counter == 0:
                # If module list scroll bar available, mouse scroll to try and find module
                if object.exists(moduleListScrollbar):
                    # Mouse scrolls up all the way to see top of visible module list
                    squish.sendEvent("QWheelEvent", squish.waitForObject(moduleListScrollbar), 103, 527, 540, 0, 2)
    
                    # If module is visible, click it, and exit loop
                    if object.exists(moduleListItem) is True:
                        squish.mouseClick(squish.waitForObject(moduleListItem))
                        break
                    
                    # If scroll bar available, scroll down a little bit each iteration
                    squish.sendEvent("QWheelEvent", squish.waitForObject(moduleListScrollbar), 3, 307, -340, 0, 2)
                
                # If mouse scroll bar not available, pass each time
                else:
                    pass
                
            counter += 1
            
            # After four attempts, if module is not found, select it from the protocol list and click the module
            if counter == 4:
                squish.mouseClick(addProtocolButton)
                squish.activateItem(squish.waitForObjectItem(addProtocolWindow, module))
                
                squish.mouseClick(squish.waitForObject(moduleListItem))
                return
        
        # If module exists from the beginning, select it and exit                
        else:
            squish.mouseClick(squish.waitForObject(moduleListItem))
            return
        
    return


def find_window(window_name):
    
    windows_dict = {"viewer1": ":moduleFrame_DcmFrameGL",          # Viewer TopLeft
                    "viewer2": ":moduleFrame_DcmFrameGL_2",        # Viewer TopRight
                    "viewer3": ":moduleFrame_DcmFrameGL_3",        # Viewer BottomLeft
                    "viewer4": ":moduleFrame_DcmFrameGL_4",        # Viewer Bottom
                    
                    "mpr1": ":mMprFrame.mRefSuperVisFrame_SuperVisFrame",
                    "mpr2": ":mMprFrame.mRefTriPlaneMprFrames0_TriPlaneMprFrame",
                    "mpr3": ":mMprFrame.mRefTriPlaneMprFrames1_TriPlaneMprFrame",
                    "mpr4": ":mMprFrame.mRefTriPlaneMprFrames2_TriPlaneMprFrame",
                    
                    "short3d": ":saxFrame.SAX3D_DcmFrameGL",        
                    "short3dlax": ":hSplitter.Ref 1_DcmFrameGL",
                    
                    "4d": ":LayoutViewer4dHFrame.mRefSuperVisFrame_SuperVisFrame",
                    
                    "2cv": ":frame1.2CV_DcmFrameGL",
                    "4cv": ":frame2.4CV_DcmFrameGL",
                    
                    "lax": ":frame1.Multiple Long_DcmFrameGL",
                    "laxshort": ":frame2.Ref_DcmFrameGL",
                    
                    "4d flow": ":mMainPrepFrame.4D Flow_DcmFrameGL",
                    
                    "flow2": ":frame2.Magnitude_DcmFrameGL",
                    "flow1": ":frame1.Phase_DcmFrameGL",
                    
                    "mitral1": ":mMprFrame.mAxialMprFrame_TriPlaneMprFrame",
                    "mitral2": ":mMprFrame.mCoronalMprFrame_TriPlaneMprFrame",
                    "mitral3": ":mMprFrame.mSagittalMprFrame_TriPlaneMprFrame",
                    
                    "aortic1": ":mMprFrame.mRefTriPlaneMprFrames1_TriPlaneMprFrame",
                    "aortic2": ":mMprFrame.mRefTriPlaneMprFrames0_TriPlaneMprFrame",
                    "aortic3": ":mMprFrame.mRefTriPlaneMprFrames2_TriPlaneMprFrame",
                    "aortic4": ":mMprFrame.mRefSuperVisFrame_SuperVisFrame",
                    
                    "fem1": ":mMprFrame.mRefTriPlaneMprFrames0_TriPlaneMprFrame_2",
                    "fem2": ":mMprFrame.mRefTriPlaneMprFrames2_TriPlaneMprFrame_2",
                    "fem3": ":mMprFrame.mRefTriPlaneMprFrames1_TriPlaneMprFrame_2",
                    "fem4": ":mMprFrame.mRefSuperVisFrame_SuperVisFrame_2"}


    for window in [k for k, v in windows_dict.items() if v == windows_dict[window_name]]:
        properties = object.properties( squish.waitForObject(windows_dict[window]))
        
        # Search for key parameters "width" and "height"
        for name, value in properties.iteritems():
            if name == "width":
                x = value
        
            if name == "height":
                y = value
        
        return windows_dict[window], x, y
    

def load_series(window_given, series_num):
    
    series = ":scrollArea.frame-%s_SeriesThumbPreview" % (series_num-1)
    series_scrollbar = "{container=':qt_tabwidget_stackedwidget.scrollArea_QScrollArea' type='QScrollBar' unnamed='1' visible='1'}"

    window, x, y = find_window(window_given)

    # if series needed is bigger than 8, check if scrolling is needed to reach the series
    if object.exists(series_scrollbar):
        squish.scrollTo(squish.waitForObject(series_scrollbar), -505)
        if series_num > 8:
            squish.scrollTo(squish.waitForObject(series_scrollbar), 255)
    
    # Load series into window requested
    squish.mouseMove(squish.waitForObject(series), 5, 5)
    squish.mousePress(squish.waitForObject(series))
    squish.snooze(1)
    squish.mouseRelease(squish.waitForObject(window))
    squish.snooze(2)
    
    return


def anonymize_study(study, anon_name):
    
    statusBar =                         ":cmr42MainWindow.cmr42StatusBar_QStatusBar"
    returnPatientlistButton =           ":cmr42MainWindow.Patient List_QToolButton"
    patientlistEditBox =                ":mFilterStringLineEdit_QLineEdit"
    studyTreeitem =                     ":listSplitter.studyListTreeWidget_DragListView"
    anonymizeWindow =                   ":Anonymize_QInputDialog"
    contextMenu =                       ":cmr42MainWindow_QMenu"
    anonymizeEditBox =                  "{type='QLineEdit' unnamed='1' visible='1'}"
    anonymizeOkButton =                 ":dcmBrowser.OK_QPushButton"
    
    # Grabs the status bar object to check current message
    status = squish.waitForObject(statusBar);
      
    # If user is not in patient list page condition
    if object.exists(returnPatientlistButton) is True:
        squish.clickButton(squish.waitForObject(returnPatientlistButton))  

    # Searches for study, and anonymizes
    squish.waitForObject(patientlistEditBox).setText(study)
    squish.openContextMenu(squish.waitForObjectItem(studyTreeitem, study), 50, 5, 0)
    
    squish.activateItem(squish.waitForObjectItem(contextMenu, "Anonymize Study"))
    squish.waitForObject(anonymizeEditBox).setText(anon_name)
    squish.clickButton(squish.waitForObject(anonymizeOkButton))
    
    start = time.time()
    squish.snooze(4)
    
    while True:
        if status.currentMessage() == "Import Study done":
            break
        else:
            pass
    end = time.time()
    
    test.log("Anonymizing %s time: %.2f" %(study, (end-start)))
    
    return

    
