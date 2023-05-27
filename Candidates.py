from MkDist import minkowskiDist

class Candidates(object):
    """
    Candidates
    """

    def __init__(self, name, titles):
        """
        Constructor

        Requires:
        name a string representing the name of the candidates;
        titles a list of numbers representing its titles vector
        Ensures:
        object of candidates created
        """
        self._name = name
        self._titles = titles

    def dimensionality(self):
        """
        Dimensionality of the titles vector

        Ensures:
        dimensionality of the titles vector
        """
        return len(self._titles)
    
    
    def setName(self, name):
        """
        Name setting

        Ensures:
        self._name = name
        """
        self._name = name


    def setTiles(self, titles):
        """
        Titles setting

        Ensures:
        self._titles = titles
        """
        self._titles = titles


    def getName(self):
        """
        Name of the candidates

        Ensures:
        name of candidates
        """
        return self._name

    def getTitles(self):
        """
        Titles vector of the candidates
    
        Ensures:
        list representing the titles vector of the animal
        """
        return self._titles
    

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
    
    
    