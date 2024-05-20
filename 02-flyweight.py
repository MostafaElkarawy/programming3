class CarInfo(object):
    """Separate class for Complex Cars"""

    def __init__(self):
        pass

    def cars(self, car_name):
        return f'car name are {car_name}'


class CarFamilies(object):
    """dictionary to store ids of the car"""

    car_family = {}

    def __new__(cls, name, car_family_id):

        try:
            obj = cls.car_family[car_family_id]

        except KeyError:
            obj = object.__new__(cls)
            cls.car_family[car_family_id] = obj
        return obj

    def set_car_info(self, car_brand):

        """set the car information"""

        cc = CarInfo()
        self.car_brand = cc.cars(car_brand)

    def get_car_info(self):

        """return the car information"""

        return (self.car_brand)


def car_main():
    car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
    car_family_objects = []
    for i in car_data:
        obj = CarFamilies(i[0], i[1])
        obj.set_car_info(i[2])
        car_family_objects.append(obj)
    """similar id's says that they are same objects """

    for i in car_family_objects:
        print("id = " + str(id(i)))
        print(i.get_car_info())


# ----------------------------------------------- Example 2 ------------------------------------------------------------
class OrderInfo(object):
    def __init__(self):
        pass

    def order_details(self, order_id):
        return f'Order details for Order ID {order_id}'


class OrderFamilies(object):
    order_family = {}

    def __new__(cls, customer_id, order_id):
        try:
            obj = cls.order_family[(customer_id, order_id)]
        except KeyError:
            obj = object.__new__(cls)
            cls.order_family[(customer_id, order_id)] = obj
        return obj

    def set_order_info(self, order_details):
        oi = OrderInfo()
        self.order_details = oi.order_details(order_details)

    def get_order_info(self):
        return self.order_details


def order_main():
    order_data = (("ahmad", 1, "Order001"), ("ibrahim", 2, "Order002"),
                  ("khbib", 3, "Order003"), ("ahmad", 1, "Order001"))
    order_family_objects = []
    for data in order_data:
        obj = OrderFamilies(data[0], data[1])
        obj.set_order_info(data[2])
        order_family_objects.append(obj)
    for obj in order_family_objects:
        print("ID:", id(obj))
        print("Order info for:", obj.get_order_info())


if __name__ == '__main__':
    car_main()
    print("                  --------------------                     ")
    order_main()
