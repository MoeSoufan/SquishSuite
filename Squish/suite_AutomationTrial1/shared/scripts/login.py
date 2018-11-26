# -*- coding: utf-8 -*-
import time
import squish
import test
import object 
import cvi42Objects

def login(user, server):
    
    # If cvi42 already running dialog popup
    if object.exists(cvi42Objects.cviAlreadyRunning):
        squish.mouseClick(squish.waitForObject(cvi42Objects.cviAlreadyRunningOk))
    
    # If cvi42 disconnected
    if object.exists(cvi42Objects.mainDialog):
        if object.exists(cvi42Objects.LoginDialog) is False:
            test.log("Already Logged In")
            return
    
    # Grabs desired server name
    squish.mouseClick(squish.waitForObject(cvi42Objects.serverBox), 164, 7, 0, squish.Qt.LeftButton)
    squish.mouseClick(squish.waitForObjectItem(cvi42Objects.serverBox, server), 105, 8, 0, squish.Qt.LeftButton)

    # Populates username and password boxes and clicks login
    squish.mouseClick(squish.waitForObject(cvi42Objects.usernameBox))
    squish.waitForObject(cvi42Objects.usernameBox).setText(user)
    squish.waitForObject(cvi42Objects.passwordBox).setText(user)
    
    squish.clickButton(squish.waitForObject(cvi42Objects.LoginButton))   
    start = time.time()
    
    # If user already logged on dialog
    if object.exists(cvi42Objects.userAlreadyLoggedOn):
        squish.mouseClick(squish.waitForObject(cvi42Objects.userAlreadyLoggedOnOk))
    
    status = squish.waitForObject(cvi42Objects.statusBar);
        
    while True:
        if status.currentMessage() == "Load image previews done":
            break
        else:
            pass

    end = time.time()
    test.log("Time to Login: %.2f" % (end-start))
    
    return 
