from __future__ import division;
import random;
import math;

class MonteCarlo:

    random.seed();  # Ustawiam random od czasu
    kwadrat = (10);  # dlugosc boku kwadratu
    center = (0, 0);  # srodek okregu
    r = (kwadrat / 2);
    Count_hit = 0;
    Count_overall = 0;
    wynik = 0;

    def calulatePi(self):
        for iterator in range(0, 1000000, 1):

            # losuje punkt
            point = (random.uniform(center[0], center[0] + r), random.uniform(center[1], center[1] + r));
            # print "Wylosowany punkt: " , "\n X:", point[0], "\n Y:", point[1];

            # Czy punkt zawiera sie w kole?
            distance = math.hypot(point[0] - center[0], point[1] - center[1]);
            # print "Odlegosc od srodka: ", distance;


            if (distance <= r):
                Count_hit = Count_hit + 1;

            Count_overall = Count_overall + 1;

            if (iterator % 100000 == 0):
                print "Ciagle licze, jestem na..", iterator;

        wynik = 4 * (Count_hit / Count_overall);
        print wynik;
