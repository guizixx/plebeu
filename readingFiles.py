# def readTitlesFile(file_name):
#     titles = []
#     inFile = open(file_name, 'r')
#     #iterates through each line in the file and append the titles that are spanned like this "2; Campeão Olímpico ; Paralímpico"
#     for line in inFile:
#         titles.append(line.split(';')[1])
#     return titles

# print(readTitlesFile('titles.txt'))

#function that reads a file organized like this "2; Campeão Olímpico ; Paralímpico" in every line and stores the titles in a dictionary
def readTitlesDict(file_name):
    titles = {}
    inFile = open(file_name, 'r')
    #iterates through each line in the file and append the titles that are spanned like this "2; Campeão Olímpico ; Paralímpico"
    for line in inFile:
        titles[line.split(';')[0]] = line.split(';')[1]
    return titles

print(readTitlesDict('titles.txt'))