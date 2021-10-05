"""Print out all the melons in our inventory."""


from melons import melons
def print_melons(melon_dict):
    """Print each melon with corresponding attribute information."""
    for melon in melon_dict.keys():
        print(f"{melon.upper()}")
        for attr in melon_dict[melon].keys():
            print(f"      {attr}:{melon_dict[melon][attr]}")

print_melons(melons)