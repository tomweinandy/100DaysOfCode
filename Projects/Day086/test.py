import blocks
import turtle

screen = turtle.Screen()

# blocks.Block(100, 100, 'red')
# blocks.Block(200, 200, 'orange')

row = blocks.Row()

row.build(-100, -100, 5, 50, 'green')

screen.exitonclick()

