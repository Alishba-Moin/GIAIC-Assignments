'''18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.'''

# Create a Product class with private attribute _price
class Product:
    def __init__(self, price):
        self._price = price  # initialize price

    # @property to get the price
    @property
    def price(self):
        return self._price  # return the price

    # @price.setter to update the price
    @price.setter
    def price(self, update_price):
        self._price = update_price  # update the price

    # @price.deleter to delete the price
    @price.deleter
    def price(self):
        print("Price Deleted!")  # print message when deleting price
        del self._price  # delete the price attribute


product = Product(15000)
print(f"Original Price: {product.price}")  # get the original price

# Update the price to 20000
product.price = 20000
print(f"Updated Price: {product.price}")  # get the updated price

# Delete the price attribute
del product.price

# Uncomment the following line to see the error after deleting the price
# print(product.price)  # This will raise an error since price is deleted
