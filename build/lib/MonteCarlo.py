from __future__ import division;
import random;
import math;
import pygame;
import sys;
import __main__

class MonteCarlo:

    random.seed();  # Ustawiam random od czasu
    kwadrat = (10);  # dlugosc boku kwadratu
    center = (0, 0);  # srodek okregu
    r = (kwadrat / 2);
    Count_hit = 0;
    Count_overall = 0;
    wynik = 0;
    iterator = 0;

    def __breakup__(self, Visual):
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
                    return True;
            if event.type == pygame.VIDEORESIZE:
                Visual.window_height = event.h;
                Visual.window_width = event.w;
                Visual.__init__();

    def calulatePi(self, Visual):

        while not (self.__breakup__(Visual)):

            self.iterator = self.iterator + 1;
            # losuje punkt
            point = (random.SystemRandom.uniform(self.center[0], self.center[0] + self.r), random.SystemRandom.uniform(self.center[1], self.center[1] + self.r));
            # print "Wylosowany punkt: " , "\n X:", point[0], "\n Y:", point[1];

            # Czy punkt zawiera sie w kole?
            distance = math.hypot(point[0] - self.center[0], point[1] - self.center[1]);
            # print "Odlegosc od srodka: ", distance;
            Visual.draw_point(self, point[0], point[1]);

            if (distance <= self.r):
                self.Count_hit = self.Count_hit + 1;

            self.Count_overall = self.Count_overall + 1;

            if (self.Count_overall != 0):
                global prevPiValue;
                global piValue;
                __main__.prevPiValue = __main__.piValue;
                __main__.piValue = 4 * (self.Count_hit / self.Count_overall);
                Visual.text_estimate();





        if (self.Count_overall !=0):
            self.wynik = 4 *(self.Count_hit / self.Count_overall);
            print self.wynik;
