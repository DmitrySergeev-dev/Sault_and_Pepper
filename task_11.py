class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name;
        self.calories = calories

    def setDessert(self, name, calories):
        self.name = name
        self.calories = calories

    def getDessert(self):
        return self.name, self.calories

    def is_healthy(self):
        try:
            if self.calories < 200:
                return True
        except:
            pass

    def is_delicious(self):
        return True


# # TEST
# dessert = Dessert()
# dessert.name = "test_name"
# print(dessert.name)
#
# dessert.name = "test_name2"
# print(dessert.name)
# if dessert.name != "test_name2":
#     raise Exception("Setter for name is not working")
#
# dessert.calories = "test_calories"
# print(dessert.calories)
# dessert.calories = "test_calories2"
# print(dessert.calories)
# if dessert.calories != "test_calories2":
#     raise Exception("Setter for calories is not working")
#
# print(dessert.is_delicious())
# if not dessert.is_delicious():
#     raise Exception("Invalid method result")
#
# print(dessert.is_healthy())
# dessert.calories = 300
# print(dessert.calories)
# print(dessert.is_healthy())
# if dessert.is_healthy():
#     raise Exception("Logical error. Method must return False")
# print(dessert.is_delicious())
# if not dessert.is_delicious():
#     raise Exception("Invalid method result")
#
# dessert.calories = 200
# print(dessert.calories)
# print(dessert.is_healthy())
# if dessert.is_healthy():
#     raise Exception("Logical error. Method must return False")
#
# dessert.calories = 199.9999
# print(dessert.is_delicious())
# if not dessert.is_delicious():
#     raise Exception("Invalid method result")
# print(dessert.calories)
# print(dessert.is_healthy())
# if not dessert.is_healthy():
#     raise Exception("Logical error. Method must return True")
