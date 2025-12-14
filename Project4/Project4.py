with open('Project4/puzzle.txt', 'r') as f:
    text = [list(line.strip()) for line in f]

paper = '@'
max_row = len(text) - 1
max_column = len(text[0]) - 1
total = 0
removed = True

while removed:
    removed = False
    for row_index, row in enumerate(text):
        for col_index, value in enumerate(row):
            count = 0

            # check all adjacent squares
            if value == paper:
                if row_index > 0:
                    if col_index > 0:
                        count = count + 1 if text[row_index - 1][col_index - 1] == paper else count
                    count = count + 1 if text[row_index - 1][col_index] == paper else count
                    if col_index < max_column:
                        count = count + 1 if text[row_index - 1][col_index + 1] == paper else count
                if col_index > 0:
                    count = count + 1 if text[row_index][col_index - 1] == paper else count
                if col_index < max_column:
                    count = count + 1 if text[row_index][col_index + 1] == paper else count
                if row_index < max_row:
                    if col_index > 0:
                        count = count + 1 if text[row_index + 1][col_index - 1] == paper else count
                    count = count + 1 if text[row_index + 1][col_index] == paper else count
                    if col_index < max_column:
                        count = count + 1 if text[row_index + 1][col_index + 1] == paper else count
            
                if count < 4:
                    total += 1
                    text[row_index][col_index] = '.'
                    removed = True
                    
    #print(f"DEBUG: Removed total of {total}")

print(total)