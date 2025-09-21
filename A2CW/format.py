unitPrice = 49.95
qty = 32
salesTaxRate = 0.05
subTotal = qty * unitPrice
salesTax = salesTaxRate * subTotal
total = salesTax + subTotal

print(f"Sales Tax Rate {salesTaxRate:.1%}")
print(f"SubTotal: ${subTotal:,.2f}")
print(f"Total: ${total:,.1f}")

print(f"SubTotal: ${subTotal:>8,.2f}")
print(f"Total: ${total:>12,.1f}")
print(f"Total: ${total:<12,.1f}")
print(f"Total: ${total:^12,.1f}")
name = "aly"
number = 1
print("Hello {0}, Your number is {1}" .format(name,number))

num = int(input("input ur number."))
num = num + 1
print(num)