import time
from djitellopy import Tello
from codetiming import Timer

# Variables to declare a timer, the tello drone, and distances.
start = time.time()
t = Timer(name="time1")
t.start()
tello = Tello()
distance = 0
maxDistance = 500
observedDistance = 0
tello.connect()

# Print pre-trip flight information, enabling mission pads & timer.
print(tello.get_battery())
print("Preflight check parameters " + (str(t.stop()) + " seconds"))
t.start()
# Initial commands for take off, set movement & speed.
tello.takeoff()
t.stop()
t.start()
tello.set_speed(30)
tello.move_forward(50)
time.sleep(.50)
tello.move_forward(50)
time.sleep(.55)
tello.move_forward(50)
time.sleep(.50)
tello.land()
t.stop()
end = time.time()
print("Total distance traveled was " + str(observedDistance))
print("Total elapsed time was " + str(end - start))
tello.end()
