class Factory:
    def __init__(self, material, zips, pockets): # self targets the location of the object created
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your object details are as follows\nMaterial: {self.material}\nNumber of pockets: {self.pockets}\nNumber of zips: {self.zips}")

reebok = Factory("leather", 3, 2)

campus = Factory("nylon", 3, 3)

# print(reebok.material)
# print(campus.zips)
reebok.show()