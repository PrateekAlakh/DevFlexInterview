def select_max(array):
    # write your function here
    # do NOT use the built-in max() function
    if len(array)<=0:
        return

    max=array[0]
    for i in array[1:]:
        if max<i:
            max=i
    return max


if __name__ == "__main__":
    # write your debug code here
    print(select_max([1,2,5,0,3]))
    print(select_max([]))
    pass
