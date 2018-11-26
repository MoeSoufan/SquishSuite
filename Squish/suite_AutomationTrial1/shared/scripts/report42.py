# -*- coding: utf-8 -*-
import time
import studyFunctions
import object
import squish 
import test


def add_to_report():
    
    addToReportButton = ":cmr42MainWindow.Add Report_QToolButton"
      
    # Click on the add to report button
    squish.clickButton(squish.waitForObject(addToReportButton))
      
    # Check report42 time
    check_report42()
    
    return


def measurement_capture():
    
    measurementCaptureButton = ":mViewerMeasurementFrame.mCameraButton_QPushButton"
    SelectAllButton = ":mCentralStack.mSelectAllButton_QPushButton"
    PushtoReportOk = ":mCentralStack.mOkButton_QPushButton"
    
    # Open measurement capture window and send to report
    squish.clickButton(squish.waitForObject(measurementCaptureButton))
    squish.clickButton(squish.waitForObject(SelectAllButton))
    squish.clickButton(squish.waitForObject(PushtoReportOk))
    
    # Check report42 time
    check_report42()
    
    return


def check_report42():
    
    reportTab = ":tabBar.Report_TabItem"
    greenStatusbar = ":webEngView.Save in progress_HTML_Object"
    reportLoading = "{container=':mCentralStack.stackWidget_QStackedWidget' name='webEndView' "
    "type='QWebEngineView' visible='1'}id='loader' tagName='DIV' type='HTML_Object' visible='true'}"
    feedbackMessage = ":webEngView.study-update-feeback_HTML_Object"
    
    counter = 0
    start = time.time()
    
    # Select the Report module to check progress, wait one second to allow the system to catch up
    studyFunctions.click_module("Report")
#     squish.snooze(1)
    
    # Wait for the green progress bar to disappear
    while True:
        if object.exists(feedbackMessage):
            if object.exists(greenStatusbar) is True:
                pass
            
            else:
                if object.exists(greenStatusbar) is True or object.exists(reportLoading) is True:
                    pass
                    counter = 0
                    
                # If dialog doesn't exist for three consecutive iterations, break and time.
                else:
                    counter += 1
                    if counter > 2:
                        break
        else:
            pass
            counter += 1
            if counter > 100:
                test.log("Can't check report42")     
                squish.mouseClick(squish.waitForObject(reportTab))       
                return
            
    end = time.time()
    test.log("Added to report42 %.2f" % (end-start))
#     squish.snooze(1)
    
    return
