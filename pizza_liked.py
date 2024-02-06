"""

Create a code that returns a list of the different pizza you have tried

"""


def main():
    # Initialize an empty list to store the pizzas tried
    pizzas_tried = []

    while True:
        # Ask the user what type of pizza they tried
        pizza = input("What other type of pizza did you try? (Enter 'quit' to exit): ").strip().lower()

        # Check if the user wants to quit
        if pizza == 'quit':
            break

        # Check if the pizza has already been tried
        if pizza in pizzas_tried:
            print("You've already tried", pizza.capitalize(), "pizza!")
        else:
            # Add the pizza to the list of pizzas tried
            pizzas_tried.append(pizza)
            print("Added", pizza.capitalize(), "pizza to your list of tried pizzas!")

    # Print the list of pizzas tried
    print("\nList of pizzas you've tried:")
    for pizza in pizzas_tried:
        print("- " + pizza.capitalize())


if __name__ == "__main__":
    main()
