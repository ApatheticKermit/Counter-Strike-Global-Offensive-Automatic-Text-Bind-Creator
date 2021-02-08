import math
import sys
import os.path

def csgo(): # Main function that actually creates the bind in the autoexec file
    cfg_dict = {} 
    key = str(input("Please enter the key you wish to bind the copypasta to: "))
    while key not in ["kp_end","kp_downarrow","kp_pgdn","kp_leftarrow","kp_5","kp_rightarrow","kp_uparrow", # Makes sure that the key input is valid for csgo
	    "kp_pgup","kp_ins","kp_del","kp_slash","kp_multiply","kp_minus","kp_plus","kp_enter","ins","del","home","end","pgup","pgdn","uparrow","leftarrow","downarrow",
	    "rightarrow","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l",
	    "m","n","o","p","q","r","s","t","u","v","w","x","y","z","space","-","=","[","]","\\","semicolon","'",",",".","/","backspace","tab","enter","capslock","shift","rshift",
	    "ctrl","rctrl","alt","ralt","mouse1","mouse2","mouse3","mouse4","mouse5","mwheeldown","mwheelup"]:
        key = str(input("The key you wished to bind the copypasta to was invalid. Please re-enter the key you wish to bind the copypasta to.\n"
                        "If the error persists go to 'https://totalcsgo.com/binds/keys' and look for the appropriate source bind code there: "))
    pastaname = str(input("Please enter the name of your copypasta: ")) 
    new_line_check = input("Does the copypasta have any newlines, like \n this? Please enter Y for Yes or N for No: ")

    while new_line_check not in["Y","N"]:
        new_line_check = input("Does the copypasta have any newlines, like \n this? Please enter Y for Yes or N for No: ")

    if new_line_check == "Y":
        print("Please enter the copypasta, then directly after enter Cntrl-Z on its own line to indicate the end of the copypasta: ")
        text = str(sys.stdin.readlines())[2:-4]
        text = text.replace("\\n', '"," ").replace( "  "," ").replace("""\\n", '""",'').replace("\\'","'").replace('''\\n", "''','').replace('''\\n', "''','').replace('"',"\''")
    else:
        text = str(input("Please enter the copypasta: ")).replace("\n"," ").replace("'","\'").replace('"',"""\''""")

    for i in range(math.ceil(len(text)/126)):
        cfg_dict[i] = 'alias "' +str(pastaname)+str(i)+ '" "say '+ text[i*126:(i+1)*126] +' ; alias '+ str(pastaname) +' '+str(pastaname)+ str(i+1) +'"\n'
    cfg_dict[len(cfg_dict)-1] = 'alias "' +str(pastaname)+str(len(cfg_dict)-1)+ '" "say '+ text[i*126:(i+1)*126] +' ; alias '+ str(pastaname) +' '+str(pastaname)+ "0" +'"\n'

    final_cfg = "bind {} {}\nalias {} {}0\n".format(key,pastaname,pastaname,pastaname)
    for i in cfg_dict:
        final_cfg += (cfg_dict[i])
    if autoexec_check != None:
        line_prepender(str(cs_folder_location_path)+"autoexec.cfg",final_cfg)
    else:
        f.write(final_cfg)

def find(name, path):			# Function that finds the location of the csgo\cfg folder location so that the created autoexec is put there automatically.
    for root, dirs, files in os.walk(path): 
        if name in files: 
            return os.path.join(root, name) 

def line_prepender(filename2, line):			# Function prepends text (writes text at the start of a file
    with open(filename2, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n\n' + content)

cs_folder_location_path = "FAIL"
no_cs_folder = False

dr = [chr(i) for i in range(ord('A'), ord('Z')+1)]			# Creates a list of letters A-Z and looks for drives from this list
drives = [d for d in dr if os.path.exists(f'{d}:')]			# Creates a list of all drives on the user's PC

print("Currently looking for your CS:GO folder, please be patient...")
for drive in drives:			# Looks for User's CSGO folder
    try: 
        cs_folder_location_path = find("gameps3.cfg",str(drive)+":\\")[:-11] 
        break 
    except: 
        pass

if cs_folder_location_path == "FAIL":
    no_cs_folder = True
    cs_folder_location_path = os.getcwd() + "\\"

autoexec_check = find("autoexec.cfg",cs_folder_location_path)

if autoexec_check != None:
    pass
else: 
    f = open(str(cs_folder_location_path)+"autoexec.cfg","w+")

csgo()

multiple_bind_check = input("Do you wish to bind another copypasta in the same file? Please enter Y for Yes or N for No: ") 
while multiple_bind_check not in["Y","N"]:
    multiple_bind_check = input("Do you wish to bind another copypasta in the same file? Please enter Y for Yes or N for No: ")
while multiple_bind_check != "N":
    csgo()
    multiple_bind_check = input("Do you wish to bind another copypasta in the same file? Please enter Y for Yes or N for No: ")

if autoexec_check != None:
    pass
else:
    f.write("host_writeconfig")
    f.close()
    if no_cs_folder == True:
        print("The created autoexec file is placed in whichever folder this python file was placed and ran from as CSGO was not found installed on your computer.")
    print("Right Click on CS-GO in your steam library, select 'Properties...', in the 'General' tab click on 'Set Launch Options...', copy and paste:"
        "+exec autoexec.cfg\ninto the text box and click 'OK'")
input("Enter anything to quit the program:  ")
