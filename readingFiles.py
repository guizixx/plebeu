# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60 André Guo

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
    inFile = open(file_name, 'r')
    for line in inFile:
        l = line.replace('\n' , '').split(';')
        titlesList.append(l)
    titlesList.pop(0)
    for i in range(len(titlesList)):
        if len(titlesList[i]) < 3:
            titlesDic[titlesList[i][1]] = titlesList[i][0]
        else:
            titlesDic[titlesList[i][1]] = titlesList[i][0]
            titlesDic[titlesList[i][2]] = titlesList[i][0]
    return titlesDic
    

print(readTitlesDict('titles.txt'))


def readCandFile(file_name):
    '''
    Reads candidates file into a list.
    '''