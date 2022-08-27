from statistics import mean
from operator import itemgetter
   
def res(l,p):
    x = list( map(itemgetter(0),l))
    y = list( map(itemgetter(1),l))
    m1 = list(map(lambda a,b: a*b, x,y))
    s = list(map(lambda a: a**2,x))
    m = (mean(x)*mean(y) - mean(m1))/(((mean(x))**2) - mean(s))
    c = mean(y) - m*mean(x)
    result = m*p + c
    return result

l = []
for i in range(5):
    a = list(map(int, input().split()))
    l.append(a)
p = 80
print(format(res(l,p),'.3f'))