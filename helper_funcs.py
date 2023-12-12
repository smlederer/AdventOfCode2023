def read_file(path):
    file = open(path,"r")
    lines = file.read()
    file.close()
    return lines

def modify_raw(string:str):
    mod_input = string.strip().split('\n')
    return mod_input
