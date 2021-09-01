#----------------------------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# KHauser, 2021-Aug-30, Modified to add tracks on a CD
# KHauser, 2021-Aug-31d, Modified code to incorporate appropriate properties and methods
#----------------------------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'c':
        if not lstOfCDObjects:
            print('No items to show\n')
        else:
            IO.ScreenIO.show_inventory(lstOfCDObjects)
            while True:
                try:
                    cd_idx = int(input('Select the CD / Album index: '))
                    cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
                    break
                except ValueError:
                    print('Please enter an integer')
                except:
                    print('CD does not exist - try again')
               # try:
               #     cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
               #     break
               # except:
               #     print('ID not valid')
            while True:
                IO.ScreenIO.print_CD_menu()
                strSubChoice = IO.ScreenIO.menu_CD_choice()
                
                if strSubChoice == 'x':
                    break
                
                if strSubChoice == 'a':
                    tplTrackInfo = IO.ScreenIO.get_track_info()
                    PC.DataProcessor.add_track(tplTrackInfo, cd)
                    
                elif strSubChoice =='d':
                    try:
                        IO.ScreenIO.show_tracks(cd)
                    except:
                        print('No tracks to display\n')
                    
                elif strSubChoice == 'r':
                    IO.ScreenIO.show_tracks(cd)
                    try:
                        track_idx = int(input('Select a track to remove: '))
                        cd.rmv_track(track_idx)
                    except:
                        print('No tracks to remove\n')
                    
                else:
                    print('There was an error with your selection')
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')