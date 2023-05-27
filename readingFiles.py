# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60262 André Guo

def readTitlesDict(file_name):
    '''
    Reads titles file into a dictionary.

    Requires: 
    file_name is the name of the titles file.
    
    Ensures:
    Returns a dictionary of titles.
    '''
    titlesList = []
    titlesDic = {}
    line_count = 0 #counter variable to keep track of the lines
    inFile = open(file_name, 'r')
    for line in inFile:
        line_count += 1
        if line_count <= 1: #skips first line
            continue
        l = line.replace('\n' , '').split(';')
        titlesList.append(l)
    for i in range(len(titlesList)):
        titlesDic[titlesList[i][1]] = titlesList[i][0]
        titlesDic[titlesList[i][2]] = titlesList[i][0]
    return titlesDic
    

print(readTitlesDict('titles.txt'))


def readCandFile(file_name):
    '''
    Reads candidates file into a list.

    Requires:
    file_name is the name of the candidates file.
    
    Ensures:
    Returns a list of candidates.
    '''
    candList = []
    line_count = 0 #counter variable to keep track of the lines
    inFile = open(file_name, 'r')
    for line in inFile:
        line_count += 1
        if line_count <= 4: #skip first 4 lines
            continue
        l = line.replace('\n', '').split(';')
        candList.append(l)
    inFile.close()
    return candList


print(readCandFile('inputFile.txt'))