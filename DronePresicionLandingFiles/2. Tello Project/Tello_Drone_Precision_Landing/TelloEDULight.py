#import time, Tello, & Timer packages .
#from time ,djitellopy, & codetiming.
import time
from djitellopy import Tello
from codetiming import Timer
#start time variable names.


start = time.time()
t = Timer(name="time1")
t.start()
#Declare tello variable equal to the Tello drone itself.
tello = Tello()
#Distance variable set to 0.
distance = 0
#Max Distance variable set to 500.
maxDistance = 500
#observed distance variable set to 0
observedDistance = 0
#Tello connection is initialized.
tello.connect()
#Print battery life before flight.
print(tello.get_battery())
#Mission pads are enabled to be identified by Tello drone.
tello.enable_mission_pads()
#Mission pad direction set to 0 for detection.
tello.set_mission_pad_detection_direction(0)
#print preflight check parameters with a string representing the length of time has passed from t.start to t.stop. 
print("Preflight check parameters " + (str(t.stop()) + " seconds"))
#start timer.
t.start()
#command tello to take off. 
tello.takeoff()
#stop timer.
t.stop()
#start timer.
t.start()
#speed of tello movement is set at 100.
tello.set_speed(100)
#command tello to move down by 50 centimeters.
tello.move_down(50)
#stop timer.
t.stop()
#declare pad variable to gather mission pad ID data.
pad = tello.get_mission_pad_id()
#If detected, print string with the mission pad ID.
print("The Mission Pad Number is: " + str(pad))
#Delay next command by .25 seconds.
time.sleep(.25)
#Begin while loop with "When observedDistance is less than maxDistance".
while observedDistance < maxDistance:
#Start time.
    t.start()
#If statement for no pad detection. When the variable pad is equal to -1, print notifications of no pad detection and still searching.
    if pad == -1:
        print("No Mission Pad Detected")
        print("Still searching")
#Set distance variable to 25
        distance = 25
#Command the drone to move forward with distance variable as the length of movement.
        tello.move_forward(distance)
#Add distance variable length with observed distance to update it.
    observedDistance = observedDistance + distance
#Print new oberved distance.
    print("Distance traveled is " + str(observedDistance))
#Declare pad to get mission pad ID.
    pad = tello.get_mission_pad_id()
#Stop timer.
    t.stop()
#New if statement where pad is detected. 
    if pad == 3:
#Start timer.
        t.start()
#Print mission pad ID data and following string to take a break.
        print("The Mission Pad Number is: " + str(pad))
        print("Time to take a little break!")
#Command Tello to land.
        tello.land()
#Stop timer.
        t.stop()
#Break from loop.
        break
#If statement where out of bounds is set when observed distance is greater than or equal to 500cm.
if observedDistance >= 500:
    print("Range is out of bounds!")
    print("Abort mission/land now!")
#else statement where the drone is still in bounds.
else:
#end the timer. 
    end = time.time()
#Print total observed distance.
    print("Total distance traveled was " + str(observedDistance))
#Print total time the drone was running.
    print("Total elapsed time was " + str(end - start))
#Command tello to end tasks.
tello.end()
#End program.
quit()
