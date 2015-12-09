def mean(a):
    return float(sum(a) / len(a))

def variance(a):
    x = mean(a)
    variance = sum([(i-x)**2 for i in a])
    return float(variance)

y = list(map(int,input().split()))
z= variance(y)
print(z)
