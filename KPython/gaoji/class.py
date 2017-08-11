#coding=utf-8

#类装饰器方法
class Color(object):
    _color = (0,0,0)

    @classmethod
    def value(cls):
        if cls.__name__ == "Red":
            cls._color = (255,0,0)
        elif cls.__name__ == 'Green':
            cls._color = (0,255,0)
        return cls._color


class Red(Color):
    pass

class Green(Color):
    pass

class UnknowColor(Color):
    pass

red = Red()
green = Green()
xcolor = UnknowColor()

print 'red = ',red.value()
print 'green = ',green.value()
print 'xcolor = ',xcolor.value()
