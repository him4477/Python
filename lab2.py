# NAME : HIMANSHU SHARMA
# PRA Section: PRA0101

import math

v=float(input("Define velocity in [m/s]: "))
theta=float(input("Define theta in [degrees]: "))
del_h=float(input("Define theta in altitude in [m]: "))

def horizontal_distance(v, theta, del_h):
    
    """ (num, num, num) -> (num)
    This function recieves initial velocity, launch angle, and altitute change
    in the landing position and returns the horizontal range of a projectile.

    v     is in [m/s]
    theta is in [degrees]
    del_h is in [m]
    g is 9.81 in [m/s^2]
    >>> range = horizontal_distance(100, 20, 40)
    >>> range
	515.5652309241808
        
    """
    g = 9.81
    
    W =v*math.cos(theta*math.pi/180)

    X=v*math.sin(theta*math.pi/180)/g

    Y=(v**2)*(math.sin(theta*math.pi/180)**2)/g**2

    Z=2*del_h/g

    range = W*(X+ math.sqrt(Y-Z))

    return range

""" THIS CAN TEST YOUR CODE """
#velocity = 100
#angle = 20
#delta_h = 40

print("\nThe range is: " + str(horizontal_distance(v, theta, del_h)))
