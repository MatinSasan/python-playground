class ClassA:
    def hi(self):
        print('lel')


class ClassB:
    def hi(self):
        print('lel')

    def another(self):
        print('In class B')


class ClassC(ClassA, ClassB):
    pass


c = ClassC()
c.hi()
c.another()
