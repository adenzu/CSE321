from collections import defaultdict
import numpy as np
import time

### QUESTION 1 ###
class Graph:
    def __init__(self):
        self.connections = defaultdict(set)
        self.reverseConnections = defaultdict(set)
        self.outdegrees = set()
    
    def addEdge(self, fromNode, toNode):
        self.outdegrees.add(toNode)
        if fromNode in self.outdegrees:
            self.outdegrees.remove(fromNode)
        self.connections[fromNode].add(toNode)
        self.reverseConnections[toNode].add(fromNode)

class DepthFirstSearchTopologicalSorter:
    def __init__(self, graph):
        self.visited = defaultdict(lambda: False)
        self.toplogicalOrder = list()
        for outdegree in graph.outdegrees:
            self.toplogicalOrder = self.toplogicalOrder + self.__getTopologicalOrder(outdegree, graph.reverseConnections)
    
    def __str__(self):
        return "->".join(self.toplogicalOrder)

    def __getTopologicalOrder(self, currentNode, reverseConnections):
        if self.visited[currentNode]:
            return []
        self.visited[currentNode] = True
        order = list()
        for node in reverseConnections[currentNode]:
            order = self.__getTopologicalOrder(node, reverseConnections) + order
        order.append(currentNode)
        return order

class NonDepthFirstSearchTopologicalSorter:
    def __init__(self, graph):
        pass
### QUESTION 1 ###

### QUESTION 2 ###
def pow(a, n):
    if n == 0:
        return 1
    elif n % 2:
        return a * pow(a, n // 2) * pow(a, n //2)
    else:
        return pow(a, n // 2) * pow(a, n //2) 
### QUESTION 2 ###

### QUESTION 3 ###
class Sudoku:
    def __init__(self):
        self.width = 9
        self.height = 9
        self.values = np.zeros((self.width, self.height), dtype=int) - 1
    
    def __str__(self):
        result = ""
        for i in range(self.height):
            for j in range(self.width):
                result += f"{self.values[i, j] if self.values[i, j] != -1 else ' '}"
            result += "\n"
        return result
    
    def put(self, value, row, column):
        self.values[column, row] = value
    
    def get(self, row, column):
        return self.values[row, column]

    def size(self):
        return self.width * self.height
    
    def copy(self):
        copySudoku = Sudoku()
        copySudoku.values = self.values.copy()
        return copySudoku

class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.sudokuCopy = sudoku.copy()

    def solve(self):
        self.__solve(0)
        
    def __solve(self, index):
        if index >= self.sudokuCopy.size():
            return self.__checkSolved()
        
        row = index // self.sudokuCopy.width
        column = index % self.sudokuCopy.width

        for i in range(9):
            if self.sudoku.get(row, column) == -1:           
                self.sudokuCopy.put(i + 1, row, column)
            if self.__solve(index + 1):
                return True
        
        return False

    def __checkSolved(self):
        print(self.sudokuCopy)
        for row in range(self.sudoku.height):
            for column in range(self.sudoku.width):
                if self.sudoku.get(row, column) != -1 and self.sudoku.get(row, column) != self.sudokuCopy.get(row, column):
                    return False

        if not (np.sum(self.sudokuCopy.values, axis=0) == 45).all():
            return False
            
        if not (np.sum(self.sudokuCopy.values, axis=1) == 45).all():
            return False
        
        for row in range(self.sudoku.height):
            for column in range(self.sudoku.width):
                if np.sum(self.sudokuCopy[row * 3 : (row + 1) * 3, column * 3 : (column + 1) * 3]) != 45:
                    return False

        return True

    def getSolved(self):
        return self.sudokuCopy

        


### QUESTION 3 ###

def main():
    # Question 1
    graph = Graph()
    print("Enter two things (numbers, words, symbols etc.) that are seperated by a space to enter an edge from left input to right input:")
    print("(Enter blank line to exit)")
    while True:
        last_input = input()
        if last_input == "":
            break
        n1, n2 = last_input.split()
        graph.addEdge(n1, n2)
    print("Result of DFS based topological sorting algorithm: ")
    print(DepthFirstSearchTopologicalSorter(graph))

    # Question 2
    print("Enter two numbers seperated by space to get first number to the power of second number:")
    print("(Enter blank line to exit)")
    while True:
        last_input = input()
        if last_input == "":
            break
        n1, n2 = [int(i) for i in last_input.split()]
        print(f"Result: {pow(n1, n2)}")

    # Question 3
    sudoku = Sudoku()
    print("Enter three numbers where first two are the row and column indeces of the third number to be put on sudoku:")
    print("(Enter blank line to exit)")
    while True:
        last_input = input()
        if last_input == "":
            break
        n1, n2, n3 = [int(i) for i in last_input.split()]
        sudoku.put(n3, n1, n2)
    print("Sudoku solving algorithm will start in 5 seconds, it prints a lot so its stopped for you to check prior prints")
    print("The sudoku solver algorithm is too bad to use practically but you can see it working:")
    time.sleep(5)    
    SudokuSolver(sudoku).solve()

if __name__ == "__main__":
    main()
