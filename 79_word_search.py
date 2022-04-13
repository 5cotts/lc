# https://leetcode.com/problems/word-search/

from typing import List, Tuple

Board = List[List[str]]

class Solution:
    def exist(self, board: Board, word: str) -> bool:
                
        def calculate_neighbors(i: int, j: int, board: Board) -> List[Tuple[int, int]]:
            neighbors = []
            # Below neighbor
            if i != 0:
                neighbors.append((i - 1, j))
            # Above neighbor
            if i < len(board) - 1:
                neighbors.append((i + 1, j))
            # left neighbor
            if j != 0:
                neighbors.append((i, j - 1))
            # right neigbor
            if j < len(board[0]) - 1:
                neighbors.append((i, j + 1))
            return neighbors
                
        
        def word_found(board: Board, word: str, i: int, j: int):
            # if you make it so far you know you match and if this is the last letter then you succesfulyl found the word
            if len(word) == 0:
                return True
            # If the value isn't equal to the first character in the word, you know you have gone down the incorrect path.
            elif board[i][j] != word[0]:
                return False
            # this asserts that board[i][j] == word[0], which means you found a valid path
            elif len(word) == 1:
                return True
            
            # Hold in-memory the original value of (i, j) and then replace it with a placeholder on the actual board.     
            val = board[i][j]
            board[i][j] = ""
            
            # Essentially recurses and iterates until the word is de-materialized as such: "WORD" -> "ORD" -> "RD" -> "D".
            # Also, only recurses/iterates if `calculate_neighbors` finds neighbors.
            # `res` is an iterator containing booleans. If any of the booleans are True, we know the word has been found.
            # As long as one neighbor exists, we know we can continue our recursion.
            res = list(map(
                lambda x: word_found(board, word[1:], x[0], x[1]),
                calculate_neighbors(i, j, board)
            ))
            # Reset the val of (i, j) to the original value
            board[i][j] = val
            return any(res)
            
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if word_found(board, word, i, j):
                    return True
        return False
