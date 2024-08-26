def count_down(x):
    def loop(y):
        if y <= 0:
            return
        else:
            print(y)
            loop(y - 1)
        
    loop(x)

count_down(10)

def count_up(x, max):
    if x >= max:
        print('Done!')
        return
    else:
        print(x)
        count_up(x + 1, max)

count_up(0, 10)