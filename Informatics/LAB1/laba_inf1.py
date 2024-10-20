def ten_to_fib(num):
    fib_nums = [1, 1]
    i = 1
    while fib_nums[i] < num:
        i += 1
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    str = ''
    while num > 0:
        print(i,num, str)
        if num - fib_nums[i] >= 0:
            num -= fib_nums[i]
            if i == 1:
                str += '1'
            else:
                str += '10'
            i -= 2
        else:
            str += '0'
            i -= 1
    if i > 0:
        str += ('0' * (i))
    str = str.lstrip('0')
    return str



