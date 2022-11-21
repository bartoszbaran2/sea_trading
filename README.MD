#Sea Trading

## Python OOP
- class
- object
- self
- method
  - default (self)
  - staticmethod ()
  - classmethod (cls)
- field/attributes
  - object field (self)
  - class field (obiekty mają tą sama wartość)
- python features (magic methods)
  - `__str__` -> string
  - `__len__` -> int - ilość elem. wew. obiektu
  - `__repr__` -> string
  - `__format__` -> string
  - `__name__` -> string
  - `__init__` -> None
  - `__new__` -> self/object
- constructor: metoda, która tworzy obiekt
- object descriptor/data object descriptor(getter/setter)
- property - class data object descriptor
- super
- MRO - method resolution order 

##OOP Rules
1. Abstraction
2. Inheritance
3. Polymorphism
4. Encapsulation
   - private
   - protected
   - public
   - read_only

##SOLID
1. single responsibility
2. open/closed
3. liskov substitution
4. interface segregation
5. dependency inversion

## Hierarchy
- Interface - requirements, no implementation (nie ma w pythonie)
- Abstract Class - requirements, partially implementation details 
- Concrete Class - implementation detail 

-----

- metaclass
- class
- object

## Examples:

```python

class X:
    b = 'on class'

    def __init__(self):
        self.a = 'on_instance' 
        print(self.a)
        print(X.b)
        self.a = 're-bound'
        self.b = 'new on instance'
        print(self.b)
        print(X.b)

```