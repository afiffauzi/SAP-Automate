import pyautogui
import time
import os
from datetime import datetime

log_file_path = r"D:\Robot\09_Log\{}_Log.txt".format(datetime.now().strftime('%Y%m%d'))

def log_entry(step, level, message):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_log = "[SAP Screen Automation][{}][{}][{}]\t{}".format(step, level, current_time, message)

    with open(log_file_path, 'a') as log_file:
        log_file.write(formatted_log + '\n')

class AutomateSAP:
    def __init__(self):
        self.sap_username = os.environ.get('SAP_USERNAME')
        self.sap_password = os.environ.get('SAP_PASSWORD')
        log_entry("Initialization", "INFO","PyAutoGUI Script Intialized")
   
    def automate(self):
        try:
            # Membuka Aplikasi SAP LOGON
            pyautogui.press("win")
            time.sleep(1)
            pyautogui.write("SAP Logon")
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(10)
            log_entry("Opening SAP", "INFO","SAP is Opened")

            # Masuk Server DH3  
            try:
                pyautogui.press("enter")
                time.sleep(5)
                log_entry("Login to Server", "INFO","Logged in into Server")

            except pyautogui.FailSafeException:
                log_entry("Login to Server", "WARNING","Failed to Loggin into Server")
                self.cleanup_actions()

            except Exception as e:
                log_entry("Login to Server", "ERROR",str(e))

            # Login
            pyautogui.write(self.sap_username)
            pyautogui.press("tab")
            pyautogui.write(self.sap_password)
            pyautogui.press("enter")
            time.sleep(2)
            log_entry("Input Username Pwd", "INFO","Successfully input credentials")

            # Masuk ke Program
            pyautogui.write("ZRS_SP_PERFORM")
            pyautogui.press("enter")
            log_entry("ZRS_SP_PERFORM", "INFO","Entering ZRS_SP_PERFORM TCODE")

            time.sleep(2)
            pyautogui.press("f8")
            time.sleep(5)
            log_entry("ZRS_SP_PERFORM", "INFO","Excecuting ZRS_SP_PERFORM TCODE")

            # Logout DEV
            log_entry("Clean-up", "INFO","Exiting SAP ...")
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(2)
            log_entry("Clean-up", "INFO","SAP Server is Closed")

            # Close SAP
            pyautogui.hotkey('alt', 'f4')
            log_entry("Clean-up", "INFO","All SAP Windows is Closed")

        except Exception as e:
            log_entry("Error", "ERROR", str(e))

        finally:
            time.sleep(5)
            self.cleanup_actions()

    def cleanup_actions(self):
        os.system("taskkill /F /IM saplogon.exe")
        log_entry("Force Clean-up", "INFO","SAP Server is Force-Closed")

automate_sap = AutomateSAP()
automate_sap.automate()
