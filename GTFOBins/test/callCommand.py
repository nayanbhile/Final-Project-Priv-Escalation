import os,sys
import subprocess
from threading import Thread
from time import sleep
from git import Repo
from pyautogui import press, typewrite, hotkey

def typePass():
	sleep(1.5)
	typewrite("1104\n")

def callCommand(command):
	print("==================== CALL COMMAND BEING EXECUTED======================")
	thread = Thread(target=typePass)
	thread.start()
	os.system(command)
	print("==================== CALL COMMAND EXECUTED SUCCESSFULLY======================")
