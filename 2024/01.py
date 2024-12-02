import re

def find_distance(entry_1, entry_2):
    entry_1_sorted = sorted(entry_1)
    entry_2_sorted = sorted(entry_2)

    distance_total = 0
    for i in range(len(entry_1_sorted)):
        distance = abs(entry_1_sorted[i] - entry_2_sorted[i])
        distance_total += distance

    return distance_total

def read_input(filename):
    tab_1 = [ ]
    tab_2 = [ ]
    with open(filename, 'r') as fileInput:
        ligne = fileInput.readline()
        while ligne:
            rx = r'([0-9]+) +([0-9]+)'
            match = re.match(rx, ligne)
            if match:
                int_1 = int(match.group(1))
                int_2 = int(match.group(2))
                tab_1.append(int_1)
                tab_2.append(int_2)
            ligne = fileInput.readline()

    return [ tab_1, tab_2 ]

tabs = read_input("01.test.input")
distance = find_distance(tabs[0], tabs[1])
print("\r")
print("\rDistance : " + str(distance))

tabs = read_input("01.input")
distance = find_distance(tabs[0], tabs[1])
print("\r")
print("\rDistance : " + str(distance))