# -*- coding: utf-8 -*-
import time
import studyFunctions
import object
import squish 


def segment_forward():

    segmentContour = ":mContourOptions.ToolButton-segAction_QToolButton"
    forwardContour = ":mContourOptions.ToolButton-segForwardAction_QToolButton"
    
    squish.mousePress(squish.waitForObject(segmentContour))
    squish.snooze(1)
    squish.mouseRelease(squish.waitForObject(segmentContour))
    
    squish.clickButton(squish.waitForObject(forwardContour))
    
    return


def select_systemic():
    
    systemicFlowButton = ":flowTabBar.Systemic Flow_TabItem"
    
    squish.mouseClick(squish.waitForObject(systemicFlowButton))
    
    return


def select_pulmonary():
    
    pulmonaryFlowButton = ":flowTabBar.Pulmonary Flow_TabItem"
    
    squish.mouseClick(squish.waitForObject(pulmonaryFlowButton))
    
    return


def select_comparison():

    comparisonFlowButton = ":flowTabBar.Comparison_TabItem"
    
    squish.mouseClick(squish.waitForObject(comparisonFlowButton))
    
    return
