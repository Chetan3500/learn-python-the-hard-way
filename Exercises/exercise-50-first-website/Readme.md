# First website

Create a first website using `flask` framework. Framework means some pkg that make it easier to me to do something.

```sh
$ sudo pip install flask
```


## Exercise
1. Create some dir and files:
    ```sh
    mkdir -p gothon/{bin,gothonweb,tests,docs,templates}
    touch gothon/gothonweb/__init__.py gothon/tests/__init__.py
    ```
2. Create an app.py in gothon dir and write the following:
```py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    return render_template("index.html", greeting = greeting)

if __name__ == "__main__":
    app.run()
```
3. Prepare an index.html file in gothon/templates:
    ```html
    <html>
            <head>
                    <title>Gothons Of Planet Percal #25</title>
            </head>
            <body>
                    {% if greeting %}
                            I just wanteed to say <em style="color: green; font-size: 2em;">{{ greeting }}</em>
                    {% else %}
                            <em>Hello</em>, world!
                    {% endif %}
            </body>
    </html>
    ```
4. Start terminal in venv:
    ```sh
    $ . ~/.venvs/lpthw/bin/activate
    ```
5. Run Script:
    ```sh
    (lpthw) $ python app.py
    ```
6. Get the link and load it on browser.

## Note

1. More to know about flask check: https://flask.palletsprojects.com/en/stable/
2. To know about template: https://jinja.palletsprojects.com/en/stable/templates/

