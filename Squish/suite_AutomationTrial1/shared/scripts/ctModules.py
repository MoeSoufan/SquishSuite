# -*- coding: utf-8 -*-
import time
import test
import testData
import object
import objectMap
import squishinfo
import squish
import studyFunctions
from random import randint

def aortic_tricuspid():
    
    tricuspidButton = ":mWorkflowGroupbox.mTricuspidPushButton_QPushButton"
    aorticWindow = ":mMprFrame.mAxialMprFrame_TriPlaneMprFrame"
    
    # Click on the tricuspid option
    squish.clickButton(squish.waitForObject(tricuspidButton))
    
    # Hardcoded mouse clicks of tricuspid locations
    squish.mouseClick(squish.waitForObject(aorticWindow), 169, 195, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(aorticWindow), 197, 249, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(aorticWindow), 134, 243, 0, squish.Qt.LeftButton)
#     squish.snooze(1.5)
        
    return

def aortic_annulus():
    
    annulusTab = ":cmr42MainWindow.mPageButtons[ePage::Annulus]_QToolButton"
    perimeterPoints = ":cmr42MainWindow.ToolButton-contourAction-perimeterPoints_QToolButton"
    aorticWindow = ":mMprFrame.mAxialMprFrame_TriPlaneMprFrame"
    
    # Click on annulus tab
    squish.clickButton(squish.waitForObject(annulusTab))
    
    # Click on the perimeter contour button
    squish.clickButton(squish.waitForObject(perimeterPoints))
    
    # Hardcoded mouse clicks for drawing annulus measurement
    squish.mouseClick(squish.waitForObject(aorticWindow), 172, 153, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(aorticWindow), 101, 208, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(aorticWindow), 172, 277, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(aorticWindow), 239, 227, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.doubleClick(squish.waitForObject(aorticWindow), 175, 152, 0, squish.Qt.LeftButton)
    
    return


def aortic_measurement_capture():

    firstIndexMeasurements = "{container=':mMprCaptureFrame_MprCaptureListWidget' type='QModelIndex'}"
    tagLVOT = ":mGroupFrame.LVOT_QModelIndex"
    
    # Drag and drop LVOT tag on first measurement capture image
    squish.mousePress(squish.waitForObject(tagLVOT))
#     squish.snooze(1)
    squish.mouseMove(squish.waitForObject(firstIndexMeasurements), 5, 5)
    squish.mouseRelease(squish.waitForObject(firstIndexMeasurements))
        
    return


def mitral_define_annulus():
    mitralWindow = ":mMprFrame.mAxialMprFrame_TriPlaneMprFrame"
    annulusTab = ":cmr42MainWindow.mPageButtons[ePage::Annulus]_QToolButton"
    annulusStartButton = ":groupBox.mStartAssistedButton_QPushButton"
    topFrame = ":mMprFrame.mSagittalMprFrame_TriPlaneMprFrame"
    bottomFrame = ":mMprFrame.mCoronalMprFrame_TriPlaneMprFrame"
    
    # Click on start annulus
    squish.mouseClick(squish.waitForObject(mitralWindow), 180, 460, 0, squish.Qt.LeftButton)
    
    # Switch to annulus tab and start annulus
    squish.clickButton(squish.waitForObject(annulusTab))
    squish.clickButton(squish.waitForObject(annulusStartButton))
    
    # Hardcoded annulus drawing
    squish.mouseClick(squish.waitForObject(topFrame), 146, 162, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(topFrame), 148, 253, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(bottomFrame), 158, 181, 0, squish.Qt.LeftButton)
#     squish.snooze(0.5)
    squish.mouseClick(squish.waitForObject(bottomFrame), 154, 252, 0, squish.Qt.LeftButton)
    
    return

def mitral_measurement_capture():
    
    firstIndexMeasurements = "{container=':mMprCaptureFrame_MprCaptureListWidget' type='QModelIndex'}"
    bottomFrame = ":mMprFrame.mCoronalMprFrame_TriPlaneMprFrame"
    lineContourEmbedFrame = ":contourHandle.ToolButton-contourAction-lineRoiContour_QToolButton"
    tagMVTOLAA = ":mGroupFrame.MV to LAA_QModelIndex"
    
    x, y = squish.waitForObject(bottomFrame).height, squish.waitForObject(bottomFrame).width
    
    squish.mouseMove(squish.waitForObject(bottomFrame), 10, x-20)

    squish.clickButton(squish.waitForObject(lineContourEmbedFrame))
    
    squish.mousePress(bottomFrame, randint(0+50, x-70), randint(0+50, y-70), squish.Qt.LeftButton);
#     squish.snooze(0.5)
    squish.mouseRelease(bottomFrame, randint(0+50, x-70), randint(0+50, y-70), squish.Qt.LeftButton);
#     squish.snooze(0.5)
    
    # Drag and drop LVOT tag on first measurement capture image
    squish.mousePress(squish.waitForObject(tagMVTOLAA))
#     squish.snooze(1)
    squish.mouseMove(squish.waitForObject(firstIndexMeasurements), 5, 5)
    squish.mouseRelease(squish.waitForObject(firstIndexMeasurements))
    
    return
