x = [4,6,1,3,5,7,25]
def draw_stars():
    star = '*'
    for i in range(0, len(x)):
        print (star * x[i])
draw_stars()
