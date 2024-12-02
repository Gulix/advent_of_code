import re

def read_input(filename):
    levels = [ ]
    with open(filename, 'r') as fileInput:
        ligne = fileInput.readline()
        while ligne:
            split_ligne = ligne.split(' ')
            level = [ ]
            for item in split_ligne:
                level.append(int(item))

            levels.append(level)

            ligne = fileInput.readline()

    return levels

def get_secure_levels(levels):
    secure_levels = [ ]
    for level in levels:
        if is_level_secure(level):
            secure_levels.append(level)
    
    return secure_levels

def is_level_secure(level):
    ## On parcourt le level en vérifiant la règle
    sens = None
    last_good_item = level[0]
    if last_good_item > level[1]:
        sens = -1 # On descend de step en step
    elif last_good_item < level[1]:
        sens = 1
    else:
        return False # Not a secure level
    
    is_safe = True
    for index in range(1, len(level)):
        if sens == -1: ## Décrément, on descend
            diff = last_good_item - level[index]
        elif sens == 1: ## Incrément, on monte
            diff = level[index] - last_good_item
        if diff > 3 or diff < 1:
            is_safe = False
            break
        else:
            last_good_item = level[index]

    return is_safe

def get_secure_levels_part2(levels):
    ## Ici, on peut avoir un élément dans un niveau qu'on supprime
    secure_levels = [ ]
    for level in levels:
        is_secure = is_level_secure(level)

        if not is_secure:
            for index in range(len(level)):
                corrected_level = level.copy()
                corrected_level.pop(index)
                if is_level_secure(corrected_level):
                    is_secure = True
                    break
                                
        if is_secure:
            secure_levels.append(level)
    
    return secure_levels

print("======= Sans le Problem Dampener =========\r\n")
print("\n")
levels = read_input("02/02.test.input")
secure_levels = get_secure_levels(levels)
print("Nb Levels Secure : " + str(len(secure_levels)))

print("\r\n")
levels = read_input("02/02.input")
secure_levels = get_secure_levels(levels)
print("Nb Levels Secure : " + str(len(secure_levels)))

print("======= Sans le Problem Dampener =========\r\n")
print("\r\n")
print("======= Avec le Problem Dampener =========\r\n")
print("\n")
levels = read_input("02/02.test.input")
secure_levels = get_secure_levels_part2(levels)
print("Nb Levels Secure : " + str(len(secure_levels)))

print("\r\n")
levels = read_input("02/02.input")
secure_levels = get_secure_levels_part2(levels)
print("Nb Levels Secure : " + str(len(secure_levels)))