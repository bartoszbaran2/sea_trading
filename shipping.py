import iso6346


class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial  # żeby zaczynało od 0 id
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code, **kwargs):  # gwarantuje, że nie będzie parametru contents
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)  # automatycznie zamienia na listę

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        # self.next_serial = self.next_serial  # RHS, odczyt, nie używać tak
        # self.serial = ShippingContainer._generate_serial()
        self.bic = type(self)._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temperature):
        if temperature > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError('Temperature too high!')
        self._celsius = temperature

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )


sc = ShippingContainer('ELO', ['drugs'])
rsc = RefrigeratedShippingContainer('ELO', ['drugs'], celsius=5)
rsc2 = RefrigeratedShippingContainer.create_empty('ELO', celsius=5)
print(sc.bic)
print(rsc.bic)
