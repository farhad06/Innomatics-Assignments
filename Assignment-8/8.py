import statistics as st

n=int(input())
x=tuple(map(float,input().split()))
y=tuple(map(float,input().split()))

result=sum([m*n for m,n in zip([i-st.mean(x) for i in x],[i-st.mean(y) for i in y])])/(n*st.pstdev(x)*st.pstdev(y))   

print(round(result,3))