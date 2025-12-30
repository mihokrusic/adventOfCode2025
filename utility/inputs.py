def read(file_name):
    input = []
    with open("inputs/" + file_name, "r") as f:
        input = f.read().splitlines()
    return input

def read_str(file_name):
    with open("inputs/" + file_name, "r") as f:
        data = f.read()
    return data
