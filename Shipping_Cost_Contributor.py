# Shipping Cost Calculator

## Input package weight adnd shipping rate
Weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"shipping cost: {shipping_cost} USD")




