from item import Item


class ItemList:
    def __init__(self):
        self.items = []

    def create_items(self, list_of_items):
        for item in list_of_items:
            self.items.append(Item(item[0], item[1], item[2], item[3]))

    def get_items_list(self):
        result = []
        for item in self.items:
            result.append([item.name, item.description, item.status, item.price])
            return result
