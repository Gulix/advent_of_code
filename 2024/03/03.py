import re

def add_uncorrupted_instructions(input_string):
    
    rx = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
    result = 0
    truc = re.findall(rx, input_string)
    for finding in re.findall(rx, input_string):
        val_1 = int(finding[0])
        val_2 = int(finding[1])
        result += val_1 * val_2
    return result

def with_conditional_inputs(input_string):
    start_index = 0
    end_index = input_string.find("don't()")
    final_result = 0
    while end_index != -1:
        final_result += add_uncorrupted_instructions(input_string[start_index:end_index])
        start_index = input_string.find("do()", end_index)
        end_index = input_string.find("don't()", start_index)

    final_result += add_uncorrupted_instructions(input_string[start_index:])
    return final_result


def read_input(filename):
    full_string = ''
    with open(filename, 'r') as fileInput:
        ligne = fileInput.readline()
        while ligne:
            full_string += ligne + '\n'
            ligne = fileInput.readline()

    return full_string

test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
expected_result = 161
result = add_uncorrupted_instructions(test_input)
print("\nTest sur la première instruction")
print(result)
print(expected_result == result)

full_input = read_input('03/03.input')
result = add_uncorrupted_instructions(full_input)
print("Avec le fichier d'input...\n")
print(result)

print("=================================\n\r")
print(" Avec les conditions ... \n\r")

test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
expected_result = 48
result = with_conditional_inputs(test_input)
print("\nTest sur la première instruction")
print(result)
print(expected_result == result)

result = with_conditional_inputs(full_input)
print("Avec le fichier d'input...\n")
print(result)