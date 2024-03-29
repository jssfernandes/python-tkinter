from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from datetime import datetime

root = tix.Tk()


def center(win):
    win.update_idletasks()  # Update "requested size" from geometry manager

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()


class Manufacturer:
    id: int
    name: str
    founded: str

class Color:
    id: int
    color: str


class Car:
    id: int
    model: str
    year_manufacture: int
    country_origin: str
    engine_power: int
    manufacturer_id: Manufacturer

list_manufacturer = []
list_cor = []
list_car = []


class Funcs():
    def limpa_fabricante(self):
        self.id_entry.delete(0, END)
        self.founded_entry.delete(0, END)
        self.name_entry.delete(0, END)

    def variaveis(self):
        self.id = self.id_entry.get()
        self.name = self.name_entry.get()
        self.founded = self.founded_entry.get()

    def OnDoubleClick(self, event):
        self.limpa_fabricante()
        # self.listaCli.selection()
        self.testes.selection()

        # for n in self.listaCli.selection():
        #     col1, col2, col3 = self.listaCli.item(n, 'values')
        #     self.id_entry.insert(END, col1)
        #     self.name_entry.insert(END, col2)
        #     self.founded_entry.insert(END, col3)

        for n in self.testes.selection():
            col1, col2, col3 = self.testes.item(n, 'values')
            self.id_entry.insert(END, col1)
            self.name_entry.insert(END, col2)
            self.founded_entry.insert(END, col3)

    def add_fabricante(self):
        self.variaveis()
        if self.name_entry.get() == "":
            msg = "Para cadastrar um novo fabricante é necessário \n"
            msg += "que seja digitado pelo menos um nome"
            messagebox.showinfo("Cadastro de Fabricantes - Aviso!!!", msg)
        else:
            manu = Manufacturer()
            if not self.id:
                if not list_manufacturer:
                    manu.id = 1
                for i in list_manufacturer:
                    manu.id = int(i.id) + 1
            else:
                manu.id = self.id
            # manu.id = 1+int(f.id for f in list_manufacturer) if not self.id else self.id
            manu.name = self.name
            manu.founded = self.founded
            list_manufacturer.append(manu)

            self.select_lista()
            self.limpa_fabricante()

    def altera_fabricante(self):
        self.variaveis()

        for i in list_manufacturer:
            if i.id == int(self.id):
                # i.id == self.id
                i.name = self.name
                i.founded = self.founded

        self.select_lista()
        self.limpa_fabricante()

    def deleta_fabricante(self):
        self.variaveis()

        for i in list_manufacturer:
            if i.id == int(self.id):
                list_manufacturer.remove(i)

        self.limpa_fabricante()
        self.select_lista()

    def select_lista(self):
        # self.listaCli.delete(*self.listaCli.get_children())
        self.testes.delete(*self.testes.get_children())

        lista = list_manufacturer
        for i in lista:
            # self.listaCli.insert("", END, values=(i.id, i.name, i.founded))
            self.testes.insert("", END, values=(i.id, i.name, i.founded))

    def busca_fabricante(self):
        # self.listaCli.delete(*self.listaCli.get_children())
        self.testes.delete(*self.testes.get_children())
        nome = self.name_entry.get()
        buscanomeCli = []
        for i in list_manufacturer:
            if i.name.__contains__(nome):
                buscanomeCli.append(i)

        for i in buscanomeCli:
            # self.listaCli.insert("", END, values=(i.id, i.name, i.founded))
            self.testes.insert("", END, values=(i.id, i.name, i.founded))

        self.limpa_fabricante()


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        # self.lista_frame2()
        # self.select_lista()
        # self.Menus()
        center(self.root)
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Fabricantes")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        # self.root.maxsize(width=1024, height=720)
        self.root.minsize(width=800, height=600)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        # self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        # self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
        #                      highlightbackground='#759fe6', highlightthickness=3)
        # self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba3 = Frame(self.abas)
        self.aba4 = Frame(self.abas)
        # self.aba2 = Frame(self.abas)
        self.aba_info_cliente = Frame(self.abas)
        self.aba_info_representante = Frame(self.abas)
        self.aba_info_grupo = Frame(self.abas)
        self.aba_info_grupo_representante = Frame(self.abas)
        self.aba_info_grupo_poder = Frame(self.abas)
        self.aba_info_assinatura = Frame(self.abas)
        self.aba_info_parametros = Frame(self.abas)

        self.aba1.configure(background="#dfe3ee")
        self.aba3.configure(background="#dfe3ee")
        self.aba4.configure(background="#dfe3ee")
        # self.aba2.configure(background="lightgray")
        self.aba_info_cliente.configure(background="#dfe3ee")
        self.aba_info_representante.configure(background="#dfe3ee")
        self.aba_info_grupo.configure(background="#dfe3ee")
        self.aba_info_grupo_representante.configure(background="#dfe3ee")
        self.aba_info_grupo_poder.configure(background="#dfe3ee")
        self.aba_info_assinatura.configure(background="#dfe3ee")
        self.aba_info_parametros.configure(background="#dfe3ee")

        self.abas.add(self.aba1, text="Fabricante")
        self.abas.add(self.aba3, text="Cor")
        self.abas.add(self.aba4, text="Carro")
        # self.abas.add(self.aba2, text="Aba 2")
        self.abas.add(self.aba_info_cliente, text="Cliente")
        self.abas.add(self.aba_info_representante, text="Representante")
        self.abas.add(self.aba_info_grupo, text="Grupo")
        self.abas.add(self.aba_info_grupo_representante, text="Grupo Representnate")
        self.abas.add(self.aba_info_grupo_poder, text="Grupo Poder")
        self.abas.add(self.aba_info_assinatura, text="Assinatura")
        self.abas.add(self.aba_info_parametros, text="Parametros")

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.canvas_bt = Canvas(self.aba1, bd=0, bg='#1e3743', highlightbackground='gray',
                                highlightthickness=5)
        self.canvas_bt.place(relx=0.19, rely=0.03, relwidth=0.22, relheight=0.095)

        ### Criacao do Botao Ajuda
        self.bt_limpar = Button(self.aba1, text="Ajuda", bd=2, bg='#107db2', fg='white',
                                activebackground='#108ecb', activeforeground="white"
                                , font=('verdana', 8, 'bold'), command=self.limpa_fabricante)
        self.bt_limpar.place(relx=0.05, rely=0.05, width=60, height=30)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=2, bg='#107db2', fg='white',
                                activebackground='#108ecb', activeforeground="white"
                                , font=('verdana', 8, 'bold'), command=self.limpa_fabricante)
        self.bt_limpar.place(relx=0.2, rely=0.05, relwidth=0.1, relheight=0.06)

        ### Criação do botao buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.busca_fabricante)
        self.bt_buscar.place(relx=0.3, rely=0.05, relwidth=0.1, relheight=0.06)

        texto_balao_buscar = "Digite no campo nome o fabricante que deseja pesquisar"
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg=texto_balao_buscar)

        ### Criação do botao novo
        self.bt_novo = Button(self.aba1,
                              bd=2, text="Novo", bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                              command=self.add_fabricante)
        self.bt_novo.place(relx=0.55, rely=0.05, relwidth=0.1, relheight=0.06)

        ### Criação do botao alterar
        self.bt_alterar = Button(self.aba1,
                                 bd=2, text="Alterar", bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                 command=self.altera_fabricante)
        self.bt_alterar.place(relx=0.67, rely=0.05, relwidth=0.1, relheight=0.06)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deleta_fabricante)
        self.bt_apagar.place(relx=0.8, rely=0.05, relwidth=0.1, relheight=0.06)

        ## Criação da label e entrada do id/codigo
        self.lb_codigo = Label(self.aba1, text="Id", bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.15)

        self.id_entry = Entry(self.aba1)
        self.id_entry.place(relx=0.15, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do name
        self.lb_nome = Label(self.aba1, text="Name", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.2)

        self.name_entry = Entry(self.aba1)
        self.name_entry.place(relx=0.15, rely=0.2, relwidth=0.8)

        ## Criação da label e entrada do campo founded
        self.lb_nome = Label(self.aba1, text="Founded", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.25)

        self.founded_entry = Entry(self.aba1)
        self.founded_entry.place(relx=0.15, rely=0.25, relwidth=0.4)

        ### Criação da Treeview para a ABA 1
        colunas =['col1', 'col2', 'col3']
        self.testes = ttk.Treeview(self.aba1, height=2, column=colunas)
        self.testes.heading("#0", text="")
        self.testes.heading("#1", text="Codigo")
        self.testes.heading("#2", text="Name")
        self.testes.heading("#3", text="Founded")
        self.testes.column("#0", width=1)
        self.testes.column("#1", width=50)
        self.testes.column("#2", width=200)
        self.testes.column("#3", width=125)
        self.testes.place(relx=0.01, rely=0.60, relwidth=0.97, relheight=0.40)

        self.scroolLista = Scrollbar(self.aba1, orient='vertical', )
        self.testes.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.98, rely=0.60, relwidth=0.02, relheight=0.40)
        self.testes.bind("<Double-1>", self.OnDoubleClick)

        #### para criar um drop down button
        # self.Tipvar = StringVar()
        # self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)")
        # self.Tipvar.set("Solteiro(a)")
        # self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        # self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
        # self.estado_civil = self.Tipvar.get()
        # print(self.estado_civil)

    # def lista_frame2(self):
    #     self.listaCli = ttk.Treeview(self.frame_2, height=2,
    #                                  column=("col1", "col2", "col3"))
    #     self.listaCli.heading("#0", text="")
    #     self.listaCli.heading("#1", text="Codigo")
    #     self.listaCli.heading("#2", text="Name")
    #     self.listaCli.heading("#3", text="Founded")
    #     self.listaCli.column("#0", width=1)
    #     self.listaCli.column("#1", width=50)
    #     self.listaCli.column("#2", width=200)
    #     self.listaCli.column("#3", width=125)
    #     self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
    #
    #     self.scroolLista = Scrollbar(self.frame_2, orient='vertical', )
    #     self.listaCli.configure(yscroll=self.scroolLista.set)
    #     self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
    #     self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    # def Menus(self):
    #     menubar = Menu(self.root)
    #     self.root.config(menu=menubar)
    #     filemenu = Menu(menubar)
    #     filemenu2 = Menu(menubar)
    #
    #     def Quit(): self.root.destroy()
    #
    #     menubar.add_cascade(label="Opções", menu=filemenu)
    #     menubar.add_cascade(label="Relatorios", menu=filemenu2)
    #
    #     filemenu.add_command(label="Sair", command=Quit)
    #     filemenu.add_command(label="Limpa Fabricante", command=self.limpa_fabricante)
    #
    #     filemenu2.add_command(label="Abrir janela 2", command=self.janela2)

    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title(" Janela 2  ")
        self.root2.configure(background='gray75')
        self.root2.geometry("360x160")
        self.root2.resizable(TRUE, TRUE)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

# print(vars(Car))
testes = Car()
testes.id = 123
testes.engine_power=233
print(Car.__dict__.keys())
for att in dir(testes):
    if not att.startswith('__'):
        # print (att, getattr(testes,att))
        print(att)
Application()
