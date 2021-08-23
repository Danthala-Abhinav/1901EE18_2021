# NAME    : Danthala Abhinav
# ROLL NO : 1901EE18

# MEMORY GAME

def isdigit(a):                 # a represents the input list(input_list) passed 
    flag = True
    for i in a:
        if(type(i)!=int):
            flag = False
            break
    b=[]                       # b represent a list (empty when declared) where we append non-int elements
    for j in a:
        if(type(j)!=int):
            b.append(j)
    if(flag == True):
        return
    else:
        print('Please enter a valid input list.Invalid inputs detected : {}'.format(b))
        exit()

def get_memory_score(input_list):       # input_list represents the passed input list(input_nums)
    mylist = []                         # mylist represents a list (empty when declared) where we append the elements as per the problem
    count = 0
    for i in input_list:
        if(len(mylist)<5):
            flag = False
            for j in mylist:
                if(i==j):
                    count+=1
                    flag = True
                    break
            if(flag == True):
                continue
            else:
                mylist.append(i)
        else:
            flag1 = False
            for k in mylist:
                if(i==k):
                    count+=1
                    flag1 = True
                    break
            if(flag1 == True):
                continue
            else:
                mylist.remove(mylist[0])
                mylist.append(i)
    return count                
input_nums = [3,4,5,3,2,1]      # Input list
isdigit(input_nums)             # Passing input list(input_nums) to isdigit() function
score = get_memory_score(input_nums)    # Passing input list(input_nums) to get_memory_score() function
print('Score: {}'.format(score))