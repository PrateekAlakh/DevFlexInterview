from math import floor

def minimum_points(threshold, points):
    # write your code here
    if len(points)<3:
        return len(points)
    i=2
    while i<len(points):
        if i==len(points):
            return len(points)
        if points[i]-points[0]>=threshold:
            return floor((i+1)/2)+1
        i+=1
    return len(points)
    


if __name__ == "__main__":
    # write your debug code here
    print(minimum_points(2, [1, 2, 3]))
    pass
