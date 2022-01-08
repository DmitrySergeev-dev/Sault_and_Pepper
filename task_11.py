class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name;
        self.__calories = calories

    def setDessert(self, name, calories):
        self.__name = name
        self.__calories = calories

    def getDessert(self):
        return self.__name, self.__calories

    def is_healthy(self):
        try:
            if self.__calories < 200:
                return True
        except:
            pass

    def is_delicious(self):
        return True


# TEST
# des = Dessert(500)
# print(des.__dict__)
# print(des.getDessert())
# des.setDessert("any", 150)
# print(des.getDessert())
# print(des.is_healthy())
# print(des.is_delicious())
