from task_11 import Dessert


class JellyBean(Dessert):
    def set_flavor(self, flavor):
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor

    def is_delicious(self):
        if self.__flavor == "black licorice":
            return False
        else:
            return True


# TEST
# if __name__ == '__main__':
#     ob1 = JellyBean()
#     ob1.set_flavor(190)
#     print(ob1.__dict__)
#     print(ob1.is_delicious())
#     ob1.set_flavor("black licorice")
#     print(ob1.__dict__)
#     print(ob1.is_delicious())
#     ob1.set_flavor("smth")
#     print(ob1.__dict__)
#     print(ob1.is_delicious())


