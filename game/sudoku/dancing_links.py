# implementation of Donald Knuth's Dancing Links algorithm for solving the sudoku board.
# the paper is linked in README.md
import sys
import pygame
from random import randint
from game.sudoku.sudoku_class import Sudoku
# class to represent a node in the dancing links algorithm
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = self 
        self.right = self
        self.up = self 
        self.down = self 
# class for the algorithm
class DancingLinks:
    def __init__(self, grid):
        self.header = self.create_linked_matrix(grid)
        self.solution = []
    def create_linked_matrix(self, grid):
        header = Node()
        columns = []
        # create column headers
        for j in range(9 * 9 * 4):
            column = Node(j)
            columns.append(column)
            column.left = header.left 
            column.right = header 
            header.left.right = column 
            header.left = column 
        for i in range(9):
            for j in range(9):
                for num in range(1, 10):
                    idx = self.get_index(i, j, num)
                    row = Node(idx)
                    columns[idx].up.down = row
                    row.up = columns[idx].up
                    row.down = columns[idx]
                    columns[idx].up = row
                    # connect to the left
                    row.left = row
                    prev_row = row 
                    for k in range(1, 10):
                        idx = self.get_index(i, j, k)
                        node = Node(idx)
                        prev_row.right = node 
                        node.left = prev_row 
                        node.up = columns[idx].up 
                        node.down = columns[idx]
                        columns[idx].up.down = node 
                        columns[idx].up = node 
                        prev_row = node 
        return header 
    def get_index(self, i, j, num):
        return i * 81 + j * 9 + num - 1
    def select_column(self):
        min_size = float('inf')
        selected_column = None 
        current = self.header.right 
        while current != self.header:
            if current.value < min_size:
                min_size = current.value 
                selected_column = current
            current = current.right 
        return selected_column 
    def cover(self, column):
        column.right.left = column.left 
        column.left.right = column.right 
        current_row = column.down 
        while current_row != column:
            current_node = current_row.right 
            while current_node != current_row:
                current_node.down.up = current_node.up
                current_node.up.down = current_node.down 
                current_node = current_node.right 
            current_row = current_row.down 
    def uncover(self, column):
        current_row = column.up 
        while current_row != column:
            current_node = current_row.left 
            while current_node != current_row:
                current_node.down.up = current_node 
                current_node.up.down = current_node 
                current_node = current_node.left 
            current_row = current_row.up 
        column.right.left = column 
        column.left.right = column 
    def search(self, k):
        if self.header.right == self.header:
            return True 
        column = self.select_column()
        self.cover(column)
        current_row = column.down 
        while current_row != column:
            self.solution.append(current_row.value)
            current_node = current_row.right 
            while current_node != current_row:
                self.cover(self.header.right)
                current_node = current_node.right 
            if self.search(k + 1):
                return True 
            current_node = current_row.left 
            while current_node != current_row:
                self.uncover(self.header.left)
                current_node = current_node.left 
            self.solution.pop()
            current_row = current_row.down 
        self.uncover(column)
        return False 
    def solve(self):
        self.solution = []
        return self.search(0)
# application of dancing links class to sudoku
class SudokuSolver(Sudoku):
    def __init__(self, sudoku : Sudoku):
        self.sudoku = Sudoku
    def extract_solution(self, solution):
        result = [[0] * 9 for _ in range(9)]
        for idx in solution:
            num, i, j = divmod(idx, 81), divmod(idx % 81, 9)
            result[i][j] = num + 1 
        return result
    '''def sudoku_solver_run(self):
        self.running = True
        self.sudoku.solver = DancingLinks(self.sudoku.grid)
        while self.running:'''
