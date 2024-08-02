class DVDPlayer:
    def on(self):
        print("DVD Player on")
    
    def play(self, movie):
        print(f"Playing {movie}")
    
    def off(self):
        print("DVD Player off")


class Projector:
    def on(self):
        print("Projector on")
    
    def wide_screen_mode(self):
        print("Projector in widescreen mode")
    
    def off(self):
        print("Projector off")


class Amplifier:
    def on(self):
        print("Amplifier on")
    
    def set_volume(self, level):
        print(f"Amplifier volume set to {level}")
    
    def off(self):
        print("Amplifier off")


class TheaterLights:
    def dim(self, level):
        print(f"Theater lights dimmed to {level}%")
    
    def on(self):
        print("Theater lights on")
class HomeTheaterFacade:
    def __init__(self, dvd, projector, amp, lights):
        self.dvd = dvd
        self.projector = projector
        self.amp = amp
        self.lights = lights
    
    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim(10)
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)
    
    def end_movie(self):
        print("Shutting movie theater down...")
        self.lights.on()
        self.projector.off()
        self.amp.off()
        self.dvd.off()
if __name__ == "__main__":
    dvd = DVDPlayer()
    projector = Projector()
    amp = Amplifier()
    lights = TheaterLights()
    
    home_theater = HomeTheaterFacade(dvd, projector, amp, lights)
    
    home_theater.watch_movie("Inception")
    print("\nAfter the movie...\n")
    home_theater.end_movie()
