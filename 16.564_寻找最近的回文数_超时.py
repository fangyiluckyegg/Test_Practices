#564. 寻找最近的回文数
#给定一个表示整数的字符串n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
#“最近的”定义为两个整数差的绝对值最小。

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n)>=1 and int(n)<=10 :return(str(int(n)-1))
        if int(n)>=11 and int(n)<=11 :return(str(int(n)-2))
        if int(n)>=12 and int(n)<=10**18-1: 
            n_up = str(int(n)+1)
            n_down =str(int(n)-1)
            for i in range(1,int(n)//2):
                l = len(n_down)
                #print(n_down)
                #print(int(n))
                #print(l)
                #print(l//2)
                if l%2!=0:
                    upper2 = int(n_down)//int(10 ** ((l-1)//2))
                    lower2 = int(n_down)%10 ** ((l+1)//2) 
                    #print(upper2, lower2)

                else:
                    upper2 = int(n_down)//int(10 ** ((l)//2))
                    lower2 = int(n_down)%10 ** ((l)//2)  
                    #print(upper2, lower2)   
                upper2 = int(str(upper2)[::-1])
                #print(upper2, lower2)   
                if upper2==lower2:
                   print(n_down,"向下" ,i)     
                   return (n_down)        
                   break

                l = len(n_up)
                #print(n)
                #print(int(n))
                #print(l)
                #print(l%2)
                if l%2!=0:
                    upper1 = int(n_up)//int(10 ** ((l-1)//2))
                    lower1 = int(n_up)%10 ** ((l+1)//2) 
                    #print(upper1, lower1)
                else:
                    upper1 = int(n_up)//int(10 ** ((l)//2))
                    lower1 = int(n_up)%10 ** ((l)//2)   
                    #print(upper1, lower1)      
                upper1 = int(str(upper1)[::-1])
                if upper1==lower1:
                   print(n_up,"向上" ,i)   
                   return (n_up) 
                   break

                #print(n_down,n_up) 
                n_up=str(int(n_up)+1) 
                if int(n_down)>=1:   
                    n_down=str(int(n_down)-1) 
             


        
if __name__ == "__main__":
    sol = Solution()
    result = sol.nearestPalindromic("807045053")   
    print(result)
