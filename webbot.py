
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        service = request.form.get("service", "").strip()
        details = request.form.get("details", "").strip()

        with open("leads.txt", "a", encoding="utf-8") as file:
            file.write(
                f"Name: {name} | Email: {email} | "
                f"Service: {service} | Details: {details}\n"
            )

        return """
        <html>
        <body style="font-family:Arial;text-align:center;padding:50px">
            <h1>Request Received!</h1>
            <p>Thanks for contacting us. We'll review your project and get back to you.</p>
            <a href="/">Submit another request</a>
        </body>
        </html>
        """

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Freelance Services</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 600px;
                margin: 30px auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,.1);
            }
            h1 { margin-top: 0; }
            input, select, textarea, button {
                width: 100%;
                box-sizing: border-box;
                padding: 12px;
                margin: 8px 0 18px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 16px;
            }
            textarea { min-height: 120px; }
            button {
                background: #111;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Freelance Services</h1>
            <p>Tell us what you need and we'll get back to you with a quote.</p>

            <form method="post">
                <label>Name</label>
                <input name="name" required>

                <label>Email</label>
                <input type="email" name="email" required>

                <label>Service</label>
                <select name="service" required>
                    <option value="">Choose a service</option>
                    <option>Logo Design</option>
                    <option>Social Media Content</option>
                    <option>Writing</option>
                    <option>Website Help</option>
                    <option>Other</option>
                </select>

                <label>Project Details</label>
                <textarea name="details" required
                    placeholder="Tell us what you need..."></textarea>

                <button type="submit">Request a Quote</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

