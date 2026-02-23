from flask import Flask, request, render_template_string
import requests,os

app = Flask(__name__)

API_KEY =os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"


def generate_explanation(topic, level):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.3-70b-versatile",  
            "messages": [
                {
                    "role": "system",
                    "content": "You are SAARTHI, an AI Study Coach. Give clear, structured, student-friendly explanations."
                },
                {
                    "role": "user",
                    "content": f"""Topic: {topic}
Level: {level}

Provide a structured explanation with:
1. Simple Definition
2. Key Concepts
3. Real-World Example
4. Tips to Remember"""
                }
            ],
            "max_tokens": 1024,
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=headers, json=data, timeout=30)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        elif response.status_code == 401:
            return "Error 401: Invalid Groq API key. Get a free one at https://console.groq.com"
        elif response.status_code == 429:
            return "Error 429: Rate limit. Wait a few seconds and try again."
        else:
            return f"API error ({response.status_code}): {response.text}"

    except Exception as e:
        return f"Request failed: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def home():
    explanation = None
    error = None

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        level = request.form.get("level", "").strip()

        if not topic or not level:
            error = "Both topic and level are required."
        else:
            explanation = generate_explanation(topic, level)

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SAARTHI - AI Study Coach</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: Arial, sans-serif; background-color: #f4f6f9; text-align: center; padding: 40px 20px; }
            h1 { font-size: 2rem; color: #2c3e50; margin-bottom: 5px; }
            .subtitle { color: #7f8c8d; margin-bottom: 25px; font-size: 0.95rem; }
            .container { background: white; padding: 35px 30px; width: 60%; margin: auto; border-radius: 10px; box-shadow: 0px 4px 16px rgba(0,0,0,0.1); }
            input[type="text"] { padding: 10px 14px; width: 70%; margin: 8px 0; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; }
            input[type="text"]:focus { outline: none; border-color: #2c3e50; }
            select { padding: 10px 14px; width: 70%; margin: 8px 0; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem; background: white; }
            button { margin-top: 14px; padding: 11px 30px; background-color: #2c3e50; color: white; border: none; border-radius: 6px; font-size: 1rem; cursor: pointer; }
            button:hover { background-color: #3d5166; }
            .result { margin-top: 25px; text-align: left; padding: 18px 20px; background: #ecf0f1; border-radius: 8px; white-space: pre-wrap; line-height: 1.6; font-size: 0.97rem; color: #2c3e50; }
            .result h3 { margin-bottom: 10px; }
            .error-box { margin-top: 16px; padding: 12px 16px; background: #fdecea; border: 1px solid #f5c6cb; border-radius: 6px; color: #c0392b; }
            .notice { background: #eaf4fb; border: 1px solid #aed6f1; border-radius: 6px; padding: 10px; margin-bottom: 20px; font-size: 0.85rem; color: #1a5276; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>SAARTHI</h1>
            <p class="subtitle">Your AI-Powered Study Coach</p>
            <div class="notice">⚡ Powered by Groq — Free & Fast AI</div>
            <form method="POST">
                <input type="text" name="topic" placeholder="Enter a topic (e.g. Photosynthesis)" required><br>
                <select name="level" required>
                    <option value="">Select Level</option>
                    <option value="Beginner">Beginner</option>
                    <option value="Intermediate">Intermediate</option>
                    <option value="Advanced">Advanced</option>
                </select><br>
                <button type="submit">Generate Explanation</button>
            </form>
            {% if error %}
                <div class="error-box">⚠️ {{ error }}</div>
            {% endif %}
            {% if explanation %}
                <div class="result">
                    <h3>📘 Explanation:</h3>
                    {{ explanation }}
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    """, explanation=explanation, error=error)


if __name__ == "__main__":
    app.run(debug=True)