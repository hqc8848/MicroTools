import base64
try:
    import pyperclip
    clipboard = True
except ModuleNotFoundError:
    clipboard = False

print("\033[31mHello! \033[0mHere's a tool to encode/decode text by Base-64.")
mode = input("\n\033[34mEncode(E) or Decode(D)?: \033[0m")

# Encode
if mode == "E" or mode == "e":
    text = input("\033[34mEnter the text you want to encode: \033[0m")
    encoded = str(base64.b64encode(text.encode("utf-8")), "utf-8")
    print("\033[2mEncoded text: \033[0m", encoded, sep = "")
    if clipboard:
        pyperclip.copy(encoded)
        print("Text copied to clipboard!")

# Decode
elif mode == "D" or mode == "d":
    text = input("\033[34mEnter the text you want to decode: \033[0m")
    decoded = str(base64.b64decode(bytes(text, "utf-8")).decode("utf-8"))
    print("\033[2mDecoded text: \033[0m", decoded, sep = "")
    if clipboard:
        pyperclip.copy(decoded)
        print("Text copied to clipboard!")

# Wrong mode
else:
    print("\033[31m[ERROR]: Invalid mode! Please enter E/e or D/d.\033[0m")
    
print("\n\033[2mBased on Base-64.\nMade by hqc8848\033[0m")
