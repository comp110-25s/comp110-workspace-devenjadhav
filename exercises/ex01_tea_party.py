"""
Tea Party Planner
This program calculates the required number of tea bags, treats, and the total cost of hosting a tea party.
"""

__author__: str = "730760482"


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed for the given number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the number of teas guests will drink."""
    teas: int = tea_bags(people=people)  # Using keyword argument
    return int(teas * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats based on fixed prices."""
    return (tea_count * 0.50) + (treat_count * 0.75)


def main_planner(guests: int) -> None:
    """Main function to orchestrate the tea party planning by calling other functions and printing results."""
    tea_needed: int = tea_bags(people=guests)
    treats_needed: int = treats(people=guests)
    total_cost: float = cost(tea_count=tea_needed, treat_count=treats_needed)

    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea bags: {tea_needed}")
    print(f"Treats: {treats_needed}")
    print(f"Cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))


my_numbers: list[float] = list()
