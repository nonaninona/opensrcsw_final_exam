import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def distance(self, other):
        if other is self:
            print("서로 다른 점이어야 합니다")
            return

        if type(other) != type(self):
            print("Point 타입 객체를 인수로 해주세요")
            return

        distance = math.sqrt((other.getX() - self.__x)**2 + (other.getY() - self.__y)**2)
        print("거리 계산 결과 :", distance)
        return distance
        
    def __add__(self, other):
        if type(other) != type(self):
            print("Point 타입 객체끼리만 연산이 가능합니다")
            return

        x = self.__x + other.getX()
        y = self.__y + other.getY()
        print("덧셈 연산 결과 : Point({0}, {1})객체를 반환합니다".format(x,y))
        return Point(self.__x + other.getX(), self.__y + other.getY())

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

p1 = Point(1,1)
p2 = Point(2,2)

p1.distance(p2)
p1 + p2
