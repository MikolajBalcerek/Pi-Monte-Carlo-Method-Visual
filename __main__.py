import MonteCarlo;
import Visual;

global piValue;
piValue = 0;
global prevPiValue;
prevPiValue = 0;


# def give_me_a_number():
#     done = False;
#     while (done == False):
#         word = raw_input("Enter desired rectangle's length as an integer number (1-1000)");
#         try:
#             word = int(word);
#             print word;
#             if (word > 1 and word < 1000):
#                 print "Correct number";
#                 done = True;
#                 return word;
#                 #OK
#             else:
#                 print("Incorrect number, out of range")
#
#
#
#         except ValueError:
#             print ("That's not a number!");
#


calculations =  MonteCarlo.MonteCarlo();
#Okno wizualizacji
window = Visual.Visual();
#asking for radius
# rectangle = give_me_a_number();
#calculations.kwadrat = rectangle;
#starting calculations
window.loop_wizualizacja(calculations);

