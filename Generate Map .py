"""
Made by Tiago Taquelim
19/03/17
Strategy game
"""

import pygame, random, os
from settings import *


pygame.init()
clock = pygame.time.Clock()

#Paths
game_folder = os.path.dirname(__file__)
graphics_folder = os.path.join(game_folder, "graphics")


font = pygame.font.SysFont(None, 25)
#game resources:
resource_food = 100
resource_wood = 100
resource_gold = 100
#CLASSES
class Window:
    def __init__(self):
    
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.display.fill(green)


        self.house = pygame.image.load(os.path.join(graphics_folder, "house.png")).convert_alpha()
        self.gold = pygame.image.load(os.path.join(graphics_folder, "gold.png")).convert_alpha()
        self.grass = pygame.image.load(os.path.join(graphics_folder, "grass.jpg")).convert_alpha()
        self.water = pygame.image.load(os.path.join(graphics_folder, "water.jpg")).convert_alpha()
        self.bar= pygame.image.load(os.path.join(graphics_folder, "bar.png")).convert_alpha()
        self.tree01 = pygame.image.load(os.path.join(graphics_folder, "tree01.png")).convert_alpha()
        

    def newMap(self):

        #Random map generation system
        tile_x = 0
        tile_y = 0

        self.tiles = []
        self.grass_tiles = []
        self.water_tiles = []

        last_rand = [0]

        for row in range(15):
            for col in range(26):

                rand = random.randint(0,1)
                last_rand.insert(0,rand)

                if rand == 0:
                    if last_rand[0] == 1:
                        rand2 = random.choice([1,1,1,1,1,1,1,1,0])
                        if rand2 == 0:
                            self.display.blit(self.grass, [tile_x,tile_y])
                            self.tiles.append([tile_x ,tile_y])
                            self.grass_tiles.append([tile_x , tile_y])
                            tile_x += 50
                        else:
                            self.display.blit(self.water, [tile_x,tile_y])
                            self.tiles.append([tile_x ,tile_y])
                            tile_x += 50
                    else:
                        self.display.blit(self.grass, [tile_x,tile_y])
                        self.tiles.append([tile_x ,tile_y])
                        self.grass_tiles.append([tile_x , tile_y])
                        tile_x += 50
                if rand == 1:
                    if last_rand[0] == 0:
                        rand2 = random.choice([0,0,0,0,0,0,0,0,1])
                        if rand2 == 1:
                            self.display.blit(self.water, [tile_x,tile_y])
                            self.tiles.append([tile_x ,tile_y])
                            tile_x += 50
                        else:
                            self.display.blit(self.grass, [tile_x,tile_y])
                            self.tiles.append([tile_x ,tile_y])
                            self.grass_tiles.append([tile_x , tile_y])
                            tile_x += 50
                    else:
                        self.display.blit(self.water, [tile_x,tile_y])
                        self.tiles.append([tile_x ,tile_y])
                        tile_x += 50

                
            tile_x = 0
            tile_y += 50
        
        #creating a list for tiles that are available to use, otherwise they would overwrite;
        self.avble_grass_tiles = self.grass_tiles.copy()
        self.avble_water_tiles = self.water.copy()

        #Gold spawning 
        self.gold_spawn_rate = random.randint(3,8)
        print("Gold spawn rate: ", self.gold_spawn_rate)

        for gold in range(self.gold_spawn_rate):
            self.gold_pos = random.choice(self.avble_grass_tiles)

            #Deleting gold from the available grass grass tiles;
            self.avble_grass_tiles.remove(self.gold_pos)

            self.display.blit(self.gold, [self.gold_pos[0], self.gold_pos[1]])
        
        #Tree spawning
        self.tree_spawn_rate = random.randint(5,18)
        print(self.tree_spawn_rate)
        for tree in range(self.tree_spawn_rate):
            self.tree_pos = random.choice(self.avble_grass_tiles)

            #Deleting tree from availavle grass tiles;
            self.avble_grass_tiles.remove(self.tree_pos)

            self.display.blit(self.tree01, [self.tree_pos[0],self.tree_pos[1]])

    
    def resourcesBar(self):
        food = str(resource_food)
        wood = str(resource_wood)
        gold = str(resource_gold)
        
        self.resources_text1 = font.render("Food: " + food , True, white)
        self.resources_text2 = font.render("Wood: "+ wood , True, white)
        self.resources_text3 = font.render("Gold: "+ gold, True, white)
        
        self.display.blit(self.resources_text1, [0,5])
        self.display.blit(self.resources_text2, [0,20])
        self.display.blit(self.resources_text3, [0,35])
        
    def highlight(self,tile):
        self.hrect = pygame.draw.rect(self.display, red, [tile[0], tile[1],50,50], 1)
        
class Build:
    def house(self,tile):
        display.display.blit(display.house, [tile[0] ,tile[1]])



#GAME LOOP
def gameLoop():
    global resource_wood, resource_food, resource_gold
    
    running = True
    while running:
        #Keep game running at right speed
        clock.tick(FPS)
        #Process input events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                                        
            if event.type == pygame.MOUSEBUTTONUP:
                action = True
                
                mouse_pos = pygame.mouse.get_pos()

                for tile in display.tiles:
                    #Knowing where i am clicking and transpalte it to a single tile;
                    if tile[0] <= mouse_pos[0] and (tile[0] + 50) >= mouse_pos[0] and tile[1] <= mouse_pos[1] and (tile[1] + 50) >= mouse_pos[1]:
                            if event.type == pygame.KEYDOWN:
                                
                                if event.key == pygame.K_b:
                                    
                                    if resource_wood - 50 >= 0:
                                        resource_wood = resource_wood - 50

                                        builder.house(tile)
                                        action = False



        #Update
        display.resourcesBar()
        #Draw / Render
        

        #Updating the display after the changes
        pygame.display.update()

    pygame.quit()
    quit()


#Game calling

display = Window()
builder = Build()
display.newMap()
gameLoop()










