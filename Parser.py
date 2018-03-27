
import csv

def read_file(path):
    max = 0
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for number in row:
                if int(max) < int(number):
                    max = int(number)
    max = max + 1
    arr = []
    lengths = [0] * max
    for i in range (max):
        arr.append(list())

    matrix = [[0 for x in range(max)] for y in range(max)]
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            row[0] = int(row[0])
            row[1] = int(row[1])
            arr[row[0]].append(row[1])
            lengths[row[0]]+=1
            arr[row[1]].append(row[0])
            lengths[row[1]]+=1
            matrix[row[0]][row[1]] = 1
            matrix[row[1]][row[0]] = 1

    return matrix,arr, max, lengths