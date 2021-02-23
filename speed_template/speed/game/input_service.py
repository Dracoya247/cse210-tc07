import sys
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _directions (Dict): A dictionary containing Points for U, D, L and R.
        _current (Point): The last direction that was pressed.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        
    def get_direction(self):
        """
        Gets the typed letter. 

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The typed letter.
        """
        result = ""
        event = self._screen.get_key()
        
        if not event is None:
            if event == 1:
                sys.exit()
            
            character = chr(event)
            if character == '\r' or character == '\n':
                result = '*'
            elif character >= 'A' and character <= 'z':
                result = char
        return result