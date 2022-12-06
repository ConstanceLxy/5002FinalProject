import time


def record(part):
    f = open('record.txt', 'a')
    # Save time
    clock = time.strftime("%Y-%m-%d%H:%M:%S", time.localtime())
    # Write time into record.txt
    f.write(f"time:{clock}  part:{part}  \n")
    f.close()
