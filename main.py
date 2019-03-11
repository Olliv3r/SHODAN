#!/usr/bin/env python3
# nome: shodan
# Criador: olive
# descrição: Traduzido de inglês-O shodan é um mecanismo de busca.


# modulos importados
import shodan
import os
import sys
import time
import subprocess


def main():
    os.system('sh cor3/.banner.sh')
    print ("""
    
    \t1 -> Adicionar {chave}
    \t2 -> Buscar IP de sistemas
    \t3 -> Sair
    \t4 -> Sobre shodan
    """)

def msg_search():
    print("\033[01;92mExemplos de coisas a ser buscado aqui, (\033[00;94mWEBCAM\033[01;96m=\033[01;91mwecamxp, \033[00;94msistemas operacionais\033[01;96m=\033[01;91mwindows, \033[00;94mservidores\033[01;96m=\033[01;91mapache2,\033[00;94m etc.\033[0m")


def api_key():
    # objeto criado
    global add_key
    add_key = ""
    api = shodan.Shodan(add_key)


sobre = """\nTraduzido de inglês-O Shodan é um mecanismo de busca que permite ao usuário encontrar tipos específicos de computadores conectados à Internet usando uma variedade de filtros. Alguns também o descreveram como um mecanismo de pesquisa de banners de serviço, que são metadados que o servidor envia de volta ao cliente\n"""


try:
    def main_program():

        main()
        op = int(input('First-stage->> '))
        if op == 1:
            if(os.path.exists('/data/data/com.termux/files/home/.shodan/api_key') == True):
                print('Chave existente !')
                time.sleep(1)
                os.system('python3 main.py')
            elif(os.path.exists('/data/data/com.termux/files/home/.shodan/api_key') == False):
                print('Chave não existe !')
                time.sleep(0.5)
                subprocess.run('clear')
                print("\033[01;93mCole aqui a chave da sua conta\033[0m")
                add_key = input('\033[01;96mfirst-stage-Add-Key->> \033[0m')
                try:
                    os.system('shodan init {}'.format(add_key))
                    if(os.path.exists('/data/data/com.termux/files/home/.shodan/api_key') == True):

                        file_key_open = open('/data/data/com.termux/files/home/.shodan/api_key','r')
                        
                        file_file_key = open('/data/data/com.termux/files/home/SHODAN/cor3/api_key','w')

                        file_open = file_key_open.read()
                        file_file_key.write('{}'.format(file_open))
                        file_file_key.close()
                        os.system("python3 main.py")
                except shodan.APIError as erro:
                    print("Erro ! {}".format(erro))
        elif op == 2:
            if(os.path.exists('/data/data/com.termux/files/home/.shodan/api_key') == True):
                api = ""

                file_addon = open('/data/data/com.termux/files/home/.shodan/api_key','r')
                api = shodan.Shodan(file_addon)

                # buscar internet das coisas expecificas
                msg_search()
                search = input('Shodan->> ')
                try:
                    # mostrar resultados da busca
                    resultado = api.search(search)
                    print ("\033[01;96mResultados: \033[0m {}".format(resultado['total']))
                    time.sleep(1.5)


                    for result in resultado['matches']:
                        print('-'*30)
                        print ('\033[01;91mIP: \033[01;94m {}\033[0m'.format(result['ip_str']))
                        #print ('\033[91mBanner: \033[01;94m{}\033[0m'.format(result['data']))
                        print ('\033[01;91mPort: \033[01;94m{}\033[0m'.format(result['port']))
                        print ('\033[01;91mOrganização: \033[01;94m{}\033[0m'.format(result['org']))
                        print ('\033[01;91mSistema Operacional: \033[01;94m{}\033[0m'.format (result['os']))
                        print('-'*30)

                except shodan.APIError as e:
                    print ("Error [!] {}".format(e))
            elif(os.path.exists('/data/data/com.termux/files/home/.shodan/api_key') == False):
                print ("Chave Não estar adicionada")
                time.sleep(2)
                os.system('python3 main.py')
        elif op == 3:
            print("Encerrado !")
            sys.exit()

        elif op == 4:
            print ("UM RESUMO DO SHODAN")
            print (sobre)
            enter = input("Da EMTER para voltar; ")
            os.system("python3 main.py")

    main_program()

except KeyboardInterrupt:
    print ("Encerrado !")
except EOFError:
    print ("Encerrado !")
except ModuleNotFoundError as a:
    print("Módulo {} Não Instalado! execute pip3 install shodan".format(a))
