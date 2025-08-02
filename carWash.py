X = int(input())
Y = int(input())
Z = int(input())
T = int(input())
V = int(input())

fixed_cost = X
per_minute_cost = Y * T
per_liter_cost = Z * V

min_cost = min(fixed_cost, per_minute_cost, per_liter_cost)
print(min_cost)        