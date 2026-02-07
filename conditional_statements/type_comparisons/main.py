# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

# Write your code here
#"Is price a float?:" <price_is_float>
#"Is count an integer?:" <count_is_int>

price_is_float= type(price)==float
count_is_int= type(count)==int

print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)