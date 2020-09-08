# Main game loop
import pygame, socket, math, argparse, time
from src.gamedata import GameData
from src.static import *
from src.render import *
from src.ui import UI

def main ():
    pygame.init()
    clock = pygame.time.Clock()
    data = GameData()
    data.key_x = FireCommand()
    data.key_space = FireCommand()
    data.key_down_pressed = MoveDown()
    data.key_down_unpressed = StopMoving()
    # Initialize Screen:
    screen = pygame.display.set_mode((Value.WINDOW_WIDTH, Value.WINDOW_HEIGHT))
    Image.init()
    data.initGroups()
    data.dungeonMap.loadCurrentRoom(data)
    data.ui = UI(data)
    while data.running:
        # track the frame number
        timer = clock.tick(Value.FRAME_RATE) #similar to timerDelay
        data.timer += 1

        # receive input
        for event in pygame.event.get():
            handle(event,data)

        # Combine the input with the current world state
        updateAll(data)
        checkCollisions(data)

        # draw
        redrawAll(screen, data)
        pygame.display.flip()
    pygame.quit()


class Command():
  pass

class FireCommand(Command):
  def execute(self, data):
    data.player.fireProjectile(data)

class MoveDown(Command):
  def execute(self, data):
    data.mostRecentDir = "down"
    data.keysPressed.append("down")
  
class StopMoving(Command):
  def execute(self, data):
    data.keysPressed.remove("down")
    if data.mostRecentDir == "down":
      data.mostRecentDir = None

def handle(event,data):
    # print(event)
    #When you quit the window
    if event.type == pygame.QUIT:
        data.running = False
#when you press the keysx
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            data.mostRecentDir = "up"
            data.keysPressed.append("up")
        if event.key == pygame.K_DOWN:
            #data.mostRecentDir = "down"
            #data.keysPressed.append("down")
            data.key_down_pressed.execute(data)
        if event.key == pygame.K_LEFT:
            data.mostRecentDir = "left"
            data.keysPressed.append("left")
        if event.key == pygame.K_RIGHT:
            data.mostRecentDir = "right"
            data.keysPressed.append("right")
        if event.key == pygame.K_ESCAPE:#when you press the escape button
            data.running = False
        if event.key == pygame.K_SPACE and data.acceptInput:
            data.key_space.execute(data)
        if event.key == pygame.K_x and data.acceptInput:
            data.key_x.execute(data)

#when you get off the keys
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            data.keysPressed.remove("up")
            if data.mostRecentDir == "up":
                data.mostRecentDir = None
        if event.key == pygame.K_DOWN:
            # data.keysPressed.remove("down")
            #if data.mostRecentDir == "down":
            #     data.mostRecentDir = None
            data.key_down_unpressed.execute(data)
        if event.key == pygame.K_LEFT:
            data.keysPressed.remove("left")
            if data.mostRecentDir == "left":
                data.mostRecentDir = None
        if event.key == pygame.K_RIGHT:
            data.keysPressed.remove("right")
            if data.mostRecentDir == "right":
                data.mostRecentDir = None
        if data.mostRecentDir == None and len(data.keysPressed)> 0:
            data.mostRecentDir = data.keysPressed[-1]

if __name__ == "__main__":
    main()
