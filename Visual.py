import pygame;
import sys;
import MonteCarlo;

class Visual:
    gameExit = False;
    clock = 0;
    pygame.init();

    FPS = 60;

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    window_width = 1000;
    window_height = 1000;

    myfont = pygame.font.SysFont("monospace", 15)
    podpis = myfont.render("Mikolaj Balcerek s416040", 1, (0, 0, 0))

    def __init__ (self):
        gameDisplay = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        pygame.display.set_caption('Pi Monte Carlo Mikolaj Balcerek s416040')
        self.clock = pygame.time.Clock();
        gameDisplay.fill(self.white);
        gameDisplay.blit(self.podpis, (0, 0));
        pygame.display.update();
        self.clock.tick(self.FPS);


    def loop_wizualizacja(self, MonteCarlo):
        while not self.gameExit:  # game_loop
            for event in pygame.event.get():  # event_loop
                if event.type == pygame.QUIT:
                    gameExit = True;
                    pygame.quit();
                    quit();
                    sys.quit();


                if event.type == pygame.KEYDOWN:
                    # CZAT
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        gameExit = True;
                        pygame.quit();
                        quit();
                        sys.quit();
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE or event.key == pygame.K_s:
                        MonteCarlo.calulatePi();


                if event.type == pygame.VIDEORESIZE:
                    self.window_height = event.h;
                    self.window_width = event.w;
                    self.__init__();
