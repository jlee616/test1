import sys

def fibo(num):
    ini_list = [0,1]
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [number]")
    num = int(sys.argv[1])
    print(fibo(num))
