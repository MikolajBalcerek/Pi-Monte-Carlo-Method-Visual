from __future__ import division;
import random;
import math;
import Visual;

#Okno wizualizacji
window = Visual.Visual();
window.loop_wizualizacja();

random.seed(); #Ustawiam random od czasu
kwadrat = (10); #dlugosc boku kwadratu
center = (0, 0); #srodek okregu
r = (kwadrat/2);
Count_hit = 0;
Count_overall = 0;
wynik = 0;

for iterator in range(0,1000000,1):

    #losuje punkt
    point = (random.uniform(center[0], center[0] + r), random.uniform(center[1],center[1] + r));
    #print "Wylosowany punkt: " , "\n X:", point[0], "\n Y:", point[1];

    #Czy punkt zawiera sie w kole?
    distance = math.hypot(point[0] - center[0], point[1] - center[1]);
    #print "Odlegosc od srodka: ", distance;


    if (distance <= r):
         Count_hit = Count_hit + 1;

    Count_overall = Count_overall + 1;

    if (iterator%100000 == 0):
        print "Ciagle licze, jestem na..", iterator;

wynik = 4 * (Count_hit / Count_overall);
print wynik;



def init_wizualizacja():
    pygame.init();
    window_width = 1000;
    window_height = 1000;
    FPS = 60;
    gameDisplay = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Pi Monte Carlo Mikolaj Balcerek s416040')
    gameExit = False
    clock = pygame.time.Clock()





