import difflib



with open('b.json') as a, open('c.json') as b:
    diff = difflib.Differ()


    result = diff.compare(a.readlines(), b.readlines())
    print('>>>'.join(result))
