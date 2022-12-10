'''def tho(number,start ,aux,end):

    if number==1:
        print ("move disk 1 from rod{} to rod {}". format(start,end))

        return
    tho (number-1,start,end ,aux)
    print ("move disk {} from rod {} to rod {}".format(number,start,end))
    tho(number-1,aux,start,end)

disc=3
tho(disc,"A","B","C")    '''


def tho(number,a ,b,c):

    if number==1:
        print ("move disk 1 from rod {} to rod {}". format(a,c))

        return
    tho (number-1,a,c ,b)
    print ("move disk {} from rod {} to rod {}".format(number,a,c))
    tho(number-1,b,a,c)

#disc=3
disc=int(input("enter the disk:"))
tho(disc,"A","B","C")         

