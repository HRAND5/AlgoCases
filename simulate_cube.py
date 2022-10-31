import ujson 


COLORS = ["w", "o", "g", "r", "b", "y"]


with open("./moves.json") as f:
    MOVES_DICT = ujson.load(f)

VALID_MOVES = list(MOVES_DICT.keys())

for m in VALID_MOVES.copy():
    VALID_MOVES.append(f"{m}p")
    VALID_MOVES.append(f"{m}2")

def raw_move(cubestate, move, raw_moves): 
    if len(cubestate) != 48:
        raise Exception("The given cubestate has the wrong length, please check you are passing the correct state.")

    outstate = cubestate.copy()

    for x,y in raw_moves:
        outstate[x-1] = cubestate[y-1]
    
    return outstate


class Cube:
    def __init__(self):
        self.state = []
        for c in COLORS:
            for i in range(8):
                self.state.append(c)

    def move(self, move):
        if move not in VALID_MOVES:
            raise Exception("Unvalid move, please check you are passing the correct move.")

        if len(move) == 1:
            self.state = raw_move(self.state, move, MOVES_DICT.get(move, []))
        elif move.endswith("2"):
            self.state = raw_move(raw_move(self.state, move, MOVES_DICT.get(move[:-1], [])), move, MOVES_DICT.get(move[:-1], []))
        elif move.endswith("p"):
            new_moves = MOVES_DICT.get(move[:-1], [])
            for i, m in enumerate(new_moves):
                new_moves[i].reverse()
            
            self.state = raw_move(self.state, move[:-1], new_moves)
        
        return self.state

