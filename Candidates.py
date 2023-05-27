# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60262 André Guo

from readingFiles import readTitlesDict, readCandFile
from MkDist import minkowskiDist

class Candidates(object):
    """
    Candidates
    """

    def __init__(self, inputFileName, titlesFileName):
        """
        Constructor

        Requires:
        inputFileName is the name of candidates file
        titlesFileName is the name of titles file
        Ensures:
        object of candidates created
        """
        self._inputFileName = inputFileName
        self._titlesFileName = titlesFileName

    def dimensionality(self):
        """
        Dimensionality of the titles vector

        Ensures:
        dimensionality of the titles vector
        """
        return len(self._titles)
    

    def candidatesList(self):
        '''
        Creates a list with the candidates
        '''
        self._candidates = readCandFile(self._inputFileName)
        return self._candidates

    
    def titlesDictionary(self):
        '''
        Creates a dictionary with the titles
        '''
        self._titles = readTitlesDict(self._titlesFileName)
        return self._titles
    

    def getCandidates(self):
        '''
        Get's the name of the candidates
        '''
        return self._candidates
    
    def getTitles(self):
        '''
        Get's the titles
        '''
        return self._titles

    def setCandidatesFileName(self, name):
        """
        Candidates file name setting

        Ensures:
        self._inputFileName = name
        """
        self._inputFileName = name


    def setTitlesFileName(self, titles):
        """
        Titles file name setting

        Ensures:
        self._titlesFileName = titles
        """
        self._titlesFileName = titles


    def getCandidatesFileName(self):
        """
        Get's the candidates file name

        Ensures:
        name of candidates file
        """
        return self._inputFileName


    def getTitlesFileName(self):
        """
        Get's the titles file name
    
        Ensures:
        name of titles file
        """
        return self._titlesFileName
    

    def distance(self, other):
        """
        Euclidean distance 

        Requires:
        other is an example
        Ensures:
        the Euclidean distance between titles vectors
        of self and other
        """
        return minkowskiDist(self._titles, other.getTitles(), 2)
    

    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form "name;titles"
        """
        return self._name + ';' + str(self._titles) 
    

    def __eq__(self, other):
        """
       Equality comparison method

       Ensures:
       returns True if the current object is equal to the other object, False otherwise
        """
        return self._name == other._name and self._titles == other._titles 
    

    def __lt__(self, other):
        """
        Less than comparison method

        Ensures:
        returns True if the current object is less than the other object, False otherwise
        """
        return self._name < other._name
    
    
    