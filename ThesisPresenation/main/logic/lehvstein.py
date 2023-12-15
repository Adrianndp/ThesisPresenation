from fuzzywuzzy import fuzz


def find_argument_value(kwargs, possible_names):
    """
    Find the value of an argument in kwargs using fuzzy string matching.
    """
    for name in possible_names:
        # Iterate through kwargs to find the best match for the current possible name
        best_match = max(kwargs.keys(), key=lambda key: fuzz.ratio(name.lower(), key.lower()))

        # If the match ratio is above a certain threshold, consider it a match
        if fuzz.ratio(name.lower(), best_match.lower()) > 80:  # Adjust the threshold as needed
            return kwargs[best_match]

    # Return None if the argument is not found
    return None


# Example usage:
args = {"Start": "value1", "startTime": "value2", "start_time": "value3", "start_date": "value4"}

# Define a list of possible names for the "start" argument
possible_start_names = ["start", "startTime", "start_time", "start_date"]

# Find the value of "start" using fuzzy string matching
start_value = find_argument_value(args, possible_start_names)

if start_value is not None:
    print("start value:", start_value)
else:
    print("start not found in args.")
