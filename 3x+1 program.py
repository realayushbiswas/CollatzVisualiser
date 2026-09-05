import matplotlib.pyplot as plt

while 1==1:
    a = 1
    b = int(input('Enter the number : '))
    c =0#step counter
    d= 0#numbers checked (n-1)
    a=b+d
    #The points
    x=[]
    y=[]
    #plot line specifications
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
    
    x.append(c)
    y.append(a)
    
    while a == a :
        if a % 2 == 0:
            a = a // 2 #used // as python floats only have 15-17 significant digits of precision
		#this invalidates below comments but it is still an interesting point to note.
            c = c + 1
            x.append(c)
            y.append(a)
            print(a)
        elif a == 1:
            print(f'{b+d} complies after {c} steps !')
            plt.title(f'Graph of {b+d}')
            plt.xlabel(f'Steps({c})')
            plt.ylabel(f'Number({b+d})')
            plt.plot(x, y)
            plt.show()
            x.clear()
            y.clear()
            c=0
            d=d+1
            a=b+d
            x.append(c)
            y.append(a)
        else:
            a = a * 3 + 1
            c = c + 1
            x.append(c)
            y.append(a)
            print(a)

#3721832837283283782328866 511,436 repeating ?!?
#37218328372832837829074 512 !??!
#3721832837283283782907 354 steps ?!?!
#1727823783728372837461 443 steps repeating ?!?!?
