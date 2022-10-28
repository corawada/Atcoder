n, k = map(int, input().split())

def custom_round(number, ndigits=0):
    if type(number) == int:#整数ならそのまま返す
        return number
    d_point = len(str(number).split('.')[1])#小数点以下が何桁あるか定義
    if ndigits >= d_point:#求める小数点以下の値が引数より大きい場合はそのまま返す
        return number
    c = (10 ** d_point) * 2
    #小数点以下の桁数分元の数に0を足して整数にして2倍するための値(0.01ならcは200)
    return round((number * c + 1) / c, ndigits)
    #元の数に0を足して整数にして2倍して1を足して2で割る。元の数が0.01なら0.015にしてroundを行う

for _ in range(k):
    n = custom_round(n/10)

print(int(n*(10**k)))

