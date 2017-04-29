import MonteCarlo;
import Visual;

global piValue;
piValue = 0;
global prevPiValue;
prevPiValue = 0;


calculations =  MonteCarlo.MonteCarlo();
#Okno wizualizacji
window = Visual.Visual();
window.loop_wizualizacja(calculations);








