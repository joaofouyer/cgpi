import turtle


def dragonCurve(order, length):
  turn(order * 45)
  dragonCurveRecursive(order, length, 1)


def dragonCurveRecursive(order, length, sign):
  if order == 0:
    drawLine(length)
  else:
    rootHalf = (1 / 2) ** (1 / 2)
    dragonCurveRecursive(order - 1, length * rootHalf, 1)
    turn(sign * -90)
    dragonCurveRecursive(order - 1, length * rootHalf, -1)