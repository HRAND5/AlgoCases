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


def reverse_moves(moves_list):
    for i, m in enumerate(moves_list):
        if m.endswith("p"):
            moves_list[i] = m[:-1]
        elif not m.endswith("2"):
            moves_list[i] = m + "p"
    moves_list.reverse()

    return moves_list


def parse_moves(moves_list):
    moves_list = rotate_moves(moves_list)
    moves_list = reverse_moves(moves_list)

    return moves_list

def pll_case(moves):
    cube = Cube()

    moves_list = parse_moves(moves.split(" "))
    

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

pll_case("Lp U Lp Up Lp Up Lp U L U L2")
