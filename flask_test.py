from flask import Flask, render_template, request

app = Flask("ma_superbe_application")

@app.route('/coucou', methods=['GET']) #décorateur qui dit que la fonction hello_world doit être executée quand on a une requête /coucou
def hello_world():


    return "coucou"

if __name__== "__main__":
    app.run('0.0.0.0')