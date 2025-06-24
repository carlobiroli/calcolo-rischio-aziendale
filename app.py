from flask import Flask, render_template, request

app = Flask(__name__)

def calcola_rischio(probabilita, danno, esposizione):
    return probabilita * danno * esposizione

def interpreta_rischio(rischio):
    if rischio <= 20:
        return "Basso"
    elif rischio <= 60:
        return "Medio"
    elif rischio <= 100:
        return "Alto"
    else:
        return "Estremo"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    probabilita = int(request.form['probabilita'])
    danno = int(request.form['danno'])
    esposizione = int(request.form['esposizione'])

    rischio = calcola_rischio(probabilita, danno, esposizione)
    interpretazione = interpreta_rischio(rischio)

    return render_template('index.html', risultato=rischio, interpretazione=interpretazione)

if __name__ == '__main__':
    app.run(debug=True)
