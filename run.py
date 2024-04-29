#coding=utf-8
import os, sys, platform
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
	import Mking64
elif bit == '32bit':
    exit('Your Device 32 Bit Not Work For You') 
