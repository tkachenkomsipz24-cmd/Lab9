class Product:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.code == other.code

    def __hash__(self) -> int:
        return hash(self.code)


items = [
    Product("A-100", "Кабель USB-C"),
    Product("B-205", "Миша бездротова"),
    Product("A-100", "Кабель USB-C"),
    Product("C-310", "Клавіатура"),
    Product("D-415", "Монітор 24 дюйми"),
    Product("B-205", "Миша бездротова"),
    Product("E-520", "Навушники"),
    Product("F-630", "Вебкамера"),
]

unique = set()
for p in items:
    unique.add(p)

stock = {}
stock[Product("A-100", "Кабель USB-C")] = 17
stock[Product("A-100", "Кабель USB-C")] = 25

a = Product("A-100", "Кабель USB-C")
b = Product("A-100", "Кабель USB-C")

print(a == b)
print(len(unique))
print(a in unique)
print(len(stock))
print(a in stock)