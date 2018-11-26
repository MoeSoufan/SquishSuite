# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish
import studyFunctions

def ml_button():
    
    mlButton = ":mContourDetectionTools.mlButton_SwitchingToolButton"
    
    squish.clickButton(squish.waitForObject(mlButton))
    
    # Wait for progress bar 
    time = studyFunctions.loading_time()           
    
    test.log("biplanarLAX ML %.2f" % time)
    
    return
