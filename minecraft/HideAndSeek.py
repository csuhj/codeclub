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

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()

    #Post a message to the minecraft chat window
    mc.postToChat("Welcome to Minecraft Hide & Seek")

    sleep(2)
  
    #Find the players position
    playerPos = mc.player.getPos()
  
    #Create random position within 50 blocks from the player, our hidden block will go there
    randomBlockPos = roundVec3(playerPos)
    randomBlockPos.x = random.randrange(randomBlockPos.x - 50, randomBlockPos.x + 50)
    randomBlockPos.y = random.randrange(randomBlockPos.y - 5, randomBlockPos.y + 5)
    randomBlockPos.z = random.randrange(randomBlockPos.z - 50, randomBlockPos.z + 50)
    print randomBlockPos
  
    #Create hidden diamond block
    mc.setBlock(randomBlockPos.x, randomBlockPos.y, randomBlockPos.z, block.LAPIS_LAZULI_BLOCK.id)
    mc.postToChat("Find the hidden block!")
  
    #Start hide and seek
    seeking = True
    while (seeking == True):
        #Get players position
        playerPos = mc.player.getPos()
        #Has the player moved
        distanceFromBlock = distanceBetweenPoints(randomBlockPos, playerPos)
        
        if distanceFromBlock < 2:
            #found it!
            mc.postToChat("You found the block!")
            seeking = False
        else:
            if distanceFromBlock > 100:
                led.off()
            else:
                blinkOn = min(distanceFromBlock / 20, 0.5)
                blinkOff = distanceFromBlock / 60

                led.blink(blinkOn, blinkOff, 1)
                sleep(blinkOn + blinkOff)
