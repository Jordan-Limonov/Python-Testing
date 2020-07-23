from turtle import *

thing = Turtle()
coordinates = [[12,54],[34,67],[54,87],[12,65],[34,87],[34,65]]
for item in coordinates:
    thing.setposition(item[0], item[1])
# test = range(0, 100)
# for item in test:
#     print(item)
#     thing.setx(item)
#     thing.sety(item)
