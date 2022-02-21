# Compare Grand Theft Auto Online Background Scirpts


Quick script deigned for downloding/viewing latest changes between bg_script.rpf for GTA Online (PC/Xbox/PS4)



# Setup


Download Python 
https://www.python.org/downloads/windows/

Note: On the first screen, enable the “Add Python 3.6 to PATH” option and then click “Install Now.”


Download GTA Background script:

Link: http://prod.cloud.rockstargames.com/titles/gta5/pcros/bgscripts/bg_ng_944_1.rpf

Every Tuesday/Thursday they tend release a new update, run it periodically throughout the day or stick it on server and leave it running


# Download rockstarMD5Comparer.py

Download Link:
https://github.com/LunusPixel/Compare-GTA-Scripts/releases/tag/Release



# Run:


Open up CMD - Press Winkey + R so you bring up the "RunBox" type “cmd” into the box and then press Ctrl+Shift+Enter to run CMD as an administrator


Navigate to your directory with `rockstarMD5Comparer.py` 
Example:

`cd c:/users/ENTER_YOUR_PC_NAME_HERE_OR_USER_NAME/desktop` and hit enter


 `python rockstarMD5Comparer.py` 


Will output if MD5 has chnaged for the file (Once they update the background script they tend change the MD5 hash for the file each time)




Note: You can add tweepy so it tweets the changes, if you would like to see this functionality added then open a new issue. 
Thanks @Prince25 for the help on this
