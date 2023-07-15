def dec1(func):
    def dec2():
        print("excecuted in dec2")
        func()
        print("excuted in func")
    return dec2
@dec1
def main():
    print("executed in main")
main()    