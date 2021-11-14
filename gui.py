import tkinter as tk
import pandas as pd
import sqlite3
from tkinter import ttk

def student_search():

    stud_window = tk.Tk()

    a = tk.Label(stud_window, text = 'Nome a pesquisar (considerar acentos)')
    def help():
        search = s.get()
        stud_window.destroy()
        return search
    s = tk.Entry(stud_window)
    b = tk.Button(stud_window, text ="Pesquisar", command = lambda:[select_student(help())])

    a.pack()
    s.pack()
    b.pack()

    stud_window.mainloop()

def select_student(search):
        results = tk.Tk()
        def helpp():
            choice = c.get()
            if int(choice)>len(matching) or int(choice)<1:
                mode = 0
                idd=0
                name = str('')
            else:
                mode = 1
                id_i = name_list.index(matching[int(choice)-1])
                idd = names[id_i][0]
                name = matching[int(choice)-1]
            results.destroy()
            return mode, name, idd
        conn = sqlite3.connect('electro.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT id,nome FROM alunos")
        names = c.fetchall()
        conn.commit()
        conn.close()

        name_list = [row[1] for row in names]
        matching = [i for i in name_list if search.lower() in i.lower()]

        if matching:
            e = tk.Scrollbar(results)
            a = tk.Listbox(results,width=100, yscrollcommand = e.set)
            for i in range(0,len(matching)):
                a.insert('end', str(i+1) + " " + matching[i])
            #a = tk.Label(results, text = out)
            b = tk.Label(results, text = 'Opção (número)')
            c = tk.Entry(results)
            d = tk.Button(results, text ="Pesquisar", command = lambda:[disp_stud(helpp())])
            d.pack(side='bottom')
            c.pack(side='bottom')
            b.pack(side='bottom')
            a.pack(side = 'left', fill = 'both' )
            e.pack(side = 'right', fill = 'y')
        else:
            a = tk.Label(results,text = "Não existe") 
            d = tk.Button(results, text ="Voltar", command = lambda:[results.destroy(),main()]) 
            a.pack()
            d.pack()

        results.mainloop()

def disp_stud(arg):
    mode = arg[0]
    name = arg[1]
    idd = arg[2]
    disp_st = tk.Tk()
    if mode == 0:
        a = tk.Label(disp_st,text= "Vai à merda")
        c = tk.Button(disp_st, text ="Voltar", command = lambda:[disp_st.destroy(),main()])
        a.pack(side='top')
        c.pack(side='bottom')
    else:
        conn = sqlite3.connect('electro.db')

        c = conn.cursor()
        query = "SELECT n_escolha,tese,proponente,orientador FROM alunos where id = "+str(idd)
        c.execute(query)
        thesis = c.fetchall()

        conn.commit()

        conn.close()

        st = str('\n')
        a = tk.Label(disp_st,text= name)
        d = tk.Scrollbar(disp_st)
        b = tk.Listbox(disp_st,width=180, yscrollcommand = d.set)
        for i in range(0,len(thesis)):
            b.insert('end', ("Escolha " + str(thesis[i][0])))
            b.insert('end', "Tema: " + thesis[i][1])
            b.insert('end', "Proponente: " + thesis[i][2])
            b.insert('end', "Orientador: " + str(thesis[i][3]))
            b.insert('end', "\n")
        c = tk.Button(disp_st, text ="Voltar", command = lambda:[disp_st.destroy(),main()])
        a.pack(side='top')
        c.pack(side='bottom')
        b.pack(side = 'left', fill = 'both' )
        d.pack(side = 'right', fill = 'y')
    disp_st.mainloop()

def thesis_search():
    thesis_window = tk.Tk()

    a = tk.Label(thesis_window, text = 'Tese a pesquisar (considerar acentos)')
    def help():
        search = s.get()
        thesis_window.destroy()
        return search
    s = tk.Entry(thesis_window)
    b = tk.Button(thesis_window, text ="Pesquisar", command = lambda:[select_thesis(help())])

    a.pack()
    s.pack()
    b.pack()

    thesis_window.mainloop()

def select_thesis(search):
    results = tk.Tk()

    def helpp():
        choice = c.get()
        if int(choice)>len(matching) or int(choice)<1:
            mode = 0
            tese = str('')
        else:
            mode = 1
            tese = matching[int(choice)-1]
        results.destroy()
        return mode,tese

    conn = sqlite3.connect('electro.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT tese FROM alunos")
    teses = c.fetchall()
    conn.commit()
    conn.close()

    teses = [row[0] for row in teses]
    matching = [i for i in teses if search.lower() in i.lower()]

    if matching:
            e = tk.Scrollbar(results)
            a = tk.Listbox(results,width=200, yscrollcommand = e.set)
            for i in range(0,len(matching)):
                a.insert('end', str(i+1) + " " + matching[i])
            b = tk.Label(results, text = 'Opção (número)')
            c = tk.Entry(results)
            d = tk.Button(results, text ="Pesquisar", command = lambda:[disp_thesis(helpp())])
            d.pack(side='bottom')
            c.pack(side='bottom')
            b.pack(side='bottom')
            a.pack(side = 'left', fill = 'both' )
            e.pack(side = 'right', fill = 'y')
    else:
        a = tk.Label(results,text = "Não existe") 
        d = tk.Button(results, text ="Voltar", command = lambda:[results.destroy(),main()]) 
        a.pack()
        d.pack()

    results.mainloop()

def disp_thesis(arg):
    mode = arg[0]
    tese = arg[1]

    disp_st = tk.Tk()
    if mode == 0:
        a = tk.Label(disp_st,text= "Vai à merda")
        c = tk.Button(disp_st, text ="Voltar", command = lambda:[disp_st.destroy(),main()])
        a.pack()
        c.pack(side='bottom')
    else:
        conn = sqlite3.connect('electro.db')

        c = conn.cursor()
        query = "SELECT nome,n_escolha FROM alunos WHERE tese = '"+tese+"' ORDER BY n_escolha ASC"
        c.execute(query)
        students = c.fetchall()

        conn.commit()

        conn.close()
        
        a = tk.Label(disp_st,text= tese)
        a.pack(side='top')
        b = tk.Frame(disp_st)
        b.pack()
        columns = ('nomes', 'escolha')
        tree = ttk.Treeview(b, columns=columns, show='headings')
        tree.column("escolha",anchor='center')
        tree.heading('nomes', text='Estudante', anchor='center')
        tree.heading('escolha', text='Escolha', anchor='center')

        for i in students:
            tree.insert('', tk.END, values=i)
        tree.pack()

        c = tk.Button(disp_st, text ="Voltar", command = lambda:[disp_st.destroy(),main()])
        c.pack(side='bottom')
        #b.pack(side = 'left', fill = 'both' )
    disp_st.mainloop()

def sim_search():
    stud_window = tk.Tk()

    a = tk.Label(stud_window, text = 'Nome a pesquisar (considerar acentos)')
    def help():
        search = s.get()
        stud_window.destroy()
        return search
    s = tk.Entry(stud_window)
    b = tk.Button(stud_window, text ="Pesquisar", command = lambda:[select_sim(help())])

    a.pack()
    s.pack()
    b.pack()

    stud_window.mainloop()

def select_sim(search):
    results = tk.Tk()
    col = pd.read_excel('predictions_final.xlsx')
    h = pd.Series.to_list(col.Nome)
    def helpp():
        choice = c.get()
        if int(choice)>len(matching) or int(choice)<1:
            mode = 0
            name = str('')
            tese = str('')
            orient = str('')
            prop = str('')
        else:
            mode = 1
            id_i = h.index(matching[int(choice)-1])
            tese = col.Tese[id_i]
            prop = col.Proponente[id_i]
            orient =  str(col.Orientador[id_i])
            name = matching[int(choice)-1]
        results.destroy()
        return mode, name, tese, prop, orient
    matching = [i for i in h if search.lower() in i.lower()]
    if matching:
        e = tk.Scrollbar(results)
        a = tk.Listbox(results,width=100, yscrollcommand = e.set)
        for i in range(0,len(matching)):
            a.insert('end', str(i+1) + " " + matching[i])
            #a = tk.Label(results, text = out)
        b = tk.Label(results, text = 'Opção (número)')
        c = tk.Entry(results)
        d = tk.Button(results, text ="Simular", command = lambda:[disp_sim(helpp())])
        d.pack(side='bottom')
        c.pack(side='bottom')
        b.pack(side='bottom')
        a.pack(side = 'left', fill = 'both' )
        e.pack(side = 'right', fill = 'y')
    else:
        a = tk.Label(results,text = "Não existe") 
        d = tk.Button(results, text ="Voltar", command = lambda:[results.destroy(),main()]) 
        a.pack()
        d.pack()
    results.mainloop()

def disp_sim(arg):
    disp_st = tk.Tk()
    if arg[0] == 0:
        a = tk.Label(disp_st,text="Vai à merda")
        c = tk.Button(disp_st, text ="Voltar", command = lambda:[disp_st.destroy(),main()])
        a.pack(side='top')
        c.pack(side='bottom')
    else:
        a = tk.Label(disp_st,text= arg[1])
        a.pack(side='top')
        b = tk.Label(disp_st,text= "\nTese: " + arg[2] + "\nProponente: " + arg[3] + "\nOrientador: " + arg[4])
        b.pack()
        c = tk.Button(disp_st, text ="Voltar", command = lambda:[disp_st.destroy(),main()])
        c.pack(side='bottom')
    disp_st.mainloop()

def main():
    window = tk.Tk()
    window.title("TeseInator")

    menu = tk.Label(text = 'Menu')
    a = tk.Button(window, text ="Pesquisar por Aluno", height=2, width=40,command = lambda:[window.destroy(),student_search()])
    b = tk.Button(window, text ="Pesquisar por Tese", height=2, width=40,command = lambda:[window.destroy(),thesis_search()])
    c = tk.Button(window, text ="Simulador de Colocações (experimental)", height=2, width=40,command = lambda:[window.destroy(),sim_search()])
    d = tk.Button(window, text ="Sair", height=2, width=40, command=window.destroy)

    menu.pack()
    a.pack()
    b.pack()
    c.pack()
    d.pack()

    window.mainloop()

main()
