import os
import pyttsx3
while True:
	print("Chrome")
	print("calculator")
	print("window media player")
	print("camera ")
	text=input("from the list enter any application u want to run:")
	programs=['chrome',"whatsapp",'calculator',"window media player","camera"]
	i=0
	#print("outside exit")
	if "exit" in text or "quit" in text:
		#print("entered exit")
		exit()
	elif "run" in text or "execute" in text:
		while i<len(programs):
			print("entered while loop")
			if programs[i] in text:
				run=programs[i]
				if run=="chrome":
					pyttsx3.speak("opening chrome for u")
					#print("helo")
					os.system("start chrome")
					break
				elif run=="calculator":
					pyttsx3.speak("opening calculator for u")
					os.system("calc")
					break
				elif run=="whatsapp":
					pyttsx3.speak("opening whatsapp")
					os.system("WhatsApp")
					break
				elif run=="window media player":
					pyttsx3.speak("opening player for u")
					os.system("start wmplayer")
					break
				elif run=="camera":
					#pyttsx3.speak("opening camera for u")
				 	os.system("start microsoft.windows.camera:")
				 	break
			else:
				i=i+1
				#print(i)
		else:	 			
			print("enter correct name")
else:
	print("please write the application")				