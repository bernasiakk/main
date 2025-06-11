class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(hour={self.hour!r}, minute={self.minute!r})'

    def __str__(self):
        return f"{self.hour}:{self.minute}"

    def __eq__(self, other):
        """
        Two clocks that represent the same time should be equal to each other.
        """
        pass

    def __add__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute + minutes)
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        pass
    
print(repr(Clock(10, 50)))