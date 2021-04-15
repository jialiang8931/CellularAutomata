import numpy as np
import time

def decimal2binary(integer):
    binary_string = format(integer, 'b')
    binary_string = binary_string.rjust(8, "0")
    return binary_string


class Cell:
    def __init__(self, states, rule):
        self.length = len(states)
        self.states = states
        self.rule = rule
        self.ruleset = decimal2binary(rule)
        return
    
    def next_generation(self):
        nextGeneration = self.states.copy()
        for i in range(1, self.length-1):
            left = self.states[i-1]
            midle = self.states[i]
            right = self.states[i+1]
            new_state = self.rules(left, midle, right)
            nextGeneration[i] = new_state
        return nextGeneration
    
    def rules(self, left, midle, right):
        condition = int("%i%i%i" %(left, midle, right), 2)
        new_state = int(self.ruleset[condition])
        return new_state
    
    def print_states(self):
        for i in range(0, self.length):
            if self.states[i] == 1: print('█', end='', sep='')
            if self.states[i] == 0: print('_', end='', sep='')
        print()
        return


states = np.zeros(101, dtype='int8')
states[len(states)//2] = 1
list_states = states.tolist()


for rule in range(177, 178):
	print("#"*20+"%03i" %rule+"#"*20)
	cells = Cell(list_states, rule)

	cells.print_states()
	for i in range(0, 60):
	    cells.states = cells.next_generation()
	    cells.print_states();
	    time.sleep(1)