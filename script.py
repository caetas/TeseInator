import pandas as pd
import sqlite3

lixo = input('Bem-vindo ao Cuscador de Teses, um projeto open-source desenvolvido por mim\nAtenção aos acentos, mas não é case sensitive (prima Enter para continuar)')

while(1):
    print('\n\nMenu\n1-Pesquisar por aluno\n2-Pesquisar por nome da Tese\n3-Simulador de Colocação (experimental)\nCtrl+c para sair\n')
    menu = input("Opção pretendida: ")
    menu = int(menu)

    if menu == 1:
        conn = sqlite3.connect('electro.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT id,nome FROM alunos")
        names = c.fetchall()
        conn.commit()
        conn.close()

        name_list = [row[1] for row in names]
        search = input('\nIntroduza o nome a pesquisar: ')
        matching = [i for i in name_list if search.lower() in i.lower()]
        if matching:
            for i in range(0,len(matching)):
                print(i+1,matching[i])
            choice = input("\nQue ocorrência quer (número)?: ")
            if int(choice)>len(matching):
                    print("Vai à merda")
            else:
                id_i = name_list.index(matching[int(choice)-1])
                idd = names[id_i][0]
                print("\n")
                print(matching[int(choice)-1])
                print("\n")
                conn = sqlite3.connect('electro.db')

                c = conn.cursor()
                query = "SELECT n_escolha,tese,proponente,orientador FROM alunos where id = "+str(idd)
                c.execute(query)
                thesis = c.fetchall()

                conn.commit()

                conn.close()
                for i in range(0,len(thesis)):
                    print("Escolha ", thesis[i][0])
                    print("Tema: ", thesis[i][1])
                    print("Proponente: ", thesis[i][2])
                    print("Orientador: ", str(thesis[i][3]))
                    print("\n")
        else:
            print('Não existe')

        input('\nPrima enter para continuar')


    elif menu == 2:
        conn = sqlite3.connect('electro.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT tese FROM alunos")
        teses = c.fetchall()
        conn.commit()
        conn.close()

        teses = [row[0] for row in teses]
        search = input('\nIntroduza a tese a pesquisar: ')
        matching = [i for i in teses if search.lower() in i.lower()]
        if matching:
            for i in range(0,len(matching)):
                print(i+1,matching[i])
            choice = input("\nQue ocorrência quer (número)?: ")
            if int(choice)>len(matching):
                print("Vai à merda")
            else:
                id_i = teses.index(matching[int(choice)-1])

                print("\n")
                print(matching[int(choice)-1])
                print("\n")
                conn = sqlite3.connect('electro.db')

                c = conn.cursor()
                query = "SELECT nome,n_escolha FROM alunos WHERE tese = '"+matching[int(choice)-1]+"' ORDER BY n_escolha ASC"
                c.execute(query)
                students = c.fetchall()

                conn.commit()

                conn.close()
                print("{:<70} {:<10}".format("Nome", "Escolha"))
                for i in students:
                    nome, escolha = i[0],i[1]
                    print("{:<70} {:<10}".format(nome, escolha))
        else:
            print('Não existe')
        input('\nPrima enter para continuar')

    elif menu == 3:
        col = pd.read_excel('predictions_final.xlsx')
        h = pd.Series.to_list(col.Nome)
        search = input('Introduza o nome a pesquisar: ')
        matching = [i for i in h if search.lower() in i.lower()]
        if matching:
            for i in range(0,len(matching)):
                print(i+1,matching[i])
            choice = input("Que ocorrência quer (número)?: ")
            if int(choice)>len(matching):
                print("Vai à merda")
            else:
                id_i = h.index(matching[int(choice)-1])
                print("\n")
                print(matching[int(choice)-1])
                print("\n")
                print("Tema: ", col.Tese[id_i])
                print("Proponente: ", col.Proponente[id_i])
                print("Orientador: ", str(col.Orientador[id_i]))
                print("\n")
        else:
            print('Não existe')
        input('\nPrima enter para continuar')
    
    else:
        print('\nNúmero inválido')