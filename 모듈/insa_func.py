#p141 insa_func.py
import hello_funs
import greeting_func

def main():
    print("insa_func 모듈입니다.")
    print("__name__: ",__name__) # __main__출력
    hello_funs.hello()
    greeting_func.greeting() #greeting_func 출력 

main()