class Foo:
    __name="Foo"
    def __getname(self):
        print(self.__name)
    def get(self):
        self.__getname()
Foo().get()