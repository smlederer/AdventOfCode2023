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