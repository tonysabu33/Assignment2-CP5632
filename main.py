from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from TonySabuA1 import load_items
from TonySabuA1 import save_list
from itemlist import ItemList
from item import Item

LIST_MODE = 0
HIRE_MODE = 1
RETURN_MODE = 0


class ItemHire(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        temp_item_list = load_items()
        self.items = ItemList()
        self.mode = LIST_MODE
        self.items.generate_list(temp_item_list)

        self.pressed_items = []

    def build(self):
        self.title = "Item hiring Application"
        self.root = Builder.load_file('app.kv')
        self.create_buttons()
        return self.root

    def create_buttons(self):
        for item in self.items.items:
            # name = self.items.items
            temp_button = Button(text=item.name)
            if item.status == "in":
                temp_button.background_color = (0, 1, 1, 1)
                temp_button.bind(on_press=self.press_entry)
                self.root.ids.entriesBox.add_widget(temp_button)

            if item.status == "out":
                temp_button.background_color = (1, 0, 1, 1)
                temp_button.bind(on_press=self.press_entry)
                self.root.ids.entriesBox.add_widget(temp_button)

    def press_button(self):
        self.mode = LIST_MODE
        self.root.ids.ListItem.state = 'down'
        self.root.ids.HireItem.state = 'normal'
        self.root.ids.ReturnItem.state = 'normal'
        self.root.ids.statusLabel.text = "Choose action from the left Menu,then select item on the right"

    def press_entry(self, instance):
        item = self.items.get_item(instance)
        if self.mode == LIST_MODE:
            name = instance.text
            self.status_text = name
            for item in self.items.items:
                if name == item.name and item.status == "out":
                    self.root.ids.statusLabel.text = item.name + '(' + item.description + ')' + '$' + str(
                        item.price) + 'is out'
                if name == item.name and item.status == "in":
                    self.root.ids.statusLabel.text = item.name + '(' + item.description + ')' + 'is available for hire' + '$' + str(
                        item.price)
        elif self.mode == HIRE_MODE:
            pass
        instance.state = 'down'

    def press_add(self):
        self.status_text = "Enter details for new item"
        self.root.ids.popup.open()

    def press_save(self, added_name, added_description, added_price):
        self.items.add_item(added_name, added_description, str(added_price), "in")

        self.root.ids.entriesBox.cols = 2

        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        temp_button.background_color = (0, 1, 1, 1)
        self.root.ids.entriesBox.add_widget(temp_button)

        self.root.ids.popup.dismiss()
        self.clear_fields()

    # def press_return(self):
    #     for item in self.items.items:
    def on_stop(self):
        """
        save to csv file on closing of the main widget
        :return:
        """
        save_list(self.items.create_list())

    def press_hire(self):
        self.root.ids.statusLabel.text = "select available item to hire"
        self.root.ids.HireItem.state = "down"
        self.root.ids.ListItem.state = "normal"
        self.root.ids.ReturnItem.state = "normal"
        self.mode = HIRE_MODE

    def press_return(self):
        self.root.ids.statusLabel.text = "select item to return"
        self.root.ids.ReturnItem.state = "down"
        self.root.ids.ListItem.state = "normal"
        self.root.ids.HireItem.state = "normal"
        self.mode = RETURN_MODE

    def press_confirm(self):
        self.root.ids.Confirm.state = "down"
        self.root.ids.HireItem.state = "normal"
        self.root.ids.ListItem.state = "normal"
        self.root.ids.ReturnItem.state = "normal"

        if self.mode == RETURN_MODE:
            for item in self.pressed_items:
                if item.status == "out":
                    item.status = "in "
                    # save(self.item_list.create_list())

        if self.mode == HIRE_MODE:
            for item in self.pressed_items:
                if item.status == "in":
                    item.status = "out"

    def clear_fields(self):
        self.root.ids.AddName.text = ""
        self.root.ids.AddDescription.text = ""
        self.root.ids.AddPrice.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""

    def hire_something(self, item_name):
        print(item_name)


ItemHire().run()
