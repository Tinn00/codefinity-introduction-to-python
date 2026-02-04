# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1= "Bubblegum"
candy2="Chocolate"
dry_goods="Pasta"

candy1=items[:9]
candy2=items[11:20]
dry_goods=items[22:]

category1="Candy Aisle"
category2="Pasta Aisle"

bubblegum_price= "$1.50"
chocolate_price= "$2.00"
pasta_price="$5.40"

print(f"we have {candy1} for {bubblegum_price} in the {category1}")

print(f"we have {candy2} for {chocolate_price} in the {category1}")

print(f"we have {dry_goods} for {pasta_price} in the {category2}")

