def meraki_helper(n):
    n=str(n)
    if(len(n)==1):
        print("Yes - {} is a Meraki number".format(n))
        return True
    else:
        i=0
        while(i<len(n)-1):
            if( abs( int(n[i]) - int(n[i+1]) ) != 1 ):
                print("No - {} is not a Meraki number".format(n))
                return False
            i+=1
        print("Yes - {} is a Meraki number".format(n))
        return True
input=[12,14,56,78,98,54,678,134,789,0,7,5,123,45,76345,987654321]
meraki=0
nmeraki=0
for i in input:
    x=meraki_helper(i)
    if(x==True):
        meraki+=1
    else:
        nmeraki+=1
print("the input list contains {} meraki and {} non meraki numbers.".format(meraki,nmeraki))
