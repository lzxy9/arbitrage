import re

def process_line_enhanced(line):
    # Remove "Yes"/"No" markers first
    line = line.replace(" Yes", "").replace(" No", "")
    
    names = find_names(line)
    print(names)
    odds = re.findall(r'\d+\.\d{2,3}', line)
    
    seen = set()
    unique_names = [n for n in names if not (n in seen or seen.add(n))]
    
    if len(unique_names) >= 2 and len(odds) >= 2:
        return f"{unique_names[0]} {unique_names[1]} {odds[0]} {odds[1]}"
    return line

def find_names(line):
    # Remove numbers
    line = ''.join(i.strip() for i in line if not i.isdigit()).strip("..\n")

    # List of names
    names = re.findall('[A-Z][^A-Z]*', line)

    # Remove duplicates
    seen = set()
    result = []
    for item in names:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result




with open("output.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = re.split(r'\d+\s*Markets?', line, maxsplit=1)
        # print(line[1])
        line = process_line_enhanced(line[1])
        # print(line)