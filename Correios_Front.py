import curses,os
def Botones_Formularios(eixo_x_botones,eixo_y_botones,Tecla,Nome_Arquivo):
  screen_Botones = curses.initscr() #initializes a new window for capturing key presses
  curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
  curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
  curses.start_color() # Lets you use colors when highlighting selected menu option
  box_Botones = curses.newwin( 3, 36, eixo_y_botones, eixo_y_botones)
  box_Botones.keypad(1) # Capture input from keypad
  # Change this to use different colors when highlighting
  curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
  getin = None #user input on top menu
  # This function controls what is displayed on the top menu (the menu first loaded when script is run)
  def topmenu():
    #Not sure if the following two lines are needed since I declare it at beginning of program, but here for safety
    box_Botones.keypad(1)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
    pos=1
    x = None #control for while loop, let's you scroll through options until return key is pressed then returns pos to program
    h = curses.color_pair(1) #h is the coloring for a highlighted menu option
    n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
    # Loop until return key is pressed
    while x !=ord('\n'):
      box_Botones.clear() #clears previous screen_Botones on key press and updates display based on pos
      box_Botones.border(0)
      Labels_Aceitar="Aceitar"
      long_Labels_Aceitar=len(Labels_Aceitar)
      Labels_Limpar="Limpar"
      long_Labels_Limpar=len(Labels_Limpar)
      Labels_Voltar="Voltar"
      long_Labels_Voltar=len(Labels_Voltar)
      if pos==1:
        box_Botones.addstr(1,2, Labels_Aceitar, h)
      else:
        box_Botones.addstr(1,2, Labels_Aceitar, n)
      if pos==2:
        box_Botones.addstr(1,long_Labels_Aceitar+10,Labels_Limpar, h)
      else:
        box_Botones.addstr(1,long_Labels_Aceitar+10, Labels_Limpar, n)
      if pos==3:
        box_Botones.addstr(1,long_Labels_Aceitar+long_Labels_Limpar+15, Labels_Voltar, h)
      else:
        box_Botones.addstr(1,long_Labels_Aceitar+long_Labels_Limpar+15, Labels_Voltar, n)
      box_Botones.refresh()
      x = box_Botones.getch()
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
    if (getin == ord('1'))and (Tecla==10): # Top menu option 1
      print (Nome_Arquivo)
      getin=ord(str(3))
      #os.system('dosbox_Botones2 /path/to/EXE -conf /path/to/dosbox_Botones.conf -exit') #Launches a dosbox_Botones program, exits back to menu after program ends
    elif getin == ord('2'): # Topmenu option 2
      Caixa_de_Texto=""
      os.system('uqm')
    elif getin == ord('3'): # Topmenu option 3
      os.system('') #VITAL!  This closes out the menu system and returns you to the bash prompt.
def Validando_Texto(Tecla,Comprimento_do_Nome):
    letra=''
    flag_ponto=True
    while  True:
        if (len(letra)==Comprimento_do_Nome):
            box.erase()
            letra=letra[:-1]
            screen.border( 0 )
            box.border( 0 )
            box.addstr( 1, 1, str(letra))
            Tecla = box.getch()

        elif (Tecla==10):
            return Tecla,letra
        elif(Tecla==8):
            box.erase()
            letra=letra[:-1]
            box.addstr( 1, 1, str(letra) )
            screen.border( 0 )
            box.border( 0 )
            screen.refresh()  # delete this line
            box.refresh()     # delete this line
            Tecla = box.getch()
        elif (Tecla==27):
            exit()
            curses.endwin()
        elif (Tecla==46) and ('.'not in letra):
            box.erase()
            letra=letra+chr(Tecla)
            box.addstr( 1, 1, str(letra) )
            screen.border( 0 )
            box.border( 0 )
            screen.refresh()  # delete this line
            box.refresh()     # delete this line
            Tecla = box.getch()
            flag_ponto=False
        elif(Tecla>=48 and Tecla<=57) or (Tecla>=65 and Tecla<=90) or (Tecla==95) or (Tecla>=97 and Tecla<=122):
            box.erase()
            letra=letra+chr(Tecla)
            box.addstr( 1, 1, str(letra) )
            screen.border( 0 )
            box.border( 0 )
            screen.refresh()  # delete this line
            box.refresh()     # delete this line
            Tecla = box.getch()
        elif (Tecla<48 or Tecla>57) and (Tecla<97 or Tecla>122):
            box.erase()
            box.addstr( 1, 1,  str(letra) )
            screen.border( 0 )
            box.border( 0 )
            screen.refresh()  # delete this line
            box.refresh()     # delete this line
            Tecla = box.getch()
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad( 1 )    # delete this line
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
highlightText = curses.color_pair( 1 )
normalText = curses.A_NORMAL
screen.border( 0 )
curses.curs_set( 0 )
#escrevendo o Titulo do form
eixo_y_titulo=2
eixo_x_titulo=10
screen.addstr(eixo_y_titulo, eixo_x_titulo, "INSERTAR BASE DE DADOS")
#Escrevendo o Exemplo a ser excrito
eixo_y_titulo=eixo_y_titulo+3
screen.addstr(eixo_y_titulo, eixo_x_titulo-5, "(EX: 'Nome_Arquivo.csv')")
#Escrevendo o Label do Nome do Arquivo
eixo_y_titulo=eixo_y_titulo+3
Label_Name_BD="Nome do Arquivo:"
long_Label_Name_BD=len(Label_Name_BD)
screen.addstr(eixo_y_titulo, 2, Label_Name_BD)
#graficando a caixa de Texto
#Estruturando a caixa de texto
Comprimento_da_Caixa=20
eixo_x_Caixa_Label_Name_BD=long_Label_Name_BD+2
eixo_y_Caixa_Label_Name_BD=eixo_y_titulo-1
Numero_Linhas=3
box = curses.newwin( Numero_Linhas, Comprimento_da_Caixa, eixo_y_Caixa_Label_Name_BD, eixo_x_Caixa_Label_Name_BD )
box.keypad( 1 )
box.box()
screen.refresh()    # delete this line
box.refresh()
#esperar para Escriver
x = box.getch()
Tecla,Nome_Arquivo=Validando_Texto(x,Comprimento_da_Caixa-2)
#Graficando os Botones
eixo_x_botones=2
eixo_y_botones=11
Botones_Formularios(eixo_x_botones,eixo_y_botones,Tecla,Nome_Arquivo)
