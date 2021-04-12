from math import sqrt
def odin(stertint,endint):
    start = stertint
    stop = endint
    step = 0.1
    last_x = 0
    last_y = 0
    len_parab = 0
    i = start
    while i <= stop:
        len_parab += sqrt((i - last_x) ** 2 + (i ** 2 - last_y) ** 2)
        last_x, last_y = i, i ** 2
        i += step
    print(len_parab)

def dva():
    import math
    start = 0
    stop = 10
    def f(x):
        return x ** 2
    step = 1
    h = (stop - start) / step
    d = 0
    i = 1
    for i in range(step):
        x1 = start + (i - 1) * h
        y1 = f(x1)
        x2 = start + i * h
        y2 = f(x2)
        d = d + math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print('d='
          '(:0.2f)'.format(start))
