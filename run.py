#coding=utf-8
import os, sys, platform
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Mking64.so'):
        os.system('curl -L https://github.com/Profaisor/files/blob/main/Mking64.cpython-311.so?raw=true -o Mking64.so') 
        import mking_menu
    else:
        import mking_menu

elif bit == '32bit':
    if not os.path.isfile('Mking32.so'):
        exit('Your Device 32 Bit Not Work For You') 
