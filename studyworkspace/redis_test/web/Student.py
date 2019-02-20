from abc import ABCMeta, abstractclassmethod





class Student():
    __slots__ = ('age')

    def __init__(self, age):
        self.age = age


class Student():
    __score = 0

    def __init__(self):
        pass


    @property
    def score(self):
        return self.__score


    @score.setter
    def score(self, value):
        if value > 100 :
            raise ValueError("can not bigger than 100")
        else:
            self.__score = value












class Humen():
    pass
    #__slots__ =  ('name')


class Man(Humen):
    __slots__ =  ('age')

    pass



if __name__ == '__main__':

    stu = Student()
    stu.score = 99
    print(stu.score)

    '''
    hu  = Humen()
    hu.age = 10

    man = Man()
    man.age = 10
    man.name = 'li'
    '''

