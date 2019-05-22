
import numpy as np
import matplotlib.pyplot as plt 
from numpy.fft import fft, fftfreq, ifft


##numero de puntos o muestras
n= 1000;

##Periodo de la señal;
N = 100;

##OMG (frecuencia angular)
W = 2.0*np.pi/N

##Array qeu contiene un intervalo de (0 a 100,con 1000 valores aleatorios entre ellos)
x=np.linspace(0,N,n);
##Señal de ejemplo
SOne= 0.5*np.cos(5.0*W*x)

##se crean las frecuencias necearias
frecuencias = fftfreq(n)

##se calcula los valores de la fft
fftOg= fft(SOne)

## se calcula la fft teorica
##Se calcula la magnitud de la señal fftOg 
##Asi mismo se normaliza la señal fftOG

fftTeorico = 2.0*np.abs(fftOg/n)

##Se dibuja la señal original
plt.figure(1)
plt.title('Señal base Original')
plt.plot(x,SOne, color='xkcd:blue', label='original')
plt.legend()

##Se dibuja la señal fft
plt.figure(2)
plt.title('FFT sin normalizar')
plt.plot(frecuencias,fftOg, color='xkcd:red', label='original')
plt.legend()


#Se cuadra el dominio de la grafica
dom = frecuencias>0


##Se dibuja la fft ya normalizada
plt.figure(3)
plt.title('fft normalizada')
plt.plot(frecuencias[dom],fftTeorico[dom], color='xkcd:green', label='verdaderos volores de la fft')
plt.show()












