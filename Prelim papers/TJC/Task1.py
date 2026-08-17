#Task 1.1
def task1_1(artefacts_list):
    with open(artefacts_list , 'r') as file:
        for line in file:
            line = line.split(',')
            print(line)
        
task1_1('Artefacts.txt')