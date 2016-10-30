from graphics import *

# window
window = GraphWin("Graphical visualisation", 1200, 700)

#color background
background = Rectangle(Point(0,0),Point(1200,700))
background.setFill(color_rgb(58,48,91))
background.draw(window)

#setting line and circle lable
line = Line(Point(700,630),Point(1100,630))
line.setOutline(color_rgb(255,255,255))
line.setWidth(1)
line.draw(window)

circle = Circle(Point(1110,630), 10)
circle.setOutline(color_rgb(255,255,255))
circle.setWidth(1)
circle.draw(window)

#setting grade number
text = Text(Point(1080,610),'44')
text.setFace('helvetica')
text.setSize(12)
text.setTextColor(color_rgb(255,255,255))
text.draw(window)


#setting line and circle lable
line2 = Line(Point(100,510),Point(500,510))
line2.setOutline(color_rgb(255,255,255))
line2.setWidth(1)
line2.draw(window)

circle2 = Circle(Point(90,510), 10)
circle2.setOutline(color_rgb(255,255,255))
circle2.setWidth(1)
circle2.draw(window)

#setting grade number
text2 = Text(Point(120,490),'52')
text2.setFace('helvetica')
text2.setSize(12)
text2.setTextColor(color_rgb(255,255,255))
text2.draw(window)


#setting line and circle lable
line3 = Line(Point(700,405),Point(1100,405))
line3.setOutline(color_rgb(255,255,255))
line3.setWidth(1)
line3.draw(window)

circle3 = Circle(Point(1110,405), 10)
circle3.setOutline(color_rgb(255,255,255))
circle3.setWidth(1)
circle3.draw(window)

#setting grade number
text3 = Text(Point(1080,385),'59')
text3.setFace('helvetica')
text3.setSize(12)
text3.setTextColor(color_rgb(255,255,255))
text3.draw(window)


#setting line and circle lable
line4 = Line(Point(100,210),Point(500,210))
line4.setOutline(color_rgb(255,255,255))
line4.setWidth(1)
line4.draw(window)

circle4 = Circle(Point(90,210), 10)
circle4.setOutline(color_rgb(255,255,255))
circle4.setWidth(1)
circle4.draw(window)

#setting grade number
text4 = Text(Point(120,190),'72')
text4.setFace('helvetica')
text4.setSize(12)
text4.setTextColor(color_rgb(255,255,255))
text4.draw(window)

#setting line and circle lable
line5 = Line(Point(700,90),Point(1100,90))
line5.setOutline(color_rgb(255,255,255))
line5.setWidth(1)
line5.draw(window)

circle5 = Circle(Point(1110,90), 10)
circle5.setOutline(color_rgb(255,255,255))
circle5.setWidth(1)
circle5.draw(window)

#setting grade number
text5 = Text(Point(1080,70),'80')
text5.setFace('helvetica')
text5.setSize(12)
text5.setTextColor(color_rgb(255,255,255))
text5.draw(window)








#1 animating mountaintops up high

mid = 105
height = 690
base_middle = Point(105,690)
left_slope = Point(0,690)
right_slope = Point(210,690)

yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(254,255,164))
    polygon.setOutline(color_rgb(254,255,164))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(254,245,154))
    polygon.setOutline(color_rgb(254,245,154))
    polygon.draw(window)
    if (height < 510):
        break

        
#2 animating mountaintops up high

mid = 105
height = 690
base_middle = Point(105,690)
left_slope = Point(70,690)
right_slope = Point(140,690)

yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(82,139,150))
    polygon.setOutline(color_rgb(82,139,150))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(82,129,140))
    polygon.setOutline(color_rgb(82,129,140))
    polygon.draw(window)
    if (height < 585):
        break

#3 animating mountaintops up high

mid = 245
height = 690
base_middle = Point(245,690)
left_slope = Point(140,690)
right_slope = Point(350,690)

yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(246,141,99))
    polygon.setOutline(color_rgb(246,141,99))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(246,131,89))
    polygon.setOutline(color_rgb(246,131,89))
    polygon.draw(window)
    if (height < 435):
        break   

#4 animating mountaintops up high

mid = 280
height = 690
base_middle = Point(280,690)
left_slope = Point(210,690)
right_slope = Point(350,690)

yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(128,161,148))
    polygon.setOutline(color_rgb(128,161,148))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(128,151,138))
    polygon.setOutline(color_rgb(128,151,138))
    polygon.draw(window)
    if (height < 555):
        break      
    
#5 animating mountaintops up high

mid = 455
height = 690
base_middle = Point(455,690)
left_slope = Point(280,690)
right_slope = Point(630,690)

yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,241,100))
    polygon.setOutline(color_rgb(255,241,100))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,231,90))
    polygon.setOutline(color_rgb(255,231,90))
    polygon.draw(window)
    if (height < 405):
        break  

#6 animating mountaintops up high

mid = 385
height = 690
base_middle = Point(385,690)
left_slope = Point(350,690)
right_slope = Point(420,690)


yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(241,97,98))
    polygon.setOutline(color_rgb(241,97,98))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(241,87,88))
    polygon.setOutline(color_rgb(241,87,88))
    polygon.draw(window)
    if (height < 360):
        break  
    
    
#7 animating mountaintops up high

mid = 455
height = 690
base_middle = Point(455,690)
left_slope = Point(420,690)
right_slope = Point(490,690)

yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(62,87,116))
    polygon.setOutline(color_rgb(62,87,116))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(62,77,106))
    polygon.setOutline(color_rgb(62,77,106))
    polygon.draw(window)
    if (height < 630):
        break      
    
    
#8 animating mountaintops up high

mid = 525
height = 690
base_middle = Point(525,690)
left_slope = Point(490,690)
right_slope = Point(560,690)

yspeed = 15

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(166,121,99))
    polygon.setOutline(color_rgb(166,121,99))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(166,111,89))
    polygon.setOutline(color_rgb(166,111,89))
    polygon.draw(window)
    if (height < 150):
        break     
    
    
#9 animating mountaintops up high

mid = 595
height = 690
base_middle = Point(595,690)
left_slope = Point(560,690)
right_slope = Point(630,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(152,52,93))
    polygon.setOutline(color_rgb(152,52,93))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(152,42,83))
    polygon.setOutline(color_rgb(152,42,83))
    polygon.draw(window)
    if (height < 105):
        break     
    
#10 animating mountaintops up high

mid = 665
height = 690
base_middle = Point(665,690)
left_slope = Point(630,690)
right_slope = Point(700,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(59,52,97))
    polygon.setOutline(color_rgb(59,52,97))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(59,42,87))
    polygon.setOutline(color_rgb(59,42,87))
    polygon.draw(window)
    if (height < 660):
        break      
    
    
#11 animating mountaintops up high

mid = 735
height = 690
base_middle = Point(735,690)
left_slope = Point(700,690)
right_slope = Point(770,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(97,150,149))
    polygon.setOutline(color_rgb(97,150,149))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(97,140,139))
    polygon.setOutline(color_rgb(97,140,139))
    polygon.draw(window)
    if (height < 570):
        break      
    
    
#12 animating mountaintops up high

mid = 805
height = 690
base_middle = Point(805,690)
left_slope = Point(770,690)
right_slope = Point(840,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,63,91))
    polygon.setOutline(color_rgb(255,63,91))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,53,81))
    polygon.setOutline(color_rgb(255,53,81))
    polygon.draw(window)
    if (height < 90):
        break     
    
    
#13 animating mountaintops up high

mid = 875
height = 690
base_middle = Point(875,690)
left_slope = Point(840,690)
right_slope = Point(910,690)


yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(60,77,107))
    polygon.setOutline(color_rgb(60,77,107))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(60,67,97))
    polygon.setOutline(color_rgb(60,67,97))
    polygon.draw(window)
    if (height < 645):
        break     

        
#14 animating mountaintops up high

mid = 945
height = 690
base_middle = Point(945,690)
left_slope = Point(910,690)
right_slope = Point(980,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(208,65,92))
    polygon.setOutline(color_rgb(208,65,92))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(208,55,82))
    polygon.setOutline(color_rgb(208,55,82))
    polygon.draw(window)
    if (height < 210):
        break         
        
        
#15 animating mountaintops up high

mid = 1015
height = 690
base_middle = Point(1015,690)
left_slope = Point(980,690)
right_slope = Point(1050,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,95,91))
    polygon.setOutline(color_rgb(255,95,91))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,85,81))
    polygon.setOutline(color_rgb(255,85,81))
    polygon.draw(window)
    if (height < 180):
        break  
        
        
#16 animating mountaintops up high

mid = 1120
height = 690
base_middle = Point(1120,690)
left_slope = Point(1050,690)
right_slope = Point(1190,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(172,188,127))
    polygon.setOutline(color_rgb(172,188,127))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(172,178,117))
    polygon.setOutline(color_rgb(172,178,117))
    polygon.draw(window)
    if (height < 480):
        break          

        
#17 animating mountaintops up high

mid = 1155
height = 690
base_middle = Point(1155,690)
left_slope = Point(1120,690)
right_slope = Point(1190,690)

yspeed = 30

while True:
    height = height - 1
    peak = Point(mid,height)
    polygon = Polygon(left_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,195,99))
    polygon.setOutline(color_rgb(255,195,99))
    polygon.draw(window)
    
    polygon = Polygon(right_slope,peak,base_middle)
    polygon.setFill(color_rgb(255,185,89))
    polygon.setOutline(color_rgb(255,185,89))
    polygon.draw(window)
    if (height < 465):
        break         


        
        
#figure climbing on the hill                                     
xcenter = 350
ycenter = 690                                   
                                     
while True:  
    xcenter = xcenter - 1 
    ycenter = ycenter - 1 
    center = Point(xcenter,ycenter)                                     
    figure = Image(center, "climbing.gif")
    figure.draw(window)
    if(xcenter < 245): 
        break
        
x2center = 630
y2center = 690                                    
                                     
while True:  
    x2center = x2center - 1 
    y2center = y2center - 1 
    center2 = Point(x2center,y2center)                                     
    figure2 = Image(center2, "climbing.gif")
    figure2.draw(window)
    if(x2center < 595): 
        break        
       
x3center = 1190
y3center = 690                                 
                                     
while True:
    x3center = x3center - 1 
    y3center = y3center - 1 
    center3 = Point(x3center,y3center)                                     
    figure3 = Image(center3, "climbing.gif")
    figure3.draw(window)
    if(x3center < 1120): 
        break        
        


        
  
#motivation text
typografie = Image(Point(70,90), "typografie2.gif")
typografie.draw(window)
   

window.getMouse()
