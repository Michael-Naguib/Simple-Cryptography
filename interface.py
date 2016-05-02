#BUILD AN ERROR HANDELING SYSTEM
allTasks = []
currentTask = None
allChoices = []
activeChoices = []
currentChoice = None
allCipher = []
#import crypto.py as crypto
allCipherMods[0] = crypto.caesar()
allCipherMods.append(crypto.afine())
allCipherMods.append(crypto.viginere)
allCipherMods.append(crypto.viginereOld)
class choice(object):
	#CREATE A CHOICE AND MAKE IT AVILIABLE
	def __init__(self,name,callback,quickDes,description):
		self.name = name # choice name to display
		self.callback = callback # what should the selection off this choice do
		self.quickDes = quickDes # Quick description to display
		self.description = description # long description with Help
		self.__addChoice()
		return
	def __addChoice(self):
		allChoices.append(self)
		return
	def display(self):
		#returns the string for consistant display
		nameN = self.name
		quickDesN = self.quickDes
		nameN += " " * 10 #MINIMUM 10
		quickDesN += ' ' * 20 #MINIMUM 20
		return nameN[0:10] + " | " + quickDesN[0:20] + " | "
	def activate(arg = None):
		if arg == None:
			self.callback()
		else:
			self.callback(arg)
		return		
	
class task(object):
	def __init__(self,cipherType,msg,keys,name):
		self.cipherType = cipherType
		self.msg = msg
		self.keys = keys
		self.name = name
		self.useMap = crypto.map('abcdefghijklmnopqrstuvwxyz')
		return
	def getPreview(self):
		#Name 7 char, ciphertype 12 char, msg 15 char keys: 16
		nameN = self.name+ (' ' * 7)
		nameN = nameN[0:7]
		keysN = self.keys
		cipherTypeN = self.cipherType + ( " " * 12)
		cipherTypeN = cipherTypeN[0:12]
		if keysN == str:
			keysN = self.keys + (' ' * 16)
		elif keysN == int:
			keysN = str(self.keys) + (' ' * 16)
		elif keysN == lst:
			keysN = 'Add:' + str(keysN[0]) + "," + 'Mult:' + str(keysN[1])
		keysN = keysN[0:16]	
		msgN = self.msg + (' ' * 15)
		msgN = msgN[0:15]
		return nameN + " | " + cipherTypeN + " | " + keysN + " | " + msgN + " | "
	def __CTO(self):
		for cipher in allCipher:
			if cipher.cipherType == self.cipherType:
				return cipher
			else:
				continue
		return
	def decryptDisplay(self):
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print('Decrypted Text:')
		print(str(self.__CTO().decrypt(self.msg,self.keys)))
		return
	def encryptDisplay(self):
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print('Encrypted Text:')
		print(str(self.__CTO().encrypt(self.msg,self.keys)))
		return
	def noKeysDecryptDisplay(self):
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print('Auto Decrypted:')
		nkd = self.__CTO().noKeysDecrypt(self.msg)
		if self.cipherType == 'afine':
			print('Add Key: ' + str(nkd[1][0]))
			print('Mult. Key: ' + str(nkd[1][1]))
		else:
			print('Key: ' + str(nkd[1]))
		print('Text:')
		print(nkd[0])
		return
def listActiveChoices(indexCoefficient = 0):
	#PRINT all choices and their display
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Please type the number of the choice you wish to select")
	global activeChoices
	print("Choice     | Quick Description    |")
	for indexAlpha in range(0,len(activeChoices)):
		print(indexAlpha.display())
	print('No more choices')
	return
def askChoice(passValue = 'none'):
	#THIS FUNCTION SHOULD LOOK AT THE CHOICES Active Choices AND BASED UPON
	#THEIR INDEX ASK THE USER TO PICK ONE AND RUN THE CALLBACK
	answer = int(input("Choice number: "))
	if ((answer < 1 ) | (answer > len(activeChoices))):
		print('You did not type a valid number')
		askChoice()
	else:
		activeChoices[answer].callback()
	return 
def exit():
	#ASk the user if they want to exit to the main menue or exit the program
	#SHOULD EXIT AND GO TO THE MAIN MENU/ the start()
	return True
def createTask():
	#CREATE TASK ask the questions etc ask what t do next with showActiveChoices() and askChoice()
	#auto asign as the current task but append it first to allTasks
	return True
def deleteTask():
	#ASKS THE USER WHAT TASK THEY WANT TO  DELETE Then does that
	#etc ask what t do next with showActiveChoices() and askChoice()
	
	return True
def previewAllTasks():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print('All Tasks')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	global allTasks
	if allTasks == []:
		print('There are no Tasks, go and make one')
	else:
		print('Name    | Cipher Type  | Key\s           | Message        ')
		print('----------------------------------------------------------')
		for taskn in range(0,len(allTasks)):
			print(taskn.getPreview())
		print('No more Tasks')
	#LOOKS AT THE CURRENT TASKS LIST AND DISPLAYS THEM WATCHES FOR EMPTY LIST
	#then ask what t do next with showActiveChoices() and askChoice()
	#CREATE A CHOICE THAT TAKES USER INPUT AND SETS GLOBAL TASK TO CURRENT TASK ONLY DO THIS UNLESS altasks != []
	return
def validateString(arg):
	#general validation for strings/user input
	return True
def validateInt(arg):
	#general validation for number/ user input
	return True
def editTask():
	#should look to current task preview it then ask the user what they want to overide
	return True
def createTaskDisplay():
	#looks at the cipherName of the currentTask and asigns a standardized way to display it
	#give the option to tell it to graph the frequency Visually----->SEE graphFrequency!!!!!!!!!!!
	#SHOULD GIVE THE CURRENT TASK A .display() method-- that does this---> checks if already present
	return True
def displayTask():
	#should call the .display() on the currentTask and then showActiveChoices etc....
	return True
def graphFrequency():
	#get the frequency of the currentTask make it able to iterate through a list of lists frequency
	#THIS IS AN ADD ON TO CREATE TASK DISPLAY
	return True
def start():
	#THE main Menue that asks the user for initial input
	return True
def setActiveChoices(arg):
	#TAKES a list of number indexes that correspond to allChoices and appends to and OVERIDES to these choices in the activeChoices
	global activeChoices
	activeChoices = []
	for index in arg:
		activeChoices.append(allChoices[index])
	return
def devMode():
	# TAKES DIRECT INPUT FROM USER NO VALIDATION!!!! FOR DEBUGGING
	return True
choice('Create Task', createTask,'Create a new Task', "This choice allows you to create a a new cryptography task that you can later access for your needs")
choice('Edit Task', editTask, 'Edit a Task', 'This allows you to preview then edit previous tasks' )
choice('Exit', exit, 'Exit', 'Exit to the main menu or exit the program')
choice('Preview the current Task', previewTask, "Shows information about the most recent Task","Shows information about the most recent Task")
choice('Show All Tasks',showAllTasks,'Look at previous tasks','Look at previous tasks')
choice('Main Menue',start,'Retrun to the main menue',' Will return you to the main menue')
choice('Dev',devMode,'---------',' For Debugging and devlopers, directly input code')
start()# START THE INTERFACE THE FIRST TIME
