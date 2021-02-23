import random
from game import constants
from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    """
    The responsibility of Food is to keep track of its letters entered by players.
    
    Stereotype:
        Information Holder

    Attributes: 
        Uhh...
    """
    def __init__(self):
        """
        The class constructor. Invokes the superclass constructor, sets the 
        position and updates the on-screen text.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        super().__init__()
        self._word = ""
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f'Buffer: {self._word}')

    def get_buffer(self):
        """
        Starts the process of buffer.
        """
        return self._word
    
    def add_letters(self, letter):
        """
        Adds given letter to buffer and updates it.

        Args:
            self(Buffer): buffer instance.
            points(integer): points to be added.
        """
        if (letter == '*'):
            self.reset()
        else:
            self._word += letter
            self.set_text(f'Buffer: {self._word}')

    def reset(self):
        """
        Resets the letters.
        """
        self._word = ""
        self.set_text(f'Buffer: {self._word}')
