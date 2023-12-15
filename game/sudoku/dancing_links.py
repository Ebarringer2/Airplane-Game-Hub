# implementation of Donald Knuth's Dancing Links algorithm for solving the sudoku board.
# the paper is linked in README.md
import sys
import pygame
from random import randint 
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
                    