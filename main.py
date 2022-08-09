import time

import pygame as pg


def pg_keybs():

    pygame.init()


    screen_wight = 600
    screen_hight = 300
    BG_COLOR = (50, 150, 250)

    screen = pg.display.set_mode((screen_wight, screen_hight))
    screen.fill(BG_COLOR)

    rect_wight = 100
    rect_height = 50
    rect_color = (200, 150, 50)
    some_rectangle = pygame.draw.rect(screen, rect_color,
                                      (int(screen_wight / 3), int(screen_hight / 3),
                                      int(screen_wight / 3 + rect_wight), int(screen_hight / 3) + rect_height))

    some_hitbox = pygame.Rect(100, 100, 10, 40)
    some_surface = pygame.Surface((10, 40))
    some_surface.fill((150, 250, 50))

    run = True

    speed = 0

    while run:

        # for event in pygame.event.get():
        #
        #     if event.type == pygame.QUIT:
        #         run = False
        #
        #     print('event.type - ', event.type)



            # if pygame.event.get() != []:
            #     print('pygame.event.get() - ', pygame.event.get())
            #     ttt = pygame.event.get()[eventtype]
            #     time.sleep(5)
            # if pygame.event.get() == pygame.QUIT:
            #     run = False

            keys = pygame.key.get_pressed()

            print('pygame.key.get_pressed() - ', pygame.key.get_pressed())
            print('keys - ', keys)

            print('keys[pygame.K_LEFT - ', keys[pygame.K_LEFT])
            print('keys[pygame.K_RIGHT - ', keys[pygame.K_RIGHT])

            if keys[pygame.K_LEFT]:
                some_hitbox.x += -10
            elif keys[pygame.K_RIGHT]:
                some_hitbox.x += 10

            time.sleep(0.1)

            # print('speed - ', speed)
            # some_hitbox.x += speed




            # if event.type == pygame.KEYDOWN:
            #     print('event.key - ', event.key)
            #     print('event.mod & pygame.KMOD_SHIFT - ', event.mod & pygame.KMOD_SHIFT)
            #
            #     if event.mod & pygame.KMOD_SHIFT == 1:
            #         step = 10
            #     elif event.mod & pygame.KMOD_SHIFT == 0:
            #         step = 30
            #
            #     # if event.key == pygame.K_RIGHT:
            #     #     step = 30
            #     if event.key == pygame.K_RIGHT:
            #         some_hitbox.x += step
            #
            #     elif event.key == pygame.K_LEFT:
            #         some_hitbox.x -= step

            screen.fill(BG_COLOR)

            screen.blit(some_surface, some_hitbox)

            pygame.display.flip()


def main():
   pg_keybs()


if __name__ == '__main__':
    main()
