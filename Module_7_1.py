class Product:
    def __init__(self,name: str,weight: float,category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        product = ''
        file = open(self.__file_name, 'r')
        product = file.read()
        file.close()
        return product

    def add(self, *products):
        products_names = []
        existing_products = self.get_products().split('\n')
        for product in existing_products:
            list = product.split(', ')
            product_name = list[0]
            products_names.append(product_name)

        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in products_names:
                file.write(str(product) + '\n')
                products_names.append(product.name)
            else:
                print(f"Продукт {product.name} уже есть в магазине")
        file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')


#print(p2)


s1.add(p1, p2, p3)


print(s1.get_products())