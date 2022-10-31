import csv
from PIL import Image, ImageDraw
  
w, h = 1000, 1000



CELL_TO_COLOR = {
    "0": "#cccccc",
    "w": "#ffffff",
    "o": "#ffa500",
    "g": "#00ff00",
    "r": "#ff0000",
    "b": "#0000ff",
    "y": "#ffff00"
}


def import_case():
    with open("case.csv") as csv_file:
        case = []
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            case.append(row)

    if len(case) != 5:
        raise Exception("The given case does not have the right dimensions")
    else:
        correct_rows = 0
        for row in case:
            if len(row) == 5:
                correct_rows += 1
        
        if correct_rows != 5:
            raise Exception("The given case does not have the right dimensions")
    return case



def draw_face(i, j, cell, draw):
    # Top left corner of rectangle
    TLx = j*200
    TLy = i*200
    shape = [(TLx, TLy), (TLx + 200, TLy + 200)]
    draw.rectangle(shape, fill=CELL_TO_COLOR.get(cell, "#FFFFFF"), outline="#000000", width=4) 


def draw_side(i, j, cell, draw):
    if cell != "0": 
        if i == -1: # Top
            TLx = 200 + j*200 + 10
            TLy = 200 + i*200 + 155
            shape = [(TLx,TLy), (TLx + 180, TLy + 30)]
            draw.rectangle(shape, fill=CELL_TO_COLOR.get(cell), outline="#000000", width=2)
        elif i == 3: # Bottom
            TLx = 200 + j*200 + 10
            TLy = 200 + i*200 + 15
            shape = [(TLx,TLy), (TLx + 180, TLy + 30)]
            draw.rectangle(shape, fill=CELL_TO_COLOR.get(cell), outline="#000000", width=2)
        elif j == -1: # Left
            TLx = 200 + j*200 + 155
            TLy = 200 + i*200 + 10
            shape = [(TLx,TLy), (TLx + 30, TLy + 180)]
            draw.rectangle(shape, fill=CELL_TO_COLOR.get(cell), outline="#000000", width=2)
        elif j == 3: # Right
            TLx = 200 + j*200 + 15
            TLy = 200 + i*200 + 10
            shape = [(TLx,TLy), (TLx + 30, TLy + 180)]
            draw.rectangle(shape, fill=CELL_TO_COLOR.get(cell), outline="#000000", width=2)



def draw_case(case):
    # creating new Image object
    img = Image.new("RGB", (w, h), color="#FFFFFF")
    
    # create rectangle image
    draw = ImageDraw.Draw(img)  

    # Bounding box so all lines have the same thickness
    draw.rectangle([(198, 198), (802,802)], outline="#000000", width=4)
    for i, row in enumerate(case):
        for j, cell in enumerate(row):
            if j in [0, 4] or i in [0, 4]:
                draw_side(i-1, j-1, cell, draw)
            else:
                draw_face(i, j, cell, draw)

    img.show()
