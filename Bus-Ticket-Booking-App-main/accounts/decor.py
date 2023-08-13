''' i studied about it sir, when we define a variable in main body of a program,then it will be treated as a global variable 
    so when called a function without the variable as a parameter also it working fine..
    i,e:def fun():
            print(s)
        s='akash'
        fun()
        print(s)

        o/p:
            'akash'
            'akash'
    but when we define the same variable both in  main and local scope python is treating them as two different varibale 
    i,e:def fun():
            s='yash'
            print(s)
        s='akash'
        fun()
        print(s)
        o/p:
            'yash'
            'akash'
     to let python know that they both (local s,global s) are same  and is already defined in global scope , we are using global in local scope

l=['mumbai','delhi','mumbai','delhi','mumbai']
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
# now d={'mumbai':3.'delhi':2}
# now we have the dictioanry with frequencies
# just pick the second_most_frequncy_value[2] from values([3,2]) by removing max frequent value
# iterate through dict and find which keys frequency==second_most_frequent_value:
# print(keys)
vals=list(d.values()) 
vals.remove(max(vals))
for i in d.keys():
    if d[i]==max(vals):
        print(i)
        break

'''

# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
# l.sort()
# print(l[-1])
# print(l[-2])
def generate(numRows):
        ans=[]
        ans=[[1],[1,1]]
        if(numRows)==1:
            return [[1]]
        if(numRows==2):
            return ans
        for i in range(2,numRows):
            l=[]
            for j in range(len(ans[-1])-1):
                l.append(ans[-1][j]+ans[-1][j+1])
            l.insert(0,1)
            l.append(1)
            ans.append(l)
        return ans
n=int(input())
a=generate(n)
for i in a:
    for j in i:
        print(j)
    print('\n')






