from turtle import Screen, Turtle, color
import random

s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Make your bet",
                  prompt="Which turtle is going to win enter a color:L ")
colors = ["red", "orange", "yellow", "purple", "green", "blue"]
y_postions = [-120, -60, 0, 60, 120, 180]
turtles = []

for turtle_index in range(6):
    t = Turtle(shape="turtle")
    t.pu()
    t.color(colors[turtle_index])
    t.goto(x=-230, y=y_postions[turtle_index])
    turtles.append(t)

race_on = False

if bet:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 230:
            winner_color = t.pencolor()
            if winner_color == bet:
                print("You won")
            else:
                print(f"You loose the winner was {winner_color}.")
            race_on = False
        steps = random.randint(0, 10)
        t.forward(steps)

s.exitonclick()
