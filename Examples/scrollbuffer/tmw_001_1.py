__doc__ = """
Demo of The Mana World map. This map uses one background layer, and two sorted
layers for a 2.5D rendered view.

If the map were not 2.5D we could just render everything onto the scroll buffer.
But in this case it's probably not enough to just render the map as background.
Rather, the game would want to mingle dynamic content with the Fringe layer
(trees and other stuff), which would result in mobile objects (players, NPCs)
passing in front of or behind trees depending on their Y position.

TO DO: Try rendering layers 1 and 2 onto their own scroll buffer (surface with
colorkey) to see if that performs better.
"""

import pygame
from pygame.locals import *
import paths
import tiledmap
import spatialhash
import scrollbuffer


def render_scrollbuffer_all(screen, sbuf, map_layer):
    def get_tiles(rect):
        tiles = map_layer.intersect_objects(rect)
        return tiles
    sbuf.pre_render()
    sbuf.render_all(get_tiles)
    screen.blit(sbuf.surface, (0,0))


def render_scrollbuffer(screen, sbuf, map_layer):
    def get_tiles(rect):
        tiles = map_layer.intersect_objects(rect)
        return tiles
    sbuf.pre_render()
    sbuf.render(get_tiles)
    screen.blit(sbuf.surface, (0,0))


def render_content(screen, camera_rect, map_layers):
    blit = screen.blit
    cx = camera_rect.x
    cy = camera_rect.y
    sortkey = lambda t:t.rect.bottom
    for sh in map_layers:
        for tile in sorted(sh.intersect_objects(camera_rect), key=sortkey):
            trect = tile.rect
            blit(tile.image, (trect.x-cx,trect.y-cy))


def main():
    global global_debug
    global_debug = False
    
    # Init pygame stuff.
    pygame.init()
    resolution = 1024,768
    screen = pygame.display.set_mode(resolution, DOUBLEBUF)
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()
    black = Color('black')
    
    # Map, camera, and scroll buffer.
    world_map = tiledmap.TiledMap('map/001-1.tmx', sortkey=lambda t:(t.rect.bottom,t.rect.x))
    map_layers = []
    for layer in world_map.get_tile_layers():
        sh = spatialhash.SpatialHash(world_map.rect, 128)
        for col in layer.content2D:
            for tile in [t for t in col if t]:
                sh.add(tile)
        map_layers.append(sh)
    print 'Resolution:',resolution
    print 'Tile Size:', world_map.tile_size
    print 'Map Size:', world_map.size
    print 'Tiles Per Screen', (screen_rect.w/float(world_map.tile_width)) * (screen_rect.h/float(world_map.tile_height))
    cam_rect = Rect(screen_rect)
    sbuf = scrollbuffer.ScrollBuffer(screen.copy(), world_map.rect)
#    sbuf = ScrollBufferOpt(screen.copy(), world_map.rect)
    
    # Render buffer in full.
#    sbuf.render_all(world_map.get_tiles_in_rect)
    render_scrollbuffer_all(screen, sbuf, map_layers[0])
    render_content(screen, sbuf.camera_rect, map_layers[1:3])
    pygame.display.flip()
    
    mouse_down = False
    mouse_pos = None
    keyx = keyy = 0
    dx = dy = 0
    speed = 1
    elapsed = 0
    nfps = fps = 0
    running = True
    
    while running:
        
        # FPS meter.
        elapsed += clock.tick()
        if elapsed >= 1000:
            pygame.display.set_caption('{0:.0f} fps | Tiles: {1},{2}'.format(
                clock.get_fps(),
                sbuf.num_tiles_x,
                sbuf.num_tiles_y,
            ))
            fps += clock.get_fps()
            nfps += 1
            elapsed %= 1000
        
        # Controls: (shift) cursor keys; mouse drag.
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RIGHT: keyx = 1
                elif e.key == K_LEFT: keyx = -1
                elif e.key == K_DOWN: keyy = 1
                elif e.key == K_UP: keyy = -1
                elif e.key == K_F2: global_debug = not global_debug
                elif e.key == K_ESCAPE: running = False
            elif e.type == KEYUP:
                if e.key in (K_LEFT,K_RIGHT): keyx = 0
                elif e.key in (K_DOWN,K_UP): keyy = 0
            elif e.type == QUIT: running = False
            elif e.type == MOUSEBUTTONDOWN:
                mouse_down = True
            elif e.type == MOUSEBUTTONUP:
                mouse_down = False
            elif e.type == MOUSEMOTION:
                dx,dy = e.rel
        
        # Update the camera position and render the buffer.
        if mouse_down:
            sbuf.scroll(dx*2,dy*2)
#            sbuf.render(world_map.get_tiles_in_rect)
            render_scrollbuffer(screen, sbuf, map_layers[0])
            dx = dy = 0
        else:
            shift = 1
            if pygame.key.get_mods() & KMOD_SHIFT:
                shift = 5
            dx = keyx * speed * shift
            dy = keyy * speed * shift
            sbuf.scroll(dx,dy)
#            sbuf.render(world_map.get_tiles_in_rect)
            render_scrollbuffer(screen, sbuf, map_layers[0])
        
        # Render the display.
        render_content(screen, sbuf.camera_rect, map_layers[1:3])
        pygame.display.flip()
    
    print 'Avg FPS:', fps / nfps


if __name__ == '__main__':
    if True:
        main()
    else:
        cProfile.run('main()', 'prof.dat')
        p = pstats.Stats('prof.dat')
        p.sort_stats('time').print_stats()
