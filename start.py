#!-
#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
from video_capture import record_video
from send_video import send_video

video_length = 30 # Measured in seconds larger numbers = larger file size smaller is better due to network
GPIO.setmode(GPIO.BOARD)
RECIPIENT_EMAIL="inyangete@gmail.com"
SENDER_EMAIL="kboysreel@gmail.com"
SENDER_PASSWORD = "19sedimat54"

#define the pin that goes to the circuit
pin_to_circuit = 7
buzzpin = 11
DARKNESS_THRESHOLD = 8000


def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count
    
def beep():

    #GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzpin, GPIO.OUT)
    GPIO.output(buzzpin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(buzzpin, GPIO.LOW)
    print("Beeping..!!!")


#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        ldr_value = rc_time(pin_to_circuit)
        print(ldr_value)
        if ldr_value > DARKNESS_THRESHOLD:
            
            beep()
            record_video(30)
            send_video(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()