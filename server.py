"""用于产生web应用"""
import webbrowser
from flask import Flask, render_template
from pyscript_list_generator import Generator

app = Flask(__name__)
generator = Generator()


@app.route('/')
def index():
    return render_template('main.html', page_title="pyscript_list", pyscript_list=generator.pyscript_list)


@app.route('/<pyscript>')
def function(pyscript):
    pyscript_function = generator.generator_pyscript(pyscript)
    if pyscript_function == 'EOF':
        return render_template('error404.html', url=pyscript)
    return render_template('main.html', page_title="pyscript_list",
                           pyscript_list=pyscript_function)


if __name__ == "__main__":
    webbrowser.open_new_tab("http://127.0.0.1:5000")
    app.run(debug="true")
