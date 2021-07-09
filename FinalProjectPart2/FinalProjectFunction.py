def answer(possibilities, option=0):
    """ Checks if more than one possible product, if so chooses the most expensive one.
    Arranges the item information in a string and prints it. If option is not 0, arranges and prints
    all items in the provided list. """
    if option == 0:
        if len(possibilities) > 1:
            price = 0
            product = []
            for item in possibilities:
                if float(item[-1]) > price:
                    price = float(item[-1])
                    product = item[::]   # This creates a copy of the item so the original item is not modified
                    # by the following changes
                    product[-1] = "$" + str(product[-1])
                    product[1] = (product[1]).capitalize()  # This capitalizes the manufacturer name
            response = ", ".join(product)
            print(response)
        else:
            item = possibilities[0]
            product = item[::]
            product[-1] = "$" + str(product[-1])
            product[1] = (product[1]).capitalize()
            response = ", ".join(product)
            print(response)
    else:
        for item in possibilities:
            product = item[::]
            product[-1] = "$" + str(product[-1])
            product[1] = (product[1]).capitalize()
            response = ", ".join(product)
            print(response)
