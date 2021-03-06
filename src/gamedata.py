# Our main gamedata class.
from src.static import *
from src.player import Player
from src.dungeon import Dungeon
import pygame

class GameData(object):
    def __init__ (self):
        self.running = True
        self.updatePositions = True
        self.acceptInput = True
        self.currentRoomsPos = (1, 2) # Magic because pressed for time.
        self.screenUI = None # Draw either a win or lose screen when this is filled
        self.dungeonMap = Dungeon()
        self.keysPressed = list()
        self.mostRecentDir = None
        self.player = None
        self.timer = 0

    def initGroups(self):
        self.groups = SpriteGroups()

    def tryTransition (self, direction):
        """
            Attempts a scene transition in the given direction.
            Repositions player if successful
        """
        if direction == "right":
            if self.currentRoomsPos[0] + 1 >= StaticDungeonLayout.DUNGEON_WIDTH:
                return
            self.currentRoomsPos = (self.currentRoomsPos[0]+1,
                                    self.currentRoomsPos[1])
            self.player.x = Value.PLAYER_SIZE / 2 # Reposition at left
        elif direction == "left":
            if self.currentRoomsPos[0] - 1 < 0:
                return
            self.currentRoomsPos = (self.currentRoomsPos[0]-1,
                                    self.currentRoomsPos[1])
            self.player.x =  Value.WINDOW_WIDTH - Value.PLAYER_SIZE / 2
        elif direction == "up":
            if self.currentRoomsPos[1] - 1 < 0:
                return
            self.currentRoomsPos = (self.currentRoomsPos[0],
                                    self.currentRoomsPos[1]-1)
            self.player.y = Value.WINDOW_HEIGHT - Value.PLAYER_SIZE / 2
        elif direction == "down":
            if self.currentRoomsPos[1] + 1 >= StaticDungeonLayout.DUNGEON_HEIGHT:
                return
            self.currentRoomsPos = (self.currentRoomsPos[0],
                                    self.currentRoomsPos[1]+1)
            self.player.y = Value.PLAYER_SIZE / 2
        self.dungeonMap.loadCurrentRoom(self)

    def gameOverSequence (self, data):
        """
            Called when the player dies. Set up the gameOver screen.
        """
        # Prevent the game from accepting some inputs and updating:
        self.acceptInput = False
        self.updatePositions = False
        self.resetAllSpriteGroups()
        self.ui.drawGameOver(data)

    def winGameSequence (self, data):
        """
            Called when the player dies. Set up the gameOver screen.
        """
        # Prevent the game from accepting some inputs and updating:
        self.acceptInput = False
        self.updatePositions = False
        self.resetAllSpriteGroups()
        self.ui.drawWinScreen(data)

    def resetAllSpriteGroups (self):
        """ Clears all sprite groups. Used for the gameover/win state """
        self.groups.spawners = pygame.sprite.Group()
        self.groups.terrain = pygame.sprite.Group()
        self.groups.walls = pygame.sprite.Group()
        self.groups.projectiles = pygame.sprite.Group()
        self.groups.player = pygame.sprite.Group()
        self.groups.monsters = pygame.sprite.Group()
        self.groups.items = pygame.sprite.Group()
        self.groups.ui = pygame.sprite.Group()

class SpriteGroups(object):
    def __init__(self):
        self.terrain = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.spawners = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.ui = pygame.sprite.Group()
