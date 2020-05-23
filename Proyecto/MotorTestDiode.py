import time
import RPi.GPIO
 
 # Initializing the GPIO pins. The numbering using is board.
RPi.GPIO.setmode(RPi.GPIO.BOARD)
 
 # Configuring the GPIO pin number 8 to be an output pin.
RPi.GPIO.setup(8, RPi.GPIO.OUT)
RPi.GPIO.setup(10, RPi.GPIO.OUT)
 
print("Running Motor.")
 # Running the motor by changing the GPIO output pin state to high.
RPi.GPIO.output(8, RPi.GPIO.HIGH)
RPi.GPIO.output(10, RPi.GPIO.LOW)
# Leave the motor running for 3 seconds.
time.sleep(3)
 
 # Stop the motor by changing the GPIO output pin state back to low.
RPi.GPIO.output(10, RPi.GPIO.HIGH)
RPi.GPIO.output(8, RPi.GPIO.LOW)

time.sleep(3)
RPi.GPIO.output(8, RPi.GPIO.LOW)
RPi.GPIO.output(10, RPi.GPIO.LOW)
 
# cleanup all GPIO pins.
print("Clean Up GPIO.")
RPi.GPIO.cleanup()
