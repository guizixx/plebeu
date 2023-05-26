# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60 André Guo

import random
import Cluster

def kmeans(examples, k, verbose):
    """
    K-means clustering
    
    Requires:
    examples a list of examples of a same type;
    k positive int, number of clusters;
    verbose Boolean, printing details on/off
    Ensures:
    list containing k clusters;
    if verbose is True, result of each iteration
    of k-means is printed
    """
    #Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(examples, k)
    
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))

    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        
        numIterations += 1

        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])

        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for the appropriate cluster
            newClusters[index].append(e)

        #Avoid having empty clusters
        for c in newClusters:
            if len(c) == 0:
                raise ValueError("Empty Cluster")

        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False

        #Trace intermediate levels of clustering if verbose on
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
            
    return clusters