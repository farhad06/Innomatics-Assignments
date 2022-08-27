if __name__ == '__main__':
    marks=[]
    total=[]
    main_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append(score)
        total.append([name,score])
    duplicate_remove=list(set(marks))
    duplicate_remove.sort()
    for name,score in total:
        if score==duplicate_remove[1]:
            main_list.append(name)
    main_list.sort()     
    for  i in main_list:
        print(i)