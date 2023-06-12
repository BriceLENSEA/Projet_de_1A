#!/usr/bin/env python
import sys
import rospy
from transfo.srv import ∗

def transfo_client(X, Y, Z,theta1,theta2,theta3):
  rospy.wait_for_service(’transfo’)
  try:
    transfo = rospy.ServiceProxy(’transfo’, Transfo)
    resp1 = transfoXYZtheta(theta1,theta2,theta3, X, Y, Z)
    return resp1.angle1,resp1.angle2,resp1.angle3,resp1.X,resp1.Y,resp1.Z
except rospy.ServiceException, e:
  print "Service call failed: %s"%e

def usage():
  return "%s [theta1,theta2,theta3, X, Y, Z]"%sys.argv[0]
if __name__ == "__main__":
  if len(sys.argv) == 6:
    X = int(sys.argv[1])
    Y = int(sys.argv[2])
    Z = int(sys.argv[3])
    angle1 = int(sys.argv[4])
    angle2 = int(sys.argv[5])
    angle3 = int(sys.argv[6])
  else:
    print usage()
    sys.exit(1)

