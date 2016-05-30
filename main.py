"""
Tony Sabu
30-5-2016
github repository: https://github.com/tonysabu33/Assignment2-CP5632
"""

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
RETURN_MODE = 1


class ItemHire(App):  # creating class ItemHire
    status_text = StringProperty()  # for showing the status of each button and item

    def __init__(self, **kwargs):  # initializer function
        super().__init__(**kwargs)

        temp_item_list = load_items()
        self.items = ItemList()
        self.mode = LIST_MODE
        self.mode1 = HIRE_MODE
        self.mode2 = RETURN_MODE

        self.items.generate_list(temp_item_list)
        self.pressed_items = []

    def build(self):  # creating function for connecting GUI
        self.title = "Item hiring Application"  # creating title
        self.root = Builder.load_file('app.kv')  # loading .kv file
        self.create_buttons()
        return self.root  # reference to root the widget

    def create_buttons(self):  # creating the layout and buttons in GUI
        self.root.ids.statusLabel.text = "Choose action from the left Menu,then select item on the right"
        for item in self.items.items:
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
        self.root.ids.statusLabel.text = "Choose action from the left Menu,then select item on the right"
        self.root.ids.ListItem.state = 'down'
        self.root.ids.HireItem.state = 'normal'
        self.root.ids.ReturnItem.state = 'normal'

    def press_entry(self, instance):  # function to handle the pressing of items in GridLayout
        item = self.items.get_item(instance)
        if self.mode == LIST_MODE:
            name = instance.text
            self.status_text = name
            for item in self.items.items:
                if name == item.name and item.status == "out":
                    self.root.ids.statusLabel.text = item.name + '(' + item.description + ')' + '$' + str(
                        item.price) + 'is out'
                if name == item.name and item.status == "in":
                    self.root.ids.statusLabel.text = item.name + '(' + item.description + ')' \
                                                     + 'is available for hire' + '$' + str(item.price)
        elif self.mode == HIRE_MODE:
            pass
        instance.state = 'down'

    def press_hire(self):  # function to hire items
        self.mode1 = HIRE_MODE
        self.root.ids.HireItem.state = "down"
        self.root.ids.ListItem.state = "normal"
        self.root.ids.ReturnItem.state = "normal"
        self.root.ids.statusLabel.text = "Select available item to hire"

    def press_entry_hire(self, instance1):  # function to handle the pressing of items in GridLayout under press_hire
        if self.mode1 == HIRE_MODE:
            name = instance1.text
            self.status_text = name
            for item in self.items.items:
                if name == item.name and item.status == "out":
                    self.root.ids.statusLabel.text = item.name + '(' + item.description + ')' + 'is out'
                elif name == item.name and item.status == "in":
                    self.root.ids.statusLabel.text = 'Hiring' + item.name + '(' + item.description + ')' \
                                                     + 'for' + '$' + str(item.price)
        elif self.mode1 == LIST_MODE:
            pass
        instance1.state = 'down'

    def press_return(self):  # function to return items
        self.root.ids.statusLabel.text = "Select item to return"
        self.root.ids.ReturnItem.state = "down"
        self.root.ids.ListItem.state = "normal"
        self.root.ids.HireItem.state = "normal"
        self.mode2 = RETURN_MODE

    def press_entry_return(self,
                           instance2):  # function to handle the pressing of items in GridLayout under press_return
        if self.mode2 == RETURN_MODE:
            name = instance2.text
            self.status_text = name
            for item in self.items.items:
                if name == item.name and item.status == "in":
                    self.root.ids.statusLabel.text = item.name + 'is not hired'
                elif name == item.name and item.status == "out":
                    self.root.ids.statusLabel.text = 'Returning:' + item.name + '(' + item.description + ')' \
                                                     + 'for' + '$' + str(item.price)
        elif self.mode1 == LIST_MODE:
            pass
        instance2.state = 'down'

    def press_confirm(self):  # function to confirm the changes like hiring and returning
        self.root.ids.Confirm.state = "down"
        self.root.ids.HireItem.state = "normal"
        self.root.ids.ListItem.state = "normal"
        self.root.ids.ReturnItem.state = "normal"

        if self.mode1 == HIRE_MODE:
            for item in self.pressed_items:
                if item.status == "in":
                    item.status = "out"

        if self.mode2 == RETURN_MODE:
            for item in self.pressed_items:
                if item.status == "out":
                    item.status = "in "

    def on_stop(self):  # function to save all the changes when the window is closed(stopped)
        save_list(self.items.make_list())

    def press_add(self):
        self.status_text = "Enter details for new item"  # status line for add_item popup
        self.root.ids.popup.open()

    def press_save(self, added_name, added_description, added_price):  # function for saving new item to the list
        self.items.add_item(added_name, added_description, str(added_price), "in")

        self.root.ids.entriesBox.cols = 2  # setting the column format in GridLayout

        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        temp_button.background_color = (0, 1, 1, 1)
        self.root.ids.entriesBox.add_widget(temp_button)

        self.root.ids.popup.dismiss()
        self.clear_fields()

    def press_cancel(self):  # function to cancel the adding of new item
        self.root.ids.popup.dismiss()  # dismissing the popup
        self.clear_fields()
        self.status_text = ""

    def clear_fields(self):  # function for clearing the fields in add_item popup
        self.root.ids.AddName.text = ""
        self.root.ids.AddDescription.text = ""
        self.root.ids.AddPrice.text = ""


ItemHire().run()
