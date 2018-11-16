# -*- coding: utf-8 -*-
import time
import studyFunctions
import object
import squish 
import test

def add_to_report():
    
    greenStatusbar = ":webEngView.Save in progress_HTML_Object"
    addToReportButton = ":cmr42MainWindow.Add Report_QToolButton"
    reportLoading = "{container=':mCentralStack.stackWidget_QStackedWidget' name='webEndView' "
    "type='QWebEngineView' visible='1'}id='loader' tagName='DIV' type='HTML_Object' visible='true'}"
    
    # Click on the add to report button
    squish.clickButton(squish.waitForObject(addToReportButton))
    
    counter = 0
    start = time.time()
    
    # Select the Report module to check progress, wait one second to allow the system to catch up
    studyFunctions.click_module("Report")
    squish.snooze(1)
    
    # Wait for the green progress bar to disappear
    while True:
        if object.exists(greenStatusbar) is True or object.exists(reportLoading) is True:
            pass
            test.log("We waiting boy")
        else:
            if object.exists(greenStatusbar) is True or object.exists(reportLoading) is True:
                pass
                test.log("We waiting boy 2")    
                counter = 0
            # If dialog doesn't exist for three consecutive iterations, break and time.
            else:
                counter += 1
                if counter > 2:
                    break
            
    end = time.time()
    
    test.log("Gimme dat time %.2f" % (end-start))
    
    return

