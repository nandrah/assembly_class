#! usr/bin/python

#Rango de medicion  de 2cm  a 3 m.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)  # Pines de acuerdo al Microprocesador

TRIG=16   # Disparo del ultrasonido
ECHO=18  # Si ECHO=1,la  senal ultrasonica ha sido recibida
print "Medicion de distancia en progreso"
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print "Esperando la respuesta del sensor "
time.sleep(2)
    
#Mandar la senal ultrasonica con un 1 en TRIG
GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

# Ver cuanto tiempo tarda el receptor estar en 0 logico
while GPIO.input(ECHO)==0:
    pulse_start=time.time()
    # Si ECHO ==1, entonces hemos recibido la senal de sonido de vuelta.
while GPIO.input(ECHO)==1:
    pulse_end=time.time()
        #Sabremos con facilidad cuanto duro el pulso con:
pulse_duration=pulse_end-pulse_start
    # La distancia total debe dividirse por 2, ya que fue de ida y vuelta. 
    # La velocidad del sonido es de 34300 cm/s.  V=D/T.
distancia=pulse_duration * 17150
    #Expresamos la distancia con dos digitos decimales.
distancia=round(distancia,2)

print "Distancia:" , distancia, "cm"

