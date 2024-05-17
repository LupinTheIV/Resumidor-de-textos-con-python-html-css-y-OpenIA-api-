from resumen import ResumeTexto
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/resumen_texto", methods=['POST'])
def result():
    idioma = request.form['idioma']
    texto = request.form['texto_r']
    if idioma != "" or texto != "":
        load_dotenv()
        gpt_resumen = ResumeTexto(api_key= os.environ.get("OPENAI_API_KEY"))
        resumen_g = gpt_resumen.resumen(texto, idioma)
        return render_template("index.html", resumen = resumen_g)
    else:
        resumen_g = "Alerta: Porfavor llena todos los campos"
        return render_template("index.html", resumen = resumen_g)
if __name__ == '__main__':
    app.run()