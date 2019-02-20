def fa():
    strs = ["A", "B", "C"]
    funcs = []
    for s in strs:
        def outer(s):
            def chi():
                print(s)

            return  chi

        funcs.append(outer(s))

    return funcs


funcs = fa()

for func in funcs:
    func()




lam = lambda x, y:  (x if x>0 else 1000) * y

re =  lam(-1, 9)
print(re)
