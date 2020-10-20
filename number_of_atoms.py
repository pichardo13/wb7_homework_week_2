"""
Given a chemical formula (given as a string), return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, 
no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), 
followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count 
(if that count is more than 1), and so on.

Example 1:
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Example 4:
Input: formula = "Be32"
Output: "Be32"
"""
#step 1: parse through the string
#step 2: make a stack, if '(' add the following into the stack 
#step 3: if ')', get the next item as it should be a number
#step 4: pop from stack, as poping add to the dictionary and multiply by number

from collections import defaultdict
def countOfAtoms(formula):
    l = len(formula)
    stack = []
    atoms = defaultdict(int)
    i = 0 
    while i < l:
        j = i + 1
        if formula[i].isupper():
            while j < l and formula[j].islower():
                j += 1
            elem = formula[i:j]
            if j == l or not formula[j].isdigit():
                atoms[elem] += 1
        elif formula[i].isdigit():
            while j < l and formula[j].isdigit():
                j += 1
            atoms[elem] = int(formula[i:j])
        elif formula[i] == '(':
            while j < l and formula[j] != ')':
                stack.append(formula[j])
                j += 1
        elif formula[i] == ')':
            while j < l and formula[j].isdigit():
                j += 1
            num = int(formula[i+1: j])

            while stack:
                e = stack.pop()
                elem = ''
                while e.islower():
                    elem = e + elem
                    e = stack.pop()
                elem = e + elem
                if elem not in atoms:
                    atoms[elem] = num
                else:
                    atoms[elem] *= num
        i = j   
    return atoms


