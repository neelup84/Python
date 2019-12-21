arrow_base_height = int(input('Enter arrow base height: \n'))
arrow_base_width = int(input('Enter arrow base width: \n'))
arrow_head_width = int(input('Enter arrow head width: '))

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width: \n'))
print("\n".rstrip("\n"))

for item in range (arrow_base_height):
    item = '*' * arrow_base_width
    print(item)
for element in range(arrow_head_width):
    element = '*' * arrow_head_width
    print (element)
    arrow_head_width -= 1
