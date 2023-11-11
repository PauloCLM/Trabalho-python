from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from view import *


co0 = "#f0f3f5"  
co1 = "#feffff"  
co2 = "#4fa882"  
co3 = "#38576b" 
co4 = "#403d3d"
co5 = "#e06636" 
co6 = "#038cfc"  
co7 = "#ef5350"  
co8 = "#263238"   
co9 = "#e9edf5"  

janela = Tk()
janela.title("Gerenciador de tarefas")
janela.geometry("1043x453")
janela.configure(background=co9 )
janela.resizable(width=False, height=False)

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0,sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

app_nome = Label(frame_cima, text= "Cadastro de tarefas", anchor=NW, font=("Ivy 13 bold"), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20) 

global tree

def inserir():
   Tarefa = e_tarefa.get()
   data = e_Data.get()
   descricao = e_Descrição_da_tarefa.get()

   lista = (Tarefa,data,descricao)

   if Tarefa=='': 
        messagebox.showerror("Erro","A tarefa não pode ser vazia")

   else:
       inserir_info(lista)
       messagebox.showinfo("Sucesso","Os dados foram inseridos com sucesso")
       e_tarefa.delete(0,'end')
       e_Data.delete(0,'end')
       e_Descrição_da_tarefa.delete(0,'end')

   for widget in frame_direita.winfo_children():
       widget.destroy()

       mostar()
 

def atualizar():
   

   try:
      treev_dados = tree.focus() 
      treev_dicionario = tree.item(treev_dados)
      tree_lista = treev_dicionario["values"]

      valor_id = tree_lista[0]

      e_tarefa.delete(0,'end')
      e_Data.delete(0,'end')
      e_Descrição_da_tarefa.delete(0,'end')

      e_tarefa.insert(0,tree_lista[1])
      e_Data.insert(0,tree_lista[2])
      e_Descrição_da_tarefa.insert(0,tree_lista[3])
      

      def update():
            Tarefa = e_tarefa.get()
            data = e_Data.get()
            descricao = e_Descrição_da_tarefa.get()

            lista = (Tarefa,data,descricao,valor_id)
         
            if Tarefa=='': 
                messagebox.showerror("Erro","A tarefa não pode ser vazia")
            else:
                atualizar_info(lista)
                messagebox.showinfo("Sucesso","Os dados foram atualizados com sucesso")
                e_tarefa.delete(0,'end')
                e_Data.delete(0,'end')
                e_Descrição_da_tarefa.delete(0,'end')
            
            for widget in frame_direita.winfo_children():
                widget.destroy()

                mostar()       
        

        b_confirmar = Button(frame_baixo, command=update, text= "Confirmar", width=10, font=("Ivy 9 bold"), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=370)    
         

          

   except IndexError:
       messagebox.showerror("Erro","Selecione uns dos dados na tabela")
def deletar():
   
   try:
        treev_dados = tree.focus() 
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario["values"]
      
        valor_id = [tree_lista[0]]

        deletar__info(valor_id)
        messagebox.showinfo("Sucesso","Os dados foram deletados com sucesso")

        for widget in frame_direita.winfo_children():
          widget.destroy()
        
        mostar() 

   except IndexError:
      messagebox.showerror("Erro","Selecione uns dos dados na tabela")

l_tarefa = Label(frame_baixo, text= "Tarefa *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
l_tarefa.place(x=10, y=10)
e_tarefa = Entry(frame_baixo, width=45, justify="left", relief='solid')
e_tarefa.place(x=15, y=40)

l_Data = Label(frame_baixo, text= "Data *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
l_Data.place(x=10, y=70)
e_Data = Entry(frame_baixo, width=45, justify="left", relief='solid')
e_Data.place(x=15, y=100)

l_Descrição_da_tarefa = Label(frame_baixo, text= "Descrição da tarefa *", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief='flat')
l_Descrição_da_tarefa.place(x=10, y=130)
e_Descrição_da_tarefa = Entry(frame_baixo, width=45, justify="left", relief='solid')
e_Descrição_da_tarefa.place(x=15, y=160)

b_Inserir = Button(frame_baixo, command=inserir, text= "Inserir", width=10, font=("Ivy 9 bold"), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_Inserir.place(x=15, y=340)

b_Atualizar = Button(frame_baixo, command=atualizar, text= "Atualizar", width=10, font=("Ivy 9 bold"), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_Atualizar.place(x=110, y=340)

b_Deletar = Button(frame_baixo, command=deletar, text= "Deletar", width=10, font=("Ivy 9 bold"), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_Deletar.place(x=205, y=340)

def mostar():
 global tree

 lista = mostrar_info()
           

 tabela_head = ['ID','Tarefa','Data','Descrição']

 tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")
 vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
 hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

 tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

 tree.grid(column=0, row=0, sticky='nsew')
 vsb.grid(column=1, row=0, sticky='ns')
 hsb.grid(column=0, row=1, sticky='ew')

 frame_direita.grid_rowconfigure(0, weight=12)

 hd=["nw","nw","nw","nw"]
 h=[30,100,80,240]
 n=0

 for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    
    tree.column(col, width=h[n],anchor=hd[n])
    
    n+=1

 for item in lista:
    tree.insert('', 'end', values=item)

mostar()
janela.mainloop()