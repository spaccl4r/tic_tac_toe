from gameparts import Board

game = Board()

print('Способ 1' '='*20)
print(type(game))

print(type(game) == Board)
print(type(game) == str)
print(type(game) == Board)

print(isinstance(game, Board))
print(isinstance(game, str))



print('Способ 2' '='*20)

print(game.__class__)



print('Способ 3' '='*20)

game = Board()
print(dir(game))
