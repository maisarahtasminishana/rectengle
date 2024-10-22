import turtle  
turtle.Screen().bgcolor("pink")
ttl = turtle.Turtle()  
ttl.fillcolor("blue")
ttl.begin_fill()
for i in range(2):  
  ttl.forward(140) 
  ttl.left(90) 
  ttl.forward(70)
  ttl.left(90) 
ttl.end_fill()
turtle.done()




