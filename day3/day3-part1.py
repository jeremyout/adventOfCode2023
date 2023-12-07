# input_file = open("input.txt", "r")
input_file = open("example_input.txt", "r")

symbol_list = ["!", "@", "#", "$", "%", "^", "&", "(", ")", "*", "-", "+", "=", "/"]
symbol_index_to_process = []
valid_engine_numbers = []
line_data = input_file.readlines()

def getNumberOfSymbolsInLine(current_line_content):
    symbol_counter = 0
    for index,char in enumerate(current_line_content):
        if char in symbol_list:
            print(f"{char} symbol found at index: {index} on line: {line_number}")
            symbol_index_to_process.append(index)
            symbol_counter += 1
    return symbol_counter

def getAdjacentAndDiagonalCharacters(line_number_with_symbol, index_of_symbol):
    char_directly_above = ""
    upper_left_diagonal = ""
    upper_right_diagonal = ""
    char_directly_below = ""
    lower_left_diagonal = ""
    lower_right_diagonal = ""
    left_char = ""
    right_char = ""

    left_char = line_data[line_number_with_symbol]
    left_char = left_char[index_of_symbol-1]
    print(f"Left char: {left_char}")

    right_char = line_data[line_number_with_symbol]
    right_char = right_char[index_of_symbol+1]
    print(f"Right char: {right_char}")

    line_directly_above = getPreviousLine(line_number_with_symbol)
    
    if line_directly_above != "":
        char_directly_above = line_directly_above[index_of_symbol]
        print(f"Char directly above: {char_directly_above}")
        upper_left_diagonal = getUpperLeftDiagonal(line_directly_above, index_of_symbol)
        print(f"Upper left diagonal: {upper_left_diagonal}")
        upper_right_diagonal = getUpperRightDiagonal(line_directly_above, index_of_symbol)
        print(f"Upper right diagonal: {upper_right_diagonal}")

    line_directly_below = getNextLine(line_number_with_symbol)

    if line_directly_below != "":
        char_directly_below = line_directly_below[index_of_symbol]
        print(f"Char directly below: {char_directly_below}")
        lower_left_diagonal = getLowerLeftDiagonal(line_directly_below, index_of_symbol)
        print(f"Lower left diagonal: {lower_left_diagonal}")
        lower_right_diagonal = getLowerRightDiagonal(line_directly_below, index_of_symbol)
        print(f"Lower right diagonal: {lower_right_diagonal}")

    return left_char, right_char, char_directly_above, upper_left_diagonal, upper_right_diagonal, char_directly_below, lower_left_diagonal, lower_right_diagonal
    

def getPreviousLine(current_line_index):
    if current_line_index == 0:
        return ""
    else:
        return line_data[current_line_index-1]
    
def getUpperLeftDiagonal(previous_line, index_of_symbol):
    if index_of_symbol == 0:
        return ""
    else:
        return previous_line[index_of_symbol-1]
    
def getUpperRightDiagonal(previous_line, index_of_symbol):
    if index_of_symbol == len(previous_line):
        return ""
    else:
        return previous_line[index_of_symbol+1]

    
def getNextLine(current_line_index):
    if current_line_index == len(line_content):
        return ""
    else:
        return line_data[current_line_index+1]
    
def getLowerLeftDiagonal(next_line, index_of_symbol):
    if index_of_symbol == 0:
        return ""
    else:
        return next_line[index_of_symbol-1]
    
def getLowerRightDiagonal(next_line, index_of_symbol):
    if index_of_symbol == len(next_line):
        return ""
    else:
        return next_line[index_of_symbol+1]

print("==========================================")
for line_number,line_content in enumerate(line_data):
    symbols_processed = 0
    symbols_in_line = getNumberOfSymbolsInLine(line_content)
    if symbols_in_line != 0:
        if (symbols_in_line == 1):
            print(f"There is {symbols_in_line} symbol in line number {line_number}")
            getAdjacentAndDiagonalCharacters(line_number, symbol_index_to_process.pop())
        else:
            print(f"There are {symbols_in_line} symbols in line number {line_number}")
            while(len(symbol_index_to_process)):
                index_to_check = symbol_index_to_process.pop()
                print(f"Processing the {line_content[index_to_check]} symbol now, from index {index_to_check}")
                getAdjacentAndDiagonalCharacters(line_number, index_to_check)
    else:
        print(f"There are no symbols in line number {line_number}")
    print("==========================================")
