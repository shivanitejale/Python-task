import pyttsx3
import os

# pyttsx3.speak("Welcome to my tools")


while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	# print(p)
	# os.system(p)

	if  (("run" in p) or ("open" in p))  and (("chrome" in p) or ("browser" in p)):
	  os.system("chrome")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif (("run" in p) or ("open" in p))  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")

	elif (("run " in p) or ("open " in p) or ("execute" in p))  and (("android" in p) and ("studio" in p)):
	  os.system("studio64")

	elif (("run " in p) or ("open " in p) or ("execute" in p))  and (("visual" in p) and ("studio" in p) and ("code" in p) or  ("visual studio" in p)):
	  os.system("Code")

	elif (("run " in p) or ("open " in p) or ("execute" in p))  and (("paint" in p) and ("mspaint" in p)):
	 os.system("mspaint")

	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("dont support")
