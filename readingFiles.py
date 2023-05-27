# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60262 André Guo

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
        if line.startswith: #skip lines that start with '#'
            continue
        l = line.replace('\n', '').split(';')
        candList.append(l)
    inFile.close()
    return candList


print(readCandFile('inputFile.txt'))