#       imports       #

# _buffer_ 
class All_Function: # Paskal,uniqueValues,evenOddLst,hex_to_decimal,bgstUnits,specialSum
    def __init__(self):
        self.__All__="all class is all the functions in the program " #attribute
    def lst2Dic(self):
        lst1= [[2,3,4,6], [2,3,4,6,9,12,18], [2,4,13,26]]
        lst2=[1,2,3]
        lst={}
        cou=0
        for i in lst2:
            lst.update({i:lst1[cou]})
            cou+=1
        return lst #{12: [2, 3, 4, 6], 36: [2, 3, 4, 6, 9, 12, 18], 52: [2, 4, 13, 26]}
    
    def uniqueValues(self): # parse dict to array only value
        x=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
        res=[]
        for i in x:
            for j in i:
                res.append(i[j])
        res=list(set(res))
        return(res)#['S007', 'S009', 'S001', 'S002', 'S005']
        
    def evenOddLst(self):
        listOne = [3, 6, 9, 12, 15, 18, 21]
        listTwo = [4, 8, 12, 16, 20, 24, 28]
        list=[]
        for i in listOne[1::2]:
            list.append(i)
        for i in listTwo[::2]:
            list.append(i)
        return list #[6, 12, 18, 4, 12, 20, 28]
    
    def isPangram(self):
        string="The quick brownfox jumps over the lazy dog" # string(a-z) 
        string=string.lower()
        words=[0]*26    # arr for a-z
        for i in string:
            if i.isalpha():
                words[ord(i)-ord("a")]+=1
        if 0 in words:
            return 0
        return 1
    
    def bgstUnits(self,lst,x,y):    # Recursion func find max between index lst[x , , , y]
        if x==y:
            return(lst[y])%10
        if lst[x]%10>lst[y]%10:
            return self.bgstUnits(lst,x,y-1)
        else:
            return self.bgstUnits(lst,x+1,y) 
        
    def specialSum(self,lst,num,low,high):   # Recursion func find num between index lst[low , , ,high]
        if low==high:
            if lst[low]>num:
                return lst[low] 
            else:
                return 0
        if lst[low]>num:
            return lst[low] + self.specialSum(lst,num,low+1,high)
        return self.specialSum(lst,num,low+1,high)
    
    def choose(self,n, k):   # note no dependencies on any of the prior code
         if k in (0, n):   # stop
             return 1
         return self.choose(n-1, k-1) + self.choose(n-1, k)
     
    def pascalTriangle(self,num):
        for row in range(num):
            for k in range(row + 1):
                # flush is a Python 3 only argument, you can leave it out,
                # but it lets us see each element print as it finishes calculating
                print(self.choose(row, k), end=' ', flush=True) 
            print()
            
    def hex_to_decimal(self,string,base):   # return string 
        res = int(string, base)   # Hexadecimal To decimal with int(string, base)
        return(f'Hexa To Decimal --> {string} = {res}')
# _buffer_ 
class multTable: # Class multTable
    
    def __init__(self,row,col): # constractor make multTable attributes  & check Limits of row and col 
        try:                                     # try
            if row <= 0: 
                print("row < 0")
                self.__row__=int(input("row: "))
            if  col <= 0:
                print("col < 0")
                self.__col__=int(input("col: "))
            else:
                self.__row__=row # attribute __row__
                self.__col__=col # attribute __col__
                self.__table__ = (col * row) # attribute __table__
        except Exception as ex:                # except
             print(ex)
        
    def display(self,x,y,z,t): # display function make mult Table 
        try:                                     # try
            if self.__col__ < y :
                raise ValueError(f"#11 .__col__ = {self.__col__} < y = {y} ")
            if self.__row__ < t :
                raise ValueError(f"#22 .__row__ = {self.__row__} < t = {t} ")
            if x>=y or z>=t:
                raise ValueError(f"#33 x={x} >= y={y} z={z} >= t={t} ")
            else:
                print("\t",end='')
                for i in range(x,y+1):
                    print(i,end="\t")
                print()
                for j in range(z,t+1):
                    for i in range(x,y+1):
                        if i==x:
                            print(j,end="\t")
                        print(i*j,end="\t")
                    print()
                    
        except Exception as err:   # except
             print(err)
# _buffer_
class My_range :#range class example
    def __init__(self,finsh,start=None,step=1):        
        if start != None:
            r = start
            start = finsh
            finsh = r
        else:
            start = 0
        self.finsh = finsh
        self.start = start
        self.step = step
        
    def __str__(self): # To String
        if self.step != 1:
            return f'range({self.start},{self.finsh},{self.step})'
        if self.start == 0:
            return f'range({self.finsh})'
        else:
            return f'range({self.start},{self.finsh})'    
    
    def range1(self):
        if self.step != 1:
            res=[0]*((self.finsh-self.start)//self.step+1)
        else:
             res=[0]*((self.finsh-self.start)//self.step) 
        indx=0
        s=self.start
        for i in res:
            res[indx]=s
            s+=self.step
            indx+=1
        return(res)
# _buffer_ 
def stam_dvarim_magnivim(): #enumerate(list)
    print("~option 1~")
    my_list=['bread', 'milk', 'butter']
    for i, x in enumerate(my_list):
        print(i, x)
      
    print("\n~option 2~")
    x=0
    for i in my_list:
        print(x,i)
        x+=1
# _buffer_    
def range_static(finsh,start=None,step=1):## range_static() 
    if start != None:
        r = start
        start = finsh
        finsh = r
    else:
        start = 0
    finsh = finsh
    start = start
    step = step
    if step != 1:
        res=[0]*((finsh-start)//step+1)
    else:
        res=[0]*((finsh-start)//step)
    indx=0
    s=start
    for i in res:
        res[indx]=s
        s+=step
        indx+=1
    return(res)   
# _buffer_

def main():
    
    try : 
        range_static(1,4)
    except Exception as err:     # Exception
        print(err)
        
main()

