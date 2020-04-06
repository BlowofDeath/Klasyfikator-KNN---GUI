import math
import sys
import numpy as np
from csv import reader

H = np.array([[1, -2, 12],[2, 0, 11],[1.5, 4, 16]])


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
           

def euclideanDistance(sample_one, sample_two):
    distance =0
    for i in range(len(sample_one)):
        distance+= pow(sample_one[i] - sample_two[i],2)
    return math.sqrt(distance)

def groupingDistanceForX(A, x):
    data = groupingDistance(A)
    groups = {}
    for j in range(len(data[0])):
        temp = []
        for i in data[0][j]:
            temp.append(euclideanDistance(i, x)) 
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
        
        

with open(sys.argv[1], 'r') as csv_data:
    csv_reader = reader(csv_data, delimiter='\t')

    A = np.array(list(csv_reader)).astype('float64')
  
    # Resoult=Knn(A,4, [2.5, 1.0, 4.0, 5.5])
    #oneVsRest(A,40)
    # print(Knn(A, 30, [2.5, 1.0, 4.0, 5.5]))
    A = normalization(A)
    if (sys.argv[2] == "1"):
        x = sys.argv[4].split(" ")
        x = [float(i) for i in x]
        k = int(sys.argv[3])
        print('\n')
        print("Knn = ",Knn(A, k, x))
        print("x = ", x)
        print("Dla k =", k)
        
        
    if (sys.argv[2] == "2"):
        print('\n Szukanie odpowiedniego k:')
        lookingForK(A)

    
    
    
    
    
   
    
    
    








