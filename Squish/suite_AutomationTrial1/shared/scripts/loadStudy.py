# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish
import cvi42Objects

def load(study, ct=False):
    
    studyWindow = "{text='%s' type='QAction' unnamed='1' visible='true'}" % study
    
    # If study is already loaded condition 
    if object.exists(studyWindow) is True:
        return
    
    # If user is not in patient list page condition
    if object.exists(cvi42Objects.returnPatientlistButton) is True:
        squish.clickButton(squish.waitForObject(cvi42Objects.returnPatientlistButton))   
    
    # Grabs the status bar object to check current message
    status = squish.waitForObject(cvi42Objects.statusBar);

    # Search for study in patient list
    squish.waitForObject(cvi42Objects.patientlistEditBox).setText(study)
    squish.doubleClick(squish.waitForObjectItem(cvi42Objects.studyTreeitem, study), 22, 7, 0, squish.Qt.LeftButton)
    start = time.time()
    
    if ct == False:           
        while True:
            # Wait until 'Loading Study done' message appears on statusbar
            if status.currentMessage() == "Loading Study done":
                end = time.time()
                test.log("Loading Study time: %.2f" % (end-start))
                break
            
            # If study already opened by another user condition
            if object.exists(cvi42Objects.studyOpenWindow) is True:
                squish.clickButton(squish.waitForObject(cvi42Objects.studyOpenOK))
                    
            # If study already opened, exit patient list window
            if status.currentMessage() == "Study Already Open":
                squish.clickButton(squish.waitForObject(cvi42Objects.returnStudyButton))
                break
        
        # If indication prompt is present
        if object.exists(cvi42Objects.NoIndicationButton) is True:
            squish.doubleClick(squish.waitForObject(cvi42Objects.NoIndicationButton))
    
    else:
        while True:
        # Wait until 'Select indication is on the screen'
            if object.exists(cvi42Objects.SelectIndicationHeader) is True:
                end = time.time()
                test.log("Loading Study time: %.2f" % (end-start))
                
                squish.doubleClick(squish.waitForObject(cvi42Objects.NoIndicationButton))
                
                break

            # If study already opened by another user condition
            if object.exists(cvi42Objects.studyOpenWindow) is True:
                squish.clickButton(squish.waitForObject(cvi42Objects.studyOpenOK))
                    
            # If study already opened, exit patient list window
            if status.currentMessage() == "Study Already Open":
                squish.clickButton(squish.waitForObject(cvi42Objects.returnStudyButton))
                break
            
            if object.exists(":mWorkflowDockWidget.mIndicationLabel_QLabel") is True:
                end = time.time()
                test.log("Loading Study time: %.2f" % (end-start))
                break
    return


        
