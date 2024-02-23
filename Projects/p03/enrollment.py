"""Enrollment analysis:  Summary report of majors enrolled in a class.
CS 210 project, Fall 2022.
Author:  Owen Ferguson
Credits:
"""
import doctest
import csv

def read_csv_column(path: str, field: str) -> list[str]:
    """Read one column from a CSV file with headers into a list of strings.

    >>> read_csv_column("data/test_roster.csv", "Major")
    ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
    """
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        majors = []
        for row in reader:
            majors += [row[field]]
        
    return majors
            
def counts(column: list[str]) -> dict[str, int]:
    """Returns a dict with counts of elements in column.

    >>> counts(["dog", "cat", "cat", "rabbit", "dog"])
    {'dog': 2, 'cat': 2, 'rabbit': 1}
    """
    # Initialize accumulator variables
    result_dict = {} # To be returned
    count_list = [] # To keep track of keys already seen
    for line in column:
        if line in count_list: # If we've seen this key before already
            result_dict[line] += 1 # Update count associated with key
        else:
            count_list += [line] # Add key to count list
            result_dict.update({line:1}) # Update final dictionary to include this key, and begin counter at 1
    
    return result_dict

def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
    """Read a CSV with column headers into a dict with selected
    key and value fields.

    >>> read_csv_dict("data/test_programs.csv", key_field="Code", value_field="Program Name")
    {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
    """
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        final_dict = {}
        keys = []
        values = []
        for row in reader:
            keys += [row[key_field]]
            values += [row[value_field]]
        
        for key in keys:
            for value in values:
                final_dict[key] = value
                values.remove(value)
                break
        
    return final_dict

def items_v_k(counts):
    '''Returns a list of (value, key) pairs for any dictionary'''
    by_count = []
    for code, count in counts.items():
        pair = (count, code)
        by_count.append(pair)

    return by_count

def main():
    doctest.testmod()
    majors = read_csv_column("data/roster_selected.csv", "Major")
    counts_by_major = counts(majors)
    program_names = read_csv_dict("data/programs.csv", "Code", "Program Name")
    # --- Next line replaces several statements
    by_count = items_v_k(counts_by_major)
    # ---  
    by_count.sort(reverse=True)  # From largest to smallest
    for count, code in by_count:
        program = program_names[code]
        print(count, program)

if __name__ == "__main__":
    main()