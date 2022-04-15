//Call a third-party library.1917494051Wang Tao-1917494045Chen Haoran-1917494031Zhang Junwei
import pygame
import sys
import time
import random
from pygame.locals import *

//Initial settings
pygame.init()  //Initialize pygame
fpsClock = pygame.display.set_mode((640,480))  //Create a pyGame display layer
playSurface = pygame.display.set_mode((640,480))  
pygame.display.set_caption('Snake Co!')  //Define title
image = pygame.image.load('game.ico')  //Load resource picture, game ICO is included in the final file.
pygame.display.set_icon(image) //Settings Icon

//Define color variables
