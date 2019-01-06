# Change is inevitable(especially when breaking a twenty). Make generateCoinChange(cents) . Accept a number of American cents, compute and print how to represent that amount with smallest number of coins. Common American coins are pennies(1 cent), nickels(5 cents), dimes(10 cents), and quarters(25 cents).

# Third: add half-dollar(50 cents) and dollar(100 cents) coins with 40 additional characters or less.
# def change(num1):
#   i = num1 // 25
#   r = num1 % 25
#   print i, "quarters"
#   print r, "leftover"
#   i = r // 10
#   r = r % 10
#   print i, "dimes"
#   print r, "leftover"
#   i = r // 5
#   r = r % 5
#   print i, "nickels"
#   print r, "leftover"
#   i = r // 1
#   print i, "pennies"

# change(30)


def gen_coin_change(num):
  denoms = (
    ('dollars', 100),
    ('half-dollars', 50),
    ('quarters', 25),
    ('dimes', 10),
    ('nickels', 5),
    ('pennies', 1)
  )
  for denom in denoms:
    print num // denom[1], denom[0]
    num = num % denom[1]

gen_coin_change(30)