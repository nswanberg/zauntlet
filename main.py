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
   
    # Init keys (move to game init module)
    data.key_x = FireCommand()
    data.key_space = FireCommand()

    data.key_up_pressed = StartMoving()
    data.key_down_pressed = StartMoving()
    data.key_left_pressed = StartMoving()
    data.key_right_pressed = StartMoving()

    data.key_up_unpressed = StopMoving()
    data.key_down_unpressed = StopMoving()
    data.key_left_unpressed = StopMoving()
    data.key_right_unpressed = StopMoving()

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

class StartMoving(Command):
  def execute(self, data, direction):
    data.mostRecentDir = direction 
    data.keysPressed.append(direction)

class StopMoving(Command):
  def execute(self, data, direction):
    data.keysPressed.remove(direction)
    if data.mostRecentDir == direction:
      data.mostRecentDir = None

def handle(event,data):
    #When you quit the window
    if event.type == pygame.QUIT:
        data.running = False
#when you press the keysx
    if event.type == pygame.KEYDOWN:
        # Movement keys
        if event.key == pygame.K_UP:
            data.key_up_pressed.execute(data, "up")
        if event.key == pygame.K_DOWN:
            data.key_down_pressed.execute(data, "down")
        if event.key == pygame.K_LEFT:
            data.key_left_pressed.execute(data, "left")
        if event.key == pygame.K_RIGHT:
            data.key_right_pressed.execute(data, "right")
        # Fire
        if event.key == pygame.K_SPACE and data.acceptInput:
            data.key_space.execute(data)
        if event.key == pygame.K_x and data.acceptInput:
            data.key_x.execute(data)
        # Quit
        if event.key == pygame.K_ESCAPE:
            data.running = False

#when you get off the keys
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            data.key_down_unpressed.execute(data, "up")
        if event.key == pygame.K_DOWN:
            data.key_down_unpressed.execute(data, "down")
        if event.key == pygame.K_LEFT:
            data.key_down_unpressed.execute(data, "left")
        if event.key == pygame.K_RIGHT:
            data.key_down_unpressed.execute(data, "right")
        if data.mostRecentDir == None and len(data.keysPressed)> 0:
            data.mostRecentDir = data.keysPressed[-1]

if __name__ == "__main__":
    main()
