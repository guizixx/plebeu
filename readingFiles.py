# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60262 André Guo

from Candidates import Candidates

def readTitlesDict(titlesFileName):
    '''
    Reads titles file into a dictionary.

    Requires: 
    titlesFileName is the name of the titles file.
    
    Ensures:
    Returns a dictionary of titles.
    '''
    titlesList = []
    titlesDic = {}
    inFile = open(titlesFileName, 'r')
    for line in inFile:
        if line.startswith('#'): #skips line that star with '#'
            continue
        l = line.replace('\n' , '').split(';')
        titlesList.append(l)
    for i in range(len(titlesList)):
        titlesDic[titlesList[i][1]] = titlesList[i][0]
        titlesDic[titlesList[i][2]] = titlesList[i][0]
    inFile.close()
    return titlesDic
    

print(readTitlesDict('titles.txt'))


def readCandFile(inputFileName):
    '''
    Reads candidates file into a list.

    Requires:
    inputFileName is the name of the candidates file.
    
    Ensures:
    Returns a list of candidates.
    '''
    candList = []
    inFile = open(inputFileName, 'r')
    for line in inFile:
        if line.startswith('#'):
            continue
        l = line.replace('\n', '').split(';')
        candidate = Candidates(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
        candList.append(candidate)
    inFile.close()
    return candList



print(readCandFile('inputFile.txt'))