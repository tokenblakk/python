
################################################################################
##    @author: TokenBlakk                                                     ##
##    2-D Platformer in Pygame                                                ##
##    res: 640, 480                                                           ##
##                                                                            ##
##                                                                            ##
##################   SMALL TIME OCTOPUS STARS ##################################
try:
    import pygame, sys
    from pygame.locals import *
except ImportError, err:
    print "%s Failed to Load Module: %s" % (__file__, err)
    import sys
    sys.exit(1)

##
##class allsprites(pygame.sprite.RenderPlain):
##    def __init__(self)
##    
##    
##class blockGroup(pygame.sprite.RenderPlain):
##    
##class playerGroup(pygame.sprite.RenderPlain):
##    
##class mobGroup(pygame.sprite.RenderPlain):
    
    




class Player(pygame.sprite.Sprite):
    """PLAYER SPRITE. Wiggly Tentacles or any player object
    takes surcace image, height, position(Must pass a Rect) ,BlockTARGETs, and speed args  """
    def __init__(self, image, height, position = 0, target = None, dx = 0, dy = 0):
        pygame.sprite.Sprite.__init__(self) #sprite init
        #Set image and rect
        self.image = image
        self.target = None
        if target:
            self.target = target
        if not position == 0:
            self.rect = position
        else:
            self.rect = image.get_rect()
        #Set speed and other personal vars
        self.key = 0
        self.dx = dx
        self.dy = dy
        self.crouched = False
        self.in_air = False
        self.jumped = False
        self.djumped = False
        #Timers on jump so it will have a delay to double jump
        self.time_in_air = pygame.time.Clock()
        self.jump_timer = pygame.time.Clock()
        
        #Hitbox slightly smaller than sprite
        self.hbox = self.rect.inflate(-5, -5)

    def move(self, press):
        '''Moves player based on User Input '''
        #Player can not move outside of US borders
        '''TODO: FIX THIS TO MAKE IT FIT THE LEVEL BOUNDS INSTEAD OF SCREEN BOUNDS'''
##        if self.rect.right > 640:
##            self.rect.right = 640
##        if self.rect.left < 0:
##            self.rect.left = 0
##        if self.rect.top < 0:
##            self.rect.top = 0
##        if self.rect.bottom > 480:
##            self.rect.bottom = 480

##        jumping = False
##        crouching = False
##        moveLeft = False
##        moveRight = False
            
        #Catch and read user input
        #Reset Jumped status 
##        if not self.in_air:
##            self.drop(0)
##            self.jumped = False
##            self.djumped = False

        #resets jumps and controls drops
        self.airbourne()
        if press == 0:
            self.stop()            
        if press ==  1:
            if self.jumped:
                if not self.djumped:
                    timey = self.jump_timer.get_time()
                    print timey 
                    if timey > 16:
                        self.djump()
            else:
                #self.jump_timer.tick()
                self.jump()
        if press == 2:
            self.crouch()
        if press != 2:
            self.crouched = False
        if press == 3:
            self.moveLeft()
        if press == 4:
            self.moveRight()
        if not self.in_air:
            print "Grounded"
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if not self.crouched:
            self.image = pygame.image.load('wiggly.gif').convert()

    def moveLeft(self):
        if self.dx == -10:
            pass
        else:
            self.dx -= 2
    def moveRight(self):
        if self.dx == 10:
            pass
        else:
            self.dx += 2
    def stop(self):
        self.dx = 0

    def jump(self):
        '''Jump And Double Jump'''
        if not self.in_air:
            self.jump_timer.tick()
            self.dy -= 10
            self.in_air = True
            self.jumped = True
            print "jump"
        
    def djump(self):
        '''Double Jump'''
        if self.jumped:
            self.dy -= 10
            self.djumped = True
            print "jumpman"
            #self.drop()
            
    def crouch(self):
        '''As of Now, moves sprite down'''
        if not self.in_air:
            self.crouched = True
            self.rect.centery += 10
            self.image = pygame.image.load('wigglycrouch3.gif').convert()
        else:
            self.drop(4)
        
    def drop(self, magnitude = 1):
        '''Gravity, maybe a higher magnitude will help(make shit fly across the map)'''
        if self.touching_floor():
            self.dy = 0
        elif self.dy > 20:
            self.dy = 20
        elif self.dy < -20:
            self.dy = -20
        elif self.in_air:
            self.dy += (4.9 * (self.time_in_air.get_time() * .01)) * magnitude
            

    def airbourne(self):
        '''TODO: Fix grounded or airbourne status, coll detect with a block(Done in the touching_floor method)'''
        #Reset Jumped status
        if not self.touching_floor():
            self.in_air = True
            self.time_in_air.tick()
            self.jump_timer.tick()
        if not self.in_air:
            self.drop(0)
            self.jumped = False
            self.djumped = False
        elif self.in_air: 
            self.drop(1)

    #
    #        char.rect.bottom = self.rect.top
    #        char.in_air = False

            
    def touching_floor(self):
        blocks = pygame.sprite.spritecollide(self, self.target, 0)
        for block in blocks:
            if abs(self.rect.left - block.rect.right) < 5:
                self.rect.left = block.rect.right + 5
                print "l"
            if abs(self.rect.right - block.rect.left) < 5:
                self.rect.right = block.rect.left - 5
                print "r"
            if abs(self.rect.top - block.rect.bottom) < 5:
                self.rect.top = block.rect.bottom + 50
                print "b"
            else:
                self.rect.bottom = block.rect.top + 1
                self.in_air = False
            #print "yee"
                return True
        #print "nah mang"
        return False
##    def touching_floor(self, target_list):
##
##        for block in target_list:
##            if abs(self.rect.bottom - block.rect.top) <2:
##                print "yee"
##                return True
##            else:
##                print "nah"
##                return False
            
    def update(self):
        """Update sprite, every frame, calls move on player input keys"""
        #print self.key
        self.move(self.key)


class Floor(pygame.sprite.Sprite):
    """Block Sprite, platform floor"""
    def __init__(self, image, height, position = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        if not position == 0:
            self.rect = Rect(position)
        else:
            self.rect = image.get_rect()
        self.hbox = self.rect.inflate(-5, -5)


    #def update(self, target_list):
     #   self.solid(target_list)

    def solid(self, target_list):
        
        col_list = pygame.sprite.spritecollide(self, target_list, 0)
        for char in col_list:
            char.rect.bottom = self.rect.top
            char.in_air = False
            #if char not in col_list:
                #char.in_air = True
        
        
       # if self.touching_player(target):
       #     target.pos.bottom = self.pos.top
#        else:
#            target.pos.bottom = target.pos.bottom


    def touching_other(self, target_list):
            if pygame.sprite.spritecollide(self, target_list, 0):
                return True
            else:
                return False
            
##    def touching_player(self, target):
##            if self.col_rect.colliderect(target.col_rect):
##                return True
##            else:
##                return False

##    def update(self, players):
##        self.solid(players)



##class ScreenScroll:
##    speed = 2
##    def __init__(self):
##        w = SCREENRECT.width
##        h = SCREENRECT.height
##        self.tileside = self.oceantile.get_height()
##        self.counter = 0
##        self.ocean = pygame.Surface((w, h + self.tileside)).convert()
##        for x in range(w/self.tileside):
##            for y in range(h/self.tileside + 1):
##                self.ocean.blit(self.oceantile, (x*self.tileside, y*self.tileside))
##    def increment(self):
##        self.counter = (self.counter - self.speed) % self.tileside
##    def decrement(self):
##        self.counter = (self.counter + self.speed) % self.tileside




class Game(object):
    """Inits pygame and sets up game, handles gameplay logic"""
    
    def __init__(self):
        """inits pygame, loads a window, tools. (Strewn through previous code)"""
        # Init Pygame
        pygame.init()
        # Create window
        self.screen = pygame.display.set_mode((640, 480))
        # Clock
        self.clock = pygame.time.Clock()
        # Baller ass window title
        pygame.display.set_caption("Small Time Octopus Stars!")

        # Pygame keys to pay attentin to
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

        # loads background
        self.background = pygame.image.load('background.png').convert()
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        # Loads images
        player_image = pygame.image.load('wiggly.gif').convert()
        block_image = pygame.image.load('block.png').convert()
        
        # A group containing all sprites
        self.sprites = pygame.sprite.RenderUpdates()
        # Group of all FloorBlocks
        self.floor_blocks = pygame.sprite.RenderUpdates()
        # list of player sprites
        self.players = pygame.sprite.RenderUpdates()

        
        # 10 Blocks created and added to groups
        for b in xrange(10):
            block = Floor(block_image, 50, Rect(b*50, 200, 50, 50))
            self.sprites.add(block)
            self.floor_blocks.add(block)
        for x in xrange(13):
            block1 = Floor(block_image, 50, Rect(x*50, 400, 50, 50))
            self.sprites.add(block1)
            self.floor_blocks.add(block1)

        # Player created and added to groups
        self.player = Player(player_image, 50, Rect(11, 22, 50, 50), self.floor_blocks)
        self.sprites.add(self.player)
        self.players.add(self.player)

        
        print "Init done."

    def run(self):
        '''Runs the game. Compute and render each frame
        within this game loop'''
        print "Game Start!"

        running = True
        while running:
            self.clock.tick(60)
            # tick clock
            
            # Ingame event handler, checks input and when to close
            running = self.eventHandle()
            # Display fps on title bar
            pygame.display.set_caption('Small Time Octopus Stars!  %d fps' % self.clock.get_fps())

            # Update sprites
            self.sprites.update()
            #self.floor_blocks.update()
            #self.players.update()

            # Render sprites
            self.sprites.clear(self.screen, self.background)
            self.screen.blit(self.background, (0, 0))
            dirty = self.sprites.draw(self.screen)

            # Flip the dirty bits
            #pygame.display.update(self.background)
            pygame.display.update(dirty)
        print "Quit"
        pygame.quit()
        sys.exit()
        
            
            
    def eventHandle(self):

    
    # Check For Events
        for event in pygame.event.get():
        # Check If User Quits
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == KEYDOWN:
                # if the user presses escape, quit the event loop.
                if event.key == K_ESCAPE:
                    return False

            if self.player.rect.right >= 640:
                print "scroll right"
                self.background.scroll(50)
##            if self.player.rect.left < 0:
##                self.rect.left = 0
##            if self.player.rect.top < 0:
##                self.player.rect.top = 0
##            if self.player.rect.bottom > 480:
##                self.rect.bottom = 480
##
            
            if self.keyPressed(K_UP):
                self.player.key = 1
            elif self.keyPressed(K_DOWN):
                self.player.key = 2
            elif self.keyPressed(K_LEFT):
                self.player.key = 3
            elif self.keyPressed(K_RIGHT):
                self.player.key = 4
            else:
                self.player.key = 0
        return True


    def keyPressed(self, inputKey):
        keysPressed = pygame.key.get_pressed()
        if keysPressed[inputKey]:
            return True
        else:
            return False
                
        # User input

    

    
'''
        if pygame.key.get_pressed()[K_UP]:
            self.player.key = 1
        if pygame.key.get_pressed()[K_DOWN]:
            self.player.key = 2
        if pygame.key.get_pressed()[K_LEFT]:
            self.player.key = 3
        if pygame.key.get_pressed()[K_RIGHT]:
            self.player.key = 4
        else:
            self.player.key = 0

        #also try if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE
                print "Space Pressed"
        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_SPACE :
              print "Space bar released." 
'''

'''MAIN FUNCTION '''

#make a game class and run it
if __name__ == '__main__':
    game = Game()
    game.run()




"""BULLSHIT"""

##
##pygame.display.update()
##keys = []
##dirty_player = [] 
##dirty_blocks = []


##block_group.update(player_group) ## calls solid on each block
##print "block updated"
##for block in block_group:
##    screen.blit(block.image, block.pos)
###dirty_blocks = block_group.draw(screen) #draws blocks and returns dirty blocks
##print "block drawn (fingers crossed)"
##dirty_player = player_group.draw(screen)
###for player in player_group:
###    screen.blit(player.image, player.pos)
##print "player drawn"
##pygame.display.update()
##print "first frame"

##GAME LOOP
##while 1:
##    keys = list(eventChecker())
##    print keys
##    print keys[0]
##    print keys[1]
##    print keys[2]
##    
    #for player in player_group:
        #player.update(keys)
    ##player_group.update(keys)
##    #block_group.update(player_group)
##    dirty_player = player_group.draw(screen) ##draw player and display changes
##    dirty_blocks = block_group.draw(screen)
##    pygame.display.update(dirty_player)
##    pygame.display.update(dirty_blocks)
##    player_group.clear(screen, background_image)
##    pygame.time.delay(100)
##
    #screen.blit(background, p.pos, p.pos)
    #dirty_rects.append(p.pos)
    #for block in blocks:
        #block.update
        #block.solid(p)
        #screen.blit(block.image, block.pos)
    
    #screen.blit(p.image, p.pos) obselete



##        self.col_rect = pygame.Rect(self.pos[0] - 5, self.pos[1] - 5, self.pos[2] - 5, self.pos[3] -5)

##        #Search if key is pressed
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.key.K_DOWN:
##                crouching = True
##            if event.key == K_UP:
##                jumping = True
##            if event.key == K_RIGHT:
##                moveRight = True
##            if event.key == K_LEFT:
##                moveLeft = True
##
##
##        #Search if key is released
##        if event.type == pygame.KEYUP:
##            if event.key == K_DOWN:
##                crouching = False
##            if event.key == K_UP:
##                jumping = False
##            if event.key == K_RIGHT:
##                moveRight = False
##            if event.key == K_LEFT:
##                moveLeft = False
