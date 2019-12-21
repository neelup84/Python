import math

# Dictionary of paint colors and cost per gallon
paintColors={'red':35,'blue':25,'green':23}
wallHeight = int(input('Enter wall height (feet): \n'))
#print(wallHeight)
wallWidth = int(input('Enter wall width (feet): \n'))
#print(wallWidth)
wallArea=wallWidth*wallHeight
print('Wall area:',float(wallArea),'square feet')
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
print('Paint needed:',wallArea/350,'gallons')
# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
print('Cans needed:',math.ceil(wallArea/350),'can(s)\n')
# FIXME (4): Calculate and output the total cost of paint can needed depending on color
Color = str(input('Choose a color to paint the wall: \n'))
#print(Color)
print('Cost of purchasing',Color,'paint:$',str(paintColors.get(Color,0))*math.ceil(wallArea/350))
