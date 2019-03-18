# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish
import cvi42Objects
import os, signal


def click_module(module, ct=False):
    
    counter = 0 
    moduleListItem = "{container=':mWorkflowDockWidget.protocolSteps_Workflow::ProtocolStepListWidget' text='%s' type='QModelIndex'}" % module

    # If the study is MR, the icon of the selected module is available in the toolbar. Checks if module already selected
    if ct == False:
        if object.exists(cvi42Objects.toolbarModuleButton) is True:
            if squish.waitForObject(cvi42Objects.toolbarModuleButton).text == module:
#                 test.log("Module Already Loaded")
                return
        
    while True:
        # If module not in the module list, search for it    
        if object.exists(moduleListItem) is False:
            
            if counter == 0:
                # If module list scroll bar available, mouse scroll to try and find module
                if object.exists(cvi42Objects.moduleListScrollbar):
                    # Mouse scrolls up all the way to see top of visible module list
                    squish.sendEvent("QWheelEvent", squish.waitForObject(cvi42Objects.moduleListScrollbar), 103, 527, 540, 0, 2)
    
                    # If module is visible, click it, and exit loop
                    if object.exists(moduleListItem) is True:
                        squish.mouseClick(squish.waitForObject(moduleListItem))
                        
                        time = loading_time()
                        if time > 10:
                            test.log("Time to load module: %.2f" % time)
                        break
                    
                    # If scroll bar available, scroll down a little bit each iteration
                    squish.sendEvent("QWheelEvent", squish.waitForObject(cvi42Objects.moduleListScrollbar), 3, 307, -340, 0, 2)
                
                # If mouse scroll bar not available, pass each time
                else:
                    pass
                
            counter += 1
            
            # After four attempts, if module is not found, select it from the protocol list and click the module
            if counter == 4:
                squish.mouseClick(squish.waitForObject(cvi42Objects.addProtocolButton))
                squish.activateItem(squish.waitForObjectItem(cvi42Objects.addProtocolWindow, module))
                
                squish.mouseClick(squish.waitForObject(moduleListItem))
                
                time = loading_time()
                if time > 10:
                    test.log("Time to load module: %.2f" % time)
                
                return
        
        # If module exists from the beginning, select it and exit                
        else:
            squish.mouseClick(squish.waitForObject(moduleListItem))
            
            time = loading_time()
            if time > 10:
                test.log("Time to load module: %.2f" % time)
                
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
                    
                    "flow2": ":mVencDcmFrame.Phase_DcmFrameGL",
                    "flow1": ":mMagnDcmFrame.Magnitude_DcmFrameGL",
                    
                    "mitral1": ":mMprFrame.mAxialMprFrame_TriPlaneMprFrame",
                    "mitral2": ":mMprFrame.mCoronalMprFrame_TriPlaneMprFrame",
                    "mitral3": ":mMprFrame.mSagittalMprFrame_TriPlaneMprFrame",
                    
                    "aortic1": ":mMprFrame.mCoronalMprFrame_TriPlaneMprFrame",
                    "aortic2": ":mMprFrame.mAxialMprFrame_TriPlaneMprFrame",
                    "aortic3": ":mMprFrame.mSagittalMprFrame_TriPlaneMprFrame",
                    "aortic4": ":mMprFrame.mRefSuperVisFrame_SuperVisFrame",
                    
                    "fem1": ":mMprFrame.mRefTriPlaneMprFrames0_TriPlaneMprFrame_2",
                    "fem2": ":mMprFrame.mRefTriPlaneMprFrames2_TriPlaneMprFrame_2",
                    "fem3": ":mMprFrame.mRefTriPlaneMprFrames1_TriPlaneMprFrame_2",
                    "fem4": ":mMprFrame.mRefSuperVisFrame_SuperVisFrame_2",

                    "coron1": ":mViewersFrame.mRefSuperVisFrame_SuperVisFrame"}
    
    for window in [k for k, v in windows_dict.items() if v == windows_dict[window_name]]:
        properties = object.properties(squish.waitForObject(windows_dict[window]))
        
        # Search for key parameters "width" and "height"
        for name, value in properties.iteritems():
            if name == "width":
                x = value
        
            if name == "height":
                y = value
        
        return windows_dict[window], x, y
    

def load_series(window_given, series_num):
    
    series = ":scrollArea.frame-%s_SeriesThumbPreview" % (series_num-1)

    window, x, y = find_window(window_given)

    # if series needed is bigger than 8, check if scrolling is needed to reach the series
    if object.exists(cvi42Objects.series_scrollbar):
        squish.scrollTo(squish.waitForObject(cvi42Objects.series_scrollbar), -505)
        
        if series_num > 8:
            squish.scrollTo(squish.waitForObject(cvi42Objects.series_scrollbar), 855)

    # Load series into window requested

    squish.mouseMove(squish.waitForObject(series), 5, 5)
    squish.mousePress(squish.waitForObject(series))
#     squish.snooze(1)
    squish.mouseRelease(squish.waitForObject(window))
    squish.snooze(0.2)
    
    if object.exists(":Load Volume.Yes_QPushButton"):
        squish.clickButton(squish.waitForObject(":Load Volume.Yes_QPushButton"))
        
    # Wait for progress bar 
    time = loading_time()

    if time > 10:
        test.log("Time to load series: %.2f" % time)
    
    return


def anonymize_study(study, anon_name):
    
    # If user is not in patient list page condition
    if object.exists(cvi42Objects.returnPatientlistButton) is True:
        squish.clickButton(squish.waitForObject(cvi42Objects.returnPatientlistButton))  
        
    # Grabs the status bar object to check current message
    status = squish.waitForObject(cvi42Objects.statusBar);
    
    if "\\" in study:
        studyUpdated = study.replace("\\","")
    else:
        studyUpdated = study
    
    # Searches for study, and anonymizes
    squish.waitForObject(cvi42Objects.patientlistEditBox).setText(studyUpdated)
    
    squish.openContextMenu(squish.waitForObjectItem(cvi42Objects.studyTreeitem, study), 50, 5, 0)
    
    squish.activateItem(squish.waitForObjectItem(cvi42Objects.contextMenu, "Anonymize Study"))
    squish.waitForObject(cvi42Objects.anonymizeEditBox).setText(anon_name)
    squish.clickButton(squish.waitForObject(cvi42Objects.anonymizeOkButton))
    
    start = time.time()
#     squish.snooze(4)
    
    while True:
        if status.currentMessage() == "Import Study done":
            break
        else:
            pass
    end = time.time()
    
    test.log("Anonymizing %s time: %.2f" %(study, (end-start)))
    
    return anon_name

    
def loading_time():

    progressbarWindow = ":_PersistentProgressDialog"
    progressBarLabelBiLAX = ":LAX4ch Contour detection is in progress..._QLabel"
    progressBarBiLAX = ":LAX4ch Contour detection is in progress..._QProgressBar"
    
    start = time.time()

    counter = 0
    while True:
    # If progress r exists, restart cycle
        if object.exists(progressbarWindow) is True or object.exists(progressBarBiLAX) is True:
            pass
    #             test.log("NOT BAD")
        else:
            # If dialog exists after initial pass, restart cycle and reset counter
            if object.exists(progressbarWindow) is True or object.exists(progressBarBiLAX) is True:
                pass
                counter = 0
                
            # If dialog doesn't exist for three consecutive iterations, break and time.
            else:
                counter += 1
                if counter > 3:
                    break
    end = time.time()
    
    return end-start


def save_workspace(workspace_name):
    
    # Grabs the status bar object to check current message
    status = squish.waitForObject(cvi42Objects.statusBar);
    
    # Saves workspace as name given
    squish.activateItem(squish.waitForObjectItem(cvi42Objects.menuBar, "Workspace"))
    squish.activateItem(squish.waitForObjectItem(cvi42Objects.workspaceButton, "Save Workspace As"))
    squish.waitForObject(cvi42Objects.workspaceWindowEdit).setText(workspace_name)
    squish.clickButton(squish.waitForObject(cvi42Objects.workspaceWindowOkButton))
    
    start = time.time()
    while True:
        if status.currentMessage() == "Save workspace done.":
            break
        else:
            pass
    end = time.time()
    
    test.log("Saving workspace: %.2f"% (end-start))
    
    return


def reset_workspace():
    
    menuBar = ":cmr42MainWindow.appMenuBar_QMenuBar"
    workspaceButton = ":cmr42MainWindow.workspaceMenu_QMenu"
    resetWorkspaceButtonOk = ":Reset Workspace.Reset_QPushButton"
    
    squish.activateItem(squish.waitForObjectItem(menuBar, "Workspace"))
    squish.activateItem(squish.waitForObjectItem(workspaceButton, "Reset Workspace"))
    squish.clickButton(squish.waitForObject(resetWorkspaceButtonOk))
#     squish.snooze(2)
    
    return

def load_workspace(workspace_name):
    
    workspace = "{column='0' container=':pLoadWorkspaceDialog.workspacesWidget_QTreeWidget' text='%s' type='QModelIndex'}" %workspace_name
    menuBar = ":cmr42MainWindow.appMenuBar_QMenuBar"
    workspaceButton = ":cmr42MainWindow.workspaceMenu_QMenu"
    
    squish.activateItem(squish.waitForObjectItem(menuBar, "Workspace"))
    squish.activateItem(squish.waitForObjectItem(workspaceButton, "Load Workspace"))

    squish.doubleClick(squish.waitForObject(workspace))
#     squish.snooze(2)
    
    return


def close_study():
    
    squish.activateItem(squish.waitForObjectItem(cvi42Objects.menuBar, "Workspace"))
    squish.snooze(0.5)
    squish.activateItem(squish.waitForObjectItem(cvi42Objects.workspaceButton, "Close Study"))
    start = time.time()
    
    while True:
        if object.exists(cvi42Objects.patientlistEditBox) is True:
            break
        else:
            pass
    end = time.time()
    
    test.log("Time to close study: %.2f" %(end-start))    
       
    return

def delete_study(study_name):
    
    squish.waitForObject(cvi42Objects.patientlistEditBox).setText(study_name)
    squish.openContextMenu(squish.waitForObjectItem(cvi42Objects.studyTreeitem, study_name), 50, 13, 0)
    squish.activateItem(squish.waitForObjectItem(cvi42Objects.contextMenu, "Delete Study"))
#     squish.snooze(1)
    squish.clickButton(squish.waitForObject(cvi42Objects.DeleteStudyOkButton))
    start = time.time()
    
    while True:
        if object.exists(cvi42Objects.UpdatingStudyListMessage):
            break
        else:
            pass
    end = time.time()
    
#     test.log("Time to delete study: %.2f" %(end-start))
    
    squish.waitForObject(cvi42Objects.patientlistEditBox).setText("")

    
    return

def close_cvi42():
    
    while True:
        process_id = [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:]
                  if "cvi42.exe" in item.split()]
 
        if len(process_id) >= 1:
            os.system("taskkill /im cvi42.exe")

            if object.exists(cvi42Objects.QuitOkButton):
                squish.clickButton(squish.waitForObject(cvi42Objects.QuitOkButton))
            
        else:
            break
 
    return

def export_study(study_name):
    
    # status bar
    status = squish.waitForObject(cvi42Objects.statusBar);

    # Searches for study, and exports
    squish.waitForObject(cvi42Objects.patientlistEditBox).setText(study_name)
    squish.openContextMenu(squish.waitForObjectItem(cvi42Objects.studyTreeitem, study_name), 50, 5, 0)
    squish.activateItem(squish.waitForObjectItem(cvi42Objects.contextMenu, "Export Study"))
    
    # export dialog flow 
    squish.mouseClick(squish.waitForObjectItem(":splitter.sidebar_QSidebar", "My Computer"), 53, 13, 0, squish.Qt.LeftButton)
    squish.mouseClick(squish.waitForObjectItem(":stackedWidget.treeView_QTreeView", "DATA (D:)"), 33, 14, 0, squish.Qt.LeftButton)
    squish.doubleClick(squish.waitForObjectItem(":stackedWidget.treeView_QTreeView", "DATA (D:)"), 34, 11, 0, squish.Qt.LeftButton)
    squish.clickButton(squish.waitForObject(":dcmBrowser.Choose_QPushButton"))
    
    start = time.time()
    while True:
        if status.currentMessage() == "Export Images done":
            break
        else:
            pass
    end = time.time()
    
    test.log("Time to export study: %.2f" % (end-start))
