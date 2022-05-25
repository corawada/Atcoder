from decimal import Decimal, ROUND_HALF_UP

y = Decimal(input())

print(y.quantize(Decimal('0'), rounding=ROUND_HALF_UP))

