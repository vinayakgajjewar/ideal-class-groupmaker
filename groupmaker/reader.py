import sys

def get_class_prefs(path_to_file):
    # Function to read text file containing class preferences and return it as a
    # dict

    # Define it now
    prefs_dict = []

    with open(sys.argv[1], "r") as file:

        # Loop over the file line by line
        for line in file:
            # rstrip() removes the trailing newline
            prefs_dict.append(line.rstrip())


    return prefs_dict
