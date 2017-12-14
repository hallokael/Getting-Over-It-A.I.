from Common import *
from time import *
import ctypes
import time
import time
import random
import ctypes
from PIL import ImageGrab
from numpy import *
MOUSE_LEFTDOWN = 0x0002     # left button down
MOUSE_LEFTUP = 0x0004       # left button up
MOUSE_RIGHTDOWN = 0x0008    # right button down
MOUSE_RIGHTUP = 0x0010      # right button up
MOUSE_MIDDLEDOWN = 0x0020   # middle button down
MOUSE_MIDDLEUP = 0x0040     # middle button up
SendInput = ctypes.windll.user32.SendInput


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def gogo(x,y):
    # y=0
    while(x!=0 or y!=0):
        dirx=x/sqrt(x*x+y*y)
        diry=y/sqrt(x*x+y*y)
        nx=int(5*dirx+random.random()*2)
        ny=int(5*diry+random.random()*2)
        if x<25:
            nx=x
        if y<25:
            ny=y
        x-=nx
        y-=ny
        ctypes.windll.user32.mouse_event(0,nx,ny,0,0)
        sleep(0.1)
# sleep(3)
# for i in range(10):
#     ctypes.windll.user32.mouse_event(0, 100, 0, 0, 0)
#     sleep(0.1)
# for i in range(10):
#     ctypes.windll.user32.mouse_event(0, -100, 0, 0, 0)
#     sleep(0.1)
x=0
speed=300
b=-1
while(True):
    x+=math.pi/100.0
    if(abs(x/(2*math.pi)-int(x/(2*math.pi)))<1e-7):
        a=random.random()
        print(a)
        if(a>0.05):
            b=-1
        else:
            b=1

        print(b)
    ctypes.windll.user32.mouse_event(0, b*int(speed*sin(x)), int(speed*cos(x)), 0, 0)
    sleep(0.005)

