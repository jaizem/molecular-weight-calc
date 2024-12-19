import re 

#load in periodic table
periodic_table = {}
with open('elements.txt', 'r') as file:
    for line in file:
        in_arr = line.strip().split('\t')
        periodic_table[in_arr[1]] = float(in_arr[2])

def calc_mol_weight(input):
    elements = {}

    def parse_formula(formula):
        #parse elements using regex
        pattern = r'([A-Z][a-z]?[a-z]?)(\d*)'
        matches = re.findall(pattern, formula)

        for element, quantity in matches:
            #set default qty to 1 if no number specified
            quantity = int(quantity) if quantity else 1
            if element in elements:
                elements[element] += quantity
            else:
                elements[element] = quantity

    formula = input
    parse_formula(formula)

    atomic_weight = 0

    for element in elements:
        atomic_weight += elements.get(element) * periodic_table.get(element)

    return atomic_weight