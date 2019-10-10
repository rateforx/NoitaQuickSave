import os
import shutil

appdataLoc = os.getenv('APPDATA')
cwd = os.getcwd()
if not os.path.exists(cwd + "\\saves"):
    os.makedirs(cwd + "\\saves")

appdataLoc = appdataLoc.replace("\\Roaming","")
# saveLoc = appdataLoc + '\\LocalLow\\Nolla_Games_Noita\\save00'
saveLoc = appdataLoc + '\\LocalLow\\Nolla_Games_Noita'

# filesToMove = ("world_state.salakieli","player.salakieli","magic_numbers.salakieli","world")
filesToMove = "save00"

def loadSave(argument):
    if not os.path.exists(cwd + "\\saves\\" + argument):
        print("This savegame does not exist!")
    else:
        try:
            for file in filesToMove:
                if not file == "world":
                    if  os.path.exists(saveLoc + "\\" + file):
                        os.remove(saveLoc + "\\" + file)
                    shutil.copy(cwd + "\\saves\\" + argument + "\\"  + file , saveLoc + "\\")
                else:
                    if  os.path.exists(saveLoc + "\\" + file):
                        shutil.rmtree(saveLoc + "\\" + file)
                    shutil.copytree(cwd + "\\saves\\" + argument + "\\" + file, saveLoc + "\\" + "world")
            print("Game loaded!")
        except:
            try:
                os.removedirs(cwd + "\\saves\\" + argument)
                print("Loading file failed, please try again.")
            except:
                print("Loading file failed, please try again.")
                print("Cleanup failed, if your game acts up you might want to manually clean the save location.")

def saveGame(argument):
    if os.path.exists(cwd + "\\saves\\" + argument):
        print("This savegame already exists!")
    else:
        os.makedirs(cwd + "\\saves\\" + argument)
        try:
            for file in filesToMove:
                if not file == "world":
                    shutil.copy(saveLoc + "\\" + file, cwd + "\\saves\\" + argument + "\\")
                else:
                    shutil.copytree(saveLoc + "\\" + file, cwd + "\\saves\\" + argument + "\\" + "world")
            print("Game saved!")
        except:
            try:
                os.removedirs(cwd + "\\saves\\" + argument)
                print("One or more of the save files couldn't be found, the save was cancelled.")
            except:
                print("One or more of the save files couldn't be found, the save was cancelled.")
                print("Cancelling the save failed too, because apparently this script is worthless or it's not allowed to remove the mess it leaves behind.")
                print("You might want to /delete the save you tried to create or manually remove the broken save, loading it might be a bad idea")
