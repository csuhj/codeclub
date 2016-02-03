#Adapted from a script by www.stuffaboutcode.com
#Raspberry Pi, Minecraft - hide and seek

import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep
import random
import math
from gpiozero import LED

led = LED(17)

#function to round players float position to integer position
def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))
  
if __name__ == "__main__":

    #Start hide and seek
    led.on()
