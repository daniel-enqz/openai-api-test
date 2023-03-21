import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name),
            temperature=0.7,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name):
    return """Suggest three anime names for the given person name.
 Name: Daniel
 Names: ShangDanielChi, DaniPo, YiwitoDaniel
 Name: Edgar
 Names: EdgarAstroBoy, EdgarKenshin, AckerEdgarMan
 Name: John
 Names: YagamiJohn, JohnShin, JohnKusanagi
 Name: {}
 Names:""".format(
         name.capitalize()
    )
