'''
    Given class Triangle, complete the program to read and set the base and height of triangle1
    and triangle2, determine which triangle's area is smaller, and output the smaller triangle's
    info, making use of Triangle's relevant methods
    ex:
        input:
            3.0 triangle1 base
            4.0 triangle1 height
            4.0 triangle2 base
            5.0 triangle2 height
        output:
            Triangle with smaller area:
            Base: 3.00
            Height: 4.00
            Area: 6.00
'''


class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    base1 = float(input())
    height1 = float(input())
    base2 = float(input())
    height2 = float(input())

    triangle1.set_base(base1)
    triangle1.set_height(height1)
    triangle2.set_base(base2)
    triangle2.set_height(height2)


    print('Triangle with smaller area:')

    area1 = triangle1.get_area()
    area2 = triangle2.get_area()
    if area1 < area2:
        triangle1.print_info()
    else:
        triangle2.print_info()

