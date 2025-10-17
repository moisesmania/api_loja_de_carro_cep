from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_BASE = "http://00.000.000.00:8080"  # Atualize para o IP correto da AWS

def listar_carros():
    """Função para obter a lista de carros da API"""
    try:
        res = requests.get(f"{API_BASE}/listarCarros")
        if res.status_code == 200:
            return res.json()
    except requests.exceptions.RequestException:
        pass
    return []

@app.route("/", methods=["GET"])
def index():
    carros = listar_carros()
    return render_template("index.html", carros=carros, cep_resultado=None)

@app.route("/add_carro", methods=["POST"])
def add_carro():
    modelo = request.form.get("modelo")
    preco = request.form.get("preco")
    if modelo and preco:
        payload = {"modelo": modelo, "preco": float(preco)}
        try:
            res = requests.post(f"{API_BASE}/saveCarro", json=payload)
        except requests.exceptions.RequestException:
            return "Erro ao adicionar carro", 400
    return redirect(url_for("index"))

@app.route("/delete_carro/<int:id>", methods=["GET"])
def delete_carro(id):
    try:
        res = requests.delete(f"{API_BASE}/deletCarro/{id}")
    except requests.exceptions.RequestException:
        return "Erro ao deletar carro", 400
    return redirect(url_for("index"))

@app.route("/api_test", methods=["GET"])
def api_test():
    try:
        res = requests.get(f"{API_BASE}/test")
        if res.status_code == 200:
            return "API de teste OK!"
        return f"API de teste retornou status {res.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API: {e}"

@app.route("/consulta_cep", methods=["GET", "POST"])
def consulta_cep():
    resultado = None
    if request.method == "POST":
        cep = request.form.get("cep")
        if cep:
            try:
                res = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
                if res.status_code == 200:
                    resultado = res.json()
                else:
                    resultado = {"erro": f"Status {res.status_code}"}
            except requests.exceptions.RequestException as e:
                resultado = {"erro": str(e)}
    carros = listar_carros()  # Mantém a lista de carros no template
    return render_template("index.html", carros=carros, cep_resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
