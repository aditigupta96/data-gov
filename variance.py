def mean(a):
    return sum(a) / len(a)

def variance(a):
    x = mean(a)
    variance = sum([(i-x)**2 for i in a])
    return variance

y = list(map(int,input().split()))
z= variance(y)
print(z)
