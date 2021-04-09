from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def test():
    return render_template("test.html", value="123")

if __name__ == "__main__":
    app.run()
