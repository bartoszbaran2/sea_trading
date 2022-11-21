class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial  # żeby zaczynało od 0 id
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # self.next_serial = self.next_serial  # RHS, odczyt, nie używać tak
        self.serial = ShippingContainer._generate_serial()









sc = ShippingContainer(42, 'drugs')
sc2 = ShippingContainer(42, 'drugs')
print(sc.serial)
print(sc2.serial)
# print(sc.next_serial)
# print(sc2.next_serial)
# ShippingContainer.next_serial = 42  # przez class, wpływa na wszystkie obiekty
# print(sc.next_serial)
# print(sc2.next_serial)
