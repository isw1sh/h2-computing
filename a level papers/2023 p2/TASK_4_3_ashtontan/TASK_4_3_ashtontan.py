def read_decompressed(filename):
    with open(filename , 'r') as file:
        codes = []
        for line in file:
            line = line.strip()
            codes.append(line)

    return codes

def buildGrid(codes):
    grid = []
    for row in range(9):
        rowcodes = []
        for col in range(9):
            rowcodes.append(codes[row * 9 + col])
        grid.append(rowcodes)
    return grid

