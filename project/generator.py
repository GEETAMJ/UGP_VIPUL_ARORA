import sys
import codecs
import re
def generate(ifname,ofname):
    y=[]
    fp=codecs.open(ifname,'r','utf-8')
    z=[]
    for x in fp:
        #y=y+re.split('; |, |\*|\n',x)
        y=y+x.split('.')
    print(y)
    fp.close()
    fo=codecs.open(ofname,'w','utf-8')
    for x in y :
        if x=="\n":
            continue
        fo.write("11"+"\t"+x.strip(' #\t\n\r')+"\t"+"0.9")
        fo.write("\n")
    fo.close()



def main():

    try:
        _, ifname ,ofname = sys.argv
    except Exception as e:
        print(e)
        sys.exit(0)

    generate(ifname,ofname)

if __name__=='__main__':
    main()
