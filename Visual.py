import pygame;
import sys;

class Visual:
    gameExit = False;

    def __init__ (self):
        pygame.init();
        window_width = 1000;
        window_height = 1000;
        FPS = 60;
        gameDisplay = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
        pygame.display.set_caption('Pi Monte Carlo Mikolaj Balcerek s416040')
        clock = pygame.time.Clock();

    def loop_wizualizacja(self):
        while not self.gameExit:  # game_loop
            for event in pygame.event.get():  # event_loop
                if event.type == pygame.QUIT:
                    gameExit = True
                    sys.exit();
                if event.type == pygame.KEYDOWN:
                    # CZAT
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        gameExit = True
                        sys.exit();
                if event.type == pygame.VIDEORESIZE:
                    window = pygame.display.set_mode((event.w, event.h),
                                                      pygame.RESIZABLE);
        pygame.display.update();
        clock.tick(FPS);
        pygame.quit();
        quit();