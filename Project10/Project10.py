with open('Project10/puzzle.txt', 'r') as f:
    text = [line.strip() for line in f]

class Machine:
    def __init__(self, input_lights, input_buttons):
        self.target_lights = list(input_lights)
        self.buttons = input_buttons

    def solve(self):
        dimension = 0
        while True:
            dimension += 1

            # get our combinations
            combinations = self._getCombinations(dimension)

            # try each one and see if it solves
            current_lights = ['.' for _ in input_lights]
            for combo in combinations:
                for i in range(0, len(current_lights)):
                    current_lights[i] = '.'

                for press in combo:
                    self._press(current_lights, press)
                if current_lights == self.target_lights:
                    return dimension

    def _getCombinations(self, dimension):
        combinations = []
        combo = [0 for _ in range(0, dimension)]
        for i in range(0, len(self.buttons)**dimension):            
            combinations.append(combo.copy())
            combo[dimension-1] += 1
            for j in range(dimension - 1, 0, -1):
                if combo[j] == len(self.buttons):
                    combo[j-1] += 1
                    combo[j] = 0
        return combinations

    def _press(self, lights, press):
        for i in self.buttons[press]:
            if lights[i] == '.':
                lights[i] = '#'
            else:
                lights[i] = '.'

sum = 0
for line in text:
    sections = line.split(' ')
    input_lights = ''
    input_buttons = []
    for section in sections:
        if section[0] == '[':
            input_lights = section.strip('[').strip(']')
        elif section[0] == '(':
            input_buttons.append(list(map(int, section.strip('(').strip(')').split(','))))
    sum += Machine(input_lights, input_buttons).solve()

print(f"Final sum: {sum}")