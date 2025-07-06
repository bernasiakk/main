class Clock:
    def __init__(self, hour: int, minute: int):
        total_minutes = hour * 60 + minute
        
        self.hour = (total_minutes // 60) % 24
        self.minute = total_minutes % 60
       
        # if hour == 24:
        #     self.hour = 0
        
        # if not 0 <= hour <= 24:
        #     raise ValueError('hour must be within 0-24 range')
        
        # if not 0 <= minute < 60:
        #     raise ValueError('minute must be within 0-60 range')

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self.hour!r}, {self.minute!r})"

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def __eq__(self, other):
        """
        Two clocks that represent the same time should be equal to each other.
        """
        if not isinstance(other, Clock):
            return NotImplemented
        return (self.hour * 60 + self.minute) == (other.hour * 60 + other.minute)

    def __add__(self, minutes: int):
        total_minutes = self.hour * 60 + self.minute + minutes
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes: int):
        total_minutes = self.hour * 60 + self.minute - minutes
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60
        return Clock(new_hour, new_minute)

clock = Clock(10, 50)
print(Clock(11, 0))