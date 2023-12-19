def read_file(path):
    file = open(path,"r")
    lines = file.read()
    file.close()
    return lines

def modify_raw(string:str):
    mod_input = string.strip().split('\n')
    return mod_input


def transpose(matrix:list) -> list:
    new_matrix = {}
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_matrix.setdefault(i,[])
            new_matrix[i].append(matrix[j][i])

    return list(new_matrix.values())


#matrix helper functions

class matrix():
    def __init__(self,matrix_list:list,empty_x=0,empty_y=0):
        if (matrix_list==None):
            self.matrix = []
            for i in range(empty_x):
                leaf = []
                for j in range(empty_y):
                    leaf.append(['.'])
                self.matrix.append(leaf)
        else:
            self.matrix = [list(x) for x in matrix_list]
        self.init_dim()
        self.init_directions()

    
    #constant stuff:
    
    def init_directions(self)->list:
        self.directions = {'core':{'N':[1,0],'E':[0,1],'W':[0,-1],'S':[-1,0]},'expaned':{'SW':[-1,-1],'SE':[-1,1],'NE':[1,1],'NW':[1,-1]}}


    def init_dim(self)->list:
        self.dimension = [len(self.matrix[0]),len(self.matrix)]
        return self.dimension

    def get_cell(self,x,y)->str:
        return self.matrix[int(y)][int(x)]
    
    def set_cell(self,x,y,value)->None:
        self.matrix[int(y)][int(x)] = str(value)

    def clamp(self,x,y)->bool:
        if (x<=self.dimension[0]-1) and (x>=0):
            if (y<=self.dimension[1]-1) and (y>=0):
                return True
        else:
            return False

    def neighbor_from_coord(self,x,y,diagonal=False)->list:
        #finds the neighbors of a cell including diagonal
        #add dir? can return n[1,0]
        #or maybe that should be a separete method where you save DIR.NORTH = [1,0] as a singleton
        coords = []
        checks = self.directions['core'].values()
        if diagonal:
            checks+= self.directions['expanded'].values()

        for coor in checks:
            neigh_x = x+coor[0]
            neigh_y = y+coor[1]
            if self.clamp(neigh_x,neigh_y):
                coords.append([neigh_x,neigh_y])
        return coords

    def get_neighbor_content(self,x,y,diagonal = False)->list:
        neighbor_dic = []
        for i in self.neighbor_from_coord(x,y,diagonal):
            neighbor_dic.append({'coord':(i[0],i[1]),'content':self.get_cell(*i)})
        return neighbor_dic

    
    def find(self,value)->list:
        found_coords = []
        for i in range(self.dimension[0]):
            for j in range(self.dimension[1]):
                if str(self.get_cell(i,j)) == str(value):
                    found_coords.append([i,j])
        return found_coords