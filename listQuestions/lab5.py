

def gather_lists(l):
    '''
    wrong
    '''
    new = []
    if not isinstance(l, list):
        new.append(l)

    elif isinstance(l, list):
        for i in l:
            new.append(gather_lists(i))
    
    return new

def max_length(l) -> int:

    if not isinstance(l, list):
        return 1

    count = 0
    for i in l:
        count += 1

    for i in l:
        if max_length(i) > count:
            count = max_length(i)
    
    return count


if __name__ == "__main__":

    list = [ 1, [2,3], [4,5,6]]
    print(max_length(list))