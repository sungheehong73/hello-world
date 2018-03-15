# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:00:02 2018

@author: 아빠
"""

#import sub_hongpackage as sh
import sub_hongpackage.temp as sh_t

#sh_t.timer3(10,0.2)

#for i in range(1000):
#    data = '당신의 숫자는 {}\n'.format(i)
#    sh_t.file_inout(data)
try:
    sh_t.couple2()
    
#   sh_t.class_4cal()
#    sh_t.timer3(100,1)
#    sh_t.ex_input()    
#    sh_t.cal_prime(100)
#    sh_t.jugde('2523hohnf')
#    print(sh_t.list2dic(['name','age'],[34,46]))
#    print(sh_t.map_test([1,2,3],[4,5,6]))
#    sh_t.file_io('hello world')
#     sh_t.file_read('test.txt')
#    sh_t.file_readline2('test.txt')
#    sh_t.list_test()
    #list_test2()
    #range_list()
    #morethan()    
    #while_test()        
    #tsum(100)    
    #mindouble(514,108,274)         
    #sum_list('hong','-7723')
    #if_in()            
    #all_list = ['hong',23,timer]
    #all_tuple = ('hong',23,timer)
    #print(tuple_sum(1,2,3,4))
    #dict_func(depth=50,color='yellow')    
    #new_list = rev(1,2,3)
    #timer2(5,0.5)
    
    #list2dic()            
    #lambda_f()
    #f_linew()
    #f_newline()
    #f2_copy()    
    #f3_read()    
    #file_size()    
    #remove_file()        
#    sh_t.rename_file('C:/Users/Home/.spyder-py3/hongpackage/sub_hongpackage/sung.txt','C:/Users/Home/.spyder-py3/hongpackage/sung.txt')
#    sh_t.file_list("c:/")
#    sh_t.now_dir()
#     sh_t.change_dir()
#    sh_t.del_all()
#    sh_t.isfile()
#    sh_t.isfiledir()
#     sh_t.time_f()
#      sh_t.elap_time()
    



    

except KeyboardInterrupt:
    print('you push keyboard hong')

except Exception as e:
    print(e)
else:
    print('no 예외')
    
finally:
    print('무조건 finally 발생')
    