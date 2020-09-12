from os import access, W_OK, path, system
from time import sleep
from filecmp import cmp
from shutil import which, copyfile

print("Script running...")
# Check if have access to sdcard
while True:
  if not access('/sdcard/', W_OK):
    system('termux-setup-storage')
    
  if access('/sdcard/', W_OK):
    break


# Defining
dir1 = './'
dir2 = '/sdcard/Android/data/com.innersloth.spacemafia/files/'

file1 = './secureNew'
file2 = '/sdcard/Android/data/com.innersloth.spacemafia/files/secureNew'


# Checking needed files and folders exists
if not path.exists(dir2):
  exit(f"Error: Not found Among Us data on path: {dir2}")

print("Waiting for file changes...")
# Replacing file 
while True:
  system(f"touch {file2}")
  if not cmp(file1, file2):
    copyfile(file1, file2)
    print("File replaced")
  time.sleep(0.25)
