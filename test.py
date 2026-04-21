from gameparts import Board
from inspect import getsource, isfunction, ismethod

game = Board()

print('Способ 1' '='*20)
print(type(game))

print(type(game) == Board)
print(type(game) == str)
print(type(game) == Board)

print(isinstance(game, Board))
print(isinstance(game, str))
print(game.board)
print(game.__dir__)

print('-------------------------------------------------------------------------------')

print('Способ 2' '='*20)

print(game.__class__)
print(game.__class__.__str__)
print(game.__class__.__dir__)
 
print('-------------------------------------------------------------------------------')

print('Способ 3' '='*20)

print(dir(game))

print('__str__' in dir(game))

print(hasattr(game, '__str__'))
print(game.board)
print(game.__dir__)

print('-------------------------------------------------------------------------------')

print('Способ 4' '='*20)

print(game.__class__.__dict__)

print(game.__class__.__str__)
print(game.__class__)

print('-------------------------------------------------------------------------------')

print('Способ 5' '='*20)
# с помощью getsource мы можем получить в комм.строке програмный код
print(getsource(Board))
print(isfunction(game.display))
print(ismethod(game.display))

print(game.board)
print(game.__dir__)
print(game.__class__)

print('-------------------------------------------------------------------------------')
