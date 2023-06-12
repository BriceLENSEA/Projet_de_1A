#!/usr/bin/env python

from transfo.srv import ∗
import math
import rospy

def transfoXYZtheta(theta1, theta2, theta3, x, y, z):
  x = x - math.cos(theta1) * L1o
  y = y - math.sin(theta1) * L1o
  z = z - Zo - L2

  theta1 = math.atan2(y, x)

  L1 = math.sqrt(x2 + y2) - Lo

  L7 = math.sqrt(L12 + z2)

  a = z / L7
  b = (L72 + Al2 - Au2) / (2 * L7 * Al)
  c = (Al2 + Au2 - L72) / (2 * Al * Au)

  theta2 = (math.atan2(a, math.sqrt(1 - a2)) + math.atan2(math.sqrt(1 - b2), b))
  theta3 = math.atan2(math.sqrt(1 - c*2), c)

  theta1 = theta1 180 / math.pi
  theta2 = (theta2 - ELBOWOFFSET) * 180 / math.pi
  theta3 = (theta3 - ELBOWOFFSET) * 180 / math.pi

  angle1 = theta1 * K
  angle2 = (theta2 + theta3) * K
  angle3 = theta3 * K
  return transfoResponse(angle1, angle2, angle3)

def transfo_server():
  rospy.init_node(’transfo_server’)
  s = rospy.Service(’transfo’, Transfo, transfoXYZtheta)
  print "Ready to transform."
  rospy.spin()

if __name__ == "__main__":
  transfo_server()
