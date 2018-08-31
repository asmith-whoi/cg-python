# Utility Function

def num_to_id(num_list):
    """Convert a list of numbers to IDs by padding single digits
    with a zero"""
    for i, num in enumerate(num_list):
        if num < 10:
            num_list[i] = str(num).rjust(2, "0")
