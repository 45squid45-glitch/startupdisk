import os
import ast
import time
import getpass

username = getpass.getuser()
file_path = "A:\launchcode.txt"  

txtlaunchcode = None
while txtlaunchcode == None:

    try:
        with open(file_path, 'r') as file:
            txtlaunchcode = file.read()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if txtlaunchcode is not None:
    code = ast.literal_eval(txtlaunchcode)
if str(code) == "netflix":
    os.startfile(r"C:\Users\\" + username + r"\Desktop\Netflix.lnk")
elif str(code) == "edge":
    os.startfile(r"C:\Users\\" + username + r"\Desktop\Personal - Edge.lnk")
elif str(code) == "minecraft":
    os.startfile(r"C:\Users\\" + username + r"\Desktop\Minecraft for Windows.lnk")
