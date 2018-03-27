import os

import sys

from Logic import getClusteringCoefficient
from Parser import read_file

matrix,arr, max, lengths = read_file(os.getcwd() + "/" + sys.argv[1])
AverageClusteringCoefficients , ClusteringCoefficients = getClusteringCoefficient(arr,matrix,lengths,max)
print AverageClusteringCoefficients
print ClusteringCoefficients

def load_graph(path):
    global matrix,arr, max, lengths
    matrix,arr, max, lengths = read_file(path)

def calculate_clustering_coefficients():
    global AverageClusteringCoefficients , ClusteringCoefficients
    AverageClusteringCoefficients , ClusteringCoefficients = getClusteringCoefficient(arr,matrix,lengths,max)

def get_average_clustering_coefficient():
    return AverageClusteringCoefficients

def clustering_coefficient(node):
    if 0<node and node<max:
        return ClusteringCoefficients[node]
    return -1

def get_all_clustering_coefficients():
    result = [[0, 0.0]]*max-1
    for node in range (max-1):
        result[node][0]=node+1
        result[node][1]=ClusteringCoefficients[node+1]
    return result