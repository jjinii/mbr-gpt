# -*- coding:utf-8 -*-
import struct

def Drivepartition(pt) :
    start = struct.unpack('<L',pt[8:8+4])
    num = struct.unpack('<L', pt[12:12+4])

    print '[MBR Partition] 시작위치 : %10d  ' % (start)
    print '                크기 : %s' % (num)

if __name__ == '__main__' :
    f = raw_input("파일을 입력하세요 : ")

    f=open(f,'rb')

    f.seek(0)

    mbr = f.read(0x200)

    if ord(mbr[510]) == 0x55 and ord(mbr[511]) == 0xAA :
        print 'MBR 읽기 성공'

        pt = []

        for i in range(4) :
            pt.append(mbr[0x1BE + (i*0x10): 0x1BE +(i*0x10) + 0x10])

        for i in range(4) :
            p = pt[i]
            if ord(p[4]) == 0xF or ord(p[4]) == 0x5 :
                print "[EBR Partition]"
            elif ord(p[4]) != 0 :
                Drivepartition(p)

else:
    print 'MBR 읽기 실패'

f.close()
