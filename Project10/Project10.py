import math

epsilon = 0.001

with open('Project10/puzzle.txt', 'r') as f:
    text = [line.strip() for line in f]

class Machine:
    def __init__(self, input_joltage, input_buttons):
        self.target_joltage = input_joltage
        self.buttons = input_buttons

    def solve(self):
        # convert all these equations to matrix form
        matrix = []
        for i in range(0, len(self.target_joltage)):
            equation = [0 for _ in self.buttons]
            equation.append(self.target_joltage[i])
            matrix.append(equation)
        
        for i, button in enumerate(self.buttons):
            for digit in button:
                matrix[digit][i] = 1

        # apply row reduction (via gaussian elimination)
        matrix = self._reduce(matrix)

        # remove any zero rows
        for i in range(len(matrix) - 1, -1, -1):
            if all(n == 0 for n in matrix[i]):
                matrix.pop(i)

        # identify free variables (can do this by seeing if we only have a single 1 and the rest 0 in a column)
        free_var = []
        for col in range(0, len(matrix[0])-1):
            free = False
            num_one = 0
            num_zero = 0

            for row in range(0, len(matrix)):
                if matrix[row][col] == 1.0:
                    num_one += 1
                elif matrix[row][col] == 0.0:
                    num_zero += 1
                else:
                    free = True
                    break
            
            if not free:
                if num_one != 1 or num_zero != len(matrix) - 1:
                    free = True

            if free:
                free_var.append(col)

        # negate the other vars for solving (since a+b+c=d => a=d-b-c)
        for i, row in enumerate(matrix):
            for j in range(row.index(1.0) + 1, len(matrix[0])-1):
                if matrix[i][j] != 0.0:
                    matrix[i][j] = -matrix[i][j]

        # now see if we can find a min solution by pressing these
        press_counter = [0 for _ in free_var]
        min_sum = math.inf
        max_presses = max(self.target_joltage)
        while True:
            results = 0
            valid = True

            # add our free vars to the result
            for x in press_counter:
                results += x
            
            # solve (and check for overflow)
            for row in matrix:
                result_row = row.copy()
                for i, x in enumerate(free_var):
                    result_row[x] *= press_counter[i]

                v = result_row.index(1.0)
                result = 0
                for i in range(v+1, len(matrix[0])):
                    result += result_row[i]

                # we found an invalid result, so stop processing
                if result < -epsilon or abs(result - round(result)) > epsilon:
                    valid = False
                    break

                results += result

            # see if we have a new valid min result
            if valid and results < min_sum:
                min_sum = round(results)

            # if we don't have any free vars, then this is our solution
            if len(press_counter) == 0:
                break

            # otherwise, let's try the next combination
            press_counter[0] += 1
            for i in range(len(press_counter)-1):
                if press_counter[i] > max_presses:
                    press_counter[i] = 0
                    press_counter[i+1] += 1
            
            # stop if we've done them all
            if press_counter[-1] > max_presses:
                break

        return int(min_sum)
    
    def _reduce(self, matrix):
        # https://en.wikipedia.org/wiki/Gaussian_elimination#Pseudocode (with modifications to make it Gauss-Jordan)
        row = 0
        col = 0
        while row < len(matrix) and col < len(matrix[0]):
            i_max = max(range(row, len(matrix)), key=lambda x: abs(matrix[x][col]))
            if matrix[i_max][col] == 0:
                # no pivot in this column, pass to next column
                col += 1
            else:
                matrix[row], matrix[i_max] = matrix[i_max], matrix[row] # swap rows

                # divide the row by the pivot
                p = matrix[row][col]
                for j in range(col, len(matrix[0])):
                    matrix[row][j] /= p
                
                # annilate entries above and below the pivot
                for i in range(0, len(matrix)):
                    if i != row:
                        f = matrix[i][col] / matrix[row][col]
                        matrix[i][col] = 0.0
                        for j in range(col+1, len(matrix[0])):
                            matrix[i][j] = matrix[i][j] - matrix[row][j] * f

                # fix any numerical instability
                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        if abs(matrix[i][j] - round(matrix[i][j])) < epsilon:
                            matrix[i][j] = round(matrix[i][j])

                row += 1
                col += 1

        return matrix

results_sum = 0
for i, line in enumerate(text):
    sections = line.split(' ')
    input_joltage = []
    input_buttons = []
    for section in sections:
        if section[0] == '{':
            input_joltage = list(map(int, section.strip('{').strip('}').split(',')))
        elif section[0] == '(':
            input_buttons.append(list(map(int, section.strip('(').strip(')').split(','))))
    results_sum += Machine(input_joltage, input_buttons).solve()

print(f"Final sum: {results_sum}")