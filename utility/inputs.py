def read(file_name):
    input = []
    with open("inputs/" + file_name, "r") as f:
        input = [line.rstrip('\n') for line in f.readlines() if line.strip()]
    return input

def read_str(file_name):
    with open("inputs/" + file_name, "r") as f:
        data = f.read()
    return data
