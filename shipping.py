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
    def create_empty(cls, owner_code):  # gwarantuje, że nie będzie parametru contents
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))  # automatycznie zamienia na listę

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # self.next_serial = self.next_serial  # RHS, odczyt, nie używać tak
        # self.serial = ShippingContainer._generate_serial()
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


sc = ShippingContainer('ELO', ['drugs'])
print(sc.bic)
