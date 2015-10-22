from eo import app

@app.route('/')
def index():
  return "<h1>Funcionou Novamente</h1>"
