x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
gamma=1

for i in range(10):
    factor = gamma*abs((5/max(x[i],5)-(x[i]/max(x[i],5))))
    print(factor)
    if factor == 0:
        memval = 1
    elif factor>0 and factor<=1:
        memval = 1-factor
    elif factor>1:
        memval = 0
    print(memval)