class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
    def show(self):
        print(f"The Material used is: {self.material}\nNumber of zips are: {self.zips}\ncolor of the leather is: {self.color}\nNumber of pockets are: {self.pockets}")

factory = PuneFactory("Vegan Leather", 2, "Brown", 3)
factory.show()