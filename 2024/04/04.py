def read_input(filename):
    lines = [ ]
    with open(filename, 'r') as fileInput:
        ligne = fileInput.readline()
        while ligne:
            line = list(ligne)
            if line[len(line) - 1 ] == "\n":
                line.remove("\n")
            lines.append(line)

            ligne = fileInput.readline()

    return lines

def find_nb_words_in_matrix(matrix, word_to_find):
    nb_result = 0

    # On parcourt la matrice, case par case. 
    # Si la case correspond au premier caractère du mot à trouver, 
    # on file en étoile pour chercher dans les huit directions
    char_to_find = word_to_find[0]
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == char_to_find:
                nb_word = find_words_from_point(matrix, x, y, word_to_find)
                nb_result += nb_word
    
    return nb_result

def find_words_from_point(matrix, x_start, y_start, word):
    directions = [ { 'x': -1, 'y': -1 }, { 'x': 0, 'y': -1 }, { 'x': 1, 'y': -1 }, 
                  { 'x': -1, 'y': 0 },{ 'x': 1, 'y': 0 },
                  { 'x': -1, 'y': 1 },{ 'x': 0, 'y': 1 },{ 'x': 1, 'y': 1 }]
       
    result = 0
    for direction in directions:
        current_x = x_start
        current_y = y_start
        word_is_good = True
        for char in word:
            # Out of bounds ?
            if current_x < 0 or current_y < 0 or current_y >= len(matrix) or current_x >= len(matrix[current_y]):
                word_is_good = False
                break
            if matrix[current_y][current_x] != char:
                word_is_good = False
                break
            current_x += direction['x']
            current_y += direction['y']
        
        if word_is_good:
            result += 1

    return result
            
def find_xmas_in_matrix(matrix):
    nb_result = 0

    # On parcourt la matrice, case par case. 
    # On cherche un A
    # Si c'est le cas, on regarde s'il fait partie d'une étoile 
    char_to_find = "A"
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == char_to_find:
                if is_xmas(matrix, x, y):
                    nb_result += 1
    
    return nb_result

def is_xmas(matrix, x, y):
    # Out of bounds ?
    if x < 1 or y < 1 or y >= len(matrix) -1 or x >= len(matrix[y]) - 1:
        return False
    
    nw_se = matrix[y-1][x-1] + matrix[y][x] + matrix[y+1][x+1]
    ne_sw = matrix[y-1][x+1] + matrix[y][x] + matrix[y+1][x-1]
    return (nw_se == "MAS" or nw_se == "SAM") and (ne_sw == "MAS" or ne_sw == "SAM")
    


print("Démarrage des tests !")
matrix = read_input("04/04.test.input")
result = find_nb_words_in_matrix(matrix, "XMAS")
print("Sur le jeu de tests...\n\r")
print(result)

matrix = read_input("04/04.input")
result = find_nb_words_in_matrix(matrix, "XMAS")
print("Sur les bonnes données...\n\r")
print(result)

print("Deuxième partie - XMAS CROSS !")
matrix = read_input("04/04.test.input")
result = find_xmas_in_matrix(matrix)
print("Sur le jeu de tests...\n\r")
print(result)

matrix = read_input("04/04.input")
result = find_xmas_in_matrix(matrix)
print("Sur les bonnes données...\n\r")
print(result)