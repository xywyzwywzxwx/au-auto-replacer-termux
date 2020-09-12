import os
import time
import filecmp
from shutil import which, copyfile


# Check if have access to sdcard
while True:
  if not os.access('/sdcard/', os.W_OK):
    os.system('termux-setup-storage')
    
  if os.access('/sdcard/', os.W_OK):
    break


# Defining
dir1 = './'
dir2 = '/sdcard/Android/data/com.innersloth.spacemafia/files/'

file1 = './secureNew'
file2 = '/sdcard/Android/data/com.innersloth.spacemafia/files/secureNew'


# Checking needed files and folders exists
if not os.path.exists(dir2):
  exit("Error: Not found Among Us data on path", dir2)


# Replacing file 
while True:
  os.system(f"touch {file2}")
  if not filecmp.cmp(file1, file2):
    copyfile(file1, file2)
  time.sleep(0.25)
