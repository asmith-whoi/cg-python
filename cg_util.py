"""
Helper modules for CGSN python scripts.
"""

def prompt_integer(user_prompt, bounds=None):
    """ 
    Prompts for user input, then validates that input is
    an integer and is in bounds. If bounds is not specified,
    then any integer will be valid.

    Params:
        user_prompt - Text to display to user
        bounds - list or range
    Returns:
        int
    """
    while True:
        try:
            user_response = int(input("%s " % user_prompt))
        except ValueError:
            print("Whoa! That's not a number.")
            continue
        if bounds is None:
            break
        if not user_response in bounds:
            print("Whoa! That's out of range.")
            continue
        break
    return user_response
