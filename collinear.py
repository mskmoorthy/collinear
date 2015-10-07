import math

def collinear1(x1,y1,x2,y2,x3,y3):
    if ((y3-y2)/(x3-x2) == (y3-y1)/(x3 -x1)):
        return (1);
    else:
        return (-1);

def collinear2(x1,y1,x2,y2,x3,y3):
    a = math.sqrt((y1-y2)*(y1-y2) +(x1-x2)*(x1-x2))
    b = math.sqrt((y2-y3)*(y2-y3) +(x2-x3)*(x2-x3))
    c = math.sqrt((y1-y3)*(y1-y3)+(x1-x3)*(x1-x3))
    s = (a+b+c)/2.0
    area = math.sqrt(s*(s-1)*(s-b)*(s-c))
    if (area==0):
        return(1)
    else:
        return (-1)

def collinear3(x1,y1,x2,y2,x3,y3):
    twicearea = x1*y1+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3
    if (twicearea==0):
        return(1)
    else:
        return(-1)
