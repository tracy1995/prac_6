from guitar import Guitar

def test():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)

    # Testing get_age() method
    current_year = 2022
    expected_age1 = 100
    expected_age2 = 9
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age(current_year)}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age(current_year)}")

    # Testing is_vintage() method
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage(current_year)}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage(current_year)}")

if __name__ == "__main__":
    test()
