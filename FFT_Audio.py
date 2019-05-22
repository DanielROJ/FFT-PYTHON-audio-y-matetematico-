
import numpy as np  
import matplotlib.pyplot as plt 
from scipy.io import wavfile 
from numpy.fft import fft, fftfreq, ifft

#Fs frecuencia de muestreo
## donde fs = 2Fmax de la señal original
#permite recuperar por medio de muestras la señal original
#cumpliendo el teorema de muestreo de Nyquist-Shannnon


#data son datos extraidos del audio

fs, data = wavfile.read('chopin.wav')
print('Esta es la frecuencia de muestreo : ',fs)
#se cuentan el numero de muestras de la señal
nMuestras = len(data)
print('esta es la data: ',data)
#se obtiene las frecuencias segun el numero de muestras
frecuencias = fftfreq(nMuestras)



#Se realiza los valores de la  fft
ffftOg = fft(data)


frecuenciaHerzt = (frecuencias*fs)
print('Frecuencia en herzt ',frecuenciaHerzt)
plt.figure(1)
plt.title('fft del audio de chopin')
plt.plot(frecuenciaHerzt,abs(ffftOg),color='xkcd:purple', label='señal en frecuencia')
plt.show()









