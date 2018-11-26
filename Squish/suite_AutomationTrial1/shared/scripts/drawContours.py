# -*- coding: utf-8 -*-
import time
import studyFunctions
import object
import squish 
from random import randint


def lineContour(window_name, num=3):
    
    lineContourButton = ":mContourTools.ToolButton-contourAction-lineRoiContour_QToolButton"
    
    # Grabs Qt equivalent of given window name 
    window, x, y = studyFunctions.find_window(window_name)
    
    # Finds and clicks on the line contour button in the toolbar
    squish.clickButton(squish.waitForObject(lineContourButton))
    
    counter = 0
    while counter < num:
        # Mouse press and release inside the frame of the selected window
        squish.mousePress(window, randint(0+50, x-70), randint(0+50, y-70), squish.Qt.LeftButton);
        squish.mouseRelease(window, randint(0+50, x-70), randint(0+50, y-70), squish.Qt.LeftButton);
        
        counter += 1
        
    return


def curvedMeasContour(window_name, num=3):
    
    curvedMeasurementContour = ":mContourTools.ToolButton-contourAction-openSplinePerimeterPoints_QToolButton"
    
    # Grabs Qt equivalent of given window name
    window, x, y = studyFunctions.find_window(window_name)
    
    # Finds and clicks on the Contour measurement button
    squish.clickButton(squish.waitForObject(curvedMeasurementContour))
    
    counter = 0 
    while counter < num-1:
        # Mouse click inside the frame of the selected window
        squish.mouseClick(squish.waitForObject(window), randint(0+50, x-70), randint(0+50, y-70), 0, squish.Qt.LeftButton)
        counter += 1
    
    squish.doubleClick(squish.waitForObject(window), randint(0+50, x-70), randint(0+50, y-70), 0, squish.Qt.LeftButton)

    return


def freehandContour(window_name):
    
    freehandContour = ":mContourTools.ToolButton-contourAction-freeDrawRoiContour_QToolButton"
    
    # Grabs Qt equivalent of given window name
    window, x, y = studyFunctions.find_window(window_name)
    
    # Finds and clicks on the Contour measurement button
    squish.clickButton(squish.waitForObject(freehandContour))
    
    # Starts drawing freehand contour by pressing the left mouse button
    squish.mousePress(squish.waitForObject(window), randint(0+50, x-70), randint(0+50, y-70), squish.Qt.LeftButton)
    
    for i in range (3):
        squish.mouseMove(squish.waitForObject(window), randint(0+50, x-70), randint(0+50, y-70))
    
    squish.mouseRelease(squish.waitForObject(window), randint(0+50, x-70), randint(0+50, y-70), squish.Qt.LeftButton)

    
    return


def flowContour(window_name, contour=1):
    
    flowContour = ":mContourTools.ToolButton-contourAction-flow1Contour_QToolButton"
    
    new_contour = ":mContourTools.ToolButton-contourAction-flow%sContour_QToolButton" % contour

    # Grabs Qt equivalent of given window name
    window, x, y = studyFunctions.find_window(window_name)
        
    # Finds and clicks on the Contour measurement button
    squish.clickButton(squish.waitForObject(new_contour))

    # Draw a handcoded contour for now
    squish.mousePress(squish.waitForObject(window), ((x/2)+20), ((y/2)+20), squish.Qt.LeftButton)
    squish.mouseMove(squish.waitForObject(window),((x/2)+20), ((y/2)-20))
    squish.mouseMove(squish.waitForObject(window), ((x/2)-30), ((y/2)-20))
    squish.mouseRelease(squish.waitForObject(window),  ((x/2)-30), ((y/2)-20), squish.Qt.LeftButton)
    
    return
