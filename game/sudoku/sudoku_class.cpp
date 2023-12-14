// reiplementation of the python sudoku structure in C++
// could potentially save computation time and allow for some better 
// algorithms

#include <iostream>
#include <vector>
#include <string.h>
using std::cout;
using std::vector;
using std::string;
using std::find;

class Sudoku {
    public:
        // init consts for the object
        const int x = 0;
        const int y = 0;
        const float dif = 500 / 9;
        const int val = 0;
        // init mutables for the object
        int flag1 = 0;
        int flag2 = 0;
        int rs = 0;
        int error = 0;
        // for updating solutions
        bool solved = false;
        bool generated = false;
        vector<int> unsolvedBoard;
        string board_string;
        // init with sample grid
        vector<vector<int>> grid = {
            {7, 0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 8, 0, 0, 1, 0, 0},
            {0, 2, 0, 0, 0, 0, 0, 0, 9},
            {0, 0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 6, 0, 0, 0},
            {0, 3, 0, 0, 8, 0, 0, 6, 0},
            {0, 0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 4, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 5, 0}
        };
        // method to check validity of a ints position in the grid
        bool isValid(int row, int col, int num) {
            for (const auto& r : this->grid){
                auto it = find(r.begin(), r.end(), num);
            }
            
        }
};