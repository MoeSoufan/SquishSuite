# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish

def load(study, ct=False):
    
    # Qt objects used 
    statusBar = ":cmr42MainWindow.cmr42StatusBar_QStatusBar"
    studyWindow = "{text='%s' type='QAction' unnamed='1' visible='true'}" % study
    returnPatientlistButton = ":cmr42MainWindow.Patient List_QToolButton"
    patientlistEditBox = ":mFilterStringLineEdit_QLineEdit"
    studyTreeitem = ":listSplitter.studyListTreeWidget_DragListView"
    studyOpenWindow = ":Study Already Open_QMessageBox"
    studyOpenOK = ":dcmBrowser.Yes_QPushButton"
    returnStudyButton = ":cmr42MainWindow.Return to Study_QToolButton"
    NoIndicationButton = ":indications.No Indication_QModelIndex"
    SelectIndicationHeader = ":Select indication:_HeaderViewItem"
    
    
    # Grabs the status bar object to check current message
    status = squish.waitForObject(statusBar);
    
    # If study is already loaded condition 
    if object.exists(studyWindow) is True:
        return
    
    # If user is not in patient list page condition
    if object.exists(returnPatientlistButton) is True:
        squish.clickButton(squish.waitForObject(returnPatientlistButton))   

    # Search for study in patient list
    squish.waitForObject(patientlistEditBox).setText(study)
    squish.doubleClick(squish.waitForObjectItem(studyTreeitem, study), 22, 7, 0, squish.Qt.LeftButton)
    
    start = time.time()
    
    if ct == False:           
        while True:
            # Wait until 'Loading Study done' message appears on statusbar
            if status.currentMessage() == "Loading Study done":
                end = time.time()
                test.log("Loading Study time: %.2f" % (end-start))
                break
            
            # If study already opened by another user condition
            if object.exists(studyOpenWindow) is True:
                squish.clickButton(squish.waitForObject(studyOpenOK))
                    
            # If study already opened, exit patient list window
            if status.currentMessage() == "Study Already Open":
                squish.clickButton(squish.waitForObject(returnStudyButton))
                break
        
        # If indication prompt is present
        if object.exists(NoIndicationButton) is True:
            squish.doubleClick(squish.waitForObject(NoIndicationButton))
    
    else:
        while True:
        # Wait until 'Select indication is on the screen'
            if object.exists(SelectIndicationHeader) is True:
                end = time.time()
                test.log("Loading Study time: %.2f" % (end-start))
                break

            # If study already opened by another user condition
            if object.exists(studyOpenWindow) is True:
                squish.clickButton(squish.waitForObject(studyOpenOK))
                    
            # If study already opened, exit patient list window
            if status.currentMessage() == "Study Already Open":
                squish.clickButton(squish.waitForObject(returnStudyButton))
                break
    
    return


        