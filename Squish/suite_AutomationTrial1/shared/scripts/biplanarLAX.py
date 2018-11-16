# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish


def ml_button():
    
    mlButton = ":mContourDetectionTools.mlButton_SwitchingToolButton"
    progressBarLabel = ":LAX4ch Contour detection is in progress..._QLabel"
    progressBar = ":LAX4ch Contour detection is in progress..._QProgressBar"
    
    squish.clickButton(squish.waitForObject(mlButton))
    
    counter = 0
    start = time.time()
    
    # Multiple catches due to dialog disappearing briefly during progress, must iterate 3 times without dialogs being found 
    while True:
        # If progress bad exists, restart cycle
        if object.exists(progressBarLabel) is True or object.exists(progressBar) is True:
            pass
#             test.log("NOT BAD")
        else:
            # If dialog exists after initial pass, restart cycle and reset counter
            if object.exists(progressBarLabel) is True or object.exists(progressBar) is True:
                pass
#                 test.log("NOT BAD on the second %s" % counter)
                counter = 0
            # If dialog doesn't exist for three consecutive iterations, break and time.
            else:
                counter += 1
                if counter > 2:
                    break
    end = time.time()
    
    test.log("biplanarLAX ML %.2f" % (end-start))
    
    return
