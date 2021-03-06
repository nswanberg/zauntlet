# Constants for various data files
import pygame
class Image(object):
    @staticmethod
    def init():
        Image.LINK = pygame.image.load("src/images/link.png").convert_alpha()
        Image.LINK = pygame.transform.scale(Image.LINK, (Value.PLAYER_SIZE, Value.PLAYER_SIZE))
        Image.PROJECTILE = pygame.image.load("src/images/projectile.png").convert_alpha()
        Image.PROJECTILE = pygame.transform.scale(Image.PROJECTILE, (Value.PROJECTILE_SIZE, Value.PROJECTILE_SIZE))
        Image.WALL = pygame.image.load("src/images/wall.png").convert_alpha()
        Image.TILE = pygame.image.load("src/images/tile.png").convert_alpha()
        Image.MONSTER = pygame.image.load("src/images/monster.png").convert_alpha()
        Image.MONSTER = pygame.transform.scale(Image.MONSTER, (Value.MONSTER_SIZE, Value.MONSTER_SIZE))
        Image.SPAWNER = pygame.image.load("src/images/spawner.png").convert_alpha()
        Image.SPAWNER = pygame.transform.scale(Image.SPAWNER, (Value.SPAWNER_SIZE, Value.SPAWNER_SIZE))
        Image.HEART = pygame.image.load("src/images/heart.png").convert_alpha()
        Image.FOODOFYENDOR = pygame.image.load("src/images/foodofyendor.png").convert_alpha()
        Image.WINSCREEN = pygame.image.load("src/images/winscreen.png")
        Image.GAMEOVERSCREEN = pygame.image.load("src/images/gameoverscreen.png")
        Image.DAMAGED_WALL_0 = pygame.image.load("src/images/damagedwall0.png").convert_alpha()
        Image.DAMAGED_WALL_1 = pygame.image.load("src/images/damagedwall1.png").convert_alpha()
        Image.DAMAGED_WALL_2 = pygame.image.load("src/images/damagedwall2.png").convert_alpha()
        Image.GHOST = pygame.image.load("src/images/ghost.png").convert_alpha()
        Image.GHOST = pygame.transform.scale(Image.GHOST, (Value.GHOST_SIZE, Value.GHOST_SIZE))
        Image.BOSS = pygame.image.load("src/images/boss.png").convert_alpha()
        Image.BOSS = pygame.transform.scale(Image.BOSS, (Value.BOSS_SIZE, Value.BOSS_SIZE))

class StaticPath ():
    DUNGEON_LAYOUT_DIR = "src/dungeonlayout/"

class StaticDungeonLayout ():
    DUNGEON_ROOM_WIDTH = 20
    DUNGEON_ROOM_HEIGHT = 15
    DUNGEON_WIDTH = 3
    DUNGEON_HEIGHT = 3
    WALL_CHAR = "#"
    TILE_CHAR = "-"
    PLAYER_CHAR = "P"
    MONSTER_CHAR = "M"
    SPAWNER_CHAR = "S"
    DAMAGED_WALL_CHAR = "%"
    GHOST_CHAR = "G"
    BOSS_CHAR = "B"

class Value(object):
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    FRAME_RATE = 60
    SPAWNER_RATE = 60 * 3 #How many seconds between each monster spawn
    CELL_SIZE = 32
    PLAYER_SIZE = 32
    PROJECTILE_SIZE = 16
    TERRAIN_SIZE = 32
    MONSTER_SIZE = 32
    SPAWNER_SIZE = 32
    UI_HEART_SIZE = 16
    GENERIC_ITEM_SIZE = 16
    FOODOFYENDOR_SIZE = 32
    HEART_CONTAINER_SIZE = 16
    MAX_HP = 3
    HEART_DROP_CHANCE = 0.25
    GHOST_SIZE = 32
    BOSS_SIZE = 64
    MONSTER_LIMIT = 16
