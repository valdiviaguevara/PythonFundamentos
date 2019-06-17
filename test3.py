#import curses, os
#def start_editor(self):
#    gc = curses.initscr() #Inicializa una nueva ventana para capturar pulsaciones de teclas.
#    try:
#        # draw the top bar
#        top_bar = 'Editing ' + self.file.name + ' [press Ctrl+G to save and close]'
#        i = len(top_bar)
#        while i < self.scr_width:
#            top_bar += ' '
#            i += 1
#        self.scr.addstr(0, 0, top_bar, curses.A_REVERSE)
#        self.scr.refresh()
#
#        # let the user edit th efile
#        box = Textbox(self.text_win)
#        box.edit()
#
#        # get the file contents
#        self.file_text = box.gather()
#    finally:
#        # return to the game
#        curses.endwin()
#        gc.clear()
#        self.file.content = self.file_text
#
#screen = curses.initscr() #Inicializa una nueva ventana para capturar pulsaciones de teclas.
#start_editor(screen)
import curses
def Validando_Texto(Tecla,Comprimento_do_Nome):
    letra=''
    flag_ponto=True
    while  True:
        if (len(letra)==Comprimento_do_Nome):
            box.erase()
            letra=letra[:-1]
            screen.border( 0 )
            box.border( 0 )
            box.addstr( 1, 1, str(Tecla) )
            box.addstr( 1+1, 1, str(letra))
            Tecla = box.getch()

        elif (Tecla==10):
            return letra
        elif(Tecla==8):
            box.erase()
            letra=letra[:-1]
            box.addstr( 1, 1, str(Tecla) )
            box.addstr( 1+1, 1, str(letra) )
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
            box.addstr( 1, 1, str(Tecla) )
            box.addstr( 1+1, 1, str(letra) )
            screen.border( 0 )
            box.border( 0 )
            screen.refresh()  # delete this line
            box.refresh()     # delete this line
            Tecla = box.getch()
            flag_ponto=False
        elif(Tecla>=48 and Tecla<=57) or (Tecla>=65 and Tecla<=90) or (Tecla==95) or (Tecla>=97 and Tecla<=122):
            box.erase()
            letra=letra+chr(Tecla)
            box.addstr( 1, 1, str(Tecla) )
            box.addstr( 1+1, 1, str(letra) )
            screen.border( 0 )
            box.border( 0 )
            screen.refresh()  # delete this line
            box.refresh()     # delete this line
            Tecla = box.getch()
        elif (Tecla<48 or Tecla>57) and (Tecla<97 or Tecla>122):
            box.erase()
            box.addstr( 1, 1, str(Tecla) )
            box.addstr( 1+1, 1,  str(letra) )
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
eixo_y_titulo=eixo_y_titulo+2
screen.addstr(eixo_y_titulo, eixo_x_titulo-5, "(EX: 'Nome_Arquivo.csv')")
#Escrevendo o Label do Nome do Arquivo
eixo_y_titulo=eixo_y_titulo+2
Label_Name_BD="Nome do Arquivo:"
long_Label_Name_BD=len(Label_Name_BD)
screen.addstr(eixo_y_titulo, 2, Label_Name_BD)
#graficando a caixa de Texto
#Estruturando a caixa de texto
Comprimento_da_Caixa=20
eixo_x_Caixa_Label_Name_BD=long_Label_Name_BD+2
eixo_y_Caixa_Label_Name_BD=eixo_y_titulo-1
Numero_Linhas=4
box = curses.newwin( Numero_Linhas, Comprimento_da_Caixa, eixo_y_Caixa_Label_Name_BD, eixo_x_Caixa_Label_Name_BD )
box.keypad( 1 )
box.box()
screen.refresh()    # delete this line
box.refresh()
x = box.getch()
Nome_Arquivo=Validando_Texto(x,Comprimento_da_Caixa-2)
print (Nome_Arquivo)
