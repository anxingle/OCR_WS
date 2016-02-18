#coding:utf-8

import ctypes
from ctypes import *
#func = cdll.LoadLibrary('Hello.dll')

func2 = cdll.LoadLibrary('ocrDLL.dll')

stru = 9    #initLibrary()
stru = func2.initLibrary()
print stru

fname = "anxingle3.jpg"
os_path="<root><elem imgPath=\"D:\\Anaconda2.7\\Test_del\\static\\Uploads\\%s\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"李四\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>"%fname
#print os_path
str1 = func2.ocr(os_path,"")
#func2.ocr("<root><elem imgPath=\"D:\\Users\\anxingle3.jpg\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"李四\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>","")

'''
ret = func.IntAdd(6,4)
print(ret)

mypan = "myPan"
str0 = func.show()
size = -1
str0 = ctypes.string_at(str0,size)
str1 = str0.decode('utf-8')
str_split = str1.split(',')
print(str1)
print(str_split)
print(".......")
a = "I love %s"%str_split[2]
print(a)
'''
'''
str1 = func.call_pic('22.jpg')
str1=ctypes.string_at(str1,size)
print(str1)
print(str1.decode('utf-8'))

str2 = func.call_char()
print(str2.value)
str3 =ctypes.string_at(str2[0],size)
print(str2.decode('utf-8'))
'''