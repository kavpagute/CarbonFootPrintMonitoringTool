from flask import Flask, render_template, request
import sqlite3
import computations
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    carbondata = query_carbonfootprint()
    return render_template("home.html", carbondata = carbondata)

@app.route("/add", methods = ["GET", "POST"])
def add_carbon():
    if request.method == "GET":
        return render_template("add_carbondata.html")
    else:
        carbondetails = (
            request.form[""]
        )
        return render_template("add_success.html")
def query_carbonfootprint():
    conn = sqlite3.connect("Carbon.db")
    c = conn.cursor()
    c.execute("""
    SELECT * FROM carbonfootprint
    """)
    return c.fetchall()

if __name__ == "__main__":
    app.run()