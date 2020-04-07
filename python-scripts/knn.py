import math
import sys
import numpy as np
from csv import reader
import metrics
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('--datafilepath', '-d', help='Path to data')
parser.add_argument('--scriptnumber','-s', default=1,help='What script start')
parser.add_argument('--k','-k', default=3, help='for what count of neightbours run algorithm ')
parser.add_argument('--x','-x', help='sample data to classification')
parser.add_argument('--metric','-m', default="euclidean",help='What metric to choose')
parser.add_argument('--p','-p', default=1,help='Paremtr only for minkowski metric')

args=parser.parse_args()
#print(args)
H = np.array([[1, -2, 12],[2, 0, 11],[1.5, 4, 16]])

metrics_dict = {
    "euclidean": metrics.euclideanDistance,
    "manhattan": metrics.manhattanDistance,
    "chessboard": metrics.chessboardDdistance,
    "log": metrics.logDistance,
    "minkowski": metrics.minkowskiDistance,
}



def normalization(A):
    for j in range(A[0].size-1):
        minimum = np.min(A[:,j])
        maximum = np.max(A[:,j])
        temp = []
        for i in A[:,j]:
            resoult = (i - minimum)/(maximum - minimum)
            temp.append(resoult)
        A[:,j] = temp
    return A
        
def groupingDistance(A):
    temp = []
    decisions = np.unique(A[:,A[1].size-1])
    for i in decisions:
        helper = A[i==A[:,A[1].size-1]]
        temp.append(helper[:,:helper[1].size-1])
    # print(temp)
    
    return [temp, decisions]
           

def metric(sample_one, sample_two):
    if (args.metric == "minkowski"):
        return metrics_dict[args.metric](sample_one,sample_two, int(args.p))
    else:
        return metrics_dict[args.metric](sample_one,sample_two)

def groupingDistanceForX(A, x):
    data = groupingDistance(A)
    groups = {}
    for j in range(len(data[0])):
        temp = []
        for i in data[0][j]:
            temp.append(metric(i, x)) 
        groups.update({data[1][j]: temp})
    return groups
def Knn(A, k, x):
    A = groupingDistanceForX(A, x)
    groups = {}
    for j in A:
        summary=0
        temp = np.sort(A[j])
        #print("J["+str(j)+"]")
        #print(temp)
        for i in range(k):
            # print("j: " + str(temp[i]))
            summary+=temp[i]
        groups.update({j: summary})
    #print(min(groups, key=groups.get))
    return min(groups, key=groups.get)

def oneVsRest(A, k):
    
    correct = 0
    for i in range((A.shape[0])):
        temp = A[i]
        T = np.delete(A, i-1, 0)
        resoult = Knn(T,k,temp[:temp.size-1])

        if(resoult == temp[temp.size-1]):
            correct+=1
    print("All = "+str(A.shape[0])+": Correct = "+str(correct))
    accuracy = (100/A.shape[0]) * correct
    print("Accuracy = " +str(accuracy)+"%")
    return accuracy
        
def lookingForK(A):
    decisions = np.unique(A[:,A[1].size-1])
    temp = []
    for i in decisions:
        temp.append(A[i==A[:,A[1].size-1]].shape[0])
    minimum = min(temp)
    
    resoults = {}
    for i in range(3,minimum):
        resoults.update({i: oneVsRest(A, i)})
        print("For k = ", i)
    maximum = max(resoults.values())
    
    print("Largest accuracy: ",maximum)
    tab = []
    for index, value in resoults.items():
        if value == maximum:
            tab.append(index)
    print("List of k with largest accuracy: ",tab)
    return tab
        
        

with open(args.datafilepath, 'r') as csv_data:
    csv_reader = reader(csv_data, delimiter='\t')

    A = np.array(list(csv_reader)).astype('float64')
  
    # Resoult=Knn(A,4, [2.5, 1.0, 4.0, 5.5])
    #oneVsRest(A,40)
    # print(Knn(A, 30, [2.5, 1.0, 4.0, 5.5]))
    A = normalization(A)
    if (args.scriptnumber == "1"):
        x = args.x.split(" ")
        x = [float(i) for i in x]
        if(len(x) != A.shape[1] - 1):
            raise ValueError('Probe length different then data')
        k = int(args.k)
        print('\n')
        print("Knn = ",Knn(A, k, x))
        print("x = ", x)
        print("Dla k =", k)
        
        
    if (args.scriptnumber == "2"):
        print('\n Szukanie odpowiedniego k:')
        lookingForK(A)

    
    
    
    
    
   
    
    
    








