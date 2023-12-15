# implementation of Donald Knuth's Dancing Links algorithm for solving the sudoku board.
# the paper is linked in README.md
'''
#### EXPLANATION OF DANCING LINKS ####

# Spare matrix representation

for the sake of understanding the algorithm, let a given problem be presented by a matrix A
of 1s and 0s, where each row corresponds to a constraint and each column corresponds to an element
or requirement

introduce a doubly linked list for each column, representing the column header. These column
headers are interconnected to form a circular doubly linked list 

Each 1 in the matrix is represented by a node, belonging to both a row-linked list 
and a column-linked list. these nodes for a toroidal structure 

# Dancing links structure 

the column header node contains metadata about the column, such as the column name, size, and pointers
to adjacent columns 

each node contains pointers to its neighbors in the row and column. these pointers facilitate efficient 
covering and uncovering operations

# Exact cover problem 

the goal here is to find a subset of rows such that each column has exactly one 1 in the chosen subset. 
this is the basis of an exact cover problem 

the covering operation involves removing a column and all nodes in its column-linked list. this is
achieved by updating the adjacent pointers appropriately 

# Algorithm operations

a heuristic is used to select as column for covering. this can be based on the column size or other criteria
the goal is to minimize the branching factor 

the algorithm uses recurvise depth-first search. after selecting a column to cover, it explores the 
possibilities and backtracks if a dead-end is reached

backtracking involves uncovering the last covered column and continuing the search. this process is repeated
until a solution is found or all possibilities are explored 

# Algorithm termination

the alggorithm terminates when all columns are covered, indicating that a valid solution has been found.
multiple solutions can be found by continuing the search

# Complexity Analysis 

the time complexity is often analyzed in terms of the number of nodes explored during the search. In well-designed
problems, the algorithm can achieve a runtime close to O(c^n), where c is a constant less than 4

the space complexity is influenced by the representation of the problem. for a matrix with n rows
and m columns, the space complexity is O(n + m)

# Applications

the dancing links algorithm has been applied to diverse problems beyond exact cover, such as, in this case
Sudoku solving
'''

'''
### TOROIDAL DOUBLY LINKED LIST ###

# Doubly linked list

a doubly linked list is a data structure in which each node contains two pointers: one pointing 
to the next node and another pointing to the previous node 

mathematically, if N_i represents a node, then N_i.next points to the next node, and N_i.prev points to
the previous node

# Circular doubly linked list

a circular doubly linked list is a doubly linked list where the last node is connected to the first node, 
forming a closed loop

mathematically, in a circular doubly linked list, the last node's next pointer points to the first node
and the first node's prev pointer points to the last node 

# Toroidal doubly linked list

in dancing links, the matrix representation is transformed into a toroidal doubly linked
list structure to efficiently represent the constraints and possibilities

for each row and column, the nodes are connected in both the horizontal and vertical directions, forming 
a toroidal structure. 

mathematically, if C_i represents a column header node, then C_i.right points to the next column header, and
C_i.left points to the previous column header node in a circular fashion

a toroidal structure is a geometric shape that resembles a ring. as a data structure, a toroidal structure
refers to a closed loop or circular arrangement where the 'ends' are connected. in technical terms:

a torus is a surface of revolution generated by revolving a circle in 3D space about an axis that is coplanar
with the circle. it has a hole in the center, creating a ring 

the surface of a torus can be parametrized using two angles, donoted as θ and ϕ

in the context of dancing links, this toroidal structure allows for continous traversal in sudoku analysis
without encountering an end, making it optimal for the wraparound behavior of the recursive 
searching algoritm utilized in this codebase
'''
# class to represent a node in the dancing links algorithm
'''
each node represents a node in the dancing links algorithm. each node has a value 
and a pointers to its left, right, up, and down neighbors. each node points to itself
in all directions
'''
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = self 
        self.right = self
        self.up = self 
        self.down = self 
# class for the algorithm
class DancingLinks:
    '''
    initialize the algorithm with a given sudoku grid and 
    use the create_linked_matrix method to refactor the grid
    to be in the linked matrix data structure that allows the grid
    to be processed by the nodes in the dancing links algorithm
    '''
    def __init__(self, grid):
        self.header = self.create_linked_matrix(grid)
        self.solution = []
    '''
    creates the linked matrix structure based on the sudoku grid

    EXPLANATION
    create a new node instance to serve as the header of the linked matrix
    initialie an empty list 'columns' to store the column headers
    iterate over all possible columns in the linked matrix (9 rows * 9 columns * 4 constraints) 
    create a new node for each column, connect it to the header, and update the left
    and right pointers of adjacent columns
    iterate over each cell in the sudoku grid
    for each cell, iterate over the numbers 1-9
    calculate the index using the get_index method, and ensure that the columns
    list has enough elements
    create a new node for the current position (row)
    connect the new node to the linked matrix in the vertical direction
    connect the new node to the left in the horizontal direction
    iterate over the numbers 1-9 again and create additional nodes based on the horizontal 
    connections
    return the header node of the linked matrix

    essentially, the method is used to create the structure of the linked matrix based
    on the constraints of the sudoku puzzle, connecting nodes both vertically and horizontally 
    to represent the possibilities for each cell in the sudoku grid
    '''
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
                    # debug print statement
                    print(f"idx: {idx}, len(columns): {len(columns)}")
                    # make sure that columns list has enough elements
                    if idx >= len(columns):
                        columns.append(Node())
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
                        node.up = columns[idx - 1].up 
                        node.down = columns[idx - 1]
                        columns[idx - 1].up.down = node 
                        columns[idx - 1].up = node 
                        prev_row = node 
        return header 
    '''
    calculated the index of a node in the linked matrix 
    based on the given row (i), column (j) and number (num)
    '''
    def get_index(self, i, j, num):
        return i * 81 + j * 9 + num - 1
    '''
    chooses the column with the fewest nodes in the linked matrix
    optimizes the backtracing search algorithm for solving using dancing links

    EXPLANATION
    min_size is initialized to positive infinity, current is set to the right 
    neighbor of the header
    the method then iterated over all of the columns in the linked matrix
    if the number of nodes in the current column is smaller than min_size, update min_size
    and set selected_column to the current column
    move to the next column
    return the selected column
    '''
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
    '''
    used to hide a column and all of the rows connected to it in the 
    linked matrix

    EXPLANATION
    update the left and right pointers of adjacent columns to bypass the 'column'
    iterate over all the rows in the selected column
    for each row, iterate over all the nodes in the row
    update the up and down pointers to bypass the current node
    move to the next row and repeat untill all rows are covered
    '''
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
    '''
    used to reveal a covered column and its connected rows in the 
    linked matrix

    EXPLANATION
    iterate over all the rows in reverse order (bottom to top) in the covered column
    for each row, iterate over all the nodes in reverse order
    update the up and down pointers to restor all of the connections
    move to the previous row and repeat untill all rows are uncovered
    update the left and right pointers of adjacent columns to include the 'column'
    again
    '''
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
    '''
    core recursive backtracking algorithm that implements dancing links
    attempts to find a solutuon for the sudoku puzzle

    EXPLANATION
    if all columns are covered, meaning that a solution is found, return True 
    select a column using select column method
    cover the selected column and iterate over all rows in that column
    for each row, append its value to the solutuon, cover connected nodes in the same row, 
    and recursively call search for the next level (k + 1)
    if a solution is found at the next level, return true
    if no solution is found at the current level, backtrack by uncovering nodes and 
    removing the last value from the solution
    move to the next row and repeat the process
    if no solution is found after trying all rows, uncover the selected column and return False
    '''
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
class SudokuSolver():
    #def __init__(self):
        #self.sudoku = Sudoku
    '''
    converts the solution indices obtained from the dancing links
    algorithm to a 2d list representing the solved sudoku puzzle

    EXPLANATION
    initialize a 2d list 'result' to represent the solved sudoku grid
    iterate over each index in the solution list obtained from the dancing links
    algorithm
    use divmod to calculate the triplit (num , i, j) representing the number, row, and column
    of the current index
    update the corresponding position in the result grid with the calculated number (num + 1
    since sudoku numbers are 1 indexed)
    return the final 2d list 'result' representing the solved sudoku grid
    '''
    def extract_solution(self, solution):
        result = [[0] * 9 for _ in range(9)]
        for idx in solution:
            num, i, j = divmod(idx, 81), divmod(idx % 81, 9)
            result[i][j] = num + 1 
        return result
