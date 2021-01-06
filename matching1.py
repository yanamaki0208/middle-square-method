# coding: utf-8 
s1='tudanuma'
s2='tsudanuma'

if s1==s2 :
 strlist = list(s1)
 print(strlist)
 print(strlist)
 i=len(strlist)
 print("[", end='')
 print("'〇' " *i ,end='')
 print("]")
else :
            s3 =s1.replace('si','shi').replace('tu','tsu')
            s4 =s1.replace('si','s i').replace('tu','t u')
            strlist2 = list(s2)
            strlist3 = list(s3)
            strlist4 = list(s4)
            print(strlist4)
            print(strlist3)
            print("[", end='')
            a = len(strlist2)
            b = len(strlist3)
            if a>=b :
                j = a 
                k=0
                while k<j :  
                    if s4[k] == s3[k] :
                        print("'〇' ", end = '')
                        k+=1
                    else :
                        print("'×' ", end = '')
                        k+=1
            else :
                k=0
                while k<j :   
                    if s4[k] == s3[k] :
                        print("'〇' ", end = '')
                        k+=1
                    else :
                        print("'×' ", end = '')
                        k+=1
            print("]") 
