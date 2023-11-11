import sqlite3 as lite

con = lite.connect("tarefas.db")

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, tarefa TEXT, data TEXT, descricao TEXT)")