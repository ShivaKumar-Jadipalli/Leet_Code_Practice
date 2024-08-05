class Checking:
    def __init__(self):
        self.valid = True
    def check_validity(self,game_cells,given=None):
        if given!=None:
            if len(given) != 9 : 
                self.valid = False
        else: 
            # checking row 
            for i in game_cells:
                self.check_validity(game_cells,set(i))
            for i in range(9):
                self.check_validity(game_cells,set([j[i] for j in game_cells]))
            for i in range(0,9,3):
                temp_1 = []
                temp_2 = []
                temp_3 = []
                for j in game_cells[i:i+3]:
                    temp_1.extend(j[:3])
                    temp_2.extend(j[3:6])
                    temp_3.extend(j[6:])
                self.check_validity(game_cells,temp_1)                      
                self.check_validity(game_cells,temp_2)                      
                self.check_validity(game_cells,temp_3)                      
            if self.valid:
                return True 
            return False 

test = "635741289782956341491832765178265934259473816346189572863524197924317658517698423"
game_cells = []
temp =[]
for i in test:
    temp.append(int(i))
    if len(temp) == 9:
        game_cells.append(temp)
        temp = []

if Checking().check_validity(game_cells):
    print('It is a valid cell')
else:
    print("Not working")