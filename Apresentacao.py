# campos formatados, funções, looping e somas
from Tkinter import *
from math import *
#from MySQLdb import *
import sys
from random import *
import StringIO

##def conexaoBanco():
##    BANCO="estagio"
##    USER="root"
##    PASSWD=""
##    HOST="127.0.0.1"
##
##    try:
##        con= MySQLdb.connect(db= BANCO, user=USER,passwd=PASSWD, host=HOST)
##        print("Conectado com sucesso")
##    except MySQLdb as erro:
##        print("ERRO.Não conectado!", erro)
##        menu()
##
##        return con
    
class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    #    self.entryVariable = tkinter.StringVar()
        
   # def getdata(self):
##    #    return self.data
##
##    class DataHora(object):
##        DataHora = None
##        def __init__(self, DataHora):
##            self.DataHora = DataHora
##            print self.DataHora
        
    def initialize(self):

        self.geometry("300x300")

        wButton = Button(self, text='Arrecadação Bruta', width= 17,bd=3, command = self.OnButtonClickUm)
        wButton.pack(anchor= E, expand=YES) ##abre a um

        wButton = Button(self, text='Custo de Manutenção', width= 17,bd=3, command = self.OnButtonClickDois)
        wButton.pack(anchor= W, expand=YES) ##abre a dois

        wButton = Button(self, text='Lucro Real', width= 17,bd=3, command = self.OnButtonClickTres)
        wButton.pack(anchor= E, expand=YES) ##abre a tres

        wButton = Button(self, text='Finanças Pessoais', width= 17,bd=3, command = self.OnButtonClickQuatro)
        wButton.pack(anchor= W, expand=YES) ##abre a quatro

        wButton = Button(self, text='Cliente', width= 17,bd=3, command = self.OnButtonClickCinco)
        wButton.pack(anchor= E, expand=YES) ##abre a cinco

        wButton = Button(self, text='Condicional', width= 17,bd=3, command = self.OnButtonClickSeis)
        wButton.pack(anchor= W, expand=YES) ##abre a seis

        wButton = Button(self, text='Contabilizar prejuízo', width= 17,bd=3, command = self.OnButtonClickSete)
        wButton.pack(anchor= E, expand=YES) ##abre a sete

        wButton = Button(self, text='Relatório', width= 17,bd=3, command = self.OnButtonClickOito)
        wButton.pack(anchor= W, expand=YES) ##abre a oito

    def entradaDados(self):
        self.edit = tk.Entry(self)
        self.edit.pack()
       # return getattr(self.tk, LerID)
        
    def acaoImprimir(self):
        print ("Estágio")

    def novo():
        LerID.delete(0, END)
        LerDataHora.delete(0, END)
        LerNovo.delete(0, END)
        LerCodProduto.delete(0, END)
        LerVU.delete(0, END)
        LerQtd.delete(0, END)
        LerST.delete(0, END)
        LerVD.delete(0, END)
        LerVF.delete(0, END)
        LerSD.delete(0, END)
        LerID.focus()
        
    def OnButtonClickUm(self):

            
        um = Toplevel(background="#f5deb3")
        um.title("Arrecadação")
        um.geometry("300x610")

        um.transient(self)

        umButton = Button(um, text="FECHAR TUDO",width= 13, command = self.destroy)
        umButton.pack(side= BOTTOM)

        bt0= Button(um,text="Novo",width= 13,command = self.novo)
        bt0.pack(side=BOTTOM)

        bt1= Button(um, background= "#fffacd",width= 13, text = "Salvar",command = self.acaoImprimir) #vincular o command onclick_Salvar
        bt1.pack(side= BOTTOM)

        bt2= Button(um,background= "#fffacd",width= 13, text = "Editar")
        bt2.pack(side= BOTTOM)

        bt3= Button(um,background= "#fffacd",width= 13, text = "Consultar")
        bt3.pack(side= BOTTOM)

        bt4= Button(um,background= "#fffacd",width= 13, text = "Inativar")
        bt4.pack(side= BOTTOM)


        ID = Label(um,text="Código:", background= "#f5deb3", anchor=W, justify=LEFT)
        ID.pack(anchor= NW)
        LerID = Entry(um)
        LerID.pack(anchor= NW)
      #  LerID = Text(um, width=15, height=1.3, bd=1, relief = RIDGE)
      #  LerID.pack(anchor = NW)  

        DataHora = Label(um,text="Data e hora:",background= "#f5deb3")
        DataHora.pack(anchor= NW)
        LerDataHora = Entry(um)
        LerDataHora.pack(anchor= NW)
     #   LerDataHora = Text(um, width=15, height=1.3, bd=1, relief = RIDGE)
      #  LerDataHora.pack(anchor = NW)

        NR = Label(um,text="Novo registro de arrecadação ?",background= "#f5deb3")        
        NR.pack(anchor= NW)

        LerNovo=[('Sim', 1), ('Não', 2)]
        var = IntVar()
        for text, value in LerNovo:
            Radiobutton(um, text=text, value=value, variable=var, background= "#f5deb3").pack(anchor=W)
        var.set(2)
        

        
#while(Novo == true):
    
    
        CodProduto = Label(um,text="Código Produto:",background= "#f5deb3")
        CodProduto.pack(anchor= NW)
        LerCodProduto = Entry(um,background= "lightblue")
        LerCodProduto.pack(anchor= NW)
      #  LerCodProduto = Text(um, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
      #  LerCodProduto.pack(anchor = NW)

        VU = Label(um,text="Valor Unitário:",background= "#f5deb3")
        VU.pack(anchor= NW)
        LerVU = Entry(um,background= "lightblue")
        LerVU.pack(anchor= NW)       
       # LerVU = Text(um, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
       # LerVU.pack(anchor = NW)         

        Qtd = Label(um,text="Quantidade:",background= "#f5deb3")
        Qtd.pack(anchor= NW)
        LerQtd = Entry(um,background= "lightblue")
        LerQtd.pack(anchor= NW) 
       # LerQtd = Text(um, width=3, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
       # LerQtd.pack(anchor = NW)
        
        ST = Label(um,text="Subtotal:",background= "#f5deb3")
        ST.pack(anchor= NW)
        LerST = Entry(um,background= "lightblue")
        LerST.pack(anchor= NW) 
      #  LerST = Text(um, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
      #  LerST.pack(anchor = NW)

        VD = Label(um,text="Valor Descontado:",background= "#f5deb3")
        VD.pack(anchor= NW)
        LerVD = Entry(um,background= "lightblue")
        LerVD.pack(anchor= NW) 
       # LerVD = Text(um, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
       # LerVD.pack(anchor = NW)

        VF = Label(um,text="Valor Final:",background= "#f5deb3")
        VF.pack(anchor= NW)
        LerVF = Entry(um,background= "lightblue")
        LerVF.pack(anchor= NW)
       # LerVF = Text(um, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
       # LerVF.pack(anchor = NW)
        
# end while

        SD = Label(um,text="Soma do dia:",background= "#f5deb3")
        SD.pack(anchor= NW)
        LerSD = Entry(um)
        LerSD.pack(anchor= NW)
        #LerSD = Text(um, width=15, height=1.3, bd=1, relief = RIDGE)
        #LerSD.pack(anchor = NW)

    def OnButtonClickDois(self):
        dois = Toplevel(background="#fff0f5")
        dois.title("Custos Manutenção")
        dois.geometry("300x650")

        dois.transient(self)

        doisButton = Button(dois, text="FECHAR TUDO",width= 13, command = self.destroy)
        doisButton.pack(side= BOTTOM)

        bt1= Button(dois, background= "#fffacd",width= 13, text = "Salvar") #vincular o command onclick_Salvar
        bt1.pack(side= BOTTOM)

        bt2= Button(dois,background= "#fffacd",width= 13, text = "Editar")
        bt2.pack(side= BOTTOM)

        bt3= Button(dois,background= "#fffacd",width= 13, text = "Consultar")
        bt3.pack(side= BOTTOM)

        bt4= Button(dois,background= "#fffacd",width= 13, text = "Inativar")
        bt4.pack(side= BOTTOM)

        lblID = Label(dois,text="Código:", background= "#fff0f5", anchor=W, justify=LEFT)
        lblID.pack(anchor= NW)
        LerID = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerID.pack(anchor = NW)

        lblEnergia = Label(dois,text=" Energia", background= "#fff0f5", anchor=W, justify=LEFT)
        lblEnergia.pack(anchor= NW)       
        LerEnergia = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerEnergia.pack(anchor = NW)

        lblInternet = Label(dois,text=" Internet", background= "#fff0f5", anchor=W, justify=LEFT)
        lblInternet.pack(anchor= NW)       
        LerInternet = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerInternet.pack(anchor = NW)

        lblTelefone = Label(dois,text=" Telefone", background= "#fff0f5", anchor=W, justify=LEFT)
        lblTelefone.pack(anchor= NW)       
        LerTelefone = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerTelefone.pack(anchor = NW)

        lblAgua = Label(dois,text=" Água", background= "#fff0f5", anchor=W, justify=LEFT)
        lblAgua.pack(anchor= NW)       
        LerAgua = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerAgua.pack(anchor = NW)

        lblFuncionario = Label(dois,text="Pagamento de Funcionário", background= "#fff0f5", anchor=W, justify=LEFT)
        lblFuncionario.pack(anchor= NW)       
        LerFuncionario = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerFuncionario.pack(anchor = NW)

        lblFornecedor = Label(dois,text="Pagamento de Fornecedor ", background= "#fff0f5", anchor=W, justify=LEFT)
        lblFornecedor.pack(anchor= NW)       
        LerFornecedor = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerFornecedor.pack(anchor = NW)

        lblAluguel = Label(dois,text=" Aluguel", background= "#fff0f5", anchor=W, justify=LEFT)
        lblAluguel.pack(anchor= NW)       
        LerAluguel = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerAluguel.pack(anchor = NW)

        lblViagemTrabalho = Label(dois,text=" Gastos com viagem a trabalho", background= "#fff0f5", anchor=W, justify=LEFT)
        lblViagemTrabalho.pack(anchor= NW)       
        LerVT = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerVT.pack(anchor = NW)

        lblRecargaCelular = Label(dois,text="  Recarga de celular (telefone comercial)", background= "#fff0f5", anchor=W, justify=LEFT)
        lblRecargaCelular.pack(anchor= NW)       
        LerRC = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerRC.pack(anchor = NW)
        
        lblOutros = Label(dois,text=" Outros", background= "#fff0f5", anchor=W, justify=LEFT)
        lblOutros.pack(anchor= NW)       
        LerOutros = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerOutros.pack(anchor = NW)
        
        lblTotal = Label(dois,text=" Total", background= "#fff0f5", anchor=W, justify=LEFT)
        lblTotal.pack(anchor= NW)       
        LerTotal = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerTotal.pack(anchor = NW)


    def OnButtonClickTres(self):
        tres = Toplevel(background= "#e6e6fa")
        tres.title("Lucro")
        tres.geometry("300x580")
        tres.transient(self)

        tresButton = Button(tres, text="FECHAR TUDO",width= 13, command = self.destroy)
        tresButton.pack(side= BOTTOM)

        bt1= Button(tres,background= "#fffacd",width= 13, text = "Salvar")
        bt1.pack(side= BOTTOM)

        bt2= Button(tres,background= "#fffacd",width= 13, text = "Editar")
        bt2.pack(side= BOTTOM)

        bt3= Button(tres,background= "#fffacd",width= 13, text = "Consultar")
        bt3.pack(side= BOTTOM)

        bt4= Button(tres,background= "#fffacd",width= 13, text = "Inativar")
        bt4.pack(side= BOTTOM)

        ID = Label(tres,text="Código:", background= "#e6e6fa", anchor=W, justify=LEFT)
        ID.pack(anchor= NW)
        LerID = Text(tres, width=15, height=1.3, bd=1, relief = RIDGE)
        LerID.pack(anchor = NW)

        lblOutros = Label(dois,text=" Outros", background= "#fff0f5", anchor=W, justify=LEFT)
        lblOutros.pack(anchor= NW)       
        LerOutros = Text(dois, width=15, height=1.3, bd=1, relief = RIDGE)
        LerOutros.pack(anchor = NW)

    def OnButtonClickQuatro(self):
        quatro = Toplevel(background="#ffebcd")
        quatro.title("Finanças Pessoais")
        quatro.geometry("300x580")

        quatro.transient(self)

        quatroButton = Button(quatro, text="FECHAR TUDO",width= 13, command = self.destroy)
        quatroButton.pack(side= BOTTOM)

        bt1= Button(quatro,background= "#fffacd",width= 13, text = "Salvar")
        bt1.pack(side= BOTTOM)

        bt2= Button(quatro,background= "#fffacd",width= 13, text = "Editar")
        bt2.pack(side= BOTTOM)

        bt3= Button(quatro,background= "#fffacd",width= 13, text = "Consultar")
        bt3.pack(side= BOTTOM)

        bt4= Button(quatro,background= "#fffacd",width= 13, text = "Inativar")
        bt4.pack(side= BOTTOM)

        ID = Label(quatro,text="Código:", background= "#ffebcd", anchor=W, justify=LEFT)
        ID.pack(anchor= NW)
        LerID = Text(quatro, width=15, height=1.3, bd=1, relief = RIDGE)
        LerID.pack(anchor = NW)  

    def OnButtonClickCinco(self):
        cinco = Toplevel(background="#fff0f5")
        cinco.title("Cliente")
        cinco.geometry("300x450")

        cinco.transient(self)

        cincoButton = Button(cinco, text="FECHAR TUDO",width= 13, command = self.destroy)
        cincoButton.pack(side= BOTTOM)

        bt1= Button(cinco,background= "#fffacd",width= 13, text = "Salvar")
        bt1.pack(side= BOTTOM)

        bt2= Button(cinco,background= "#fffacd",width= 13, text = "Editar")
        bt2.pack(side= BOTTOM)

        bt3= Button(cinco,background= "#fffacd",width= 13, text = "Consultar")
        bt3.pack(side= BOTTOM)

        bt4= Button(cinco,background= "#fffacd",width= 13, text = "Inativar")
        bt4.pack(side= BOTTOM)

        btCondicional= Button(cinco,width= 33, text = "Acessar Condicional do Cliente")
        btCondicional.pack(side= TOP)

        IDCli = Label(cinco,text="Código:", background= "#fff0f5", anchor=W, justify=LEFT)
        IDCli.pack(anchor= NW)
        LerIDCli = Text(cinco, width=15, height=1.3, bd=1, relief = RIDGE)
        LerIDCli.pack(anchor = NW)  

        Nome = Label(cinco,text="Nome:", background= "#fff0f5", anchor=W, justify=LEFT)
        Nome.pack(anchor= NW)
        LerNome = Text(cinco, width=15, height=1.3, bd=1, relief = RIDGE)
        LerNome.pack(anchor = NW)

        Endereco = Label(cinco,text="Rua/número:", background= "#fff0f5", anchor=W, justify=LEFT)
        Endereco.pack(anchor= NW)
        LerEnd1 = Text(cinco, width=15, height=1.3, bd=1, relief = RIDGE)
        LerEnd1.pack(anchor = NW)

        Endereco2 = Label(cinco,text="Bairro:", background= "#fff0f5", anchor=W, justify=LEFT)
        Endereco2.pack(anchor= NW)
        LerEnd2 = Text(cinco, width=15, height=1.3, bd=1, relief = RIDGE)
        LerEnd2.pack(anchor = NW)

        Telefone = Label(cinco,text="Telefone:", background= "#fff0f5", anchor=W, justify=LEFT)
        Telefone.pack(anchor= NW)
        LerTelefone = Text(cinco, width=15, height=1.3, bd=1, relief = RIDGE)
        LerTelefone.pack(anchor = NW)

        CPF = Label(cinco,text="CPF:", background= "#fff0f5", anchor=W, justify=LEFT)
        CPF.pack(anchor= NW)
        LerCPF = Text(cinco, width=15, height=1.3, bd=1, relief = RIDGE)
        LerCPF.pack(anchor = NW)


        Nascimento = Label(cinco,text="Data de Nascimento:", background= "#fff0f5", anchor=W, justify=LEFT)
        Nascimento.pack(anchor= NW)
        LerNascimento = Text(cinco, width=15, height=1.3, bd=1, relief = RIDGE)
        LerNascimento.pack(anchor = NW)

                ## vai se ligar à  janela do condicional - criar função aqui
        



    def OnButtonClickSeis(self):
        seis = Toplevel(background="#f5deb3")
        seis.title("Condicional")
        seis.geometry("300x620")

        seis.transient(self)

        seisButton = Button(seis, text="FECHAR TUDO",width= 13, command = self.destroy)
        seisButton.pack(side= BOTTOM)

        bt1= Button(seis,background= "#fffacd",width= 13, text = "Salvar")
        bt1.pack(side= BOTTOM)

        bt2= Button(seis,background= "#fffacd",width= 13, text = "Editar")
        bt2.pack(side= BOTTOM)

        bt3= Button(seis,background= "#fffacd",width= 13, text = "Consultar")
        bt3.pack(side= BOTTOM)

        bt4= Button(seis,background= "#fffacd",width= 13, text = "Inativar")
        bt4.pack(side= BOTTOM)


        btCli= Button(seis,width= 33, text = "Acessar Cadastro do Cliente")
        btCli.pack(side= TOP)

        ID = Label(seis,text="ID:", background= "#f5deb3", anchor=W, justify=LEFT)
        ID.pack(anchor= NW)
        LerID = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerID.pack(anchor = NW)

        DH = Label(seis,text="Data/ Hora:", background= "#f5deb3", anchor=W, justify=LEFT)
        DH.pack(anchor= NW)
        LerDH = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerDH.pack(anchor = NW)

        IDCli = Label(seis,text="Código do Cliente:", background= "#f5deb3", anchor=W, justify=LEFT)
        IDCli.pack(anchor= NW)
        LerIDCli = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerIDCli.pack(anchor = NW)


        QR = Label(seis,text="Qtde Retirada:", background= "#f5deb3", anchor=W, justify=LEFT)
        QR.pack(anchor= NW)
        LerQR = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerQR.pack(anchor = NW)
################# Looping ##############################


        Descricao = Label(seis,text="Descrição da Peça:", background= "#f5deb3", anchor=W, justify=LEFT)
        Descricao.pack(anchor= NW)
        LerDescricao = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerDescricao.pack(anchor = NW)  
       # self.LerDescricao.get() # não funciona

        Preco = Label(seis,text="Preço:", background= "#f5deb3", anchor=W, justify=LEFT)
        Preco.pack(anchor= NW)
        LerPreco = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerPreco.pack(anchor = NW)

        QA = Label(seis,text="Qtd Adquirida:", background= "#f5deb3", anchor=W, justify=LEFT)
        QA.pack(anchor= NW)
        LerQA = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerQA.pack(anchor = NW)


################# Fim Looping ##############################
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()

#status

        Status = Label(seis,text="Status:", background= "#f5deb3", anchor=W, justify=LEFT)
        Status.pack(anchor= NW)

        status=[('aguardando', 1), ('enviado', 2), ('devolvido', 3)]
        var = IntVar()
        for text, value in status:
            Radiobutton(seis, text=text, value=value, variable=var, background= "#f5deb3").pack(anchor=W)
        var.set(3)
        

##        
##        a = Checkbutton(seis, text="aguardando",background= "#f5deb3", variable= var1)
##        a.pack(anchor= NW)
##        
##        b = Checkbutton(seis, text="enviado",background= "#f5deb3", variable= var2)
##        b.pack(anchor= NW)
##        
##        c = Checkbutton(seis, text="devolvido",background= "#f5deb3", variable= var3)
##        c.pack(anchor= NW)


# total em vendas
        Total = Label(seis,text="Total em vendas:", background= "#f5deb3", anchor=W, justify=LEFT)
        Total.pack(anchor= NW)
        LerTotal = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerTotal.pack(anchor = NW)

                        ## vai se ligar à  janela do cli - criar função aqui

    def OnButtonClickSete(self):
        sete = Toplevel(background="#ffebcd")
        sete.title("Prejuízos")
        sete.geometry("300x380")

        sete.transient(self)

        seteButton = Button(sete, text="FECHAR TUDO",width= 13, command = self.destroy)
        seteButton.pack(side= BOTTOM)

        bt1= Button(sete,background= "#fffacd",width= 13, text = "Salvar")
        bt1.pack(side= BOTTOM)

        bt2= Button(sete,background= "#fffacd",width= 13, text = "Editar")
        bt2.pack(side= BOTTOM)

        bt3= Button(sete,background= "#fffacd",width= 13, text = "Consultar")
        bt3.pack(side= BOTTOM)

        bt4= Button(sete,background= "#fffacd",width= 13, text = "Inativar")
        bt4.pack(side= BOTTOM)

        ID = Label(sete,text="ID:", background= "#ffebcd", anchor=W, justify=LEFT)
        ID.pack(anchor= NW)
        LerID = Text(sete, width=15, height=1.3, bd=1, relief = RIDGE)
        LerID.pack(anchor = NW)

        Data = Label(sete,text="Data:",background= "#ffebcd")
        Data.pack(anchor= NW)
        LerData = Text(sete, width=15, height=1.3, bd=1, relief = RIDGE)
        LerData.pack(anchor = NW)    
        
        VE = Label(sete,text="Valores estornados:", background= "#ffebcd")
        VE.pack(anchor= NW)
        LerVE = Text(sete, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
        LerVE.pack(anchor = NW)

        Qtd = Label(sete,text="Valor em peças danificadas:",background= "#ffebcd",)
        Qtd.pack(anchor= NW)
        LerQtd = Text(sete, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
        LerQtd.pack(anchor = NW)

        VD = Label(sete,text="Valor Descontado:",background= "#ffebcd",)
        VD.pack(anchor= NW)
        LerVD = Text(sete, width=15, height=1.3, bd=1,background= "lightblue", relief = RIDGE)
        LerVD.pack(anchor = NW)

        VF = Label(sete,text="Soma :",background= "#ffebcd",)
        VF.pack(anchor= NW)
        LerVF = Text(sete, width=15, height=1.3, bd=1, relief = RIDGE)
        LerVF.pack(anchor = NW)

    class GetSet(object):
               LerVF = 0
    def set_LerVF(self, LerVF):
             self.LerVF = LerDescricao
    def get_LerVF(self):
             return self.LerVF        

    def OnButtonClickOito(self):
        oito = Toplevel()
        oito.title("Relatório Mensal")
        oito.geometry("300x150")

        oito.transient(self)

        oitoButton = Button(oito, text="FECHAR TUDO",width= 13, command = self.destroy)
        oitoButton.pack(side= BOTTOM)


        btPrejuizo= Button(oito,background= "#fffacd",width= 30, text = "Consultar formulários de Prejuízo")
        btPrejuizo.pack(side= TOP)

        btArrecadacao= Button(oito,background= "#fffacd",width= 30, text = "Consultar formulários de Arrecadação")
        btArrecadacao.pack(side=TOP, anchor= CENTER, expand=YES )

        btLucro= Button(oito,background= "#fffacd",width= 30, text = "Consultar formulários de Lucro")
        btLucro.pack(side= BOTTOM, expand=YES)

        Descricao = Label(seis,text="Descrição da Peça:", background= "#f5deb3", anchor=W, justify=LEFT)
        Descricao.pack(anchor= NW)
        LerDescricao = Text(seis, width=15, height=1.3, bd=1, relief = RIDGE)
        LerDescricao.pack(anchor = NW)
        


 

if __name__ == "__main__":
    window = Window(None)

    window.title("Anadré - APOIO FINANCEIRO")

    window.mainloop()

