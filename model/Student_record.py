import time
def record(part):
    f=open('record.txt','a')
    #save time
    clock = time.strftime("%Y-%m-%d%H:%M:%S",time.localtime())
    #write time into record.txtx
    f.write(f"time:{clock}  part:{part}  \n")
    f.close()