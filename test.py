import re

def clean_names(arg):
    # Remove numbers
    newline = ''.join(i.strip() for i in arg if not i.isdigit()).strip("..\n")
    newline = newline.replace(".", "")

    # Split camelCase/PascalCase
    names = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', newline)

    # Handle text in brackets (ensure space before opening bracket if not already present)
    names = re.sub(r'(?<!\s)\(', ' (', names)
    names = names.split()

    # Remove 'fc' or 'FC' from start (^) or end ($) of the string (case-insensitive)
    removed_fc = []
    for elem in names:
        new_elem = re.sub(r'^fc|fc$', '', elem, flags=re.IGNORECASE)
        removed_fc.append(new_elem)

    # Remove empty strings
    result = [elem for elem in removed_fc if elem]

    return result

def process_line_enhanced(arg):
    # Remove "Yes"/"No" markers first
    arg = arg.replace(" Yes", "").replace(" No", "")

    
    names = find_names(arg)
    odds = re.findall(r'\d+\.\d{2,3}', arg)
    
    seen = set()
    unique_names = [n for n in names if not (n in seen or seen.add(n))]
    
    if len(unique_names) >= 2 and len(odds) >= 2:
        return f"{unique_names[0]} {unique_names[1]} {odds[0]} {odds[1]}"
    return arg

def find_names(arg):
    # Parse names
    names = clean_names(arg)

    # Remove duplicates
    seen = set()
    result = []
    for item in names:
        if item not in seen:
            seen.add(item)
            result.append(item)

    condensed_result = []
    for i in range(0, len(result) - 1, 2):
        condensed_result.append(result[i] + " " + result[i+1])
    print(condensed_result)
    return condensed_result

with open("output.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = re.split(r'\d+\s*Markets?', line, maxsplit=1)
        line = process_line_enhanced(line[1])
        # print(line)