############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        #Don't touch!
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # self.add_pairing("")
    # Fill in the rest

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)
    
    yellow = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow.add_pairing("ice cream")
    all_melon_types.append(yellow)
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # melon_types = make_melon_types()

    for melon in melon_types:
        print()
        print(f"{melon.name} pairs with:")
        for pairing in melon.pairings:
            print(f" {pairing}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_by_id = {}

    for melon in melon_types:
        if melon.code not in melons_by_id:
            melons_by_id[melon.code] = melon

    return melons_by_id

    # for melon in melon_types:
    #     melons_by_code[melon.code] = melons_by_code.get(melon, 0) + 1
############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(
        self, melon_type, shape_rating, color_rating, field, harvester
    ):
        """Initialize a particular melon."""
    # Needs and is_sellable methods

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):

        # a melon is able to be sold if
        # both its shape and color ratings are greater than 5
        # and it didn’t come from field 3

        # can_sell = True

        # if shape is 5 or less
            # can_sell = False
        # if color is 5 or less
            # can_sell = False
        # if field is field 3
            # can_sell = False

        # if self.shape_rating <= 5:
        #     can_sell = False
        # elif self.color_rating <= 5:
        #     can_sell = False
        # elif self.field == 3:
        #     can_sell = False

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False

        # return can_sell

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')

    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, 'Michael')

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        harvester = f"Harvested by {melon.harvester}"
        field = f"Field #{melon.field}"
        sellable = " (Can Be Sold)" if melon.is_sellable() else " (Cannot Be Sold)"
        print(f"{harvester} from {field}{sellable}")
