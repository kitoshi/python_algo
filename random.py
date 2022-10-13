""" https://codereview.stackexchange.com/questions/86389/recursive-math-expression-eval
    start = 0
    end = len(str) -1
    mid = len(str) // 2

    for (i, c) in enumerate(str):
        if c == '(':
            start = i
            print(str[start])
        if c == ')':
            end = i + 1
            print(str[i])
            break
    if (len(str) %  2) == 0:
        return do_operator('', start, end), len(str)
    return do_operator(str[mid], start, end), len(str) """