# bulky-sort

File **bulky_sort.py** contains the *sort* function as per the defailed description and can be called by import (e.g *from bulky_sort import bulky*).

The **sort** function sorts packages into 'STANDARD', 'SPECIAL', or 'REJECTED' stacks based on their volume and mass.
    Args:
        width (float or int): The width of the package in centimeters.
        height (float or int): The height of the package in centimeters.
        length (float or int): The length of the package in centimeters.
        mass (float or int): The mass of the package in kilograms.

    Returns:
        str: The name of the stack ('STANDARD', 'SPECIAL', 'REJECTED')
             where the package should go.

File **test_bulky_sort.py** contains the test cases. **Pytest** can be used (preferred) to execute the test case (e.g. *% pytest test_bulky_sort.py*).
