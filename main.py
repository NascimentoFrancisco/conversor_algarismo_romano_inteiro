from tkinter import * 
import logica

class BackEnd:
    def converter(self):
        romano = self.algarismo_romano.get()
        if romano != '':
            inteiro = logica.romano_para_inteiro(romano.upper())
            try:
                inteiro = int(inteiro)
                self.numero_inteiro['text'] = str(inteiro)
            except:
                self.numero_inteiro['text'] = inteiro +' não é um algarismo romano'
        else:
            self.numero_inteiro['text']='Sem dados para converter!'
    
    
    def valida_entrada_romanos(self,event=None):
        self.texto = self.algarismo_romano.get()
        self.novo_texto=""
        self.cont = 0
        if event.keysym.lower() == "backspace": return
        for i in range(len(self.texto)):
            if self.texto[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or self.texto[i] in 'abcdefghijklmnopqrstuvwxyz':
                self.novo_texto += self.texto[i]
                self.algarismo_romano.delete(0,END)
                self.algarismo_romano.insert(0,self.novo_texto)
            else:
                self.novo_texto += ''
                self.algarismo_romano.delete(0,END)
                self.algarismo_romano.insert(0,self.novo_texto)
                
            
class FrontEnd(BackEnd):
    def __init__(self):
        janela = Tk()
        self.janela = janela
        self.tela()
        self.widgets()

        janela.mainloop()
        
    def tela(self):
        self.janela.title('Conversor de algarismos romanos para inteiro')
        self.janela.configure(bg='#420080',bd=3,highlightbackground='#0f38bd',highlightthickness=3)
        self.janela.geometry('500x400')
        self.janela.resizable(False,False)
    def widgets(self):
        self.frame = Frame(self.janela,bg='#29034d',bd=3,highlightbackground='#0f38bd',highlightthickness=3)
        self.frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
        Label(self.frame, text='CONVERSOR',bg='#29034d',fg='#08bf45',font='Arial 22 bold').place(relx=0.28,rely=0.04)

        Label(self.frame, text='Digite algum número em algarismo romano',bg='#29034d',fg='#08bf45',font='Arial 14 bold').place(relx=0.1,rely=0.35)
        self.algarismo_romano = Entry(self.frame,bg='#b3c7af',fg='#000121',font='Arial 14 bold',bd=3)
        self.algarismo_romano.place(relx=0.25,rely=0.45,relwidth=0.50,relheight=0.08)
        self.algarismo_romano.bind("<KeyRelease>",self.valida_entrada_romanos)

        self.numero_inteiro = Label(self.frame,text='Resultado',bg='#29034d',fg='white',font='Arial 14 bold',bd=3)
        self.numero_inteiro.place(relx=0.05,rely=0.60,relwidth=0.90,relheight=0.08)
                
        Button(self.frame,text='CONVERTER',bg='#d94b09',fg='#000121',font='Arial 14 bold',bd=3,command=self.converter).place(relx=0.35,rely=0.75)
FrontEnd()
