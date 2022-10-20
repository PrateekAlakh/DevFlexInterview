from math import floor


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2

    if 0 not in array:
        return array

    number_of_zeroes=0
    for i in array:
        if i == 0:
            number_of_zeroes+=1
            array.remove(0)
    
    center_of_arr=floor(len(array)/2)
    
    return array[:center_of_arr]+([0]*number_of_zeroes)+array[center_of_arr:]

if __name__ == "__main__":
    # write your debug code here
    print(center_zeros([1, 1, 3, 0, 6, 0]))
    print(center_zeros([]))
    
    pass