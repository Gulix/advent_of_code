def read_input(filename, obstacles, size, start):

    lignes = [ ]
    with open(filename, 'r') as file_input:
        lignes = file_input.readlines()
        
    size['x'] = len(lignes[0])
    size['y'] = len(lignes)

    for y in range(len(lignes)):
        for x in range(len(lignes[y])):
            if lignes[y][x] == '#':
                obstacles.append({ 'x': x, 'y': y })
            if lignes[y][x] == '^':
                start['x'] = x
                start['y'] = y

def get_cases_visitees(filename):
    obstacles = [ ]
    size = dict()
    start = dict()

    read_input(filename, obstacles, size, start)
    cases_visitees = [ ]
    cases_visitees.append(str(start['x']) + ";" + str(start['y']))
    out_of_bounds = False
    direction_x = 0
    direction_y = -1
    current_x = start['x']
    current_y = start['y']
    while not out_of_bounds:
        new_x = current_x + direction_x
        new_y = current_y + direction_y
        # Y a-t-il un obstacle ?
        if { 'x': new_x, 'y': new_y } in obstacles:
            ## On tourne
            if direction_x != 0:
                direction_y = direction_x
                direction_x = 0
            elif direction_y != 0:
                direction_x = direction_y * -1
                direction_y = 0
            ## Nouvelle direction
            new_x = current_x + direction_x
            new_y = current_y + direction_y

        ## Out of bounds ?
        if new_x < 0 or new_x >= size['x'] or new_y < 0 or new_y >= size['y']:
            out_of_bounds = True
            continue

        current_x = new_x
        current_y = new_y
        ## Ajouter la case visitée
        str_case = str(new_x) + ";" + str(new_y)
        if str_case not in cases_visitees:
            cases_visitees.append(str_case)

    return len(cases_visitees)

print("Test du Jour 6")
print("Sur le jeu de test (attendu 41)")
nb = get_cases_visitees("06/06.test.input")
print(nb)

print("Sur le jeu complet")
nb = get_cases_visitees("06/06.input")
print(nb)