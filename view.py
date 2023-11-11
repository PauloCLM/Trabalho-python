import sqlite3 as lite

con = lite.connect("tarefas.db")



def inserir_info(i):
 with con:
    cur = con.cursor()
    query = "INSERT INTO tarefa(tarefa, data, descricao) VALUES (?,?,?)" 
    cur.execute(query,i)



def mostrar_info():
    lista = []
    with con:
       cur = con.cursor()
       query = "SELECT * FROM tarefa" 
       cur.execute(query)   
       informacao = cur.fetchall()

       for i in informacao:
          lista.append(i)
    return lista
    


def atualizar_info(i):
 with con:
    cur = con.cursor()
    query = "UPDATE tarefa SET tarefa=?, data=?, descriao=? WHERE id=?" 
    cur.execute(query,i)    


def deletar__info(i):
 with con:
    cur = con.cursor()
    query = "DELETE FROM tarefa WHERE id=?" 
    cur.execute(query,i)        

