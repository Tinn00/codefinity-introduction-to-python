seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

overstock_risk=True
discount_eligible=True
make_discount=True

discount_eligible= high_stock_threshold and (current_stock> seasonal) 
discount_eligible=  not selling_well and not on_sale
make_discount= overstock_risk or discount_eligibl

print(f"Should the item be discounted?", True)

#Should the item be discounted? <make_discount>