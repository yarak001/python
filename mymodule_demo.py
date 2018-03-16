import mymodule
import asia.korea.korm as kor


mymodule.say_hi()
print("Version", mymodule.__version__)

for prop in dir(mymodule):
    print("---", prop,)

kor.print_kor()