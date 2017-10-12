import os
path =''
print('please input the location of the gps-igr file')
file_name=input()
infile=open('C:\\Users\\廖斐凡\\Desktop\\新建文件夹 (2)\\brdc2800.17n','r')
nfile=infile.readlines()
nfile_header=nfile[0:8]
nfile=nfile[8:]
f_t=[]

def chunks (arr,n):
    return[arr[i:i+n] for i in range(0,len(arr),n)]
nf_sta_tims=chunks(nfile,8)
