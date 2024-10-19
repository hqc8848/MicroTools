try:
	import pyperclip
	clipboard = 1
except ModuleNotFoundError:
	clipboard = 0
print('''\n\033[31mHello! \033[0mHere's a tool to help you input the releases file's link in the website "ghp.ci".''')
publisher = input("\033[34mWho's the pubilsher of the releases file? \033[0m")
code_name = input("\033[34mWhat does the the code called? \033[0m")
version = input("\033[34mHow many is the version of the releases file (input the number in the tag)? \033[0m")
file_name = input("\033[34mWhat does the the releases file called? \033[0m")
github_link = f"https://github.com/{publisher}/{code_name}/releases/download/{version}/{file_name}"
ghproxy_link = f"https://ghp.ci/{github_link}"
print(f"\nThe link that you should input is {github_link}, and the ghp.ci will download {ghproxy_link}.")
if clipboard == 1:
    pyperclip.copy(ghproxy_link)
    print("We've copied the download link in your clipboard!")
print("\n\n\033[2mMade by hqc8848\033[0m")