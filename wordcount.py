a=[]
count1=0
count2=0
fi=open("C:\\Users\\刘兆琦的游戏本\\Desktop\\1.txt","r+")
for f in fi:
    print(f)
    f1=f.replace(","," ")
    a=f1.split(" ")
    f2=f.replace(" ","").replace(",","")
    count1 += len(a)
    count2 += len(f2)
    print(count1)
    print(count2)