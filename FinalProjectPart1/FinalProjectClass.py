# Itzel Munoz Monroy PSID: 1888446
class Items:
    def __init__(self):
        self.item_id = "0"
        self.item_name = "none"
        self.item_type = "none"
        self.item_price = "0"
        self.item_date = "1/1/1"
        self.item_damage = ""

    def csv_line(self, all_list):
        # '''This method creates a string line for the FullInventory file'''
        all_atr = [self.item_id, self.item_name, self.item_type, self.item_price, self.item_date, self.item_damage]
        line = ",".join(all_atr)
        all_list[self.item_name] = line

    def new_type(self, types_list):
        # '''This method finds the number of types of items'''
        if self.item_type not in types_list:
            types_list.append(self.item_type)

    def type_line(self, type_dict):
        # '''This method creates a key:value pair meant for the types files'''
        line = [self.item_id, self.item_name, self.item_price, self.item_date, self.item_damage, self.item_type]
        type_dict[self.item_id] = line

    def add_damage(self, damage, price_list):
        # This method checks if the item is damaged
        # and if so creates a string line for the damaged file.
        if "damage" in self.item_damage:
            damage_atr = [self.item_id, self.item_name, self.item_type, self.item_price, self.item_date]
            line = ",".join(damage_atr) + "\n"
            damage[self.item_price] = line
            price_list.append(int(self.item_price))

    def add_date(self, date_dic, date_list):
        # This method checks if the item is past it's service date
        # and if so creates a string line for the past service date file.
        import datetime
        date = str(self.item_date).split("/")
        month = date[0]
        day = date[1]
        year = date[2]
        if datetime.date(int(year), int(month), int(day)) < datetime.date.today():
            date_item = datetime.date(int(year), int(month), int(day))
            date_atr = [self.item_id, self.item_name, self.item_type, self.item_price, self.item_date, self.item_damage]
            line = ",".join(date_atr)
            date_dic[date_item] = line
            date_list.append(date_item)
