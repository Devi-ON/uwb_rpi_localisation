#xi,yi are the coordinates of the cooresponding anchor and di is the distance of this anchor to the tag. Input data types should be float.

def trilateration(x1,y1,d1,x2,y2,d2,x3,y3,d3):
    a1 = 2*(x1-x3)
    a2 = 2*(y1-y3)
    a3 = 2*(x2-x3)
    a4 = 2*(y2-y3)
    b1 = pow(x1,2)-pow(x3,2)+pow(y1,2)-pow(y3,2)+pow(d3,2)-pow(d1,2)
    b2 = pow(x2,2)-pow(x3,2)+pow(y2,2)-pow(y3,2)+pow(d3,2)-pow(d2,2)

    det_ATA = (pow(a1,2)+pow(a3,2))*(pow(a2,2)+pow(a4,2)) - (a1*a2+a3*a4)*(a1*a2+a3*a4)
    estimatedLocation = [0,0] 
    estimatedLocation[0] = (1/det_ATA)*((pow(a2,2)+pow(a4,2))*(a1*b1+a3*b2)-(a1*a2+a3*a4)*(a2*b1+a4*b2)) #estimated x coordinate
    estimatedLocation[1] = (1/det_ATA)*((pow(a1,2)+pow(a3,2))*(a2*b1+a4*b2)-(a1*a2+a3*a4)*(a1*b1+a3*b2)) #estimated y coordinate

    return estimatedLocation #output is an array of size 2.