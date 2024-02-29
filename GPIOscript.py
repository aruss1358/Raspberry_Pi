#flip state test
import time
import RPi.GPI O as GPIO

GPIO.setmode(GPIO.BOARD)
channel=2
GPIO.setup(channel,GPIO)
state=False
def change_state(state):
    state= not state
    return(state)
def write_file(filename,text):
    with open(filename,a) as file:
        file.write(text)
        file.close()
filename="motion_log.txt"
while True:
    state=change_state(state)
    GPIO.output(channel,state)
    if state=True:
        text=f"Movement started{time.time()}"
    else:
        text=f"Movement stopped {time.time()}"
    write_file(filename,text)
    try:
        time.sleep(round(rand.uniform(30.0,180.0),2)
    except KeyboardInterrupt:
        break
    
