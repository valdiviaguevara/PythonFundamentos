# -*- coding: utf-8 -*-
import curses, os #curses is the interface for capturing key presses on the menu, os launches the files
def Botones_Formularios(eixo_x_botones,eixo_y_botones):
  screen = curses.initscr() #initializes a new window for capturing key presses
  curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
  curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
  curses.start_color() # Lets you use colors when highlighting selected menu option
  box = curses.newwin( 3, 36, eixo_y_botones, eixo_y_botones)
  box.keypad(1) # Capture input from keypad
  # Change this to use different colors when highlighting
  curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
  getin = None #user input on top menu
  # This function controls what is displayed on the top menu (the menu first loaded when script is run)
  def topmenu():
    #Not sure if the following two lines are needed since I declare it at beginning of program, but here for safety
    box.keypad(1)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
    pos=0 #pos is the position of the hightlighted menu option.  Every time topmenu is called, position retuns to 1, when topmenu ends the position is returned and tells the program what option   has been selected
    x = None #control for while loop, let's you scroll through options until return key is pressed then returns pos to program
    h = curses.color_pair(1) #h is the coloring for a highlighted menu option
    n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
    # Loop until return key is pressed
    while x !=ord('\n'):
      box.clear() #clears previous screen on key press and updates display based on pos
      box.border(0)
      # Detects what is higlighted, every entry will have two lines, a condition if the menu is highlighted and a condition for if the menu is not highlighted
      # to add additional menu options, just add a new if pos==(next available number) and a correspoonding else
      # I keep exit as the last option in this menu, if you do the same make sure to update its position here and the corresponding entry in the main program
      Labels_Aceitar="Aceitar"
      long_Labels_Aceitar=len(Labels_Aceitar)
      Labels_Limpar="Limpar"
      long_Labels_Limpar=len(Labels_Limpar)
      Labels_Voltar="Voltar"
      long_Labels_Voltar=len(Labels_Voltar)
      if pos==1:
        box.addstr(1,2, Labels_Aceitar, h)
      else:
        box.addstr(1,2, Labels_Aceitar, n)
      if pos==2:
        box.addstr(1,long_Labels_Aceitar+10,Labels_Limpar, h)
      else:
        box.addstr(1,long_Labels_Aceitar+10, Labels_Limpar, n)
      if pos==3:
        box.addstr(1,long_Labels_Aceitar+long_Labels_Limpar+15, Labels_Voltar, h)
      else:
        box.addstr(1,long_Labels_Aceitar+long_Labels_Limpar+15, Labels_Voltar, n)
      box.refresh()
      x = box.getch() # Gets user input
      # What is user input? This needs to be updated on changed equal to teh total number of entries in the menu
      # Users can hit a number or use the arrow keys make sure to update this when you add more entries
      if x == ord('1'):
        pos = 1
      elif x == ord('2'):
        pos = 2
      elif x == ord('3'):
        pos = 3
      elif x == 261:
      # This needs to be updated on changes to equal the total number of entries in the menu
        if pos < 3:
      # This doesn't need to be changed no matter how many entries you have
          pos += 1
        else: pos = 1
      elif x == 260:
        if pos > 1:
          pos += -1
    # This needs to be updated on changes to equal the total number of entries in the menu
        else: pos = 3
      elif x != ord('\n'):
        curses.flash()
    return ord(str(pos))
  # Main program
  # This needs to be updated on changes equal to the number you use for exit
  while getin != ord('3'): #Loop until the user chooses to exit the program
    getin = topmenu() # Get the menu item selected on the top menu
    if getin == ord('1'): # Top menu option 1
      #Beginning of submenu 1 control logic
      # This needs to be updated on changes equal to the number of menu items in submenu 1
      os.system('dosbox2 /path/to/EXE -conf /path/to/dosbox.conf -exit') #Launches a dosbox program, exits back to menu after program ends
    elif getin == ord('2'): # Topmenu option 2
      os.system('uqm')
    elif getin == ord('3'): # Topmenu option 3
      os.system('') #VITAL!  This closes out the menu system and returns you to the bash prompt.
eixo_x_botones=8
eixo_y_botones=2
Botones_Formularios(eixo_x_botones,eixo_y_botones)
