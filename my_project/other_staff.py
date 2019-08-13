import types

class animal:
    """
    abstract base class
    """
    def __init__(self, species: str):
        """
        Base class constractor
        """
        self.species = species

    def voice(self):
        """
        return string with a noise
        """
        pass

class Dog(animal):
    """
    Dog class. It inherits the animal
    """
    def __init__(self, name:str):
        """
        Constructer of a dog
        """
        self.name = name
        super(self).__init__(species='dog')

    def voice(self):
        """
        Dog's raw
        """
        return "Wowww"