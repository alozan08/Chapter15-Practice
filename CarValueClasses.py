'''
    Complete the Car class by creating an attribute purchase_price (type int) and the method
    print_info() that outputs the car's information
    ex:
        input:
            2011
            18000
            2018
        output:
            Car's information:
                Model year: 2011
                Purchase price: $18000
                Current value: $5770
'''

class Car:
    def __init__(self):
        self.modelYear = 0
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        car_age = current_year - self.modelYear
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        format_str = (f"Car's information:\n  Model year: {self.modelYear}\n  Purchase price: ${self.purchase_price}\n"
                      f"  Current value: ${self.current_value}")
        print(format_str)


if __name__ == "__main__":
    year = int(input())
    price = int(input())
    current_year = int(input())

    my_car = Car()
    my_car.modelYear = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()