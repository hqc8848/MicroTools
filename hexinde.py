import os
try:
    import pyperclip
    clipboard = True
except ModuleNotFoundError:
    clipboard = False
# Whole ISO 8859-1 (Latin-1) Table
charList = [
    "\u0000", "\u0001", "\u0002", "\u0003", "\u0004", "\u0005", "\u0006", "\u0007", "\u0008", "\u0009", "\u000a", "\u000b", "\u000c", "\u000d", "\u000e", "\u000f",
    "\u0010", "\u0011", "\u0012", "\u0013", "\u0014", "\u0015", "\u0016", "\u0017", "\u0018", "\u0019", "\u001a", "\u001b", "\u001c", "\u001d", "\u001e", "\u001f",
    " ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?",
    "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_",
    "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "\u007f"
    "\u0080", "\u0081", "\u0082", "\u0083", "\u0084", "\u0085", "\u0086", "\u0087", "\u0088", "\u0089", "\u008a", "\u008b", "\u008c", "\u008d", "\u008e", "\u008f",
    "\u0090", "\u0091", "\u0092", "\u0093", "\u0094", "\u0095", "\u0096", "\u0097", "\u0098", "\u0099", "\u009a", "\u009b", "\u009c", "\u009d", "\u009e", "\u009f",
    "\u00a0", "¡", "¢", "£", "¤", "¥", "¦", "§", "¨", "©", "ª", "«", "¬", "\u00ad","®", "¯",
    "°", "±", "²", "³", "´", "µ", "¶", "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿",
    "À", "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï",
    "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß",
    "à", "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï",
    "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷", "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ"

]

os.system("clear && figlet HEXINDE")
print("\033[2mHex -> Hexadecimal | in -> Sounds like \"en\", encode | de -> decode\033[0m")
print("\n\033[31mHello! \033[0mThis is a tool to encode/decode the information you enter.")
mode = input("\033[34mEncode(E) or Decode(D)?: \033[0m")
# Encode
if mode == "E" or mode == "e":
    text = input("\033[34mEnter the text you want to encode: \033[0m")
    encodedText = ""
    for char in text:
        encodedText += hex(charList.index(char))[2:].upper()
    print("\033[2mEncoded text: \033[0m" + encodedText)
    if clipboard:
        pyperclip.copy(encodedText)
        print("Text copied to clipboard!")
# Decode
elif mode == "D" or mode == "d":
    text = input("\033[34mEnter the text you want to decode: \033[0m")
    eachByte = [text[i:i+2] for i in range(0, len(text), 2)]
    decodedText = ""
    for byte in eachByte:
        decodedText += charList[int(byte, 16)]
    print("\033[2mDecoded text: \033[0m" + decodedText)
    if clipboard:
        pyperclip.copy(decodedText)
        print("Text copied to clipboard!")
# Wrong mode
else:
    print("\033[31m[ERROR]: Invalid mode! Please enter E/e or D/d.\033[0m")
print("\n\n\033[2mBased on ISO 8859-1 (Latin-1).\nMade by hqc8848\033[0m")