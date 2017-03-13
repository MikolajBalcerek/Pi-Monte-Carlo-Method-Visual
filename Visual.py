import __main__
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
    window_width = 1080;
    window_height = 720;
    radius = window_height * window_width / 4000;
    gameDisplay = 0;
    myfont = pygame.font.SysFont("monospace", (window_width * window_height) / 35000)

    def __init__ (self):
        self.gameDisplay = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        pygame.display.set_caption('Pi Monte Carlo Mikolaj Balcerek s416040')
        self.clock = pygame.time.Clock();


        self.gameDisplay.fill(self.white);



        podpis = self.myfont.render("Mikolaj Balcerek s416040", 1, (0, 0, 0))

        self.text_estimate();

        instructions = self.myfont.render("Press SPACEBAR or s to start and resume..", 1, (0, 0, 0))
        self.gameDisplay.blit(podpis, (0, 0));
        self.gameDisplay.blit(instructions, (0, 0.95 * self.window_height));

        pygame.draw.circle(self.gameDisplay, 30, [self.window_width/2, self.window_height/2], (self.window_height * self.window_width) / 4000, 2);

        pygame.draw.line(self.gameDisplay, 0, [0, self.window_height/2], [self.window_width, self.window_height/2], 2);
        pygame.draw.line(self.gameDisplay, 0, [self.window_width/2, self.window_height], [self.window_width/2, 0], 2);

        pygame.display.update();
        self.clock.tick(self.FPS);


    def text_estimate(self):
        global prevPiValue;
        piprevEstimate = self.myfont.render("Current Pi approximation: " + str(__main__.prevPiValue), 500, self.white);
        self.gameDisplay.blit(piprevEstimate, (0, self.window_height * 0.9));


        global piValue;
        piEstimate = self.myfont.render("Current Pi approximation: " + str(__main__.piValue), 1, self.red);

        self.gameDisplay.blit(piEstimate, (0, self.window_height * 0.9));
        pygame.display.update();
        self.clock.tick(self.FPS);


    def loop_wizualizacja(self, MonteCarlo):

        while not self.gameExit:  # game_loop
            pygame.display.update();
            self.clock.tick(self.FPS);

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
                        MonteCarlo.calulatePi(self);


                if event.type == pygame.VIDEORESIZE:
                    self.window_height = event.h;
                    self.window_width = event.w;
                    self.__init__();
