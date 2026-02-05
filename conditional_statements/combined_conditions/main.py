# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = True
promotion=True
promotion= not movingProduct
movingProduct= discounted or lowStock
print("Is the item eligible for promotion?", promotion )