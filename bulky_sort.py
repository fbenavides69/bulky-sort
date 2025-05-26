def sort(width, height, length, mass):
    """
    Sorts packages into 'STANDARD', 'SPECIAL', or 'REJECTED' stacks
    based on their volume and mass.

    Args:
        width (float or int): The width of the package in centimeters.
        height (float or int): The height of the package in centimeters.
        length (float or int): The length of the package in centimeters.
        mass (float or int): The mass of the package in kilograms.

    Returns:
        str: The name of the stack ('STANDARD', 'SPECIAL', 'REJECTED')
             where the package should go.
    """

    # Calculate volume
    volume = width * height * length

    # Determine if bulky
    is_bulky = (volume >= 1_000_000) or \
               (width >= 150) or \
               (height >= 150) or \
               (length >= 150)

    # Determine if heavy
    is_heavy = mass >= 20

    # Determine the stack
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        # Use ternary operator as required for LLM
        return "SPECIAL" if (is_heavy or is_bulky) else "This should not be reached"
    else:
        return "STANDARD"
