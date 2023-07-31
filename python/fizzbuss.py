t = 0
with open("newfile.txt") as f:
    for i in f.readlines():
        t += 1
        wordBreak =i.split()
        print(wordBreak)
        print( "Line", str(t) + ":",len(wordBreak) - 1)
