from abc import ABC, abstractmethod


class Sandwich:
    def __init__(self, client_name=None, price=10):
        self.name = client_name
        self.price = price
        self.ingredients = {}
        self.sauce = {}

    def add_ingredients(self, key, value):
        self.ingredients[key] = value

    def display(self):
        return f'{self.ingredients.values()}'


class SandwichBuilder(ABC):
    def __init__(self, client_name):
        self.sandwich = Sandwich(client_name)

    @abstractmethod
    def add_ingredients(self):
        pass

    def add_extra(self, extra: dict):
        if dict:
            for _key, _value in extra.items():
                self.sandwich.add_ingredients(_key, _value)
                self.sandwich.price += _value

    def build(self):
        sandwich = self.sandwich
        self.sandwich = Sandwich()
        return sandwich


class VegetableSandwich(SandwichBuilder):
    def __init__(self, client_name):
        super().__init__(client_name)
        self.sandwich = self.build()
        self.kind = 'Vegetable'
        self.add_ingredients()
        self.sandwich.price += 5

    def add_ingredients(self):
        self.sandwich.add_ingredients('breed', 'bran bread')
        self.sandwich.add_ingredients('lettuce', 'lettuce')
        self.sandwich.add_ingredients('tomato', 'tomato')
        self.sandwich.add_ingredients('cucumber', 'cucumber')
        self.sandwich.add_ingredients('bean flesh', 'bean flesh')


class MeatSandwich(SandwichBuilder):
    def __init__(self, client_name):
        super().__init__(client_name)
        self.sandwich = self.build()
        self.kind = 'Meat'
        self.add_ingredients()
        self.sandwich.price += 8

    def add_ingredients(self):
        self.sandwich.add_ingredients('breed', 'white bread')
        self.sandwich.add_ingredients('sausage', 'sausage')
        self.sandwich.add_ingredients('meatball', 'meatball')


if __name__ == '__main__':
    clint1_order = VegetableSandwich('Ali: ')
    clint1_order.add_extra({'cheese': 4, 'tomato': 2})
    clint2_order = MeatSandwich('Hasan: ')

    print(clint1_order.sandwich.name, end=' ')
    print(clint1_order.kind, end=' ')
    print(clint1_order.sandwich.price)

    print(clint2_order.sandwich.name, end=' ')
    print(clint2_order.kind, end=' ')
    print(clint2_order.sandwich.price)
