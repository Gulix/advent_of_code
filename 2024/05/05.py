def read_input(filename, rules, prints):
    ## rules is a dict()
    ## prints is a list of lists
    
    with open(filename, 'r') as fileInput:
        ligne = fileInput.readline()
        is_rules = True
        while ligne:
            if ligne == '\n':
                is_rules = False
                ligne = fileInput.readline()
                continue

            ligne = ligne.replace('\n', '')
            if is_rules:
                elements = ligne.split('|')
                key = elements[0]
                if key in rules.keys():
                    rules[key].append(elements[1])
                else:
                    rules[key] = [ elements[1] ]
            else:
                elements = ligne.split(',')
                prints.append(elements)

            ligne = fileInput.readline()

def check_print_line(print_line, rules):
    
    previous_pages = [ ]
    for page in print_line:
        if len(previous_pages) > 0:
            if page in rules.keys():
                for rule in rules[page]:
                    if rule in previous_pages:
                        return -1
        previous_pages.append(page)
    
    middle = int(print_line[int((len(print_line) - 1) / 2)])
    return middle

def is_line_incorrect(print_line, rules):
        
    previous_pages = [ ]
    for page in print_line:
        if len(previous_pages) > 0:
            if page in rules.keys():
                for rule in rules[page]:
                    if rule in previous_pages:
                        return True
        previous_pages.append(page)
    
    return False

def correct_line(print_line, rules):

    page_ref = dict()
    for page in print_line:
        if page in rules.keys():
            page_rule = [ ]
            for rule in rules[page]:
                if rule in print_line:
                    page_rule.append(rule)
            page_ref[page] = page_rule
        else:
            page_ref[page] = [ ]

    sorted_line = sorted(page_ref.items(), key=lambda item: len(item[1]))

    middle = int(sorted_line[int((len(sorted_line) - 1) / 2)][0])
    return middle

def get_weight(page, rules, print_line):
    weight = 1
    if page not in rules.keys():
        return 1
    children_pages = rules[page]
    for child_page in children_pages:
        if child_page in print_line:
            weight += get_weight(child_page, rules, print_line)
    
    return weight

def get_answer(filename):
    rules = dict()
    print_lines = [ ]
    read_input(filename, rules, print_lines)
    sum = 0
    for print_line in print_lines:
        val = check_print_line(print_line, rules)
        if val > -1:
            sum += val
    
    return sum

def get_answer_second(filename):
    rules = dict()
    print_lines = [ ]
    read_input(filename, rules, print_lines)
    sum = 0
    for print_line in print_lines:
        if is_line_incorrect(print_line, rules):
            val = correct_line(print_line, rules)
            sum += val
    
    return sum

print("Démarrage sur la première partie")
answer = get_answer("05/05.test.input")
print("Réponse (attendue 143): " + str(answer))
print("Et sur le véritable fichier ...")
answer = get_answer("05/05.input")
print("Réponse : " + str(answer))

print("=================")
print("Démarrage sur la seconde partie")
answer = get_answer_second("05/05.test.input")
print("Réponse (attendue 123): " + str(answer))
print("Et sur le véritable fichier ...")
answer = get_answer_second("05/05.input")
print("Réponse : " + str(answer))