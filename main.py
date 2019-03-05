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


# modulos criados importados
from cor3.banner import banner


def main():
    banner()
    print ("""

	\t1 - Add-Key
	\t2 - Search
	\t3 - Exit
        \t4 - Sobre
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
        op = int(input('Shodan->> '))
        if op == 1:
            if(os.path.exists('.Key/key.txt') == True):
                print('Chave existente !')
                time.sleep(1)
                os.system('python3 main.py')
            elif(os.path.exists('.Key/key.txt') == False):
                add_key = input('Add-Key->> ')
                file_key = open('.Key/key.txt','x+t')
                file_key.write('{}'.format(add_key))
                file_key.close()
            
        elif op == 2:
            if(os.path.exists('.Key/key.txt') == True):
                api = ""

                file_addon = open('.Key/key.txt','r')
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
                        print ('\033[91mBanner: \033[01;94m{}\033[0m'.format(result['data']))
                        print ('\033[01;91mPort: \033[01;94m{}\033[0m'.format(result['port']))
                        print ('\033[01;91mOrganização: \033[01;94m{}\033[0m'.format(result['org']))
                        print ('\033[01;91mSistema Operacional: \033[01;94m{}\033[0m'.format (result['os']))
                        print('-'*30)

                except shodan.APIError as e:
                    print ("Error [!] {}".format(e))
            if(os.path.exists('.Key/key.txt') == False):
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
