from app import app
 
 
@app.route("/")
def index():
    return "Hello word!"

@app.route("/test", defaults={'name': None})
@app.route("/test/<name>") 
def test(name):
   if name:
      return f"Olá, {name} !"   
   else:
      return "Olá, usuário !"


