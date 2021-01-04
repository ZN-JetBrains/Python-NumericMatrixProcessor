def startswith_capital_counter(names):
    if not names:
        return -1

    counter = 0

    for name in names:
        if name.istitle():
            counter += 1
    return counter
