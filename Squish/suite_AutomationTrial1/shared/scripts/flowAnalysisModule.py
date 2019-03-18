# -*- coding: utf-8 -*-
import time
import studyFunctions
import object
import squish 


def segment_forward():
                        
    segmentContour = ":mContourOptions.ToolButton-mSegAction_QToolButton"
    forwardContour = ":mContourOptions.ToolButton-mSegForwardAction_QToolButton"

    squish.mousePress(squish.waitForObject(segmentContour))
#     squish.snooze(1)
    squish.mouseRelease(squish.waitForObject(segmentContour))
    
    squish.clickButton(squish.waitForObject(forwardContour))
    
    return


def select_systemic():
    
    systemicFlowButton = ":mFlowSeriesPanelButtons.ToolButton-mFlow0PanelAction_QToolButton"
    
    squish.mouseClick(squish.waitForObject(systemicFlowButton))
    
    return


def select_pulmonary():
    
    pulmonaryFlowButton = ":mFlowSeriesPanelButtons.ToolButton-mFlow1PanelAction_QToolButton"
    
    squish.mouseClick(squish.waitForObject(pulmonaryFlowButton))
    
    return


def select_comparison():

    comparisonFlowButton = ":mFlowSeriesPanelButtons.ToolButton-mFlow2PanelAction_QToolButton"
    
    squish.mouseClick(squish.waitForObject(comparisonFlowButton))
    
    return
