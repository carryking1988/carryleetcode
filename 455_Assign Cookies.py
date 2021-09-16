

def assigncookies(children,cookies):
    children.sort()
    cookies.sort()
    child = cookie = 0
    while child < len(children) and cookie < len(cookies):
        if children[child] <= cookies[cookie]:
            child += 1
        cookie += 1
    return child


import random
g = [random.randint(1,100) for _ in range(5)]
s = [random.randint(1,100) for _ in range(6)]

# g = [1,2]
# s = [1,2,3]


print('g = ', g)
print('s = ',s)
print(assigncookies(g, s))





