from generate_case import *
from simulate_cube import *

def rotate_moves(moves_list):
    for i, m in enumerate(moves_list):
        if "U" in m: 
            moves_list[i] = m.replace("U", "D")
        if "D" in m: 
            moves_list[i] = m.replace("D", "U")
        if "F" in m: 
            moves_list[i] = m.replace("F", "B")
        if "B" in m: 
            moves_list[i] = m.replace("B", "F")

    return moves_list

def pll_case(moves):
    cube = Cube()

    moves_list = rotate_moves(moves.split(" "))
    

    cube.algorithm(moves_list)

    draw_case(cube.get_face_case("y"))

def oll_case(moves):
    cube = Cube()

    moves_list = moves.split(" ")

    for i, m in enumerate(moves_list):
        if "U" in m: 
            moves_list[i] = m.replace("U", "D")
        if "D" in m: 
            moves_list[i] = m.replace("D", "U")

    cube.algorithm(moves_list)
    
    draw_case(cube.get_face_case("y", face_only=True))

pll_case("R U Rp Up Rp F R2 Up Rp Up R U Rp Fp")
