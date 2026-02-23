from flask import Flask, request, render_template_string

app = Flask(__name__)

# -----------------------------
# Adaptive Logic Function
# -----------------------------
def generate_explanation(topic, level):
    topic = topic.lower()

    if level == "Beginner":
        return f"""
        {topic.capitalize()} is a fundamental concept used in modern software systems.
        At the beginner level, the focus is on understanding what it is,
        why it is important, and where it is commonly used.
        Simple examples and practical demonstrations help build clarity.
        """

    elif level == "Intermediate":
        return f"""
        {topic.capitalize()} plays an important role in application design.
        At the intermediate level, we examine internal mechanisms,
        architectural patterns, implementation strategies,
        and real-world use cases.
        We also consider efficiency and modular structuring.
        """

    elif level == "Advanced":
        return f"""
        {topic.capitalize()} involves deep theoretical foundations,
        optimization strategies, scalability considerations,
        security layers, and production-level configurations.
        Advanced understanding includes performance tuning,
        system integration, and architectural trade-offs.
        """

    else:
        return "Invalid level selected."


# -----------------------------
# Single Route (GET + POST)
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    explanation = None
    error = None

    try:
        if request.method == "POST":
            topic = request.form.get("topic")
            level = request.form.get("level")

            if not topic or not level:
                error = "Both topic and level are required."
            else:
                explanation = generate_explanation(topic, level)

    except Exception:
        error = "Internal server error occurred."

    # -----------------------------
    # Embedded HTML Template
    # -----------------------------
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SAARTHI</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f4f6f9;
                text-align: center;
                padding: 40px;
            }

            .container {
                background: white;
                padding: 30px;
                width: 60%;
                margin: auto;
                border-radius: 8px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            }

            input, select {
                padding: 10px;
                width: 60%;
                margin: 10px;
            }

            button {
                padding: 10px 20px;
                background-color: #2c3e50;
                color: white;
                border: none;
                cursor: pointer;
            }

            .result {
                margin-top: 20px;
                text-align: left;
                padding: 15px;
                background: #ecf0f1;
                border-radius: 6px;
            }

            .error {
                color: red;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>SAARTHI</h1>

            <form method="POST">
                <input type="text" name="topic" placeholder="Enter Topic"><br>

                <select name="level">
                    <option value="">Select Level</option>
                    <option value="Beginner">Beginner</option>
                    <option value="Intermediate">Intermediate</option>
                    <option value="Advanced">Advanced</option>
                </select><br>

                <button type="submit">Generate</button>
            </form>

            {% if error %}
                <p class="error">{{ error }}</p>
            {% endif %}

            {% if explanation %}
                <div class="result">
                    <h3>Explanation:</h3>
                    <p>{{ explanation }}</p>
                </div>
            {% endif %}
        </div>

    </body>
    </html>
    """, explanation=explanation, error=error)


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)