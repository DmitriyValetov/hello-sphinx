"""
main.py
====================================
The core module of my example project
"""

from .other_staff import Dog

def test():
    """
    test funrction in main.py
    """
    dog = Dog('Sharik')
    print(dog.voice())


def foo(a: int, b=None):
    """This function does something.
    Some text more

    Parameters
    ----------
    a: int
        this is a return value
    b: callable
        this can be callend
    
    Returns
    -------
    describe: type
        Explanation of return value
    """
    if b is not None:
        a = b(a)
    return a

if __name__ == "__main__":
    """
    entry point
    """
    test()


def about_me(your_name):
    """
    Return the most important thing about a person.
    Parameters
    ----------
    your_name: str
        A string indicating the name of the person.
    """
    return "The wise {} loves Python.".format(your_name)


class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        """
        Blah blah blah.
        Parameters
        ---------
        name
            A string to assign to the `name` instance attribute.
        """
        self.name = name

    def about_self(self):
        """
        Return information about an instance created from ExampleClass.
        """
        return "I am a very smart {} object.".format(self.name)