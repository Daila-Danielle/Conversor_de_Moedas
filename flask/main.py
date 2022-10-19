#pip install requests
from optparse import OptionContainer
import requests
from flask import Flask, render_template, request
#importar o json facilita na hora de consumir api
import json 
from datetime import date, datetime

app = Flask(__name__)

@app.route('/')
def abre():
    return render_template("index.html")

@app.route('/index',methods=['POST'])
def abre_index():
    reais       = float(request.form['reais'])
    opcao       = request.form['moeda']
    dados       = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,BTC-BRL,EUR-BRL")
    conteudo    = json.loads(dados.content) #Exibe conteudo
    
    
    valor_dolar = float(conteudo['USDBRL']['bid'])
    data_dolar = (conteudo['USDBRL']['create_date'])

    valor_btc   = float(conteudo['BTCBRL']['bid'])
    data_btc = (conteudo['BTCBRL']['create_date'])

    valor_euro  = float(conteudo['EURBRL']['bid'])
    data_euro = (conteudo['EURBRL']['create_date'])

    if opcao == 'DOLAR':
        return render_template("index.html", convertido = (f'{reais/valor_dolar:.2f} USD') ,real=reais,opcaoo = opcao,cotacao =(f'''{valor_dolar} USD'''), data = (f'''Ultima atualização - {data_dolar}'''))
    elif opcao == 'EURO':
        return render_template("index.html", convertido = (f'{reais/valor_euro:.2f} EUR'),real=reais,opcaoo = opcao,cotacao =(f'''{valor_euro} EUR'''), data = (f'''Ultima atualização - {data_euro}'''))
    elif opcao == 'BITCOIN': 
        return render_template("index.html", convertido = (f'{(reais/valor_btc)/1000:.4f} BTC'),real=reais,opcaoo = opcao,cotacao =(f'''{valor_btc} BTC '''), data = (f'''Ultima atualização - {data_btc}'''))
    elif opcao == 'PESO ARGENTINO':
        return render_template("index.html", convertido = 'INDISPONIVEL',real=reais,opcaoo = opcao)

    return abre()

app.run(debug=True)




