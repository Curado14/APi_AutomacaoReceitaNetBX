import os
import subprocess
import traceback
from urllib import urlencode
import urllib2
import json
import time
import calendar
import logging
from java.net import URL
from java.io import BufferedReader, InputStreamReader
import unicodedata
from urllib import urlencode
import re
#
#FINALIDADE DA FUNÇÃO: retirar caracteres especiais para facilitar a leitrua OCR
def normalizar_texto(s):    
    if not s:
        return u""
    return u"".join(
        c for c in unicodedata.normalize("NFD", unicode(s)) #NFD (normalization form decompesed) responsável por retirar o "ç" e acentos crases (`)
        if unicodedata.category(c) != "Mn" #Mn (Mark, Nonspacing) retira os acentos 
    ).upper().strip()


Debug.setDebugLevel(3)

indice_comeco = 0 #variável global para faciliar o scroll (De certa forma não é útil)
Region(674,458,559,161)

#FINALIDADE DA FUNÇÃO: conexão com a API
def http_get(url):
    connection = URL(url).openConnection()

    Debug.log(3, "0")
    reader = BufferedReader(InputStreamReader(connection.getInputStream(), "UTF-8"))
    lines = []
    line = reader.readLine()
    Debug.log(3, "1") 
    j = 0 
    while line is not None:
        lines.append(line)
        line = reader.readLine()
        j = j + 1
        if j > 20000:
            break
    reader.close()
    Debug.log("\n".join(lines))
    return "\n".join(lines)





imgVerPedidos = Pattern("imgVerPedidos.png").targetOffset(-1,2)
imgTrocarPerfil = "imgTrocarPerfil.png"
imgBotaoTrocarPefil = "imgBotaoTrocarPefil.png"
imgCertF2Selecionado = "1748365816277.png"
imgCertF2NaoSelecionado = "1748365880661.png"
imgSelecionarPerfil = Pattern("1748366657632.png").similar(0.59).targetOffset(227,-1)
imgRodape = Pattern("imgRodape.png").targetOffset(203,-1)
imgPesquisaArquivos = "1748368733762.png"
imgLabelSelecioneUmSistema = Pattern("imgLabelSelecioneUmSistema.png").targetOffset(433,1)
imgLabelSelecioneTipoArquivo = Pattern("imgLabelSelecioneTipoArquivo.png").targetOffset(451,-4)
imgLabelSelecioneTipoPesquisa = Pattern("imgLabelSelecioneTipoPesquisa.png").targetOffset(454,-1)
imgOpcoesTipoPesquisaEFDContribuicoes = Pattern("1748371532516.png").targetOffset(-143,7)
imgBotaoPesquisaAcompanhamento = Pattern("imgBotaoPesquisaAcompanhamento.png").targetOffset(-21,27)
imgBotaoPesquisaAcompanhamentoPesquisar = Pattern("imgBotaoPesquisaAcompanhamento.png").targetOffset(-22,-5)
imgQuemRepresenta = Pattern("imgQuemRepresenta.png").targetOffset(-134,0)
imgLabelDataInicio = Pattern("1748373196671.png").targetOffset(57,0)
imgLabelDataFim = Pattern("imgLabelDataFim.png").targetOffset(56,1)


imgCamposEFDICMS = "imgCamposEFDICMS.png"
imgCamposEFDICMSBotaoSelecionarTodos = Pattern("imgCamposEFDICMSBotaoSelecionarTodos.png").targetOffset(131,2)
imgCamposEFDICMSBotaoUltimosArquivos = Pattern("imgCamposEFDICMSBotaoUltimosArquivos.png").targetOffset(131,-1)

imgCamposEFDICMSBotaoDataInicio = Pattern("imgCamposEFDICMSBotaoDataInicio.png").targetOffset(138,-1)

imgLabelDataInicioEFDICMS = Pattern("imgLabelDataInicioEFDICMS.png").targetOffset(227,-2)
imgLabelDataFimEFDICMS = Pattern("imgLabelDataFimEFDICMS.png").targetOffset(170,0)


imgRodapePesquisa = "imgRodapePesquisa.png"
imgBotaoPesquisar = Pattern("imgRodapePesquisa.png").targetOffset(-115,-2)
imgBotaoSolicitarArquivos = Pattern("imgRodapePesquisa.png").targetOffset(44,-3)

imgBtnPesquisar = "imgBtnPesquisar.png"

imgAguardandoSolicitacao = "aguardandosolicitacao.png"

imgPedidos = Pattern("imgPedidos.png").similar(0.53).targetOffset(-21,42)
imgConfirmarPedidos = Pattern("imgConfirmarPedidos.png").targetOffset(-24,36)
imgArquivosDoPedido = Pattern("imgArquivosDoPedido.png").targetOffset(-2,31)
imgBotaoBaixar = "1748434637096.png"
imgTemBaixando = "1748434701709.png"
imgTemAguardando = "1748434754412.png"
imgTemRecebendo = "1748434788522.png"
imgComecouABaixar = "imgEstaBaixando.png"
imgAcabouDeBaixar = "imgAcabouDeBaixar.png"
imgBotaoSair = Pattern("imgBotaoSair.png").similar(0.88)

   
imgCabecalhoResultado = Pattern("imgCabecalhoResultado.png").similar(0.50).targetOffset(-2,25)

imgCabecalhoResultadoPesquisaEFDICMS = Pattern("imgCabecalhoResultadoPesquisaEFDICMS.png").similar(0.60).targetOffset(-223,-16)
imgCabecalhoResultadoPesquisaEFDICMSProcurador = Pattern("imgCabecalhoResultadoPesquisaEFDICMSProcurador.png").targetOffset(-133,54)

imgNenhumArquivoEncontrado = Pattern("imgNenhumArquivo.png").targetOffset(-6,32)


imgErroSemProcuracao = Pattern("imgErroSemProcuracao.png").targetOffset(1,45)
imgErroSemProcuracao2 = Pattern("imgErroSemProcuracao2.png").targetOffset(-6,46)
imgErroProcuracaoExpirou = Pattern("imgErroProcuracaoExpirou.png").targetOffset(-1,46)
imgErroSemResultados = Pattern("imgErroSemResultados.png").targetOffset(-1,33)
imgErroCertificadoExpirou = Pattern("imgErroCertificadoExpirou.png").targetOffset(-5,36)

imgTemDadosSelecionados = Pattern("imgTemDadosSelecionados.png").similar(0.64)
imgTemDadosSelecionados2 = Pattern("imgTemDadosSelecionados2.png").similar(0.46)


imgBotaoSolicitarPesquisa = "1748375935889.png"
imgPesquisaRealizada = Pattern("imgPesquisaRealizada.png").targetOffset(-1,36)

imgCabecalhoSelecaoCertificado = "imgCabecalhoSelecaoCertificado.png"

imgInfoDataFimEhObrigatorio = Pattern("imgInfoDataFimEhObrigatorio.png").targetOffset(-2,38)






def esperarTelaSelecaoCertificado():
    if not exists(Pattern("ReceitaNetBX-Certificados.png").targetOffset(275,-33), 60):
        return False
    return True
    

def selecionarPerfilCertificado(nome_prioritario):

    nome_prioritario = normalizar_texto(nome_prioritario)  #Recebe o primeiro parâmetro do JSON, a qual a função normalizar_texto retira os caracteres especiais da variável (nome_prioritario)
    Debug.log(3, "PROCESSANDO NOME = %s" % nome_prioritario) 

    linhas_regioes = [
        Region(674,475,260,19),
        Region(674,493,251,20),
        Region(675,511,255,21),
        Region(672,529,260,20),
        Region(673,548,250,18),
        Region(670,564,274,20),
        Region(673,585,287,17),
        Region(672,600,277,18)
    ]

    max_scrolls = 10 #Limite scroll, considerando a propriedade de mouse como sendo scroll o número de linhas de cada vez = 3
    scrolls = 0
    ultima_linha = u""

    while scrolls < max_scrolls:

        for regiao in linhas_regioes:
            try:
                texto = unicode(regiao.text()).upper()
                Debug.log(3, "TEXTO OCR = %s" % texto)
            except:
                texto = u""

            if nome_prioritario in texto:
                click(regiao)
                sleep(0.4)

                if exists(imgErroCertificadoExpirou, 2):
                    click(imgErroCertificadoExpirou)
                    return False

                return True

        try:
            nova_ultima_linha = unicode(linhas_regioes[-1].text()).upper() #trecho responsável por definir última região e realizar scroll
        except:
            nova_ultima_linha = u""

        if nova_ultima_linha == ultima_linha:
            Debug.log(3, "FIM DA LISTA NA TELA")
            break

        ultima_linha = nova_ultima_linha 
        wheel(regiaoCertificados, WHEEL_DOWN, 3)
        sleep(1)
        scrolls += 1

    return False

def selecionarCertF2():
    linhas_regioes = [
        Region(673,477,342,18),
        Region(671,497,349,15),
        Region(674,515,344,16),
        Region(673,532,344,16),
        Region(674,550,341,15),
        Region(673,567,342,17),
        Region(672,585,343,18),
        Region(673,603,343,15)
    ]

    regiaoCertificados = Region(674,457,573,163)
    Lista = ["F2 SERVICOS ADMINISTRATIVOS LTDA"]

    max_scrolls = 20
    scrolls_feitos = 0

    mouseMove(regiaoCertificados.getCenter()) #trecho responsável por "focar" mouse na tela do ReceitaNetBX
    click(regiaoCertificados)
    sleep(0.2)

    while scrolls_feitos < max_scrolls:

        for regiao in linhas_regioes:
            try:
                texto = unicode(regiao.text()).upper().strip()
                Debug.log(3, "texto lido foi: " + texto)
            except:
                texto = u""

            for nome in Lista:
                if nome.upper() in texto:
                    
                    Debug.log(3, "encontrado: " + nome)
                    click(regiao)
                    sleep(0.6)

                    if exists(imgErroCertificadoExpirou, 2):
                        click(imgErroCertificadoExpirou)
                        sleep(0.3)
                        return False

                    return True

        try:
            ultima_antes = unicode(linhas_regioes[-1].text()).upper().strip()
        except:
            ultima_antes = u""

        wheel(regiaoCertificados, WHEEL_DOWN, 3)
        sleep(0.5)

        try:
            ultima_depois = unicode(linhas_regioes[-1].text()).upper().strip()
        except:
            ultima_depois = u""

        Debug.log(3, "ULTIMA LINHA antes='%s' depois='%s'" % (ultima_antes, ultima_depois))

        if ultima_depois == ultima_antes:
            Debug.log(3, "SEM MOVIMENTO NO SCROLL (fim da lista ou wheel nao funcionou)")
            return False

        scrolls_feitos += 1

    Debug.log(3, "LIMITE DE SCROLL ATINGIDO - F2 nao encontrado")
    return False


def selecionarPerfilProcurador():
    if find(imgSelecionarPerfil):
        click(imgSelecionarPerfil)
        Debug.log(3, "KD1")
        type(Key.DOWN)


def definirCnpj(cnpj):
    wait(imgQuemRepresenta, 30)
    click(imgQuemRepresenta)
    type(Key.DOWN)
    Debug.log(3, "XXXX2")
    type(Key.TAB)
    type("a", Key.CTRL)  
    type(Key.DELETE)     
    type(cnpj)
    type(Key.ENTER)
    
def trocarPerfil():
    wait(imgTrocarPerfil, 30)
    click(imgTrocarPerfil)

def clicarEntrar():
    find(imgRodape)
    click(imgRodape)
    waitVanish(imgCabecalhoSelecaoCertificado, 60)

def clicarBotaoPesquisar():
    wait(imgBotaoPesquisaAcompanhamentoPesquisar, 10)
    click(imgBotaoPesquisaAcompanhamentoPesquisar)
    
def clicarBotaoTrocarPerfil():
    wait(imgBotaoTrocarPefil, 30)
    click(imgBotaoTrocarPefil)

def selecionarECFteste():
    wait(imgLabelSelecioneUmSistema, 30)
    click(imgLabelSelecioneUmSistema)
    sleep(0.1)
    type(Key.DOWN)
    Debug.log(3, "KD3")
    for i in range(2):
        type(Key.DOWN)
    type(Key.ENTER)
    wait(imgLabelSelecioneTipoArquivo, 30)
    click(imgLabelSelecioneTipoArquivo)
    type(Key.DOWN)
    type(Key.ENTER)
    wait(imgLabelSelecioneTipoArquivo, 30)
    click(imgLabelSelecioneTipoPesquisa)
    sleep(0.1)
    type(Key.DOWN)
    for i in range(1):
        type(Key.DOWN)
    type(Key.ENTER)

def selecionarECDteste():
    wait(imgLabelSelecioneUmSistema, 30)
    click (imgLabelSelecioneUmSistema)
    sleep(0.1)
    type(Key.DOWN)
    Debug.log(3, "KD4")
    type(Key.ENTER)
    wait(imgLabelSelecioneTipoArquivo, 30)
    click(imgLabelSelecioneTipoArquivo)
    sleep(0.1)
    type(Key.DOWN)
    type(Key.ENTER)
    wait(imgLabelSelecioneTipoPesquisa, 30)
    click(imgLabelSelecioneTipoPesquisa)
    sleep(0.1)
    type(Key.DOWN)
    for i in range(2):
        type(Key.DOWN)
    type(Key.ENTER)

   
def selecionarEFDContribuicoes():
    wait(imgLabelSelecioneUmSistema, 30)
    click(imgLabelSelecioneUmSistema)
    sleep(0.1)
    type(Key.DOWN)
    for i in range(5):
        type(Key.UP)
    type(Key.ENTER)
    wait(imgLabelSelecioneTipoArquivo, 30)
    click(imgLabelSelecioneTipoArquivo)
    type(Key.DOWN)
    type(Key.ENTER)
    wait(imgLabelSelecioneTipoPesquisa, 30)
    click(imgLabelSelecioneTipoPesquisa)
    wait(imgOpcoesTipoPesquisaEFDContribuicoes)
    click(imgOpcoesTipoPesquisaEFDContribuicoes)



def selecionarEFDICMS():
    wait(imgLabelSelecioneUmSistema, 30)
    click(imgLabelSelecioneUmSistema)
    sleep(0.1)
    type(Key.DOWN)
    Debug.log(3, "KD5")
    for i in range(5):
        type(Key.UP)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER)
    wait(imgLabelSelecioneTipoArquivo, 30)
    click(imgLabelSelecioneTipoArquivo)
    type(Key.DOWN)
    wait(imgCamposEFDICMS, 30)
    click(imgCamposEFDICMS)
    wait(imgCamposEFDICMSBotaoSelecionarTodos)
    click(imgCamposEFDICMSBotaoUltimosArquivos)



def selecionarDataEFDICMS(data_inicio, data_fim):
    wait(imgLabelDataInicioEFDICMS, 10)
    click(imgLabelDataInicioEFDICMS)
    type(data_inicio)
    click(imgLabelDataFimEFDICMS)
    type(data_fim)
    
 


def selecionarDataEFDContribuicoes(data_inicio, data_fim):
    wait(imgLabelDataInicio, 10)
    click(imgLabelDataInicio)
    type(data_inicio)
    click(imgLabelDataFim)
    type(data_fim)

def selecionarDataECDteste(data_inicio, data_fim):
    wait(imgLabelDataInicio, 10)
    click(imgLabelDataInicio)
    type(data_inicio)
    click(imgLabelDataFim)
    type(data_fim)

def selecionarDataECFteste(data_inicio, data_fim):
    wait(imgLabelDataInicio, 10)
    click(imgLabelDataInicio)
    type(data_inicio)
    click(imgLabelDataFim)
    type(data_fim)

def clicarPesquisarEFDContribuicoes():
    wait(imgRodapePesquisa, 10)
    click(imgBotaoPesquisar)

def clicarPesquisarEFDICMS():
    wait(imgBtnPesquisar, 10)
    click(imgBtnPesquisar)
    if exists(imgInfoDataFimEhObrigatorio):
        click(imgInfoDataFimEhObrigatorio)
        click(imgBtnPesquisar)

def clicarECDteste():
    wait(imgBtnPesquisar, 10)
    click(imgBtnPesquisar)
    if exists(imgInfoDataFimEhObrigatorio):
        click(imgInfoDataFimEhObrigatorio)
        click(imgBtnPesquisar)
        
def clicarECFteste():
    wait(imgBtnPesquisar, 10)
    click(imgBtnPesquisar)
    if exists(imgInfoDataFimEhObrigatorio):
        click(imgInfoDataFimEhObrigatorio)
        click(imgBtnPesquisar)

def processarPesquisaEFDICMS():
    if exists(imgNenhumArquivoEncontrado):
        click(imgNenhumArquivoEncontrado)
        return False
    if exists(imgErroSemProcuracao):
        click(imgErroSemProcuracao)
        return False
    elif exists(imgErroSemProcuracao2):
        click(imgErroSemProcuracao2)
        return False
    elif exists(imgErroSemResultados):
        click(imgErroSemResultados)
        return False
    elif exists(imgErroProcuracaoExpirou):
        click(imgErroProcuracaoExpirou)
        return False
    else:
        wait(imgCabecalhoResultadoPesquisaEFDICMSProcurador, 180)
        rightClick(imgCabecalhoResultadoPesquisaEFDICMSProcurador)
        mousePos = Env.getMouseLocation()
        x = mousePos.getX()
        y = mousePos.getY()
        new_x = x + 15
        new_y = y + 10
        click(Location(new_x, new_y))
        wait(imgTemDadosSelecionados2,10)
        wait(imgBotaoSolicitarPesquisa, 10)
        click(imgBotaoSolicitarPesquisa)
        wait(imgPesquisaRealizada, 180)
        click(imgPesquisaRealizada)
        return True

#Função responsável por acessar a pasta e separar por lista(tipo, data, cnpj) cada arquivo baixado do ReceitaNetBX
def validarArquivos():
    caminho = r"C:\Users\patrick\Documents\Arquivos ReceitanetBX"
    achados = [] #constrói a lista aqui
    if not os.path.isdir(caminho):
        print("caminho nao encontrado ou erro")
        return

    for nome in os.listdir(caminho):
        nome = nome.strip()
        dados = None

        base, _ = os.path.splitext(nome) #linha responsavel ao ler o arquivo na pasta retornar a seguinte lógica (parte_sem_extensao, extensao), por exemplo: "arquivo.txt" retorna: (arquivo, txt)
                                         #OBS: o uso do "_" tem como a seguinte lógica: o valor existe, mas não é relevante, ou seja, o nome do arquivo existe, mas não importa qual seja

        if base.startswith("PISCOFINS_"): #Lógica de filtrar o nome do arquivo com o padrão "PISCOFINS"
            p = base.split("_") #começa a filtrar o nome a partir do uso do caractere: "_"
            if len(p) >= 4: #garante que exista 4 blocos
                dados = {
                    "arquivo": nome, #mantem o nome do arquvio
                    "tipo": "EFDContribuicoes",
                    "data": p[1][0:6],
                    "cnpj": p[3],
                }


        elif base.startswith("SPEDECF-"):
            sem_barra = base.split("-", 1)[1]
            p = sem_barra.split("-")
            if len(p) >= 3:
                dados = {
                    "arquivo": nome,
                    "tipo": "ECF",
                    "cnpj": p[0],
                    "data": p[1][0:6],  
                }

        elif "-SPED-" in base.upper():
            p = base.upper().split("-")

            if len(p) >= 4 and p[-2] == "SPED":
                sufixo = p[-1] 

                if sufixo == "EFD":
                    tipo = "EFDICMS"
                elif sufixo == "ECD":
                    tipo = "ECD"
                else:
                    tipo = None

                if tipo:
                    dados = {
                        "arquivo": nome,
                        "tipo": tipo,
                        "data": p[2][0:6],
                        "cnpj": p[0],  
                    }
        if dados:
            if (
                len(dados["cnpj"]) == 14 and dados["cnpj"].isdigit() and
                len(dados["data"]) == 6 and dados["data"].isdigit()
            ):
                achados.append(dados)
    return achados

#Função auxiliar, ou seja, tem como finalidade "quebrar" (separar) a data recebida pelo JSON (exemplo: 202209) em ano (2022) e mes (09)
def quebrar_ano_mes(data_yyyymm):
    if not data_yyyymm or len(data_yyyymm) != 6 or not data_yyyymm.isdigit():
        return ("SEM_ANO", "SEM_MES")
    ano = data_yyyymm[0:4]
    #mes = data_yyyymm[4:6]
    return (ano)

#Finalidade da função: Mover os arquivos baixados para o servidor ---- OBS: O caminho do servidor é definido na chamada
def mover_arquivos_com_validacao(caminho_base_destino):
    origem = "C:\Users\patrick\Documents\Arquivos ReceitanetBX"
    achados = validarArquivos()

    if not achados:
        try:
            Debug.log(3, "Nenhum arquivo válido encontrado.")
        except:
            print("Nenhum arquivo válido encontrado.")
        return

    #Aproveita o resultado da função validarArquivos()
    for item in achados:
        cnpj = item["cnpj"]
        tipo = item["tipo"]
        data = item["data"]
        nome_arquivo = item["arquivo"]
        
        ano = quebrar_ano_mes(data)

        destino_dir = os.path.join(caminho_base_destino, cnpj, tipo, ano) #Define que o destino do arquivo tenha o caminho_base_destino com a pasta "cnpj" e sub-pasta: "tipo" e outra sub_pasta: "ano"

        if not os.path.exists(destino_dir): #Caso o destino não tenha as pastas criadas
            os.makedirs(destino_dir) #Crias as pastas e sub-pastas

        src = os.path.join(origem, nome_arquivo) #Movimentação do arquivo (origem)
        dst = os.path.join(destino_dir, nome_arquivo) #Movimentação do arquivo (destino)

        try:
            os.rename(src, dst) #Responsável por renomear as pastas conforme o JSON
            try:
                Debug.log(3, "Movido: " + nome_arquivo)
            except:
                print("Movido: " + nome_arquivo)
        except Exception as e:
            try:
                Debug.log(3, "Erro ao mover: " + nome_arquivo + " | " + str(e))
            except:
                print("Erro ao mover: " + nome_arquivo + " | " + str(e))
                

#Função responsável por receber parâmetros JSON da a API com a finalidade de preencher no DB a coluna DataProcessamento conforme a automação
def finalizar_processo(dados):
    tipo = dados.get("tipo") or dados.get("Tipo")
    cnpj_raw = dados.get("cnpj") or dados.get("Cnpj")
    periodo = dados.get("data") or dados.get("Data") or dados.get("Periodo")

    if not (tipo and cnpj_raw and periodo):
        raise Exception("finalizar_processo: item invalido: %s" % str(dados))

    cnpj_filtro = re.sub(u"\\D", u"", unicode(cnpj_raw)) #Retira os caracteres que compõe o cnpj, exemplo ("-", "/", ".")

    if len(cnpj_filtro) != 14: #inválida caso o cnpj não esteja correto
        raise Exception("CNPJ invalido (menos de 14 digitos): %s" % unicode(cnpj_raw))

    cnpj_mask = u"%s.%s.%s/%s-%s" % (  #exemplo: 23.982.164/0001-67
        cnpj_filtro[0:2], #filtra 23
        cnpj_filtro[2:5], #filtra 982
        cnpj_filtro[5:8], #filtra 164
        cnpj_filtro[8:12], #filtra 0001
        cnpj_filtro[12:14], #filtra 67
    )

    #Envia os parametros para API para que assim valide a coluna DataProcessamento
    params = urlencode({
        "aCNPJ": unicode(cnpj_mask),
        "aPeriodo": unicode(periodo),
        "aTipo": unicode(tipo),
    })

    url_finalizar = (
        "http://192.168.5.176:2781/automacao_receita_bx/"
        "AutomacaoReceitaBX/FinalizarProcesso?" + params
    )

    Debug.log(3, "FinalizarProcesso GET: %s" % url_finalizar)

    resp = http_get(url_finalizar)
    Debug.log(3, "Resposta FinalizarProcesso: %s" % resp)
    return resp

def processarPesquisaEFDContribuicoes():
    if exists(imgNenhumArquivoEncontrado):
        click(imgNenhumArquivoEncontrado)
        return False
    if exists(imgErroSemProcuracao):
        click(imgErroSemProcuracao)
        return False
    elif exists(imgErroSemProcuracao2):
        click(imgErroSemProcuracao2)
        return False
    elif exists(imgErroSemResultados):
        click(imgErroSemResultados)
        return False
    elif exists(imgErroProcuracaoExpirou):
        click(imgErroProcuracaoExpirou)
        return False
    else:
        wait(imgCabecalhoResultadoPesquisaEFDICMSProcurador, 180)
        rightClick(imgCabecalhoResultadoPesquisaEFDICMSProcurador)
        mousePos = Env.getMouseLocation()
        x = mousePos.getX()
        y = mousePos.getY()
        new_x = x + 15
        new_y = y + 10
        click(Location(new_x, new_y))
        wait(imgTemDadosSelecionados2,10)
        wait(imgBotaoSolicitarPesquisa, 10)
        click(imgBotaoSolicitarPesquisa)
        wait(imgPesquisaRealizada, 180)
        click(imgPesquisaRealizada)
        return True

def processarPesquisaECDteste():
    if exists(imgNenhumArquivoEncontrado):
        click(imgNenhumArquivoEncontrado)
        return False
    if exists(imgErroSemProcuracao):
        click(imgErroSemProcuracao)
        return False
    elif exists(imgErroSemProcuracao2):
        click(imgErroSemProcuracao2)
        return False
    elif exists(imgErroSemResultados):
        click(imgErroSemResultados)
        return False
    elif exists(imgErroProcuracaoExpirou):
        click(imgErroProcuracaoExpirou)
        return False
    else:
        wait(imgCabecalhoResultado, 180)
        rightClick(imgCabecalhoResultado)
        mousePos = Env.getMouseLocation()
        x = mousePos.getX()
        y = mousePos.getY()
        new_x = x + 15
        new_y = y +10
        click(Location(new_x, new_y))
        wait(imgBotaoSolicitarPesquisa, 10)
        click(imgBotaoSolicitarPesquisa)
        wait(imgPesquisaRealizada, 180)
        click(imgPesquisaRealizada)
        return True

def processarPesquisaECFteste():
    if exists(imgNenhumArquivoEncontrado):
        click(imgNenhumArquivoEncontrado)
        return False
    if exists(imgErroSemProcuracao):
        click(imgErroSemProcuracao)
        return False
    elif exists(imgErroSemProcuracao2):
        click(imgErroSemProcuracao2)
        return False
    elif exists(imgErroSemResultados):
        click(imgErroSemResultados)
        return False
    elif exists(imgErroProcuracaoExpirou):
        click(imgErroProcuracaoExpirou)
        return False
    else:
        wait(imgCabecalhoResultado, 180)
        rightClick(imgCabecalhoResultado)
        mousePos = Env.getMouseLocation()
        x = mousePos.getX()
        y = mousePos.getY()
        new_x =  x + 15
        new_y = y +10
        click(Location(new_x, new_y))
        wait(imgBotaoSolicitarPesquisa, 10)
        click(imgBotaoSolicitarPesquisa)
        wait(imgPesquisaRealizada, 180)
        click(imgPesquisaRealizada)
        return True

def abrirAcompanhamento():
    wait(imgBotaoPesquisaAcompanhamento, 10)
    click(imgBotaoPesquisaAcompanhamento)

#Função auxiliar, na qual sua finalidade é tratar a data(202209) commo sendo 2022 e 09
def gerar_lista_datas(data_inicio, data_final):
    
    data_inicio = unicode(data_inicio or u"").strip()
    data_final = unicode(data_final or u"").strip()
    
    if len(data_inicio) != 6 or len(data_final) != 6: #Se não tiver no padrão do JSON, ou seja (202209) 6 dígitos invalida operação
        return []
    
    try: #Lógica de separar "quebrar" a data
        ano_ini = int(data_inicio[0:4]) 
        mes_ini = int(data_inicio[4:6])
        ano_fim = int(data_final[0:4])
        mes_fim = int(data_final[4:6])
       
    except:
        return []
    
    if mes_ini < 1 or mes_ini > 12 or mes_fim < 1 or mes_fim > 12: #lógica de validação ::   1 <= B <= 12, sendo que B = (mes, ano)
        return []
    
    atual = ano_ini * 12 + (mes_ini - 1) #lógica de indice linear, tendo como finalidade as "virada de ano". Por exemplo: atual = 2024 * 12 + (1 - 1) = 24.288, logo, fim = 2024 * 12 + (12 - 1) = 24.299. Logo pode ser feito a interação de +1
    fim = ano_fim * 12 + (mes_fim - 1) #  f(ano, mes) = 12 * ano + (mes - 1)
    
    if fim < atual:
        return []
    
    out = []
    
    while atual < fim: #Cada interação gera a validação de intervalo, ou seja, gerar_lista_datas(202201, 202211) retorna = [202201, 202202, 202203, ..., 202210, 202211]
        ano = atual // 12
        mes = (atual % 12) + 1
        out.append("%04d%02d" % (ano, mes))
        atual += 1
        
    return out 
   

def baixarUltimoPedido():
    try:
        if not exists(imgPedidos, 5):
            wait(imgVerPedidos, 20)
            click(imgVerPedidos)
            wait(imgPedidos, 20)
        
        
        if exists(imgConfirmarPedidos, 5):
            click(imgConfirmarPedidos)
            waitVanish(imgConfirmarPedidos, 10)

        try:
            wait(imgArquivosDoPedido, 30)
        except FindFailed:
            return False
        
        rightClick(imgArquivosDoPedido)
        mousePos = Env.getMouseLocation()
        x = mousePos.getX()
        y = mousePos.getY()
        new_x = x + 15
        new_y = y + 45
        click(Location(new_x, new_y))

        wait(imgTemDadosSelecionados2, 300)
        sleep(2)
        click(imgBotaoBaixar)
     
        try:
            wait(imgAcabouDeBaixar, 14400)
        except:
           
            if exists(imgComecouABaixar, 10):
                sleep(300)  
            else:
                return False
                
        return True  
        
    except Exception as e:
        return False  
    
def sair():
    try:
        wait(imgBotaoSair, 10)
        click(imgBotaoSair)
    except:
        pass
        


#lista = []
CAMINHO_BASE = r"C:\Users\patrick\Desktop\testes" #Caminho de onde será enviado (Padrão do caminho é: P:\Ficus\Dados\BI)
PASTA_DOWNLOAD = r"C:\Users\patrick\Documents\Arquivos ReceitanetBX" #Caminho onde os arquivos da ReceitaNetBX estão baixados (Padrão do caminho é esse, logo, deve mudar conforme o nome do usuário)
arquivoReceitaNet = r"C:\Program Files (x86)\Programas RFB\Receitanet BX\executar.bat" #Caminho do arquivo .bat para abrir o ReceitaNetBX


url = ".env/automacao_receita_bx/AutomacaoReceitaBX/PegarProximaParadaPraBaixar" #URL destacando a função da API responsável por ordenar os valores JSON
response = http_get(url) #Requisição GET
Debug.log(3, response)

try:
    dados = json.loads(response) #Converte a string JSON para estrutura python
except Exception:
    Debug.log(3, "ERRROOO COM JSON")
    Debug.log(3, "Traceback: %s" % traceback.format_exc())
    raise


registros = dados.get("Result", []) #JSON entrega um Result sendo uma lista de objetos, logo, a variável registro é responsável por "pegar" esses objetos

Debug.log(3, "API recebeu os registros")
Debug.log(3, str(registros))


lista = []

for reg in registros: #lista auxiliar 
    if not isinstance(reg, dict):
        Debug.log(3, "Item nao e dicionario: %s" % str(reg))
        continue

    nome = reg.get("Nome", u"")
    lista.append({
    "nome": nome,
    "raw": reg,
})
    
try: 
    for reg in registros: #Aqui é a mesma lógica, ideia de ser uma lista auxiliar, logo, a automação percorre cada objeto da API e "armazena" 
        cnpj_raw = reg.get("Cnpj", u"") 
        tipo = reg.get("Tipo", u"")
        data_ini_json = reg.get("DataInicio", u"")
        data_fim_json = reg.get("DataFinal", u"")
        lista_datas = gerar_lista_datas(data_ini_json, data_fim_json)

        cnpj_digits = u"".join(ch for ch in unicode(cnpj_raw) if ch.isdigit()) #faz disso 23.982.164/0001-67 virar isso 23982164000167
        nome = reg.get("Nome", u"")
        cert_proc = reg.get("CertificadoProcuracao", u"")
        cert_proc_norm = unicode(cert_proc).strip().upper()

        App.open(arquivoReceitaNet)
        sleep(2)

        Debug.log(3, "00001")
        achados_iniciais = validarArquivos()
        Debug.log(3, "validarArquivos inicial len=%s" % (len(achados_iniciais) if achados_iniciais else 0))
        Debug.log(3, "00002")

        esperarTelaSelecaoCertificado()

        if cert_proc_norm == u"PROCURAÇÃO ELETRÔNICA":
            selecionarCertF2()
            selecionarPerfilProcurador()
            definirCnpj(cnpj_digits)
        else:
            ok = selecionarPerfilCertificado(nome)

        clicarEntrar()
        clicarBotaoPesquisar()


        if tipo == "EFDICMS":
            for data in lista_datas:
                Debug.log(3, "EFDICMS periodo=%s cnpj=%s" % (data, cnpj_raw))

                ano = data[0:4]
                mes = data[4:6]
                data_inicio = "01/%s/%s" % (mes, ano)
                ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
                data_fim = "%02d/%s/%s" % (ultimo_dia, mes, ano)

                selecionarEFDICMS()
                selecionarDataEFDICMS(data_inicio, data_fim)
                clicarPesquisarEFDICMS()

                b = processarPesquisaEFDICMS()
                if b:
                    abrirAcompanhamento()
                    download_ok = baixarUltimoPedido()

                    if download_ok:

                        achados = validarArquivos()
                        Debug.log(3, "validarArquivos pós-download len=%s" % (len(achados) if achados else 0))

                        resp = finalizar_processo({"Cnpj": cnpj_raw, "Tipo": tipo, "Data": data})
                        Debug.log(3, "FinalizarProcesso resp=%s (cnpj=%s tipo=%s data=%s)" % (resp, cnpj_raw, tipo, data))
                        mover_arquivos_com_validacao(CAMINHO_BASE)

                    else:
                        Debug.log(3, "DOWNLOAD FALHOU periodo=%s" % data)

                    clicarBotaoPesquisar()
                else:
                    Debug.log(3, "ERRO AO PROCESSAR PERIODO=%s" % data)

            sair()

        elif tipo == "EFDContribuicoes":
            for data in lista_datas:
                Debug.log(3, "EFDContribuicoes periodo=%s cnpj=%s" % (data, cnpj_raw))

                ano = data[0:4]
                mes = data[4:6]
                data_inicio = "01/%s/%s" % (mes, ano)
                ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
                data_fim = "%02d/%s/%s" % (ultimo_dia, mes, ano)

                selecionarEFDContribuicoes()
                selecionarDataEFDContribuicoes(data_inicio, data_fim)
                clicarPesquisarEFDContribuicoes()

                b = processarPesquisaEFDContribuicoes()
                if b:
                    abrirAcompanhamento()
                    download_ok = baixarUltimoPedido()

                    if download_ok:
                        achados = validarArquivos()
                        Debug.log(3, "validarArquivos pós-download len=%s" % (len(achados) if achados else 0))

                        resp = finalizar_processo({"Cnpj": cnpj_raw, "Tipo": tipo, "Data": data})
                        Debug.log(3, "FinalizarProcesso resp=%s (cnpj=%s tipo=%s data=%s)" % (resp, cnpj_raw, tipo, data))
                        mover_arquivos_com_validacao(CAMINHO_BASE)
                    else:
                        Debug.log(3, "DOWNLOAD FALHOU periodo=%s" % data)

                    clicarBotaoPesquisar()
                else:
                    Debug.log(3, "ERRO AO PROCESSAR PERIODO=%s" % data)

            sair()

        elif tipo == "ECF":
            for data in lista_datas:
                Debug.log(3, "ECF periodo=%s cnpj=%s" % (data, cnpj_raw))

                ano = data[0:4]
                mes = data[4:6]
                data_inicio = "01/%s/%s" % (mes, ano)
                ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
                data_fim = "%02d/%s/%s" % (ultimo_dia, mes, ano)

                selecionarECFteste()
                selecionarDataECFteste(data_inicio, data_fim)
                clicarECFteste()

                b = processarPesquisaECFteste()
                if b:
                    abrirAcompanhamento()
                    download_ok = baixarUltimoPedido()

                    if download_ok:
                        achados = validarArquivos()
                        Debug.log(3, "validarArquivos pós-download len=%s" % (len(achados) if achados else 0))

                        resp = finalizar_processo({"Cnpj": cnpj_raw, "Tipo": tipo, "Data": data})
                        Debug.log(3, "FinalizarProcesso resp=%s (cnpj=%s tipo=%s data=%s)" % (resp, cnpj_raw, tipo, data))
                        mover_arquivos_com_validacao(CAMINHO_BASE)
                    else:
                        Debug.log(3, "DOWNLOAD FALHOU periodo=%s" % data)

                    clicarBotaoPesquisar()
                else:
                    Debug.log(3, "ERRO AO PROCESSAR PERIODO=%s" % data)

            sair()

        elif tipo == "ECD":
            for data in lista_datas:
                Debug.log(3, "ECD periodo=%s cnpj=%s" % (data, cnpj_raw))

                ano = data[0:4]
                mes = data[4:6]
                data_inicio = "01/%s/%s" % (mes, ano)
                ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
                data_fim = "%02d/%s/%s" % (ultimo_dia, mes, ano)

                selecionarDataECDteste()
                selecionarDataECDteste(data_inicio, data_fim)
                clicarECFteste()

                b = processarPesquisaECFteste()
                if b:
                    abrirAcompanhamento()
                    download_ok = baixarUltimoPedido()

                    if download_ok:
                        achados = validarArquivos()
                        Debug.log(3, "validarArquivos pós-download len=%s" % (len(achados) if achados else 0))

                        resp = finalizar_processo({"Cnpj": cnpj_raw, "Tipo": tipo, "Data": data})
                        Debug.log(3, "FinalizarProcesso resp=%s (cnpj=%s tipo=%s data=%s)" % (resp, cnpj_raw, tipo, data))
                        mover_arquivos_com_validacao(CAMINHO_BASE)
                    else:
                        Debug.log(3, "DOWNLOAD FALHOU periodo=%s" % data)

                    clicarBotaoPesquisar()
                else:
                    Debug.log(3, "ERRO AO PROCESSAR PERIODO=%s" % data)

            sair()

        else:
            Debug.log(3, "TIPO NAO TRATADO: %s" % tipo)
            sair()

except Exception: 
    Debug.log("Traceback: %s" % traceback.format_exc())

