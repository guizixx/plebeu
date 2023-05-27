# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60262 André Guo

from Cluster import Cluster
from Candidates import Candidates
from kmeans import kmeans
from MkDist import minkowskiDist
import sys





if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 clusteringRealities.py k titles.txt inputFile.txt")
        sys.exit(1)
    k = int(sys.argv[1])
    titles_file = sys.argv[2]
    input_file = sys.argv[3]

    clusteringRealities(k, titles_file, input_file)
