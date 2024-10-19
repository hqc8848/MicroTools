from random import choice as ch
def ordinal(num: int):
    strNum = str(num)
    if len(strNum) != 1 and strNum[-2] == "1":
        return "th"
    else:
        if strNum[-1] == "1":
               return "st"
        elif strNum[-1] == "2":
            return "nd"
        elif strNum[-1] == "3":
            return "rd"
        else:
            return "th" 

print("\n\033[31mHello! \033[0mHere's a tool to help you choose things.")
how_many = int(input("\033[34mHow many things do you want to choose? \033[0m"))
if how_many == 0 or how_many == 1:
    print("What?")
    quit()
choose = []
for i in range(how_many):
    choose.append(input(f"\033[34mEnter the {i + 1}{ordinal(i + 1)} thing: \033[0m"))
print(f"Just choose {ch(choose)}!")
print("\n\n\033[2mMade by hqc8848\033[0m")