    

def main():    
    
    attachToApplication("MyApplicationAttachable")
#     login.login("moe", "absinthe")
    series = "{container=':scrollArea.Primary Study_QGroupBox' name='seriesPreview' type='SeriesPreview' visible='1'}"
    box = "{container=':scrollArea.Primary Study_QGroupBox' name='blackBackground' type='QWidget' visible='1'}"


    if object.exists(series) is True:
        counter = 0
        while True:
            if counter == 0:
                series_next = series
            else:
                series_next = "{container=':scrollArea.Primary Study_QGroupBox' name='seriesPreview' occurrence='%s' type='SeriesPreview' visible='1'}" %(counter+1)
 
            if object.exists(series_next) is True:
                mouseClick(waitForObject(series_next), 53, 13, 0, Qt.LeftButton)
                mouseMove(waitForObject(series_next), 5, 5)
                mousePress(waitForObject(series_next))
                mouseRelease(waitForObject(series_next))
                counter+=1

                if object.exists(":Loading Workspace.Cancel_QPushButton") is True:
                    clickButton(waitForObject(":Loading Workspace.Cancel_QPushButton"))
                    test.log("Series#%s is a workspace"%counter)
                
                else:
                    clickButton(waitForObject(":viewerOptionToolWidget.ToolButton-mAutoSeriesInfoAction_QToolButton"))
                    test.log("Series #%s, %s"%(counter,waitForObject(":mCentralStack.qt_msgbox_label_QLabel").text))
                    clickButton(waitForObject(":mCentralStack.OK_QPushButton"))
                 
                 
            else:
                break