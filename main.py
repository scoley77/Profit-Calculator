#challenge: figure out how many of each product I'll need to sell at my next con in order to triple the booth investment

import classes

products = []

products.append( classes.Product('Choco Pins', 1.10, 7.00, 14) )
products.append( classes.Product('Nerikiri Pets', 3.80, 15.00, 12) )
products.append( classes.Product('Mini Teapots', 4.50, 15.00, 5) )
products.append( classes.Product('5x7 Prints', 0.70, 8.00, 20) )
products.append( classes.Product('11x17 Prints', 1.00, 15.00, 10) )
products.append( classes.Product('Big Fat Potion', 2.50, 10.00, 7) )
products.append( classes.Product('Big Potion', 1.50, 7.00, 7) )
products.append( classes.Product('Little Potion', 0.75, 5.00, 13) )
products.append( classes.Product('Bottled Clay Pins', 1.75, 10.00, 6) )
# products.append( classes.Product('Large Vinyl', 0, 3.00, 30) )
# products.append( classes.Product('Tiny Vinyl', 0, 1.00, 30) )
# products.append( classes.Product('Old Prints', 0, 5.00, 35) )


import calc

print(calc.sell_out(products))
print(calc.challenge(products, 300))