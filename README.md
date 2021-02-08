# Counter-Strike: Global Offensive Automatic Text Bind Creator

Python Script that looks for a Counter-Strike: Global Offensive install and either creates or modifies an existing autoexec file with the user's chosen text bind / copy-pasta.
Users can enter which key the want the text bind to be bound to, what the bind is called, and can bind multiple different text binds in one go.

Currently there is a bug that leads to part of the users text bind being cut off.
This only occurs if input text contains newline characters and the text has more than ~500 characters between each newline.
This is due to some limitation on line 23 with sys.stdin.readlines only reading ~500 characters before requiring a newline.
