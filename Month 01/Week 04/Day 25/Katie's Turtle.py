from turtle import Turtle, Screen

francis = Turtle()
screen = Screen()

turtle_shape = ((0, 16), (-2, 14), (-1, 10), (-4, 7),
(-7, 9), (-9, 8), (-6, 5), (-7, 1), (-5, -3), (-8, -6),
(-6, -8), (-4, -5), (0, -7), (4, -5), (6, -8), (8, -6),
(5, -3), (7, 1), (6, 5), (9, 8), (7, 9), (4, 7), (1, 10),
(2, 14), (0, 16))

big_turtle = ()



def turtle_size(amount):
    li = []
    for a, b in turtle_shape:
        num_1 = a * amount
        num_2 = b * amount
        if a == 0:
            num_1 += amount
        if b == 0:
            num_2 += amount
        print(a, b, num_1, num_2)


turtle_size(10)

print(big_turtle)


# for index, tuple in enumerate(list_of_tuples):
#
# 	element_one = tuple[0]
#
# 	element_two = tuple[1]
#
# 	print(element_one, element_two)


# francis.shape('turtle')
# francis.color('darkred')
# francis.turtlesize(stretch_wid=5, stretch_len=5)
# screen.bgcolor('light blue')
francis.ht()
francis.pu()
francis.goto(0, 16)
francis.pd()

for x in turtle_shape:
    francis.goto(x)


screen.exitonclick()

"""
"arrow" : Shape("polygon", ((-10,0), (10,0), (0,10))),
                  "turtle" : Shape("polygon", ((0,16), (-2,14), (-1,10), (-4,7),
                              (-7,9), (-9,8), (-6,5), (-7,1), (-5,-3), (-8,-6),
                              (-6,-8), (-4,-5), (0,-7), (4,-5), (6,-8), (8,-6),
                              (5,-3), (7,1), (6,5), (9,8), (7,9), (4,7), (1,10),
                              (2,14))),
                  "circle" : Shape("polygon", ((10,0), (9.51,3.09), (8.09,5.88),
                              (5.88,8.09), (3.09,9.51), (0,10), (-3.09,9.51),
                              (-5.88,8.09), (-8.09,5.88), (-9.51,3.09), (-10,0),
                              (-9.51,-3.09), (-8.09,-5.88), (-5.88,-8.09),
                              (-3.09,-9.51), (-0.00,-10.00), (3.09,-9.51),
                              (5.88,-8.09), (8.09,-5.88), (9.51,-3.09))),
                  "square" : Shape("polygon", ((10,-10), (10,10), (-10,10),
                              (-10,-10))),
                "triangle" : Shape("polygon", ((10,-5.77), (0,11.55),
                              (-10,-5.77))),
                  "classic": Shape("polygon", ((0,0),(-5,-9),(0,-7),(5,-9))),
                   "blank" : Shape("image", self._blankimage())     """
