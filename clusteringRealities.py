# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60262 André Guo

from Cluster import Cluster
from Candidates import Candidates
from kmeans import kmeans
from MkDist import minkowskiDist
import sys


def generateClustersFile(num_clusters, features_file, candidates_file):
    candidates = Candidates(candidates_file, features_file)
    candidates_list = candidates.candidatesList()
    print(candidates_list)
    titles_dict = candidates.titlesDictionary()
    print(titles_dict)
    clusters = kmeans(candidates_list, num_clusters, False)  # Apply k-means clustering

    output_file = "candidates.txt"

    with open(output_file, 'w') as f:
        for i, cluster in enumerate(clusters):
            exemplar = cluster.getCentroid()  # Get the exemplar (centroid) of the cluster
            f.write("#exemplar " + str(i+1) + ":\n")
            f.write(exemplar[0] + "; " + "; ".join(exemplar[1:]) + "\n")
            f.write("#cluster " + str(i+1) + ":\n")
            for candidate in cluster.getMembers():
                f.write(candidate[0] + "; " + "; ".join(titles_dict[title] for title in candidate[1:]) + "\n")
            f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 clusteringRealities.py k titles.txt inputFile.txt")
    else:
        k = int(sys.argv[1])
        titles_file = sys.argv[2]
        candidates_file = sys.argv[3]
        generateClustersFile(k, titles_file, candidates_file)

