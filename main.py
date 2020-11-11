import requests

#INDICO O USO DESTA APLICAÇÃO COM O TERMUX NO ANDROID
#FAÇA UMA LISTA UTILIZANDO O NETSTAT E COMBINE COM ESTE
#SCRIPT

#use ip.txt como exemplo
print('Programa para supervisionar conecções no Android\n Desenvolvido por Romildo Silva')
lista = input('Digite o caminho até a lista: ')
ipslist = open(lista)

for ip in ipslist.readlines():
    ipn = str(ip.replace('\n', ''))
    url = str('https://king.host/wiki/wp-content/themes/kinghost-wiki/includes/ip-api.php?ip={}'.format(ipn))
    print('------------------------------------')
    req = requests.get(url)
    reque = req.text.replace(',', '\n')
    print(reque.replace('"', ''))
    print('------------------------------------')
