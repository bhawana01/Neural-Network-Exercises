# McCullouch Pitts OR Simulation
# y =x1w1 +x2w2 - t

'''
x1 x2 y
0 0 0
0 1 1 w2>t
1 0 1 w1 >t
1 1 1 w1+w2 >t
w1 =0.7, w2 = 0.7, t = 0.5
'''

def mcCullouch():
    x1 =0
    x2 = 0

    y= 0.7 *x1 +0.7*x2 

