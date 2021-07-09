# Itzel Munoz Monroy PSID: 1888446
class Items:
    def __init__(self):
        self.item_id = "0"
        self.item_name = "none"
        self.item_type = "none"
        self.item_price = "0"
        self.item_date = "1/1/1"
        self.item_damage = ""

    def good_items(self, all_list, date_list, damage):
        # '''This method checks if an item is not past it's due date or damaged,'''
        # and if it's not then it adds it to the 1st provided list
        if (self.item_id not in date_list) and (self.item_id not in damage):
            line = [self.item_id, self.item_name, self.item_type, self.item_price]
            all_list.append(line)

    def add_damage(self, damage):
        # This method checks if the item is damaged
        # and if so adds it's id to the damage list
        if "damage" in self.item_damage:
            damage.append(self.item_name)

    def add_date(self, date_list):
        # This method checks if the item is past it's service date
        # and if so appends it to the date list provided.
        import datetime
        date = str(self.item_date).split("/")
        month = date[0]
        day = date[1]
        year = date[2]
        if datetime.date(int(year), int(month), int(day)) < datetime.date.today():
            date_list.append(self.item_id)
