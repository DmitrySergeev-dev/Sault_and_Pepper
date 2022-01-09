class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name;
        self.__calories = calories
        # print("__init__ of Dessert")

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

class JellyBean(Dessert):
    def __init__(self, name = None, calories = None, flavor=None):
        super().__init__(name=None, calories=None)
        # print("__init__ of JellyBean")
        self.__flavor = flavor

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor

    def is_delicious(self):
        if self.__flavor == "black licorice":
            return False
        else:
            return True
# j = JellyBean("smb", 450, 500)
# print(j.__dict__)
# j.set_flavor("black licorice")
# print(j.__dict__)
# print(j.is_delicious())

