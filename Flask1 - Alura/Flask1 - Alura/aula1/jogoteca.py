from flask import Flask, render_template

app = Flask(__name__) # objeto flask que apresenta a aplicação


@app.route('/inicio') #caminho
def ola(): #função para retornar um texto
    lista = ['Tetris', 'Super Mario', "Pokemon Gold"]
    return render_template('lista.html', titulo='Jogos', jogos=lista) # pode colocar o html direto


app.run() # roda
