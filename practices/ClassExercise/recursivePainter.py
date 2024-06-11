import random

#first I randomly generate a ppm file
columns = '200' #input()
rows = '200' #input()
content = "P3 " + columns + ' ' + rows + ' ' + '255' + '\n'

color_diversity = '3' #input() #color diversity is here because I want some clusters to form
colors_list = []
for i in range(int(color_diversity)):
    colors_list.append(str(random.randint(0,255)) + ' ' + str(random.randint(0,255)) + ' ' +str(random.randint(0,255)))

for row in range(int(rows)):
    for column in range(int(columns)):    
        if column+1 == int(columns): 
            content = content + colors_list[random.randint(0, int(color_diversity)-1)]
        else:
            content = content + colors_list[random.randint(0, int(color_diversity)-1)] + ' '
    content = content + '\n' 

my_random_ppm_file = open('my_random_picture.ppm', 'w')
my_random_ppm_file.write(content)
my_random_ppm_file.close()
#random ppm file generated


ppm_file = open('my_random_picture.ppm', 'r')
ppm_file.readline()
rows_list = ppm_file.read().split('\n')
image = []
for row in range(int(rows)):
    current_pixels = rows_list[row].split()
    row = []
    for col in range(0, int(columns)*3, 3):
        rgbTuple = (current_pixels[col+0], current_pixels[col+1], current_pixels[col+2])
        row.append(rgbTuple)
    image.append(row)
ppm_file.close()
#3d image list done



def color_region(row, col, img, newColorTuple, oldColorTuple):
    if not (0<=row<int(rows) and 0<=col<int(columns)):
        return
    if is_colored[row][col]:
        return
    if img[row][col] != oldColorTuple:
        return
    img[row][col] = newColorTuple
    is_colored[row][col] = True

    color_region(row+1, col, img, newColorTuple, oldColorTuple)
    color_region(row-1, col, img, newColorTuple, oldColorTuple)
    color_region(row, col+1, img, newColorTuple, oldColorTuple)
    color_region(row, col-1, img, newColorTuple, oldColorTuple)    


def color(img):
    for row in range(int(rows)):
        for col in range(int(columns)):
            if not is_colored[row][col]:
                current_color = img[row][col]
                # while current_color == img[row][col]:
                #     current_color = colors_list[random.randint(0, int(color_diversity)-1)].split()
                #     current_color = (current_color[0], current_color[1], current_color[2])
                current_color = colors_list[random.randint(0, int(color_diversity)-1)].split()
                current_color = (current_color[0], current_color[1], current_color[2])                
                color_region(row, col, img, current_color, img[row][col])

is_colored = [[False for col in range(int(columns))] for row in range(int(rows))]

for i in range(10000):
    color(image)

#writing new ppm file
new_ppm_file = open('new_ppm_file.ppm', 'w')
newContent = "P3 " + columns + ' ' + rows + ' ' + '255' + '\n'
for row in range(int(rows)):
    for col in range(int(columns)):   
        currentPixel = ' '.join(image[row][col])
        if col+1 == int(columns): 
            newContent = newContent + currentPixel
        else:
            newContent = newContent + currentPixel + ' '
    newContent = newContent + '\n' 
new_ppm_file.write(newContent)
new_ppm_file.close()