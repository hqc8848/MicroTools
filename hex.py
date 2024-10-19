try:
	import pyperclip
	clipboard = 1
except ModuleNotFoundError:
	clipboard = 0
print("\n\033[31mHello! \033[0mHere's a tool to help you input Hex of a color, with the RGB of the color.")
R = int(input("\033[34mEnter the R of the color: \033[0m"))
G = int(input("\033[34mEnter the G of the color: \033[0m"))
B = int(input("\033[34mEnter the B of the color: \033[0m"))
HEXR = hex(R) [2:]
if len(HEXR) < 2:
    HEXR = "0" + HEXR
HEXG = hex(G) [2:]
if len(HEXG) < 2:
    HEXG = "0" + HEXG
HEXB = hex(B) [2:]
if len(HEXB) < 2:
    HEXB = "0" + HEXB
HEX = (HEXR + HEXG + HEXB).upper()
print(f"The Hex of this color is #{HEX}.")
if clipboard == 1:
    pyperclip.copy("#" + HEX)
    print("Copied to clipboard!")
print("\n\n\033[2mMade by hqc8848\033[0m")