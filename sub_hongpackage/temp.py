
def list_test():
    
    a_list = ['hong sung-hee','kim ki-hyun', 'yoon ja-ha']
    
    for i in a_list:
        if 'yoon' == i.split()[0]:
            print('yoon OK')
    
    for i in a_list:
        if 'hee' in i:
            print('hee OK')


def list_test2():
    b_list = 'hong sung hee'
    b_list2 = b_list.split()
    for i in b_list2:
        print(i)

def range_list():
    for i in range(1,10,3):
        print(i)
        
def morethan():
    for i in range(1,10):
        if i >= 5:
            break
        else:
            print(i)

def while_test():
    i = 0
    while i < 10:
        i += 1
        if ((i >= 3) & (i <= 7)):
            print(i)
        else:
            continue

def tsum(a):
    sum = 0
    for i in range(a+1):
        sum += i
    
    print('from 1 to {} sum is {}'.format(a,sum))

#최소공배수 
def mindouble(a,b,c): # 
    i = 1
    while True:
        i += 1
        if ((i%a == 0) & (i%b == 0) & (i%c == 0)):
            print(i)
            break

def sum_list(a,b):
    print(a+b)
    
def if_in():
    a = ['abc','def','zfe']
    for i in a:
        if 'abc' in a:
            print('OK')
            break


#중요한 내용
from time import sleep

def timer():
    for i in range(100):
        msg = '\r 진행률 {} %'.format(i+1)
        print(msg,end='')
        sleep(0.1)
    
def timer2(num,speed):
    for i in range(1,num+1):
        print('\r {}'.format(i),end='')
        sleep(speed)

def timer3(num,speed):
    for i in range(num):
        print('\r {}'.format('*'*i),end='')
        sleep(speed)
    
def tuple_sum(*hong):
    sum =0
    for i in hong:
        sum += i
    return sum

def dict_func(**hong):
    print(hong)
    return

param = 10

def func10():
    global param
    param = 20
    print(param)
    return

def rev(a,b,c):
    return c,a,b

def file_inout(data):
    f =  open('hong.txt','a')
    f.write(data)
    f.close()

def list2dic():
    name = ['hong','kim','yoon']
    grade = [98,80,73]
    e_name = enumerate(name)
    dic = {}
    for i,j in e_name:
        dic[j] = grade[i]
    print(dic)
    

def lambda_f(): 
    add = lambda x,y : x*y
    
    a = [1,2,3]
    b = [4,5,6]
    s = map(add,a,b)
    print(list(s))

def f_linew():
    data = input('your data = ?')
    f = open('test.txt','w')
    f.write(data)
    f.close()

def f_newline():
    print('insert your new line')
    data_list = []
    count = 1
    while True:
        txt = input('{} line :'.format(count))
        if txt =='':
            break
        data_list.append(txt+'\n')
        count += 1
    f = open('test.txt','w')
    f.writelines(data_list)
    f.close()

def f_copy():
    f = open('test.txt','r')
    fc = open('test_copy.txt','w')
    f_data = f.read()
    fc.write(f_data)
    f.close()
    fc.close()

def f2_copy():
    bufsize = 1024
    f = open('a.png','rb')
    fc = open('a_copy.png','wb')
    f_data = f.read(bufsize)    
    while f_data:
        fc.write(f_data)
        f_data = f.read(bufsize)
    f.close()
    fc.close()
    
def f3_read():
    f = open('test.txt','r')
    f.seek(3)
    data = f.read(5)
    print(data)
    f.close()

from os.path import getsize

def file_size():
    print(getsize('test.txt'))

from os import remove
    
def remove_file():
    k = input('remove ? yes')
    if k == 'yes':
        remove('test.txt')
        print('delete ok')        

from os import rename
import os
         
def rename_file(a,b):
    rename(a,b)

def file_list(folder):
    fileList = os.listdir(folder)
    print(fileList)
    
def now_dir():
    print(os.getcwd())

def change_dir():
    now_position = os.getcwd()
    print(now_position)
    os.chdir('..')
    print(os.getcwd())
    os.chdir(now_position)
    print(os.getcwd())
    os.mkdir('test')
    msg = input('do you want delete dir ? yes?')
    if msg == 'yes':
        os.rmdir('test')
        print('directory delete')

import shutil    

def del_all():
    msg = input('you want delete all ?')
    if msg == 'yes':
        shutil.rmtree('a')
        print('all delete OK')

from os.path import exists

def isfile():
    dir_name = input('dir name ?')
    if not exists(dir_name):
        os.mkdir(dir_name)
        print('we made {}'.format(dir_name))
    else:
        print('same name')
    
from os.path import isdir, isfile
    
def isfiledir():
    file_list = os.listdir()
    for file in file_list:
        if isfile(file):
            print('{} => file'.format(file))
        elif isdir(file):
            print('{} => directory'.format(file))

from time import localtime

def time_f():
    t = localtime()
    day_list = ['mon','tue','wed','thu','fri','sat','sun']
    print('today is {}'.format(day_list[t.tm_wday]))

from datetime import datetime
import math    

def elap_time():
    start = datetime.now()
    math.acosh(2432.235)
    end = datetime.now()
    print('duration is {}'.format(end-start))


class new_obj:

    def __init__(self,name):
        print('class creation')
        self.name = name
        
    def __str__(self):
        return 'your name is {}'.format(self.name)
    
    def __del__(self):
        print('class delete')
    
    def call_name(self):
        print('Hi')
        
    def sayhello(self,name):
        print('hello {}'.format(name))


class c_sum:
         
    def sum(self):
        return print('sum = {}'.format(self.a+self.b))
        
class c_minus():

    def minus(self):
        return print('minus = {}'.format(self.a-self.b))

class c_cal(c_sum,c_minus):

    def __init__(self,a,b):
        self.a = a
        self.b = b
   
def class_4cal():
    a = c_cal(3,6)
    a.sum()
    a.minus()
    
def class_def():
    a = new_obj('hongsunghee')
    print(a)
    a.call_name()
    a.sayhello('sunghee')
    a.name = 'hsh'
    print(a)
    
def ex_input():
    number_list = input('input your numbers\n')
    print('your number_list is {}'.format(number_list.split(' ')[2]))

def cal_prime(num):    
    p_list = list(range(3,num))
    n_list = list(range(1,num))
    for i in p_list:
        if prime(i) == None:
            n_list.remove(i)
    print(n_list)
                
def prime(number):
    
    if number%2 == 0:
        return
    
    else:    
        for i in range(3,int(number/2),2):
            if number%i ==0:
                return

        return number
  
def jugde(a):
    if a.isalpha():
        print('alpha')
    elif a.isdigit():
        print('digit')
    else:
        print('mix')

def list2dic(a,b):
    dic = {}
    e_a = enumerate(a)
    for i,j in e_a:
        dic[j] = b[i]
    return dic
        
def map_test(a1,a2):
    addmap = lambda a1,a2 : a1*a2
    b = map(addmap,a1,a2)
    return list(b)

def file_io(a):
    f = open('test.txt','w')
    f.write(a)
    f.close()
    
def file_read(file_name):
    f = open(file_name,'r')
    data = f.read()
    print(data)
    f.close()

def file_readline(file_name):
    f = open(file_name,'r')
    i = 1
    data = f.readline()
    while data:
        print('{} line :  {} '.format(i,data),end='')
        data = f.readline()
        i += 1
    f.close()

def file_readline2(file_name):
    f = open(file_name,'r')
    data = f.readlines()
    print(data)
    for i,j in enumerate(data):
        print('{} line : {}'.format(i+1,j),end='')
    f.close()

def number3point(num):

   print('Again')

def delaycha():
    data = input('type your data')
    list_data = list(data)
    first = list_data.pop(0)
    list_data.append(first)
    result = "".join(list_data)
    print(result)

def splitstring(a):
    b = a.split('/')
    print(b[2])

def querystring(a):
    b = a.split('?')
    c = b[1].split('&')
    for i in c:
        print(i)

import string
    
def getTextFreq(filename):
    f = open('test.txt','r')
    data = f.read()
    
    for i in string.ascii_letters[0:55]:
        print('{} => {}'.format(i,data.count(i)))

def getwordfile():
    f = open('test.txt','r')
    data = f.read()
    data_list = data.split()
    print('number of word is {}'.format(len(data_list)))
    
    
def getsomeword(word):
    f = open('test.txt','r')
    data = f.read()
    i = data.count(word)
    print('{} => {}'.format(word,i))
    
def replaceword(old,new):
    f = open('test.txt','r')
    data = f.read()
    new_data = data.replace(old,new)
    
    f1 = open('test2.txt','w')
    f1.write(new_data)
    
    f.close()
    f1.close()
    
from urllib.request import urlopen

def urlread(url):
    with urlopen(url) as f:
        data = f.read().decode()
        print(data)
        f_out = open('urltest.html','w')
        f_out.write(data)
        f_out.close()

def webfiledown():    
    Buffer = 1024*256
    fileurl = 'https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe'
    filename = fileurl.split('/')[-1]
    with urlopen(fileurl) as f:
        with open(filename,'wb') as h:
            buf = f.read(Buffer)
            while buf:
                h.write(buf)
                buf = f.read(Buffer)
    
def filesplite():
    filename = 'python-3.5.2.exe'
    subsize = 1024*1024 # Mbyte
    i = 0
    
    with open(filename,'rb') as f:
        buf = f.read(subsize)
        while buf:
            subfilename = filename + '_' + str(i)
            with open(subfilename,'wb') as h:
                h.write(buf)
            buf = f.read(subsize)
            i += 1
import random            
def lotto():
    num = []
    total_list = list(range(1,45))

    
    random.shuffle(total_list)
    num = total_list[1:6]
    print(num)
        
def couple2():
    a = ['hong','kim','lee']
    b = ['yoon','kang','jung']
    random.shuffle(a)
    random.shuffle(b)
    c = zip(a,b)
    c_list = list(c)
    for i,j in c_list:
        print('{} & {}'.format(i,j))
            

    