import math


class SpaceAge:
    EARTH_TIME = 31557600
    MERCURY_FACTOR = 0.2408467
    VENUS_FACTOR = 0.61519726
    MARS_FACTOR = 1.8808158
    JUPITER_FACTOR = 11.862615
    SATURN_FACTOR = 29.447498
    URANUS_FACTOR = 84.016846
    NEPTUNE_FACTOR = 164.79132

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / self.EARTH_TIME, 2)

    def on_mercury(self):
        return round(self.on_earth() / self.MERCURY_FACTOR, 2)

    def on_venus(self):
        # for some reason round(val, 2) doesn't work here
        return math.ceil(self.on_earth() / self.VENUS_FACTOR * 100) / 100

    def on_mars(self):
        return round(self.on_earth() / self.MARS_FACTOR, 2)

    def on_jupiter(self):
        return round(self.on_earth() / self.JUPITER_FACTOR, 2)

    def on_saturn(self):
        return round(self.on_earth() / self.SATURN_FACTOR, 2)

    def on_uranus(self):
        return round(self.on_earth() / self.URANUS_FACTOR, 2)

    def on_neptune(self):
        return round(self.on_earth() / self.NEPTUNE_FACTOR, 2)
