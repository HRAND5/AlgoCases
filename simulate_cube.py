import ujson 


COLORS = ["w", "o", "g", "r", "b", "y"]

FACES = {
    "w": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 18, 19, 25, 26, 27, 33, 34, 35],
    "o": [9, 10, 11, 12, 13, 14, 15, 16, 35, 36, 37, 47, 48, 41, 23, 24, 17, 7, 8, 1],
    "g": [17, 18, 19, 20, 21, 22, 23, 24, 11, 12, 13, 41, 42, 43, 31, 32, 25, 5, 6, 7],
    "r": [25, 26, 27, 28, 29, 30, 31, 32, 19, 20, 21, 43, 44, 45, 39, 40, 33, 3, 4, 5],
    "b": [37, 38, 39, 40, 33, 34, 35, 36, 15, 16, 9, 1, 2, 3, 27, 28, 29, 45, 46, 47],
    "y": [41, 42, 43, 44, 45, 46, 47, 48, 13, 14, 15, 37, 38, 39, 29, 30, 31, 21, 22, 23]
}


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
            
            new_moves = [mv[:] for mv in MOVES_DICT.get(move[:-1], [])]
            for i, m in enumerate(new_moves):
                new_moves[i].reverse()
            self.state = raw_move(self.state, move[:-1], new_moves)
        return self.state

    def get_face_case(self, face, face_only=False):
        f = FACES[face]
        s = self.state
        case = [
            ["0"         , s[f[19] - 1], s[f[18] - 1], s[f[17] - 1], "0"         ],
            [s[f[8] - 1] , s[f[0] - 1] , s[f[1] - 1] , s[f[2] - 1] , s[f[16] - 1]],
            [s[f[9] - 1] , s[f[7] - 1] , face        , s[f[3] - 1] , s[f[15] - 1]],
            [s[f[10] - 1], s[f[6] - 1] , s[f[5] - 1] , s[f[4] - 1] , s[f[14] - 1]],
            ["0"         , s[f[11] - 1], s[f[12] - 1], s[f[13] - 1], "0"         ]
        ]
        
        if face_only:
            for i, row in enumerate(case): 
                for j, cell in  enumerate(row):
                    if cell != face:
                        case[i][j] = "0"
        
        return case
    
    def algorithm(self, moves):
        for m in moves:
            self.move(m)


    

