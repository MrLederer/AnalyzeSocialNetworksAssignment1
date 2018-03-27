def getFriends (arr, someone):
    return arr[someone]
#O(friendList^2)
def getFriendsConnectionsDegree (matrix, friendList):
    counter=0
    for friend in friendList:
        for other in friendList:
            counter+=matrix[friend][other]
    return counter
def getClusteringCoefficientForNode (someone, arr, matrix, degree):
    if degree[someone] <= 1:
        return 0
    return float(getFriendsConnectionsDegree (matrix, (getFriends(arr,someone)))) /float((degree[someone] * (degree[someone] - 1)))
def getClusteringCoefficient (arr, matrix, degree, max):
    ClusteringCoefficients = [0.0] * max
    counterAll=0.0
    for node in range (max):
        ClusteringCoefficients[node]=getClusteringCoefficientForNode(node, arr, matrix, degree)
        counterAll+=ClusteringCoefficients[node]
    return counterAll/(max-1), ClusteringCoefficients