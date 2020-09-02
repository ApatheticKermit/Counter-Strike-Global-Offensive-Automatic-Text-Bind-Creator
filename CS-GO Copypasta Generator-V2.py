import math
import sys
import os.path

dr = [chr(i) for i in range(ord('A'), ord('Z')+1)] # Creates a list of letters A-Z and looks for drives from this list
drives = [d for d in dr if os.path.exists(f'{d}:')] # Creates a list of all drives on the user's PC

def find(name, path): # Function that finds the location of the csgo\cfg folder location so that the created autoexec is put there automatically.
    for root, dirs, files in os.walk(path): # Function that finds the location of the csgo\cfg folder location so that the created autoexec is put there automatically.
        if name in files: # Function that finds the location of the csgo\cfg folder location so that the created autoexec is put there automatically.
            return os.path.join(root, name) # Function that finds the location of the csgo\cfg folder location so that the created autoexec is put there automatically.

for drive in drives: # Iterates through the list of drives on the user's PC and breaks the loop if the csgo folder is found
    try: # Iterates through the list of drives on the user's PC and breaks the loop if the csgo folder is found
        cs_folder_location_path = find("gameps3.cfg",str(drive)+":\\")[:-11] # Iterates through the list of drives on the user's PC and breaks the loop if the csgo folder is found
        break # Iterates through the list of drives on the user's PC and breaks the loop if the csgo folder is found
    except: # Iterates through the list of drives on the user's PC and breaks the loop if the csgo folder is found
        pass # Iterates through the list of drives on the user's PC and breaks the loop if the csgo folder is found

def line_prepender(filename2, line): # Function that writes text at the start of a file
    with open(filename2, 'r+') as f: # Function that writes text at the start of a file
        content = f.read() # Function that writes text at the start of a file
        f.seek(0, 0) # Function that writes text at the start of a file
        f.write(line.rstrip('\r\n') + '\n' + content) # Function that writes text at the start of a file

auto_check = find("autoexec.cfg",cs_folder_location_path) # Auto looks for autoexec file

if auto_check != None: # If the user already has an auto exec file it carries on with the code
    pass
else: # if there is no autoexec it creates a new autoexec file in the csgo\cfg folder
    f = open(str(cs_folder_location_path)+"autoexec.cfg","w+")

def csgo(): # The function that actually makes the binds
    cfg_dict = {} # Creates an empty dict that will store each of the copypasta lines
    key = str(input("Please enter the key you wish to bind the copypasta to: ")) # Gets the key the user wishes to bind the copypasta to
    while key not in ["kp_end","kp_downarrow","kp_pgdn","kp_leftarrow","kp_5","kp_rightarrow","kp_uparrow","kp_pgup","kp_ins","kp_del","kp_slash","kp_multiply","kp_minus","kp_plus","kp_enter","ins","del","home","end","pgup","pgdn","uparrow","leftarrow","downarrow","rightarrow","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","space","-","=","[","]","\\","semicolon","'",",",".","/","backspace","tab","enter","capslock","shift","rshift","ctrl","rctrl","alt","ralt","mouse1","mouse2","mouse3","mouse4","mouse5","mwheeldown","mwheelup"]:
        key = str(input("The key you wished to bind the copypasta to was invalid.\nPlease re-enter the key you wish to bind the copypasta to.\nIf the error persists go to 'https://totalcsgo.com/binds/keys' and look for the appropriate source bind code there: "))
    # Makes sure that the key input is valid for csgo
    pastaname = str(input("Please enter the name of your copypasta: ")) # Gets the name of the specific pasta
    new_line_check = input("Does the copypasta have any newlines, like \n this? Please enter Y for Yes or N for No: ") # Checks if the pasta has any new lines or returns in it
    while new_line_check not in["Y","N"]: # Only allow Yes or No
        new_line_check = input("Does the copypasta have any newlines, like \n this? Please enter Y for Yes or N for No: ") # Only allow Yes or No
    if new_line_check == "Y": # If it does have run on lines then 
        print("Please enter the copypasta, then directly after enter Cntrl-Z on its own line to indicate the end of the copypasta: ")
        text = str(sys.stdin.readlines())[2:-4]
        print(text)
    else:
        text = str(input("Please enter the copypasta: ")).replace("\n"," ").replace("'","\'").replace('"',"\"")

    for i in range(math.ceil(len(text)/126)):
        cfg_dict[i] = 'alias "' +str(pastaname)+str(i)+ '" "say '+ text[i*126:(i+1)*126]     +' ; alias '+ str(pastaname) +' '+str(pastaname)+ str(i+1) +'"\n'
    cfg_dict[len(cfg_dict)-1] = 'alias "' +str(pastaname)+str(len(cfg_dict)-1)+ '" "say '+ text[i*126:(i+1)*126]     +' ; alias '+ str(pastaname) +' '+str(pastaname)+ "0" +'"\n'

    final_cfg = "bind {} {}\nalias {} {}0\n".format(key,pastaname,pastaname,pastaname)
    for i in cfg_dict:
        final_cfg += (cfg_dict[i])
    if auto_check != None:
        line_prepender(str(cs_folder_location_path)+"autoexec.cfg",final_cfg)
    else:
        f.write(final_cfg)

csgo()

choice2 = input("Do you wish to bind another copypasta in the same file? Please enter Y for Yes or N for No: ") 
while choice2 not in["Y","N"]:
    choice2 = input("Do you wish to bind another copypasta in the same file? Please enter Y for Yes or N for No: ")
while choice2 != "N":
    csgo()
    f.write("\n")
    choice2 = input("Do you wish to bind another copypasta in the same file? Please enter Y for Yes or N for No: ")

if auto_check != None:
    pass
else:
    f.write("host_writeconfig")
    f.close()
    print("Right Click on CS-GO in your steam library, select 'Properties...', in the 'General' tab click on 'Set Launch Options...', copy and paste:\n+exec autoexec.cfg\ninto the text box and click 'OK'")
quit_check = input("Enter anything to quit the program:  ")


