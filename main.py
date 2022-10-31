"""
Hver opmærksom på at de moves der laves er i forhold til orientationen. Derfor skal de enten konverteres til at være når gul er opad, eller de bare laves med hvid opad og farveren konverteres derefter. Det er nok nemmest at konverterer moves først, men idfk. 

"""




from generate_case import *
from simulate_cube import *

def oll_case(moves):
    cube = Cube()

    moves_list = moves.split(" ")

    for m in moves_list:
        cube.move(move)


cube = Cube()

cube.move("R")
