import numpy as np

def printSnake(board, snake):
    print("-----")
    for x in range(0, board[0]):
        for y in range(0, board[1]):
            if ([x, y] in snake):
                if ([x, y] == snake[0]):
                    print("C", end="")
                else:
                    print("X", end="")

            else:
                print("O", end="")
        print("")
    print("-----")


def inBoard(board, corX, corY):
    if corX >= 0 and corY >= 0 and corX < board[0] and corY < board[1]:
        return True
    else:
        return False


numberOfPaths = 0
def numberOfAvailableDifferentPaths(board, snake, depth):
    global numberOfPaths
    around_array = [[1, 0], [-1, 0], [0, 1], [0, -1]] #array with all possible movements

    if depth >0:
        for around in around_array:
            future_mov = list(np.add(snake[0], around)) #Creating the next possible movement
            tail = snake.pop()

            if (future_mov not in snake) and inBoard(board,future_mov[0],future_mov[1]):
                snakeModified = [future_mov] + snake

                snake.append(tail) #Saving the tail for can calculate next movements

                numberOfAvailableDifferentPaths(board, snakeModified, depth - 1)

                if depth == 1:
                    numberOfPaths = numberOfPaths + 1 #We consider a new path only when it was completed

            else:
                snake.append(tail) #if the movement is not correct, will save the tail for next movement


print("Test 1:")
board = [4,3]
snake =[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
depth = 3
numberOfAvailableDifferentPaths(board, snake, depth)
print(numberOfPaths)

print("Test 2:")
numberOfPaths=0
board = [2, 3]
snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
depth = 10
numberOfAvailableDifferentPaths(board, snake, depth)
print(numberOfPaths)

print("Test 3:")
numberOfPaths=0
board = [10, 10]
snake = [[5,5], [5,4], [4,4], [4,5]]
depth = 4
numberOfAvailableDifferentPaths(board, snake, depth)
print(numberOfPaths)