import requests_html, requests, telebot, re, json
import random
import string
import string
from random import *
from time import sleep

bot = telebot.TeleBot("1550795018:AAHv93_RaqDaLm8917rwi_RH4WU4C3GjHKM")

PRIVADO = [1310754581,1220841895]
#
#
GRUPO = []
#
#
EXCEPT = [-1001254182046,-1001279149596,-1001483799497]  # QUANDO UM GRUPO PODER TER TELEFONE BOTA O ID AI ( TEL, NOME, CEP ETC... )
#
#
ANONY = [] # OFF


@bot.message_handler(commands=['start'])
def boavinda(message1):
    ide = message1.chat.id
    liste = PRIVADO + ANONY
    if ide in liste:

        bot.reply_to(message1, '<b>' 'ð¥ VOCÃ TEM ACESSO PORRA! ð¥' '</b>', parse_mode='HTML')
        bot.send_message(ide, 'â ' '<b>' 'use ' '</b>''<code>' '/menu' '</code>''<b>' ' e veja os comandos' '</b>' ' â', parse_mode='HTML')
    
    else:
        bot.reply_to(message1, '<b>' + 'ð« ' + '@'+message1.chat.username + ' ACESSO NEGADO! ð«' '</b>', parse_mode='HTML')
        bot.send_message(ide, '<b>' 'â Compre o seu acesso com meu Dono @iara_limaz' '</b>', parse_mode='HTML')
        
@bot.message_handler(commands=['trabalhos'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cpf')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://cadsusnonny.000webhostapp.com/cpfsusDKZ.php?token=9DatOhxI2jlu2k2&cpf=' + ip)
                    req = url.json
                    op = req()['data_nasc'][6:10]
                    jog = 2020 - int(op)
                    reeq = url.json()
                    hels = bot.reply_to(nome, '<b>' '  CONSULTA VIP FEITA â' '</b>' + '\n\n' + '<b>' 'â¢ CPF: ' '</b>' '<code>' + req()['cpf'] + '</code>' '\n' + '<b>' 'â¢ CNS: ' '</b>' '<code>' + req()['cns'] + '</code>' '\n' + '<b>' 'â¢ NOME: ' '</b>' '<code>' + req()['nome'] + '</code>' '\n' + '<b>' 'â¢ NASCIMENTO: ' '</b>' '<code>' + req()['data_nasc'] + '</code>' '\n' + '<b>' 'â¢ IDADE: ' '</b>' '<code>' + str(jog) + '</code>' + '\n' + '<b>' 'â¢ MÃE: ' '</b>' '<code>' + req()['nomeMae'] + '</code>' '\n' + '<b>' 'â¢ PAI: ' '</b>' '<code>' + req()['nomePai'] + '</code>' '\n' + '<b>' 'â¢ RAÃA COR: ' '</b>' '<code>' + req()['descricaoRacaCor'] + '</code>' '\n' + '<b>' 'â¢ SEXO: ' '</b>' '<code>' + req()['descricaoSexo'] + '</code>' '\n' + '<b>' 'â¢ MUNICIPIO NASC: ' '</b>' '<code>' + req()['municipioNasc'] + '</code>' '\n' + '<b>' 'â¢ ESTADO NASC: ' '</b>' '<code>' + req()['estadoNasc'] + '</code>' '\n\n' + '<b>' 'â¢ LOGRADOURO: ' '</b>' '<code>' + req()['nomeLogradouro'] + '</code>' '\n' + '<b>' 'â¢ NÃMERO: ' '</b>' '<code>' + req()['numero'] + '</code>' '\n' + '<b>' 'â¢ COMPLEMENTO: ' '</b>' '<code>' + req()['complemento'] + '</code>' '\n' + '<b>' 'â¢ BAIRRO: ' '</b>' '<code>' + req()['bairro'] + '</code>' '\n' + '<b>' 'â¢ CEP: ' '</b>' '<code>' + req()['numeroCEP'] + '</code>' '\n' + '<b>' 'â¢ MUNICIPIO: ' '</b>' '<code>' + req()['nomeMunicipio'] + '</code>' '\n' + '<b>' 'â¢ UF: ' '</b>' '<code>' + req()['siglaUF'] + '</code>' '\n' + '<b>' 'â¢ ESTADO: ' '</b>' '<code>' + req()['nomeUF'] + '</code>' '\n' + '<b>' 'â¢ PAÃS: ' '</b>' '<code>' + req()['nomePais'] + '</code>' '\n\n' + '<b>' 'â¢ TELEFONE: ' '</b>' '<code>' + str(reeq['telefone'][0]['numero']) + '</code>' + '\n' + '<b>' 'â¢ DD: ' '</b>' '<code>' + str(reeq['telefone'][0]['dd']) + '</code>' + '\n' + '<b>' 'â¢ TIPO: ' '</b>' '<code>' + str(reeq['telefone'][0]['tipo']) + '</code>' + '\n\n' + '<b>' 'â¢ RG: ' '</b>' '<code>' + str(req()['dadosRg'][0]['numeroIdentidade']) + '</code>' + '\n' + '<b>' 'â¢ IDENTIFICADOR: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['identificador'][10:20]) + '</code>' + '\n' + '<b>' 'â¢ EXPEDIÃÃO: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['dataExpedicao']) + '</code>' + '\n' + '<b>' 'â¢ EMISSOR: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['nomeOrgaoEmissor']) + '</code>' + '\n' + '<b>' 'â¢ SIGLA: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['siglaOrgaoEmissor']) + '</code>' + '\n' + '<b>' 'â¢ NIS: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['identificadorNis'][9:20]) + '</code>' + '\n' + '<b>' 'â¢ DOCUMENTO: ' '</b>' '<code>' + str(reeq['dadosRg'][0]['numeroDocumento']) + '</code>' + '\n\n' + '<b>' 'â¢ CERTIDÃO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['identificador'][9:20]) + '</code>' + '\n' + '<b>' 'â¢ TIPO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['TipoCertidao']) + '</code>' + '\n' + '<b>' 'â¢ CARTORIO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['nomeCartorio']) + '</code>' + '\n' + '<b>' 'â¢ LIVRO/FOLHA: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['livro']) + '</code>' + '\n' + '<b>' 'â¢ TERMO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['termo']) + '</code>' + '\n' + '<b>' 'â¢ EMISSÃO: ' '</b>' '<code>' + str(reeq['dadosCertidao'][0]['dataEmissaoCertidao']) + '</code>' + '\n\n' + '<b>' 'â¢ DONO: @iara_limaz' '\n' 'â¢ GRUPO: @iara_consultas' '\n' 'â¢ CANAL: @iara_referencias' '</b>', parse_mode='HTML')
                    hells = bot.reply_to(nome, '<b>' 'ð® CONSULTA SE APAGARÃ EM 1 MINUTO ð®' '</b>', parse_mode='HTML')
                    sleep(60)
                    bot.delete_message(id1, hels.message_id)
                    bot.delete_message(id1, hells.message_id)
                    bot.delete_message(id1, nome.message_id)
                except:
                	bot.reply_to(nome, '<b>' 'TÃ ERRADO VEI !' '</b>', parse_mode='HTML')
            else:
                		bot.reply_to(nome, '<b>' 'â Compre acesso com meu Dono @iara_limazâ' '</b>', parse_mode='HTML')
                		
##

session = requests_html.HTMLSession()

##

@bot.message_handler(commands=['bin'] + ['BIN'])
def lbz(men):
            notbin = []
            bid = men.chat.id
            cp = men.text
            if bid in notbin:
                bot.reply_to(men, 'â  ðð¤ð£ð¨ðªð¡ð©ð ðð ððð£ ððð¨ðð©ðð«ððð ð¥ðð§ð ðð¨ð©ð ðð§ðªð¥ð¤ â ')
            else:
                try:
                    bn = re.sub('[^0-9]', '', cp)
                    response = requests.get('https://binlist.io/lookup/{}'.format(bn))
                    res = response.content
                    r = json.loads(res)
                    if str(r['success']) == str('True'):

                        bot.reply_to(men, '\n         ã¤   ã¤<b>â DADOS DA BIN â</b>\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n\n<b>â¢ BIN</b>: ' + '<code>' + str(
                            r['number']['iin']) + '</code>' + '\n' +
                                     '<b>â¢ BANDEIRA</b>: ' + '<code>' + str(r['scheme']) + '</code>' + '\n' +
                                     '<b>â¢ TIPO</b>: ' + '<code>' + str(r['type']) + '</code>' + '\n' +
                                     '<b>â¢ NÃVEL</b>: ' + '<code>' + str(r['category']) + '</code>' + '\n' +
                                     '<b>â¢ BANCO</b>: ' + '<code>' + str(r['bank']['name']) + '</code>' + '\n' +
                                     '<b>â¢ TEL BANCO</b>: ' + '<code>' + str(r['bank']['phone']) + '</code>' + '\n' +
                                     '<b>â¢ URL</b>: ' + str(r['bank']['url']) + '\n' +
                                     '<b>â¢ PAÃS</b>: ' + '<code>' + str(r['country']['name']) + '</code>' + '\n' +
                                     '<b>â¢ ID</b>: ' + '<code>' + str(r['country']['alpha3']) + '</code>' + '\n' +
                                     '<b>â¢ SIGLA</b>: ' + '<code>' + str(r['country'][
                                                               'alpha2']) + '</code>' + '\n' +  '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n<b>â¢ DONO: @iara_limaz' + '\n' + 'â¢ GRUPO: @iara_consultas' + '\n' + 'â¢ CANAL:@iara_referencias' + '</b>', parse_mode='HTML')
                    else:
                        bot.reply_to(men, '<b>VEJA O EXEMPLO</b>: "' + '<code>' + '/bin 651652' + '</code>' + '"', parse_mode='HTML')
                except:
                    bot.reply_to(men, '<b>â  DIGITE UMA BIN KRAI â </b>', parse_mode='HTML')

##

@bot.message_handler(commands=['cep'] + ['CEP'])
def bno(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/cep':
        bot.reply_to(men, '<b>' + 'â  DIGITE UM CEP â ' + '</b>', parse_mode='HTML')
    if men.text == '/CEP':
        bot.reply_to(men, '<b>' + 'â  DIGITE UM CEP â ' + '</b>', parse_mode='HTML')
    else:
        try:
        	ipp = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cep/search/' + ipp + '?token=4f8d9149be4858c837b8b38f5c0d194a')
        	reqi = url.json
        	bot.reply_to(men, '<b>' 'ã¤â CONSULTA DE CEP â' '</b>' + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n\n' + '<b>' 'â¢ CEP: ' '</b>' '<code>' + ipp + '</code>' '\n' + '<b>' 'â¢ UF: ' '</b>' '<code>' + reqi()['data']['state'] + '</code>' '\n' + '<b>' 'â¢ ESTADO: ' '</b>' '<code>' + reqi()['data']['state_name'] + '</code>' '\n' + '<b>' 'â¢ CIDADE: ' '</b>' '<code>' + reqi()['data']['city'] + '</code>' '\n\n' + '<b>' 'â¢ LOGRADOURO: ' '</b>' '<code>' + reqi()['data']['address'] + '</code>' '\n' + '<b>' 'â¢ BAIRRO: ' '</b>' '<code>' + reqi()['data']['district'] + '</code>' '\n' + '<b>' 'â¢ NAME: ' '</b>' '<code>' + reqi()['data']['address_name'] + '</code>' '\n' + '<b>' 'â¢ IBGE: ' '</b>' '<code>' + reqi()['data']['city_code'] + '</code>' '\n' + '<b>' 'â¢ STATUS: ' '</b>' '<code>' + reqi()['data']['status'] + '</code>' '\n' + '<b>' 'â¢ MENSAGEM: ' '</b>' '<code>' + reqi()['data']['message'] + '</code>' '\n\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' + '<b>' 'â¢ DONO: @iara_limaz' + '\n' + 'â¢ GRUPO: @@iara_consultas' + '\n' + 'â¢ CANAL: @iara_referencias' + '</b>', parse_mode='HTML')
        except:
                   bot.reply_to(men, '<b>' + 'TA ERRADO ;(' + '</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['menu'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + 'â  ERRADO CARA â ' + '</b>', parse_mode='HTML')
    else:
        try:
        	bot.reply_to(men, '<b>' ' iara_limaz- CÃ¸nsultas Menuâ¡' '</b>' + '\n\n' + '<b>' 'ð¹[â] CEP:</b><code> /cep 89874000' '</code>' + '\n' + '<b>' 'ð¹[â] BIN:</b><code> /bin 545323' + '</code>' '\n' + '<b>' 'ð¹[â] CPF:</b><code> /cpf 29993559806' + '</code>' '\n' + '<b>' 'ð¹[â] TELEFONE: ' '</b>''<code>' '/tel 49991059058' '</code>' + '\n' + '<b>' 'ð¹[â] NOME: ' '</b>''<code>' '/nome Jhonny Carvalho' '</code>' + '\n' + '<b>' 'ð¹[â] VIZINHOS: ' '</b>' '<code>' + '/vizinhos 03493217528' + '</code>' + '\n' + '<b>' 'ð¹[â] EMAIL: ' '</b>' '<code>' + '/email alexandre.akl@ig.com.br' + '</code>' + '\n' + '<b>' 'ð¹[â] IP: ' '</b>' '<code>' + '/ip 204.152.203.157' + '</code>' + '\n' + '<b>' 'ð¹[â] PLACA: ' '</b>' '<code>' + '/placa GTJ6699' + '</code>' + '\n\n' + '<b>' 'â[OFF] CHK CC: </b><code>/chkcc 6509079001042420' '</code>' '\n\n' + '<b>' 'ð¹[â] GERAR CPF:</b><code> /gencpf' '</code>' + '\n' + '<b>' 'ð¹[â] GERAR EMAIL:</b><code> /genemail' + '</code>' + '\n' + '<b>' 'ð¹[â] GERAR CNPJ:</b><code> /gencnpj' + '</code>' '\n\n' + '<b>' 'ð¹[â] VALIDAR CPF:</b><code> /validar 03655915993' + '</code>' + '\n\n' + '<b>' 'ð[â] ID: ' '</b>' '<code>' + '/id' + '</code>' + '\n\n' + '<b>ð By: @BOT_DA_LIMAA_TA?</b>' , parse_mode='HTML')
        except:
                    bot.reply_to(men, '<b>' + '.' + '</b>', parse_mode='HTML')

##
@bot.message_handler(commands=['validar'] + ['VALIDAR'])
def bnio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + 'â  DIGITE UM CPF â ' + '</b>', parse_mode='HTML')
    if men.text == '/VALIDAR':
        bot.reply_to(men, '<b>' + 'â  DIGITE UM CPF â ' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	urrl = requests.get("http://geradorapp.com/api/v1/cpf/validate/" + ip + "?token=4f8d9149be4858c837b8b38f5c0d194a")
        	reeq = urrl.json
        	bot.reply_to(men, '<b>' 'ã¤â VALIDAR CPF â' + '</b>' +'\nâ±â±â±â±â±â±â±â±â±â±â±\n\n' + '<b>' + 'â¢ CPF: ' + '</b>' + '<code>' + reeq()['data']['number_formatted'] + '</code>' + '\n' + '<b>' + 'â¢ NOME: ' + '</b>' + '<code>' + 'N/A' + '</code>' + '\n' + '<b>' + 'â¢ SITUAÃÃO: ' + '</b>' + '<code>' + reeq()['data']['message'] + '</code>' + '\n\nâ±â±â±â±â±â±â±â±â±â±â±\n' + '<b>' + 'â¢ DONO: @iara_limaz' + '\n' + 'â¢ GRUPO: @iara_consultas' + '\n' + 'â¢ CANAL: @iara_referencias' + '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '<b>' + 'OPS, CPF INVÃLIDO OU NÃO ENCONTRADO! :(' + '</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['cnpj'] + ['CNPJ'])
def bnioo(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/cnpj':
        bot.reply_to(men, 'â  ð¿ððððð ðð ð¾ððð, ðð¿ðððð¼ â ')
    if men.text == '/CNPJ':
        bot.reply_to(men, 'â  ð¿ððððð ðð ð¾ððð, ðð¿ðððð¼ â ')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	
        	header = {"Authorization": "Bearer NU.FRdMla45531d4c68b1e837fde9d4c401dc56c56875e8a560595081f2d06ba8068d7e4"}
        	
        	url = requests.get('https://api.nudata.com.br/receita/{}'.format(ip), headers=header)
        	o = url.text
        	req = json.loads(o)
        
        	bot.reply_to(men, 'ã¤ã¤ã¤ã¤ã¤â ð¿ð¼ð¿ðð ð¾ððð â' +
'â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\nð¾ððð: ' '<code>' + str(req['result']['cnpj']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\nðððð: ' '<code>' + str(req['result']['tipo']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ðððð: ' '<code>' + str(req['result']['nome']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ððððððððð: ' '<code>' + str(req['result']['telefone']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ððð¼ðð: ' '<code>' + str(req['result']['email']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ððððð¼ð¾Ì§ð¼Ìð: ' '<code>' + str(req['result']['situacao']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ððððð¼ð¿ðððð: ' '<code>' + str(req['result']['logradouro']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ð½ð¼ðððð: ' '<code>' + str(req['result']['bairro']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ððÌðððð: ' '<code>' + str(req['result']['numero']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' + 
                     'ð¾ðð: ' '<code>' + str(req['result']['cep']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' + 
                     'ððððð¾ðÌððð: ' '<code>' + str(req['result']['cidade']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n'
                     'ððððð: ' '<code>' + str(req['result']['porte']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ð¼ð½ðððððð¼: ' '<code>' + str(req['result']['dataAbertura']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ðð¼ððð¼ððð¼: ' '<code>' + str(req['result']['nomeFantasia']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ððð¼ððð: ' '<code>' + str(req['status']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ð¾ð¼ðððð¼ð: ' '<code>' + str(req['result']['capitalSocial']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n'
                     'ð¼ððððð¿ð¼ð¿ð ððððð¾ððð¼ð: ' '<code>' + str(req['result']['atividadePrimaria']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ð¼ððððð¿ð¼ð¿ð ððð¾ððð¿ð¼Ìððð¼: ' '<code>' + str(req['result']['atividadeSecundaria']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                     'ð¿ð¼ðð¼ ððððð¼ð¾Ì§ð¼Ìð: ' '<code>' + str(req['result']['dataSituacao']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' + 'ðð: ' '<code>' + str(req['result']['estado']) + '</code>' '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' + 'ð¿ðððð: ' '<code>' + str(req['result']['qsa']) + '</code>'  '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±â±\nððððð:  @iara_limaz\nð¾ð¼ðð¼ð:  @iara_referencias', parse_mode='HTML')
        except:
                     	bot.reply_to(men, 'CNPJ NÃO ENCONTRADO MANIN')
##

@bot.message_handler(commands=['gencpf'])
def lbx(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + 'â  â ' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	resposta = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	cpff = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzinn = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbx = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lb = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbzinn = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkz = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	andrei = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	pc = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	gamer = respostaa()['data']['number_formatted']
        	bot.reply_to(men, '<b>' 'ã¤â¡ GERADOR DE CPF â¡' '</b>' + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + resposta + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>' '<code>' + cpff + '</code>' + '\n' + '<b>' + 'â¢ CPF: ' + '</b>' '<code>' + dkzinn + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + lbx + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + lb + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + lbzinn + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + dkz + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + andrei + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + pc + '</code>' + '\n' + '<b>' 'â¢ CPF: ' '</b>''<code>' + gamer + '</code>' + '\n\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' + '<b>' + 'â¢ DONO:@iara_limaz' + '\n' + 'â¢ GRUPO: @iara_consultas' + '\n' + 'â¢ CANAL: @iara_referencias' + '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '.')

##

@bot.message_handler(commands=['gencnpj'])
def lbxk(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + 'â  â ' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	respostak = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	cpffk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzinnk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbxk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbzinnk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	andreik = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	pck = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	gamerk = respostaa()['data']['number_formatted']
        	bot.reply_to(men, '<b>' 'ã¤â¡ GERADOR DE CNPJ â¡' '</b>' + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±\n\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + respostak + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>' '<code>' + cpffk + '</code>' + '\n' + '<b>' + 'â¢ CNPJ: ' + '</b>' '<code>' + dkzinnk + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + lbxk + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + lbk + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + lbzinnk + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + dkzk + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + andreik + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + pck + '</code>' + '\n' + '<b>' 'â¢ CNPJ: ' '</b>''<code>' + gamerk + '</code>' + '\n\nâ±â±â±â±â±â±â±â±â±â±â±â±â±â±\n' + '<b>' + 'â¢ DONO: @iara_limaz' + '\n' + 'â¢ GRUPO: @@iara_consultas' + '\n' + 'â¢ CANAL: @iara_referencias' + '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '.')

####

@bot.message_handler(commands=['placa'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT + ANONY
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json", verify=False)
                    req = url.json()
                    helss = bot.reply_to(nome, '<b>' 'â CONSULTA CONCLUIDA â' '</b>' + '\n\n' + '<b>' 'â¢ PLACA: ' '</b>''<code>' + req['placa'] + '</code>' + '\n' + '<b>' 'â¢ ANO: ' '</b>''<code>' + req['ano'] + '</code>' + '\n' + '<b>' 'â¢ CHASSI: ' '</b>''<code>' + req['chassi'] + '</code>' + '\n' + '<b>' 'â¢ COR: ' '</b>''<code>' + req['cor'] + '</code>' + '\n' + '<b>' 'â¢ DATA: ' '</b>''<code>' + req['data'] + '</code>' + '\n' + '<b>' 'â¢ ALARME: ' '</b>''<code>' + req['dataAtualizacaoAlarme'] + '</code>' + '\n' + '<b>' 'â¢ VEÃCULO: ' '</b>''<code>' + req['dataAtualizacaoCaracteristicasVeiculo'] + '</code>' + '\n' + '<b>' 'â¢ ROUBO/FURTO: ' '</b>''<code>' + req['dataAtualizacaoRouboFurto'] + '</code>' + '\n\n' + '<b>' 'â¢ MARCA: ' '</b>''<code>' + req['marca'] + '</code>' + '\n' + '<b>' 'â¢ MODELO: ' '</b>''<code>' + req['modelo'] + '</code>' + '\n\n' + '<b>' 'â¢ MUNICÃPIO: ' '</b>''<code>' + req['municipio'] + '</code>' + '\n' + '<b>' 'â¢ UF: ' '</b>''<code>' + req['uf'] + '</code>' + '\n\n' + '<b>' 'â¢ SITUAÃÃO: ' '</b>''<code>' + req['situacao'] + '</code>' + '\n\n' + '<b>' + 'â¢ DONO: @iara_limazâ¢ GRUPO: @iara_consultas\nâ¢ CANAL: @iara_referencias' + '</b>',parse_mode='HTML')
                    hellss = bot.reply_to(nome, '<b>' 'ð® CONSULTA SE APAGARÃ EM 1 MINUTO ð®' '</b>', parse_mode='HTML')
                    sleep(60)
                    bot.delete_message(id1, helss.message_id)
                    bot.delete_message(id1, hellss.message_id)
                    bot.delete_message(id1, nome.message_id)
                except:
                	bot.reply_to(nome, '<b>' 'TÃ ERRADO, IDIOTA!' '</b>', parse_mode='HTML')
            else:
                		bot.reply_to(nome, '<b>' 'â Compre acesso com meu Dono @iara_limaz â' '</b>', parse_mode='HTML')

####

@bot.message_handler(commands=['id'])
def boavinnda(message1):
    bot.reply_to(message1, '<b>' 'â¢ SEU ID: ' '</b>''<code>' + str(message1.chat.id) + '</code>' '\n'+ '<b>' 'â¢ NOME: ' '</b>' '<code>'+ message1.chat.first_name + '</code>' '\n' + '<b>''â¢ USERNAME: '+'@'+message1.chat.username + '</b>' , parse_mode='HTML')

##

@bot.message_handler(commands=['tel'] + ['TEL'])
def beroi(men):
            idee = men.chat.id
            permitidos = PRIVADO + EXCEPT + ANONY + [-1001481944556]
            if int(idee) in permitidos:
                session = requests_html.HTMLSession()

                if men.text == '/tel':
                    bot.reply_to(men, '<b>DIGITE UM NÃMERO, ANIMAL!</b>',
                                 parse_mode='HTML')
                elif men.text == '/TEL':
                    bot.reply_to(men, '<b>DIGITE UM NÃMERO, ANIMAL!</b>',
                                 parse_mode='HTML')
                else:

                    num = re.sub('[^0-9]', '', men.text)
                    r = session.get(
                        'http://191.252.153.147/buscasjl.php?token=Pg6ZKyXcrYfzSG2TKqc1&telefone={}'.format(num))
                    ar = r.html.find("td")
                    ar1 = r.html.find('tr')
                    try:
                        txt = ar[0].html
                        cpf = re.sub('[^0-9]', '', txt)
                        dados = str(ar1[1].text)

                        txt2 = ar[5].html
                        cpf2 = re.sub('[^0-9]', '', txt2)
                        dados2 = str(ar1[2].text)

                        txt3 = ar[10].html
                        cpf3 = re.sub('[^0-9]', '', txt3)
                        dados3 = str(ar1[3].text)

                        bot.reply_to(men,
                                     dados + '\n<b>CPF: </b>' + cpf + '\n\n' + dados2 + '\n<b>CPF: </b>' + cpf2 + '\n\n' + dados3 + '\n<b>CPF: </b>' + cpf3 + '\n\n<b>â¢ DONO: @iara_limaz\nâ¢ GRUPO: @iara_consultas\nâ¢ CANAL: @iara_referencias</b>',
                                     parse_mode='HTML')
                    except:
                        try:
                            txt = ar[0].html
                            cpf = re.sub('[^0-9]', '', txt)
                            dados = str(ar1[1].text)

                            txt2 = ar[1].html
                            cpf2 = re.sub('[^0-9]', '', txt2)
                            dados2 = str(ar1[2].text)

                            bot.reply_to(men,
                                         dados + '\n<b>CPF: </b>' + cpf + '\n\n' + dados2 + '\n<b>CPF: </b>' + cpf2 + '\n\n<b>â¢ DONO: @iara_limaz\nâ¢ GRUPO: @iara_consultas\nâ¢ CANAL: @iara_referencias</b>',
                                         parse_mode='HTML')
                        except:
                            try:
                                txt = ar[0].html
                                cpf = re.sub('[^0-9]', '', txt)
                                dados = str(ar1[1].text)
                                bot.reply_to(men, '<b>' 'â CONSULTA DE TEL CONCLUIDA â' '</b>' + '\n\n' + '<code>' +
                                             dados + '</code>' + '\n<b>CPF: </b>' '<code>' + cpf + '</code>' + '\n\n<b>â¢ DONO: @iara_limaz\nâ¢ GRUPO: @iara_consultasâ¢ CANAL: @iara_referencias</b>',
                                             parse_mode='HTML')
                            except:
                                bot.reply_to(men, '<b>NÃO ENCONTRADO PARSERO</b>', parse_mode='HTML')




            else:
                bot.reply_to(men, '<b>' 'â Compre acesso com meu Dono @iara_limaz â' '</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['vizinhos'])
def byti(men):
            chtid = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT + ANONY
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF, BURRO!' '</b>' ,
                                 parse_mode='HTML')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' 'â CONSULTA CONCLUIDA â' '</b>' + '\n\n' + '<b>' 'â¢ VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' 'â¢ DONO: @iara_limaz\nâ¢ GRUPO: @iara_consultas\nâ¢ CANAL: @iara_referencias' '</b>' , parse_mode='HTML')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' 'â CONSULTA CONCLUIDA â' '</b>' + '\n\n' + '<b>' 'â¢ VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' 'â¢ DONO: @iara_lmaz\nâ¢ GRUPO: @iara_consultas\nâ¢ CANAL: @iara_referencias' '</b>',
                                             parse_mode='HTML')
                            except:
                                bot.reply_to(men, '<b>NENHUM VIZINHO ENCONTRADO</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>OPS, NENHUM VIZINHO ENCONTRADO </b>', parse_mode="HTML")

            else:
                bot.reply_to(men, '<b>â Compre acesso com meu Dono @iara_limaz â</b>',
                             parse_mode='HTML')

##

@bot.message_handler(commands=['ip', 'IP'])
def bxniy(men):
            liberadoip = PRIVADO + GRUPO + EXCEPT + ANONY
            bid = men.chat.id
            if bid in liberadoip:
                mensagem = men.text
                if men.text == '/ip':
                    bot.reply_to(men, '<b>' 'DIGITE UM IP, ANIMAL!' '</b>', parse_mode='HTML')
                elif men.text == '/IP':
                    bot.reply_to(men, '<b>' 'DIGITE UM IP, ANIMAL!' '</b>', parse_mode='HTML')
                else:
                    try:
                        ip = re.sub('[^0-9.]', '', mensagem)
                        url = requests.get(
                            'https://king.host/wiki/wp-content/themes/kinghost-wiki/includes/ip-api.php?ip={}'.format(ip))
                        req = json.loads(url.text)
                        bot.reply_to(men,
                                     'â±â±â±â±â±â±â±â±â±â±â±â±â±\nðð: ' + req['query'] + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\nðð¼ðÌð: ' + req[
                                         'country'] + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ððððð¼ ðð¼ðÌð: ' + str(req['countryCode']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ððððð¼Ìð: ' + str(req['region']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ððððð¼Ìð ðð¼ðð: ' + str(req['regionName']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ð¾ðð¿ð¼ð¿ð: ' + str(req['city']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ð¾ðð: ' + str(req['zip']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ðð¼ððððð¿ð: ' + str(req['lat']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ðððððððð¿ð: ' + str(req['lon']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\n' +
                                     'ðððððð¿ðð: ' + str(req[
                                                                    'org']) + '\nâ±â±â±â±â±â±â±â±â±â±â±â±â±\nððððð:  @iara_consultas')
                    except:
                        bot.reply_to(men, '<b>IP NÃO ENCONTRADO</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>â Compre acesso com meu Dono iara_limaz  â</b>', parse_mode='HTML')

##

@bot.message_handler(commands=['email'] + ['EMAIL'])
def bqpwi(men):
            idee = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT + ANONY
            if int(idee) in permitidos:
                session = requests_html.HTMLSession()
                mensagem = men.text
                oi = str(mensagem[7:])

                if men.text == '/email':
                    bot.reply_to(men, '<b>' 'DIGITE UM EMAIL, ANIMAL' '</b>',
                                 parse_mode='HTML')
                elif men.text == '/EMAIL':
                    bot.reply_to(men, '<b>' 'DIGITE UM EMAIL, ANIMAL' '</b>',
                                 parse_mode='HTML')
                else:

                    r = session.get(
                        'http://191.252.153.147/buscasjl.php?token=Pg6ZKyXcrYfzSG2TKqc1&email={}'.format(oi))
                    ar = r.html.find("td")
                    ar1 = r.html.find('tr')
                    try:
                        txt = ar[0].html
                        cpf = re.sub('[^0-9]', '', txt)
                        dados = str(ar1[1].text)

                        txt2 = ar[5].html
                        cpf2 = re.sub('[^0-9]', '', txt2)
                        dados2 = str(ar1[2].text)

                        txt3 = ar[10].html
                        cpf3 = re.sub('[^0-9]', '', txt3)
                        dados3 = str(ar1[3].text)

                        bot.reply_to(men, '<b>' 'â CONSULTA CONCLUIDA â' '</b>' + '\n\n' +
                                    '<code>' + dados + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf + '</code>' + '\n\n' + '<code>' + dados2 + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf2 + '</code>' + '\n\n' + '<code>' + dados3 + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf3 + '</code>' + '\n\n<b>DONO: @iara_limaz: @iara_consultas\nCANAL: @iara_referencias</b>',
                                     parse_mode='HTML')
                    except:
                        try:
                            txt = ar[0].html
                            cpf = re.sub('[^0-9]', '', txt)
                            dados = str(ar1[1].text)

                            txt2 = ar[1].html
                            cpf2 = re.sub('[^0-9]', '', txt2)
                            dados2 = str(ar1[2].text)

                            bot.reply_to(men, '<b>' 'â CONSULTA CONCLUIDA â' '</b>' + '\n\n' +
                                        '<code>' + dados + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf + '</code>' + '\n\n' + '<code>' + dados2 + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf2 + '</code>' + '\n\n<b>DONO: @iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>',
                                         parse_mode='HTML')
                        except:
                            try:
                                txt = ar[0].html
                                cpf = re.sub('[^0-9]', '', txt)
                                dados = str(ar1[1].text)
                                bot.reply_to(men, '<b>' 'â CONSULTA CONCLUIDA â' '</b>' + '\n\n' +
                                            '<code>' + dados + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf + '</code>' + '\n\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>',
                                             parse_mode='HTML')
                            except:
                                N = bot.reply_to(men, '<b>EMAIL NÃO ECONTRADO!</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>' 'â Compre acesso com meu Dono @Iara_limaz â' '</b>',
                             parse_mode='HTML')

##

@bot.message_handler(commands=['master'] + ['MASTER'])
def bijgh(men):
            idee = men.chat.id
            permitidos = PRIVADO + EXCEPT + [-1001164204059] + ANONY
            if int(idee) in permitidos:

                if men.text == '/master':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF, ANIMAL!' '</b>',
                                 parse_mode='HTML')
                elif men.text == '/MASTER':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF, ANIMAL!' '</b>',
                                 parse_mode='HTML')
                else:
                    try:

                        num = re.sub('[^0-9]', '', men.text)
                        url = requests.get('http://191.252.157.10/getran.php?cpf={}'.format(num)).content
                        resp = json.loads(url)
                        try:
                            tel = ('<b>CODIGO OPERADORA: </b><code>' + str(
                                resp['telefone'][0]['codigo']) + '</code>\n' +
                                   '<b>DDD: </b><code>' + str(resp['telefone'][0]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(resp['telefone'][0]['numero']) + '</code>\n' +
                                   '<b>TIPO: </b><code>' + str(resp['telefone'][0]['tipoDescricao']) + '</code>\n\n' +
                                   '<b>CODIGO OPERADORA: </b><code>' + str(
                                        resp['telefone'][1]['codigo']) + '</code>\n' +
                                   '<b>DDD: </b><code>' + str(resp['telefone'][1]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(resp['telefone'][1]['numero']) + '</code>\n' +
                                   '<b>TIPO: </b><code>' + str(resp['telefone'][1]['tipoDescricao']) + '</code>\n\n' +
                                   '<b>CODIGO OPERADORA: </b><code>' + str(
                                        resp['telefone'][2]['codigo']) + '</code>\n' +
                                   '<b>DDD: </b><code>' + str(resp['telefone'][2]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(resp['telefone'][2]['numero']) + '</code>\n' +
                                   '<b>TIPO: </b><code>' + str(resp['telefone'][2]['tipoDescricao']) + '</code>\n'
                                   )
                        except:
                            try:
                                tel = ('<b>CODIGO OPERADORA: </b><code>' + str(
                                    resp['telefone'][0]['codigo']) + '</code>\n' +
                                       '<b>DDD: </b><code>' + str(resp['telefone'][0]['ddd']) + '</code>\n' +
                                       '<b>NUMERO: </b><code>' + str(resp['telefone'][0]['numero']) + '</code>\n' +
                                       '<b>TIPO: </b><code>' + str(
                                            resp['telefone'][0]['tipoDescricao']) + '</code>\n\n' +
                                       '<b>CODIGO OPERADORA: </b><code>' + str(
                                            resp['telefone'][1]['codigo']) + '</code>\n' +
                                       '<b>DDD: </b><code>' + str(resp['telefone'][1]['ddd']) + '</code>\n' +
                                       '<b>NUMERO: </b><code>' + str(resp['telefone'][1]['numero']) + '</code>\n' +
                                       '<b>TIPO: </b><code>' + str(resp['telefone'][1]['tipoDescricao']) + '</code>\n')
                            except:
                                try:
                                    tel = ('<b>CODIGO OPERADORA: </b><code>' + str(
                                        resp['telefone'][0]['codigo']) + '</code>\n' +
                                           '<b>DDD: </b><code>' + str(resp['telefone'][0]['ddd']) + '</code>\n' +
                                           '<b>NUMERO: </b><code>' + str(resp['telefone'][0]['numero']) + '</code>\n' +
                                           '<b>TIPO: </b><code>' + str(
                                                resp['telefone'][0]['tipoDescricao']) + '</code>\n\n')
                                except:
                                    tel = 'NULL'
                        try:
                            certidao = ('<b>CODIGO: </b><code>' + str(resp['certidao'][0]['codigo']) + '</code>\n' +
                                        '<b>TIPO: </b><code>' + str(resp['certidao'][0]['tipo']) + '</code>\n' +
                                        '<b>MODELO: </b><code>' + str(resp['certidao'][0]['modelo']) + '</code>\n' +
                                        '<b>CARTORIO: </b><code>' + str(resp['certidao'][0]['cartorio']) + '</code>\n' +
                                        '<b>LIVRO: </b><code>' + str(resp['certidao'][0]['livro']) + '</code>\n' +
                                        '<b>FOLHA: </b><code>' + str(resp['certidao'][0]['folha']) + '</code>\n' +
                                        '<b>TERMO: </b><code>' + str(resp['certidao'][0]['termo']) + '</code>\n' +
                                        '<b>EMISSÃO: </b><code>' + str(resp['certidao'][0]['dataEmissao']) + '</code>\n\n')
                        except:
                            certidao = 'NULL\n\n'
                        try:
                            cart = ('<b>CNS: </b><code>' + str(resp['cartoesAgregados'][0]['cns']) + '</code>\n' +
                                    '<b>DADOS: </b><code>' + str(resp['cartoesAgregados'][0]['data']) + '</code>\n' +
                                    '<b>MANUAL: </b><code>' + str(resp['cartoesAgregados'][0]['manual']) + '</code>\n' +
                                    '<b>TIPO: </b><code>' + str(resp['cartoesAgregados'][0]['tipo']) + '</code>\n\n' +
                                    '<b>CNS: </b><code>' + str(resp['cartoesAgregados'][1]['cns']) + '</code>\n' +
                                    '<b>DADOS: </b><code>' + str(resp['cartoesAgregados'][1]['data']) + '</code>\n' +
                                    '<b>MANUAL: </b><code>' + str(resp['cartoesAgregados'][1]['manual']) + '</code>\n' +
                                    '<b>TIPO: </b><code>' + str(resp['cartoesAgregados'][1]['tipo']) + '</code>\n\n' +
                                    '<b>CNS: </b><code>' + str(resp['cartoesAgregados'][2]['cns']) + '</code>\n' +
                                    '<b>DADOS: </b><code>' + str(resp['cartoesAgregados'][2]['data']) + '</code>\n' +
                                    '<b>MANUAL: </b><code>' + str(resp['cartoesAgregados'][2]['manual']) + '</code>\n' +
                                    '<b>TIPO: </b><code>' + str(resp['cartoesAgregados'][2]['tipo']) + '</code>\n\n')
                        except:
                            try:
                                cart = ('<b>CNS: </b><code>' + str(resp['cartoesAgregados'][0]['cns']) + '</code>\n' +
                                        '<b>DADOS: </b><code>' + str(
                                            resp['cartoesAgregados'][0]['data']) + '</code>\n' +
                                        '<b>MANUAL: </b><code>' + str(
                                            resp['cartoesAgregados'][0]['manual']) + '</code>\n' +
                                        '<b>TIPO: </b><code>' + str(
                                            resp['cartoesAgregados'][0]['tipo']) + '</code>\n\n' +
                                        '<b>CNS: </b><code>' + str(resp['cartoesAgregados'][1]['cns']) + '</code>\n' +
                                        '<b>DADOS: </b><code>' + str(
                                            resp['cartoesAgregados'][1]['data']) + '</code>\n' +
                                        '<b>MANUAL: </b><code>' + str(
                                            resp['cartoesAgregados'][1]['manual']) + '</code>\n' +
                                        '<b>TIPO: </b><code>' + str(
                                            resp['cartoesAgregados'][1]['tipo']) + '</code>\n\n')
                            except:
                                try:
                                    cart = ('<b>CNS: </b><code>' + str(
                                        resp['cartoesAgregados'][0]['cns']) + '</code>\n' +
                                            '<b>DADOS: </b><code>' + str(
                                                resp['cartoesAgregados'][0]['data']) + '</code>\n' +
                                            '<b>MANUAL: </b><code>' + str(
                                                resp['cartoesAgregados'][0]['manual']) + '</code>\n' +
                                            '<b>TIPO: </b><code>' + str(
                                                resp['cartoesAgregados'][0]['tipo']) + '</code>\n\n')
                                except:
                                    cart = 'NULL\n'
                        try:
                            rgg = ('<b>NUMERO: </b><code>' + str(resp['rgNumero']) + '</code>\n' +
                                   '<b>ORGAO EMISSOR: </b><code>' + str(resp['rgOrgaoEmissorDescricao']) + '</code>\n' +
                                   '<b>UF RG: </b><code>' + str(resp['rgUf']) + '</code>\n' +
                                   '<b>DATA EMISSÃO: </b><code>' + str(resp['rgDataEmissao']) + '</code>')
                        except:
                            rgg = 'NULL\n'
                        try:
                            cep = (str(resp['enderecoCep']))
                        except:
                            cep = 'X\n'

                        bot.reply_to(men, '<b>' 'â CONSULTA CONCLUIDA â' '</b>' + '\n\n<b>NOME: </b><code>' + str(
                            resp['nome']) + '</code>\n' + '<b>CPF: </b><code>' + str(resp['cpf']) + '</code>\n\n' +
                                     '<b>NOME MÃE: </b><code>' + str(
                            resp['nomeMae']) + '</code>\n' + '<b>NOME PAI: </b><code>' + str(
                            resp['nomePai']) + '</code>\n\n' +
                                     '<b>VIVO: </b><code>' + str(
                            resp['vivo']) + '</code>\n' + '<b>SEXO DESCRIÃÃO: </b><code>' + str(
                            resp['sexoDescricao']) + '</code>\n' +
                                     '<b>COR: </b><code>' + str(
                            resp['racaCorDescricao']) + '</code>\n' + '<b>DATA NASCIMENTO: </b><code>' + str(
                            resp['dataNascimento']) + '</code>\n' +
                                     '<b>NACIONALIDADE: </b><code>' + str(
                            resp['nacionalidade']) + '</code>\n' + '<b>PAIS NASCIMENTO: </b><code>' + str(
                            resp['paisNascimento']) + '</code>\n' +
                                     '<b>MUNICIPIO DE NASCIMENTO: </b><code>' + str(
                            resp['municipioNascimento']) + '</code>\n' + '<b>PAIS DE RESIDENCIA: </b><code>' + str(
                            resp['paisResidenciaDescricao']) + '</code>\n\n<b>ENDEREÃO: </b>\n' +
                                     '<b>MUNICIPIO: </b><code>' + str(
                            resp['enderecoMunicipio']) + '</code>\n' + '<b>TIPO LOGRADOURO: </b><code>' + str(
                            resp['enderecoTipoLogradouro']) + '</code>\n' +
                                     '<b>LOGRADOURO: </b><code>' + str(
                            resp['enderecoLogradouro']) + '</code>\n' + '<b>NUMERO: </b><code>' + str(
                            resp['enderecoNumero']) + '</code>\n' +
                                     '<b>COMPLEMENTO: </b><code>' + str(
                            resp['enderecoComplemento']) + '</code>\n' + '<b>BAIRRO: </b><code>' + resp[
                                         "enderecoBairro"] + '</code>\n' +
                                     '<b>CEP: </b><code>' + cep + '</code>\n\n' + '<b>TELEFONES: </b>\n' + tel + '<b>RG: </b> \n\n' + rgg + '\n<b>CERTIDÃO: </b>\n\n' + certidao + '<b>CARTOES AGREGADOS: </b>\n\n' + cart
                                     + '\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>', parse_mode='HTML')
                    except:
                        A = bot.reply_to(men, '<b>' 'OPS, NÃO ENCONTRADO!' '</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>' 'â Compre acesso com meu Dono @Iara_limazâ' '</b>',
                             parse_mode='HTML')

##

@bot.message_handler(commands=['nome'] + ['NOME'])
def sjjsn(nome):
            id1 = nome.chat.id
            men = nome.text
            oi = str(men[6:])
            ltnome = EXCEPT + PRIVADO + ANONY + [-1001481944556]
            if id1 in ltnome:

                session = requests_html.HTMLSession()
                if men == '/nome':
                    bot.reply_to(nome, '<b>DIGITE UM NOME, ANIMAL!</b>',
                                 parse_mode='HTML')
                elif men == '/NOME':
                    bot.reply_to(nome, '<b>DIGITE UM NOME, ANIMAL!</b>',
                                 parse_mode='HTML')
                else:
                    try:
                        bot.reply_to(nome, '<code>ESTOU BUSCANDO NO BANCO DE DADOS...</code>', parse_mode='HTML')

                        r = session.get(
                            'http://191.252.153.147/buscasjl.php?token=Pg6ZKyXcrYfzSG2TKqc1&nome={}'.format(oi))
                        ar = r.html.find("td")
                        ar1 = r.html.find('tr')
                        try:
                            bot.reply_to(nome,
                                         str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[0].html) + '\n\n' +
                                         str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[5].html) + '\n\n' +
                                         str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[10].html) + '\n\n' +
                                         str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[15].html) + '\n\n' +
                                         str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[20].html) + '\n\n' +
                                         str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[25].html) + '\n\n' +
                                         str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[30].html) + '\n\n' +
                                         str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[35].html) + '\n\n' +
                                         str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[40].html) + '\n\n' +
                                         str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[45].html) + '\n\n' +
                                         str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[50].html) + '\n\n' +
                                         str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[55].html) + '\n\n' +
                                         str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[60].html) + '\n\n' +
                                         str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[65].html) + '\n\n' +
                                         str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[70].html) + '\n\n' +
                                         str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[75].html) + '\n\n' +
                                         str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[80].html) + '\n\n' +
                                         str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[85].html) + '\n\n' +
                                         str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[90].html) + '\n\n' +
                                         str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[95].html) + '\n\n' +
                                         str(ar1[21].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[100].html) + '\n\n' +
                                         str(ar1[22].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[105].html) + '\n\n' +
                                         str(ar1[23].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[110].html) + '\n\n' +
                                         str(ar1[24].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[115].html) + '\n\n' +
                                         str(ar1[25].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[120].html) + '\n\n' +
                                         str(ar1[26].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[125].html) + '\n\n' +
                                         str(ar1[27].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[130].html) + '\n\n' +
                                         str(ar1[28].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[135].html) + '\n\n' +
                                         str(ar1[29].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[140].html) + '\n\n' +
                                         str(ar1[30].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[145].html) + '\n\n' +
                                         str(ar1[31].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[150].html) + '\n\n' +
                                         str(ar1[32].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[155].html) + '\n\n' +
                                         str(ar1[33].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[160].html) + '\n\n' +
                                         str(ar1[34].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[165].html) + '\n\n' +
                                         str(ar1[35].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[170].html) + '\n\n' +
                                         str(ar1[36].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[175].html) + '\n\n' +
                                         str(ar1[37].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[180].html) + '\n\n' +
                                         str(ar1[38].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[185].html) + '\n\n' +
                                         str(ar1[39].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[190].html) + '\n\n' +
                                         str(ar1[40].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[195].html) + '\n\n' +
                                         str(ar1[41].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[200].html) + '\n\n' +
                                         str(ar1[42].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[205].html) + '\n\n' +
                                         str(ar1[43].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[210].html) + '\n\n' +
                                         str(ar1[44].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[215].html) + '\n\n' +
                                         str(ar1[45].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[220].html) + '\n\n' +
                                         str(ar1[46].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[225].html) + '\n\n' +
                                         str(ar1[47].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[230].html) + '\n\n' +
                                         str(ar1[48].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[235].html) + '\n\n' +
                                         str(ar1[49].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[240].html) + '\n\n' +
                                         str(ar1[50].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                             245].html) + '\n\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>', parse_mode='HTML')
                        except:
                            try:
                                bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                              ar[0].html) + '\n\n' +
                                             str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[5].html) + '\n\n' +
                                             str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[10].html) + '\n\n' +
                                             str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[15].html) + '\n\n' +
                                             str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[20].html) + '\n\n' +
                                             str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[25].html) + '\n\n' +
                                             str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[30].html) + '\n\n' +
                                             str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[35].html) + '\n\n' +
                                             str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[40].html) + '\n\n' +
                                             str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[45].html) + '\n\n' +
                                             str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[50].html) + '\n\n' +
                                             str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[55].html) + '\n\n' +
                                             str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[60].html) + '\n\n' +
                                             str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[65].html) + '\n\n' +
                                             str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[70].html) + '\n\n' +
                                             str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[75].html) + '\n\n' +
                                             str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[80].html) + '\n\n' +
                                             str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[85].html) + '\n\n' +
                                             str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[90].html) + '\n\n' +
                                             str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[95].html) + '\n\n' +
                                             str(ar1[21].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[100].html) + '\n\n' +
                                             str(ar1[22].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[105].html) + '\n\n' +
                                             str(ar1[23].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[110].html) + '\n\n' +
                                             str(ar1[24].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[115].html) + '\n\n' +
                                             str(ar1[25].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[120].html) + '\n\n' +
                                             str(ar1[26].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[125].html) + '\n\n' +
                                             str(ar1[27].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[130].html) + '\n\n' +
                                             str(ar1[28].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[135].html) + '\n\n' +
                                             str(ar1[29].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[140].html) + '\n\n' +
                                             str(ar1[30].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[145].html) + '\n\n' +
                                             str(ar1[31].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[150].html) + '\n\n' +
                                             str(ar1[32].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[155].html) + '\n\n' +
                                             str(ar1[33].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[160].html) + '\n\n' +
                                             str(ar1[34].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[165].html) + '\n\n' +
                                             str(ar1[35].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[170].html) + '\n\n' +
                                             str(ar1[36].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[175].html) + '\n\n' +
                                             str(ar1[37].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[180].html) + '\n\n' +
                                             str(ar1[38].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[185].html) + '\n\n' +
                                             str(ar1[39].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[190].html) + '\n\n' +
                                             str(ar1[40].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                    195].html) + '\n\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas	\nCANAL: @iara_referencias</b>', parse_mode='HTML')
                            except:
                                try:
                                    bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                  ar[0].html) + '\n\n' +
                                                 str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[5].html) + '\n\n' +
                                                 str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[10].html) + '\n\n' +
                                                 str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[15].html) + '\n\n' +
                                                 str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[20].html) + '\n\n' +
                                                 str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[25].html) + '\n\n' +
                                                 str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[30].html) + '\n\n' +
                                                 str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[35].html) + '\n\n' +
                                                 str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[40].html) + '\n\n' +
                                                 str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[45].html) + '\n\n' +
                                                 str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[50].html) + '\n\n' +
                                                 str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[55].html) + '\n\n' +
                                                 str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[60].html) + '\n\n' +
                                                 str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[65].html) + '\n\n' +
                                                 str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[70].html) + '\n\n' +
                                                 str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[75].html) + '\n\n' +
                                                 str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[80].html) + '\n\n' +
                                                 str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[85].html) + '\n\n' +
                                                 str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[90].html) + '\n\n' +
                                                 str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[95].html) + '\n\n' +
                                                 str(ar1[21].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[100].html) + '\n\n' +
                                                 str(ar1[22].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[105].html) + '\n\n' +
                                                 str(ar1[23].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[110].html) + '\n\n' +
                                                 str(ar1[24].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[115].html) + '\n\n' +
                                                 str(ar1[25].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[120].html) + '\n\n' +
                                                 str(ar1[26].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[125].html) + '\n\n' +
                                                 str(ar1[27].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[130].html) + '\n\n' +
                                                 str(ar1[28].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[135].html) + '\n\n' +
                                                 str(ar1[29].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[140].html) + '\n\n' +
                                                 str(ar1[30].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[145].html) + '\n\n')
                                except:
                                    try:
                                        bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                            0].html) + '\n\n' +
                                                     str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[5].html) + '\n\n' +
                                                     str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[10].html) + '\n\n' +
                                                     str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[15].html) + '\n\n' +
                                                     str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[20].html) + '\n\n' +
                                                     str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[25].html) + '\n\n' +
                                                     str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[30].html) + '\n\n' +
                                                     str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[35].html) + '\n\n' +
                                                     str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[40].html) + '\n\n' +
                                                     str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[45].html) + '\n\n' +
                                                     str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[50].html) + '\n\n' +
                                                     str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[55].html) + '\n\n' +
                                                     str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[60].html) + '\n\n' +
                                                     str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[65].html) + '\n\n' +
                                                     str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[70].html) + '\n\n' +
                                                     str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[75].html) + '\n\n' +
                                                     str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[80].html) + '\n\n' +
                                                     str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[85].html) + '\n\n' +
                                                     str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[90].html) + '\n\n' +
                                                     str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                            95].html) + '\n\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>', parse_mode='HTML')
                                    except:
                                        try:
                                            bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                          ar[
                                                                                                              0].html) + '\n\n' +
                                                         str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                5].html) + '\n\n' +
                                                         str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                10].html) + '\n\n' +
                                                         str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                15].html) + '\n\n' +
                                                         str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                20].html) + '\n\n' +
                                                         str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                25].html) + '\n\n' +
                                                         str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                30].html) + '\n\n' +
                                                         str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                35].html) + '\n\n' +
                                                         str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                40].html) + '\n\n' +
                                                         str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                45].html) + '\n\n' +
                                                         str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                50].html) + '\n\n' +
                                                         str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                55].html) + '\n\n' +
                                                         str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                60].html) + '\n\n' +
                                                         str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                65].html) + '\n\n' +
                                                         str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                70].html) + '\n\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>', parse_mode='HTML')
                                        except:
                                            try:
                                                bot.reply_to(nome,
                                                             str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            0].html) + '\n\n' +
                                                             str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            5].html) + '\n\n' +
                                                             str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            10].html) + '\n\n' +
                                                             str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            15].html) + '\n\n' +
                                                             str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            20].html) + '\n\n' +
                                                             str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            25].html) + '\n\n' +
                                                             str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            30].html) + '\n\n' +
                                                             str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            35].html) + '\n\n' +
                                                             str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            40].html) + '\n\n' +
                                                             str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                         ar[
                                                                                                             45].html) + '\n\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>',
                                                             parse_mode='HTML')
                                            except:
                                                try:
                                                    bot.reply_to(nome,
                                                                 str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                0].html) + '\n\n' +
                                                                 str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                5].html) + '\n\n' +
                                                                 str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                10].html) + '\n\n' +
                                                                 str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                15].html) + '\n\n' +
                                                                 str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                20].html) + '\n\n<b>DONO: @Iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>',
                                                                 parse_mode='HTML')
                                                except:
                                                    try:
                                                        bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '', ar[0].html) + '\n\n' +
                                                                     str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '', ar[5].html) + '\n\n' +
                                                                     str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '', ar[10].html) + '\n\n' +
                                                                     str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '',
                                                            ar[15].html) + '\n\n<b>DONO: @iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>',
                                                                     parse_mode='HTML')
                                                    except:
                                                        try:
                                                            bot.reply_to(nome,
                                                                         str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                             '[^0-9]', '', ar[0].html) + '\n\n' +
                                                                         str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                             '[^0-9]', '', ar[5].html) + '\n\n' +
                                                                         str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                             '[^0-9]', '', ar[
                                                                                 10].html) + '\n\n<b>DONO: @iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>',
                                                                         parse_mode='HTML')
                                                        except:
                                                            try:
                                                                bot.reply_to(nome,
                                                                             str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                                 '[^0-9]', '',
                                                                                 ar[0].html) + '\n\n' +
                                                                             str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                                 '[^0-9]', '',
                                                                                 ar[
                                                                                     5].html) + '\n\n<b>DONO: @iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_refetencias</b>',
                                                                             parse_mode='HTML')
                                                            except:
                                                                try:
                                                                    bot.reply_to(nome, str(
                                                                        ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                               '',
                                                                                                               ar[
                                                                                                                   0].html) + '\n\n<b>DONO: @iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias</b>',
                                                                                 parse_mode='HTML')
                                                                except:
                                                                    bot.reply_to(nome, '<b>SEM RESULTADOS!</b>',
                                                                                 parse_mode='HTML')
                    except:
                        bot.reply_to(nome, '<b>ALGO DEU ERRADO :(</b>', parse_mode='HTML')
            else:
                bot.reply_to(nome, '<b>â Compre acesso com meu Dono @iara_limaz/b>',
                             parse_mode='HTML')

##

@bot.message_handler(commands=['cpf'] + ['CPF'])
def bunda(message1):
            ideee = message1.chat.id
            text = message1.text
            lib = PRIVADO + EXCEPT + ANONY
            if ideee in lib:
                if message1.text == '/trabalhos':
                    help1 = bot.reply_to(message1,
                                         '<b>DIGITE UM CPF, ANIMAL!</b>', parse_mode='HTML' )
                    sleep(10)
                    bot.delete_message(ideee, help1.message_id)
                    bot.delete_message(ideee, message1.message_id)
                elif message1.text == '/CPF':
                    help2 = bot.reply_to(message1,
                                         '<b>DIGITE UM CPF, ANIMAL!</b>', parse_mode='HTML')
                    sleep(10)
                    bot.delete_message(ideee, help2.message_id)
                    bot.delete_message(ideee, message1.message_id)
                else:
                    try:

                        filtr = re.sub('[^0-9]', '', text)
                        url = requests.get(
                            'http://191.252.153.147/MasterTarget/teste.php?token=HhH2BXDKTSyNwhaZzyCh&cpf={}'.format(
                                filtr)).content
                        resp = json.loads(url)

                        ##########################################
                        try:
                            ende = ('<b>TIPO LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['tipoLogradouro']) + '</code>\n'
                                                                                                           '<b>LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['logradouro']) + '</code>\n'
                                                                                                       '<b>NUMERO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['numero']) + '</code>\n'
                                                                                                   '<b>COMPLEMENTO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['complemento']) + '</code>\n'
                                                                                                        '<b>BAIRRO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['bairro']) + '</code>\n'

                                                                                                   '<b>CIDADE: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['cidade']) + '</code>\n'
                                                                                                   '<b>UF: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['uf']) + '</code>\n'
                                                                                               '<b>CEP: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0][
                                    'cep']) + '</code>\n\n' + '<b>TIPO LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['tipoLogradouro']) + '</code>\n'
                                                                                                           '<b>LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['logradouro']) + '</code>\n'
                                                                                                       '<b>NUMERO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['numero']) + '</code>\n'
                                                                                                   '<b>COMPLEMENTO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['complemento']) + '</code>\n'
                                                                                                        '<b>BAIRRO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['bairro']) + '</code>\n'
                                                                                                   '<b>CIDADE: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['cidade']) + '</code>\n'
                                                                                                   '<b>UF: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1][
                                    'uf']) + '</code>\n\n' + '<b>TIPO LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'tipoLogradouro']) + '</code>\n' + '<b>LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'logradouro']) + '</code>\n' + '<b>NUMERO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'numero']) + '</code>\n' + '<b>COMPLEMENTO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'complemento']) + '</code>\n' + '<b>BAIRRO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'bairro']) + '</code>\n' + '<b>CIDADE: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'cidade']) + '</code>\n' + '<b>UF: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'uf']) + '</code>\n' + '<b>CEP: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2]['cep']) + '</code>\n\n')
                            # TRATAMENTO ENDEREÃO
                        except:
                            try:
                                ende = ('<b>TIPO LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0][
                                        'tipoLogradouro']) + '</code>\n'
                                                             '<b>LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['logradouro']) + '</code>\n'
                                                                                                           '<b>NUMERO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['numero']) + '</code>\n'
                                                                                                       '<b>COMPLEMENTO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['complemento']) + '</code>\n'
                                                                                                            '<b>BAIRRO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['bairro']) + '</code>\n'

                                                                                                       '<b>CIDADE: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['cidade']) + '</code>\n'
                                                                                                       '<b>UF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['uf']) + '</code>\n'
                                                                                                   '<b>CEP: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0][
                                        'cep']) + '</code>\n\n' + '<b>TIPO LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1][
                                        'tipoLogradouro']) + '</code>\n'
                                                             '<b>LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['logradouro']) + '</code>\n'
                                                                                                           '<b>NUMERO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['numero']) + '</code>\n'
                                                                                                       '<b>COMPLEMENTO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['complemento']) + '</code>\n'
                                                                                                            '<b>BAIRRO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['bairro']) + '</code>\n'
                                                                                                       '<b>CIDADE: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['cidade']) + '</code>\n'
                                                                                                       '<b>UF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['uf']) + '</code>\n\n')
                            except:
                                try:
                                    ende = ('<b>TIPO LOGRADOURO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0][
                                            'tipoLogradouro']) + '</code>\n'
                                                                 '<b>LOGRADOURO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0][
                                            'logradouro']) + '</code>\n'
                                                             '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['numero']) + '</code>\n'
                                                                                                           '<b>COMPLEMENTO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0][
                                            'complemento']) + '</code>\n'
                                                              '<b>BAIRRO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['bairro']) + '</code>\n'

                                                                                                           '<b>CIDADE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['cidade']) + '</code>\n'
                                                                                                           '<b>UF: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['uf']) + '</code>\n'
                                                                                                       '<b>CEP: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['cep']) + '</code>\n\n')
                                except:
                                    ende = 'ENDEREÃO NÃO ENCONTRADO'
                        ##############################
                        try:
                            parent = ('<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][0]['nomeCompleto']) + '</code>\n'
                                                                                                           '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                    'cpf']) + '</code>\n' + '<b>GRAU DE PARENTESCO: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                    'grauDeParentesco']) + '</code>\n\n' + '<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][1]['nomeCompleto']) + '</code>\n'
                                                                                                           '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][1][
                                    'cpf']) + '</code>\n' + '<b>GRAU DE PARENTESCO: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][1][
                                    'grauDeParentesco']) + '</code>\n\n')
                            # TRATAMENTO PARENTESCO
                        except:
                            try:
                                parent = ('<b>NOME: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                        'nomeCompleto']) + '</code>\n'
                                                           '<b>CPF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                        'cpf']) + '</code>\n' + '<b>GRAU DE PARENTESCO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                        'grauDeParentesco']) + '</code>\n\n')
                            except:
                                parent = 'PARENTES NÃO ENCONTRADOS'
                        #################################
                        try:
                            viz = ('<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'nomePrimeiro']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'nomeMeio']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'cpf']) + ' </code>\n\n' + '<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomePrimeiro']) + ' ' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomeMeio']) + ' ' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                    'nomeUltimo']) + '</code>\n<b>CPF: </b>' + '<code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                    'cpf']) + '</code>\n\n' + '<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'nomePrimeiro']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'nomeMeio']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'cpf']) + ' </code>\n\n')
                            # TRATAMENTO VIZINHOS
                        except:
                            try:
                                viz = ('<b>NOME: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'nomePrimeiro']) + ' </code><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'nomeMeio']) + ' </code><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'cpf']) + ' </code>\n\n' + '<b>NOME: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomePrimeiro']) + ' ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomeMeio']) + ' ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                        'nomeUltimo']) + '</code>\n<b>CPF: </b>' + '<code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                        'cpf']) + '</code>\n\n')
                            except:
                                try:
                                    viz = ('<b>NOME: </b><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'nomePrimeiro']) + ' </code><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'nomeMeio']) + ' </code><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'cpf']) + ' </code>\n\n')
                                except:
                                    viz = 'SEM VIZINHOS'
                        ################################
                        try:
                            emai = (str(resp['result'][0]['pessoa']['contato']['email'][0]['email']) + '\n' + str(
                                resp['result'][0]['pessoa']['contato']['email'][1]['email']) + '\n' + str(
                                resp['result'][0]['pessoa']['contato']['email'][2]['email']) + '\n')
                            # TRATAMENTO EMAILS
                        except:
                            try:
                                emai = (str(resp['result'][0]['pessoa']['contato']['email'][0]['email']) + '\n' + str(
                                    resp['result'][0]['pessoa']['contato']['email'][1]['email']) + '\n')
                            except:
                                try:
                                    emai = (str(resp['result'][0]['pessoa']['contato']['email'][0]['email']) + '\n')
                                except:
                                    emai = 'SEM EMAIL'
                        ##############################
                        try:
                            tel = ('<b>DDD: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['telefone'][0]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0]['numero']) + '</code>\n' +
                                   '<b>OPERADORA: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0][
                                            'operadora']) + '</code>\n' +
                                   '<b>TIPO TELEFONE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0][
                                            'tipoTelefone']) + '</code>\n\n' +
                                   '<b>DDD:</b><code> ' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1]['numero']) + '</code>\n' +
                                   '<b>OPERADORA: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1][
                                            'operadora']) + '</code>\n' +
                                   '<b>TIPO TELEFONE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1][
                                            'tipoTelefone']) + '</code>\n\n' +
                                   '<b>DDD:</b><code> ' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2]['numero']) + '</code>\n' +
                                   '<b>OPERADORA: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2][
                                            'operadora']) + '</code>\n' +
                                   '<b>TIPO TELEFONE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2][
                                            'tipoTelefone']) + '</code>\n\n')
                            # TRATAMENTO TELEFONES
                            # TELEFONES
                        except:
                            try:
                                tel = ('<b>DDD: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['telefone'][0]['ddd']) + '</code>\n' +
                                       '<b>NUMERO: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                'numero']) + '</code>\n' +
                                       '<b>OPERADORA: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                'operadora']) + '</code>\n' +
                                       '<b>TIPO TELEFONE: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                'tipoTelefone']) + '</code>\n\n' +
                                       '<b>DDD: </b><code>' + str(resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                                      'ddd']) + '</code>\n' +
                                       '<b>NUMERO: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                'numero']) + '</code>\n' +
                                       '<b>OPERADORA: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                'operadora']) + '</code>\n' +
                                       '<b>TIPO TELEFONE: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                'tipoTelefone']) + '</code>\n\n')
                            except:
                                try:
                                    tel = ('<b>DDD: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0]['ddd']) + '</code>\n' +
                                           '<b>NUMERO: </b><code>' + str(
                                                resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                    'numero']) + '</code>\n' +
                                           '<b>OPERADORA: </b><code>' + str(
                                                resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                    'operadora']) + '</code>\n' +
                                           '<b>TIPO TELEFONE: </b><code>' + str(
                                                resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                    'tipoTelefone']) + '</code>\n\n')
                                except:
                                    tel = 'TELEFONE NÃO ENCONTRADO'
                        ###################################
                        try:
                            psocietaria = ('<b>CNPJ: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0]['nr_cnpj']) + '\n'
                                                                                                                  '<b>RAZÃO SOCIAL: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                    'razaoSocial']) + '\n'
                                                      '<b>PARTICIPAÃÃO: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                    'participacao']) + '\n'
                                                       '<b>QUALIFICAÃÃO: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                    'qualificacao']) + '\n\n' +
                                           '<b>CNPJ: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'nr_cnpj']) + '\n'
                                                          '<b>RAZÃO SOCIAL: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'razaoSocial']) + '\n'
                                                              '<b>PARTICIPAÃÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'participacao']) + '\n'
                                                               '<b>QUALIFICAÃÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'qualificacao']) + '\n\n' +
                                           '<b>CNPJ: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'nr_cnpj']) + '\n'
                                                          '<b>RAZÃO SOCIAL: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'razaoSocial']) + '\n'
                                                              '<b>PARTICIPAÃÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'participacao']) + '\n'
                                                               '<b>QUALIFICAÃÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'qualificacao']) + '\n\n')
                            # TRATAMENTO PARTICIPAÃÃES SOCIETARIAS
                        except:
                            try:
                                psocietaria = ('<b>CNPJ: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'nr_cnpj']) + '\n'
                                                      '<b>RAZÃO SOCIAL: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'razaoSocial']) + '\n'
                                                          '<b>PARTICIPAÃÃO: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'participacao']) + '\n'
                                                           '<b>QUALIFICAÃÃO: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'qualificacao']) + '\n\n' +
                                               '<b>CNPJ: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'nr_cnpj']) + '\n'
                                                              '<b>RAZÃO SOCIAL: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'razaoSocial']) + '\n'
                                                                  '<b>PARTICIPAÃÃO: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'participacao']) + '\n'
                                                                   '<b>QUALIFICAÃÃO: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'qualificacao']) + '\n\n')
                            except:
                                try:
                                    psocietaria = ('<b>CNPJ: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'nr_cnpj']) + '\n'
                                                          '<b>RAZÃO SOCIAL: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'razaoSocial']) + '\n'
                                                              '<b>PARTICIPAÃÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'participacao']) + '\n'
                                                               '<b>QUALIFICAÃÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'qualificacao']) + '\n\n')
                                except:
                                    psocietaria = 'SEM PARTICIPAÃÃES SOCIETARIAS'
                        ####################################
                        try:
                            empregador = ('CNPJ: ' + str(
                                resp['result'][0]['pessoa']['vinculo']['empregador'][0]['cnpj']) + '\n'
                                                                                                   'RAZAO SOCIAL: ' + str(
                                resp['result'][0]['pessoa']['vinculo']['empregador'][0]['razaoSocial']) + '\n'
                                                                                                          'ADMISSÃO: ' + str(
                                resp['result'][0]['pessoa']['vinculo']['empregador'][0]['dataAdmissao']) + '\n\n' +
                                          'CNPJ: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][1]['cnpj']) + '\n'
                                                                                                           'RAZAO SOCIAL: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][1]['razaoSocial']) + '\n'
                                                                                                                  'ADMISSÃO: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][1][
                                            'dataAdmissao']) + '\n\n' +
                                          'CNPJ: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][2]['cnpj']) + '\n'
                                                                                                           'RAZAO SOCIAL: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][2]['razaoSocial']) + '\n'
                                                                                                                  'ADMISSÃO: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][2]['dataAdmissao']) + '\n')
                            # TRATAMENTO EMPREGADOR
                        except:
                            try:
                                empregador = ('CNPJ: ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['empregador'][0]['cnpj']) + '\n'
                                                                                                       'RAZAO SOCIAL: ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['empregador'][0]['razaoSocial']) + '\n'
                                                                                                              'ADMISSÃO: ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['empregador'][0]['dataAdmissao']) + '\n\n' +
                                              'CNPJ: ' + str(
                                            resp['result'][0]['pessoa']['vinculo']['empregador'][1]['cnpj']) + '\n'
                                                                                                               'RAZAO SOCIAL: ' + str(
                                            resp['result'][0]['pessoa']['vinculo']['empregador'][1][
                                                'razaoSocial']) + '\n'
                                                                  'ADMISSÃO: ' + str(
                                            resp['result'][0]['pessoa']['vinculo']['empregador'][1][
                                                'dataAdmissao']) + '\n')
                            except:
                                try:
                                    empregador = ('CNPJ: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][0]['cnpj']) + '\n'
                                                                                                           'RAZAO SOCIAL: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][0]['razaoSocial']) + '\n'
                                                                                                                  'ADMISSÃO: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][0]['dataAdmissao']) + '\n')
                                except:
                                    empregador = 'NULL'
                        #####################################
                        try:
                            veiculo = ('MARCA: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                    'MODELO: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['modelo']) + '\n'
                                                                                                     'ANO: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['ano']) + '\n'
                                                                                                  'CATEGORIA: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                    'CLASSIFICAÃÃO: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['classificacao']) + '\n\n' +
                                       'MARCA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                            'MODELO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['modelo']) + '\n'
                                                                                                             'ANO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['ano']) + '\n'
                                                                                                          'CATEGORIA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                            'CLASSIFICAÃÃO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1][
                                            'classificacao']) + '\n\n' +
                                       'MARCA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['marca']) + '\n'
                                                                                                            'MODELO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['modelo']) + '\n'
                                                                                                             'ANO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['ano']) + '\n'
                                                                                                          'CATEGORIA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['marca']) + '\n'
                                                                                                            'CLASSIFICAÃÃO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2][
                                            'classificacao']) + '\n\n')
                            # TRATAMENTO VEICULO
                        except:
                            try:
                                veiculo = ('MARCA: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                        'MODELO: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['modelo']) + '\n'
                                                                                                         'ANO: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['ano']) + '\n'
                                                                                                      'CATEGORIA: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                        'CLASSIFICAÃÃO: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['classificacao']) + '\n\n' +
                                           'MARCA: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                                'MODELO: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['modelo']) + '\n'
                                                                                                                 'ANO: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['ano']) + '\n'
                                                                                                              'CATEGORIA: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                                'CLASSIFICAÃÃO: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1][
                                                'classificacao']) + '\n\n')
                            except:
                                try:
                                    veiculo = ('MARCA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                            'MODELO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['modelo']) + '\n'
                                                                                                             'ANO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['ano']) + '\n'
                                                                                                          'CATEGORIA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                            'CLASSIFICAÃÃO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0][
                                            'classificacao']) + '\n\n')
                                except:
                                    veiculo = 'NULL'
                        ################################
                        bot.reply_to(message1,
                                     '<b>CPF: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['CPF']) + '</code>\n' +

                                     '<b>NOME: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['nomePrimeiro']) + ' ' +
                                     str(resp['result'][0]['pessoa']['cadastral']['nomeMeio']) + ' ' + str(
                                         resp['result'][0]['pessoa']['cadastral']['nomeUltimo']) + '</code>\n' +

                                     '<b>SEXO: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['sexo']) + '</code>\n' +
                                     '<b>DATA NASC: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['dataNascimento']) + '</code>\n' +
                                     '<b>STATUS RECEITA FEDERAL: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral'][
                                             'statusReceitaFederal']) + '</code>\n\n' +
                                     '<b>RG: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['rgNumero']) + '</code>\n' +
                                     '<b>ORGÃO EMISSOR: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['rgOrgaoEmissor']) + '</code>\n' +
                                     '<b>UF RG: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['rgUf']) + '</code>\n\n' +
                                     '<b>TITULO ELEITORAL: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['tituloEleitoral']) + '</code>\n' +
                                     '<b>NACIONALIDADE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['nacionalidade']) + '</code>\n' +
                                     '<b>ESTADO CIVIL: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['estadoCivil']) + '</code>\n\n' +

                                     '<b>NOME MÃE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral'][
                                             'maeNomePrimeiro']) + ' </code><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral'][
                                             'maeNomeMeio']) + ' </code><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['maeNomeUltimo']) + '</code>\n' +
                                     '<b>CPF MÃE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['maeCPF']) + '</code>\n' +
                                     '<b>ESCOLARIDADE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['escolaridade']) + '</code>\n' +
                                     '<b>CNS: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['cns']) + '</code>\n\n' +
                                     '<b>BOLSA FAMILIA: </b><code>' + str(
                                         resp['result'][0]['pessoa']['beneficiarioProgramaSocial'][
                                             'bolsaFamilia']) + '</code>\n\n' +
                                     '<b>ENDEREÃO: </b>\n' + ende +
                                     '\n\n<b>PARENTESCO: </b>\n\n' + parent +
                                     '\n\n<b>VIZINHOS: </b>\n\n' + viz + '<b>' + '\n\nEMAIL:\n' + '</b>' + str(emai) +
                                     '<b>' + '\nTELEFONES:\n\n' + '</b>' + str(tel) + '<b>' +
                                     'CONJUGE:\n'
                                     'NOME: ' + '</b>' + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['nomePrimeiro']) + ' ' + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['nomeMeio']) + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['nomeUltimo']) + '\n' + '<b>' +
                                                                                                            'PARENTESCO: ' + '</b>' + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['parentesco']) + '\n\n'
                                                                                                            'ðð¼ðððð¾ððð¼ð¾Ì§ð¼Ìð ððð¾ðððð¼ððð¼:\n\n' + psocietaria +
                                     '\n\nððððððð¼ð¿ðð:\n' + empregador +
                                     '\n\nðððð¾ðððð: \n' + veiculo +
                                     '\n\nðððððððð¼Ìð: ' + str(
                                         resp['result'][0]['pessoa']['socioDemografico']['profissao']) +
                                     '\nðððð¿ð¼ ðððððððð¿ð¼:: ' + str(
                                         resp['result'][0]['pessoa']['socioDemografico'][
                                             'rendaPresumida']) + '<b>' + '\n\nDONO: @iara_limaz\nGRUPO: @iara_consultas\nCANAL: @iara_referencias' + '</b>',
                                     parse_mode='HTML')
                    except:
                        bot.reply_to(message1, '<b>' + 'ERRO, VERIFIQUE O CPF' + '</b>', parse_mode='HTML')

            else:
                bot.reply_to(message1,
                             '<b>' + 'â Compre acesso com meu dono @iara_limazâ' + '</b>',
                             parse_mode='HTML')

bot.polling()