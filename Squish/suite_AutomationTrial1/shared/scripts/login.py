# -*- coding: utf-8 -*-
import time
import squish
import test
import object 

def login(user, server):
    
    # Qt objects used 
    serverBox = ":comboBoxServer_QComboBox"
    usernameBox = ":lineEditUserId_QLineEdit"
    passwordBox = ":lineEditPassword_QLineEdit"
    LoginButton = ":dialog.buttonLogin_QPushButton"
    statusBar = ":cmr42MainWindow.cmr42StatusBar_QStatusBar"
    
    cviAlreadyRunning = ":Detected Running cvi42 Instance_QMessageBox"
    cviAlreadyRunningOk = ":Detected Running cvi42 Instance.Yes_QPushButton"
    
    userAlreadyLoggedOn = ":User Already Logged on_QMessageBox"
    userAlreadyLoggedOnOk = ":User Already Logged on.Yes_QPushButton"
    
    # If cvi42 already running dialog popup
    if object.exists(cviAlreadyRunning):
        squish.mouseClick(squish.waitForObject(cviAlreadyRunningOk))
    
    # Grabs desired server name
    squish.mouseClick(squish.waitForObject(serverBox), 164, 7, 0, squish.Qt.LeftButton)
    squish.mouseClick(squish.waitForObjectItem(serverBox, server), 105, 8, 0, squish.Qt.LeftButton)

    # Populates username and password boxes and clicks login
    squish.mouseClick(squish.waitForObject(usernameBox))
    squish.waitForObject(usernameBox).setText(user)
    squish.waitForObject(passwordBox).setText(user)
    
    squish.clickButton(squish.waitForObject(LoginButton))   
    start = time.time()
    
    # If user already logged on dialog
    if object.exists(userAlreadyLoggedOn):
        squish.mouseClick(squish.waitForObject(userAlreadyLoggedOnOk))
    
    status = squish.waitForObject(statusBar);
        
    while True:
        if status.currentMessage() == "Load image previews done":
            break
        else:
            pass

    end = time.time()
    test.log("Time to Login: %.2f" % (end-start))
    
    return 
