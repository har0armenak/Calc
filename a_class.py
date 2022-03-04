class Avto:
    def __init__(self, speed, ak, dur):
        self.max_speed = speed
        self.aker = ak
        self.durs = dur
    
    def get_durs(self):
        print(self.durs)
    
    def get_speed(self):
        print(self.max_speed)

car1 = Avto(60, 4 , 2)
car2 = Avto(120, 2, 0)
car1.get_durs()
car2.get_durs()
car1.get_speed()

