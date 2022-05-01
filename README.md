# Conversor de Algarismos romanos para inteiro

Este projeto é feito na linguagem Python na versão 3.7.6 com uso da biblioteca tkinter do próprio Python para gerar a interface gráfica e suas interações. Clique [aqui](https://docs.python.org/3/library/tkinter.html) para ir até a documentação do tkinter.

## Preparativos

É necessário a criação uma pasta para armazenar os dois arquivos para este pequeno projeto, um arquivo terá a interface e o outro terá a lógica da aplicação. Criemos dois arquivos com os seguintes nomes:

`main.py`

`logica.py`

## Importando as bibliotecas

~~~ python
from tkinter import *
import logica
~~~

A bibliteca de nome `logica` é um arquivo que como o próprio nome já diz vai ter a lógica do app.

## Criação da janela para o app

Para isso no arquivo `main.py` será gerado uma classe de nome `Front_End` para comportar as características da interface gráfica e dentro dessa classe será criado o método construtor `def __init__(self):` que é um método interno do Python, e dentro desse método será criado a variável `janela` que receberá a instância `Tk()` do _tkinter_, logo em seguida a variável `janela` será encapsulada dentro da variável `self.janela`, para a janela aparecer na tela basta usar a variável janela, dentro do método construtor, com o comando `mainloop()` para assim a janela está em um loop infinito, mas para a janela realmente rodar é necessário chamar a classe na parte de baixo do código, veja o código abaixo:

~~~ python
from tkinter import *
import logica

class FrontEnd(BackEnd):
    def __init__(self):
        janela = Tk()
        self.janela = janela
        janela.mainloop()
FrontEnd()
~~~

## Dando características para a janela

Agora fora do método construtor será gerado um método `def tela(self):` no qual será responsável por dar definições da interface gráfica da tela tipo o tamanho, cor de fundo e etc.

Para a chamada dos métodos de definições do _tkinter_ será usado a variável `self.janela`, para as definições serem executadas na janela a função deve se chamada desta maneira `self.tela()` dentro do método construtor. Veja abaixo como o código deve ficar até o momento:

~~~ python
from tkinter import *
import logica

class FrontEnd(BackEnd):
    def __init__(self):
        janela = Tk()
        self.janela = janela
        self.tela()
        janela.mainloop()
    
    def tela(self):
        self.janela.title('Conversor de algarismos romanos para inteiro')
        self.janela.configure(bg='#420080',bd=3,highlightbackground='#0f38bd',highlightthickness=3)
        self.janela.geometry('500x400')
        self.janela.resizable(False,False)
    
FrontEnd()
~~~

## Criando widgets

Para que seja possível a interação co usuário ao app é necessário a criação de alguns elementos para tal interação, então será criado o métedo `def widgets(self):` que gerará alguns textos que são as `Labels`, campos para entradas de dados é deominda `Entry` e o butão `Button` para executar a operação de conversão. Dentro do métedo será criado um `Frame` para comportar os elementos a serem criados, o Frame é como se fosse um conteiner que comporta outros widgets da janela. Veja abaixo como será o métedo:

~~~ python
def widgets(self):#Criação do Frame que tem como pai o objeto self.janela
        self.frame = Frame(self.janela,bg='#29034d',bd=3,highlightbackground='#0f38bd',highlightthickness=3)
        self.frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        #Texto para o título do app
        Label(self.frame, text='CONVERSOR',bg='#29034d',fg='#08bf45',font='Arial 22 bold').place(relx=0.28,rely=0.04)
        
        #Texto para onformar o usuário o que deve ser feito
        Label(self.frame, text='Digite algum número em algarismo romano',bg='#29034d',fg='#08bf45',font='Arial 14 bold').place(relx=0.1,rely=0.35)

        #Campo para a entrada dos digitos do usuário
        self.algarismo_romano = Entry(self.frame,bg='#b3c7af',fg='#000121',font='Arial 14 bold',bd=3)
        self.algarismo_romano.place(relx=0.25,rely=0.45,relwidth=0.50,relheight=0.08)
        
        #Texto para retornar o resultado da operação
        self.numero_inteiro = Label(self.frame,text='Resultado',bg='#29034d',fg='white',font='Arial 14 bold',bd=3)
        self.numero_inteiro.place(relx=0.05,rely=0.60,relwidth=0.90,relheight=0.08)
          
        #Botão para executar a função para resolver o problema.       
        Button(self.frame,text='CONVERTER',bg='#d94b09',fg='#000121',font='Arial 14 bold',bd=3).place(relx=0.35,rely=0.75)
~~~

## Criando o Back End da aplicação

Para isso será criado uma classe `BackEnd` que conterá as funções responsáveis de executar o que o programa se propõe a fazer.

~~~ Python
class BackEnd:
    def converter(self):#Função que chamará o método que tem a lógica da aplicação.
        romano = self.algarismo_romano.get()#Coletando os dados contidos na Entry
        if romano != '':
            """
                Dentro da variável inteiro ficará armazenado o resultado da operação feita no método romano_para_inteiro
                do arquivo logica.py....
            """
            inteiro = logica.romano_para_inteiro(romano.upper())
            try:#Tentará converter o resultado do metodo para certificar que realmente retornou um número inteiro
                inteiro = int(inteiro)
                self.numero_inteiro['text'] = str(inteiro)
            except:
                #Em caso de erro uma mensagem de erro será exibida na label escolhida para mostrar os resultados.
                self.numero_inteiro['text'] = inteiro +' não é um algarismo romano'
        else:
            self.numero_inteiro['text']='Sem dados para converter!'
    
    
    def valida_entrada_romanos(self,event=None):#Função para não permitir dígitos de números inteiros ou simbolos na Entry
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

~~~

Para a classe `BackEnd` funcionar deve -se passar ela com parâmero na classe `FrontEnd` dessa forma:

~~~ Python
 #Código omitido
class FrontEnd(BackEnd):
    #Código omitido
    #Código omitido
~~~

## Arquivo logica.py

Agora é hora de realmente de trablahar com alógica, no arquivo logica.py será criado um método `def romano_para_inteiro` que receberá uma string com parâmetro e será criado um outro métedo `validador` para verificar se o calor recebido na função é realmente um algarismo romano.

~~~ python

def verifica_romano(romano):
    """
        Esse métedo irá verificar se o valor recebido é um algarismo romano, caso não seja ele retornará o algarismo
        que não é um algarismo romano, por exemplo se entrar um valor XVT na função ela retornará T, se for válido a 
        função retornará True.
    """
    for i in romano:
        if i in 'IVXLCDM':
            resultado = True
        else:
            resultado = i
            break     
    return resultado

def romano_para_inteiro(romano):
    validador = verifica_romano(romano)#Fazendo a verificação do valor recebido 
    if validador == True:
        tam_romano = len(romano)
        inteiro = 0
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(tam_romano):
            atual =  romano[i]
            try:
                prox = romano[i+1]
            except IndexError: 
                prox = False
            if (prox and dic[prox] > dic[atual]):
                inteiro -= dic[atual]
            else:
                inteiro += dic[atual]
        return inteiro
    else:
        return validador
~~~

A lógica aqui é a seguinte, se o algarismo for válido, faremos um loop no algarismo par verificarmos se o algarismo atual é menor do que o próximo, antes temos que verificar se o póroximo existe, se o algarismo atual for menor que o próximo a gente subtraí, caso contrário somamos retornamos o valor em inteiro, caso o algarismo não seja válido retornaos o algarismo inválido para o usuário.

Agora para a lógica realmente acontecer basta ir no `main.py` e chamar a função no botão da aplicação como comando `command=self.converter`.

~~~ python
Button(self.frame,text='CONVERTER',bg='#d94b09',fg='#000121',font='Arial 14 bold',bd=3,command=self.converter).place(relx=0.35,rely=0.75)
~~~

## Observações de bugs

Pós testar o App foi notado que na lógica adotada há um bug, quando o usuário informa um número em algarismo romano da seguinte forma `IIIV` o retorno não é `2` mas sim `6`. Mas se o usuário informa p valor `IV`o retrno é `4`, para o algoritmo retornar `2` o usuário tem que informar `II` e o mesmo se aplica as demais formas, por exemplo, para ter rtorno `8` o usuário deve informar `VIII` e não  `IIX`.
