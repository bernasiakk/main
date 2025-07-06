import random
import string

class Robot:
    used_names = set()  # Class variable to track all used names
    
    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        if self._name is None:
            self._name = self._generate_unique_name()
        return self._name
    
    def reset(self):
        if self._name:
            Robot.used_names.discard(self._name)  # Remove from used names
        self._name = None
    
    def _generate_unique_name(self):
        while True:
            # Generate 2 uppercase letters + 3 digits
            letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
            new_name = letters + digits
            
            # Check if name is unique
            if new_name not in Robot.used_names:
                Robot.used_names.add(new_name)
                return new_name
