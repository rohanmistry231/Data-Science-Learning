def read_data_as_int(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def read_data_as_float(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers