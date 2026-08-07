from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        service = request.form["service"]

        with open("leads.txt", "a", encoding="utf-8") as file:
            file.write(f"{name} - {service}\n")

        return "Request received! Thank you."

    return """
    <h1>Request a Service</h1>
    <form method="post">
        Name:<br>
        <input name="name"><br><br>
        Service needed:<br>
        <input name="service"><br><br>
        <button type="submit">Send Request</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

