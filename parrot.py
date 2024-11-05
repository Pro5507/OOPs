class parrot:
    spicies= "bird"
    def __init__(self,name,age):
        self.name= name
        self.age= age
blue= parrot("Blue",3)
voe= parrot("Voe", 4)
print("Blue is a {}".format(blue.spicies))
print("Voe is a {}".format(voe.spicies))
print("{} is {} years old ".format(blue.name,blue.age))
print("{} is {} years old ".format(voe.name,voe.age))