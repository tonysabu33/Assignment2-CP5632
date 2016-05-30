from item import Item


class ItemList:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "{}".format(self.items)

    def create_list(self):

        new_list = []
        for item in self.items:
            name = item.name
            description = item.description
            price = item.price
            status = item.status
            new_list.append([name, description, price, status])
        return new_list

    def add_item(self, name, description, price, status):

        self.items.append(Item(name, description, price, status))

    def generate_list(self, item_list):

        for item in item_list:
            self.items.append(Item(item[0], item[1], float(item[2]), item[3]))

    def get_item(self, name):

        for item in self.items:
            if item.name == name:
                return item
