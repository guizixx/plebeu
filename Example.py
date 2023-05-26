from MkDist import minkowskiDist

class Example(object):
    """
    Example for clustering
    """

    def __init__(self, name, features, label = None):
        """
        Constructor

        Requires:
        features is list of numbers representing the feature vector;
        label is string with the label of the example
        Ensures:
        object of type Example created
        """
        self._name = name
        self._features = features
        self._label = label


    def dimensionality(self):
        """
        Dimensionality of the feature vector

        Ensures:
        dimensionality of the feature vector
        """
        return len(self._features)


    def setName(self, name):
        """
        Name setting

        Ensures:
        self._name = name
        """
        self._name = name

        
    def setFeatures(self, features):
        """
        Features setting

        Ensures:
        self._features = features
        """
        self._features = features
        

    def setLabel(self, label):
        """
        Label setting

        Ensures:
        self._label = label
        """
        self._label = label

    
    def getFeatures(self):
        """
        Features

        Ensures:
        feature vector
        """
        return self._features[:]


    def getLabel(self):
        """
        Object label

        Ensures:
        object label
        """
        return self._label


    def getName(self):
        """
        Object Name

        Ensures:
        object name
        """
        return self._name


    def distance(self, other):
        """
        Euclidean distance wrt a given example

        Requires:
        other is an example
        Ensures:
        the Euclidean distance between feature vectors
        of self and other
        """
        return minkowskiDist(self._features, other.getFeatures(), 2)


    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form "name:features:label"
        """
        return self._name + ':' + str(self._features) + ':' + str(self._label)
    
       
    def __eq__(self, other):
        """
       Equality comparison method

       Ensures:
       returns True if the current object is equal to the other object, False otherwise
        """
        return self._name == other._name and self._features == other._features and self._label == other._label


    def __lt__(self, other):
        """
        Less than comparison method

        Ensures:
        returns True if the current object is less than the other object, False otherwise
        """
        return self._name < other._name
    
<<<<<<< HEAD
   def __eq__(self):
        """
       Equality comparison method

       Ensures:
       
        """
##
##
##    def __lt__(self): #to be implemented
##            pass
        
=======
           
>>>>>>> main
