price = 500000
quantity = 3

total_cost = price * quantity
discount = total_cost * 0.2
final_cost = total_cost - discount
vat = final_cost * 0.1
real_final_cost = final_cost + vat

print(total_cost)
print(discount)
print(final_cost)
print(vat)
print(real_final_cost)