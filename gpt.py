# -*- coding:utf-8 -*-
import struct

def Drivepartition(pt) :
    start = struct.unpack("<Q",pt[32:32+8])
    #num = struct.unpack('<L', pt[12:12+4])

    print '[GPT Partition] 시작위치 : %10d  ' % (start)
    print '                크기 : 20 MB'

if __name__ == '__main__' :
    f = raw_input("파일을 입력하세요 : ")

    f=open(f,'rb')

    f.seek(0)

    gpt = f.read()

    pt = []

    for i in range(128) :
        pt.append(gpt[0x400 + (i*0x80): 0x400 +(i*0x80) + 0x80])


    for i in range(128) :
        p = pt[i]
        if ord(p[0]) != 0 :
            Drivepartition(p)
        else :
            print '파티션 없음'
            break


f.close()