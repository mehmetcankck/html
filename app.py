
from flask import Flask, render_template, request
import random

app = Flask(__name__)

matches = [
    {"home": "Barcelona", "away": "Real Madrid"},
    {"home": "Liverpool", "away": "Manchester United"},
    {"home": "Bayern Munich", "away": "Dortmund"},
    {"home": "PSG", "away": "Marseille"},
    {"home": "Juventus", "away": "AC Milan"},
    {"home": "Chelsea", "away": "Arsenal"},
    {"home": "Inter Milan", "away": "Napoli"},
    {"home": "Atletico Madrid", "away": "Sevilla"},
]

def generate_odds():
    return {
        match["home"]: round(random.uniform(1.5, 3.0), 2),
        match["away"]: round(random.uniform(1.5, 3.0), 2),
        "Draw": round(random.uniform(2.0, 3.5), 2)
    }

odds = {i: generate_odds() for i in range(len(matches))}
real_results = [random.choice([match["home"], match["away"], "Draw"]) for match in matches]

@app.route("/", methods=["GET", "POST"])
def index():
    winnings = 0
    if request.method == "POST":
        user_bet = [request.form.get(f"bet{i}") for i in range(8)]
        stake = float(request.form["stake"])
        correct_bets = sum(1 for i in range(8) if user_bet[i] == real_results[i])
        if correct_bets == 8:
            winnings = stake * 10

    return render_template("index.html", matches=matches, odds=odds, winnings=winnings)

if __name__ == "__main__":
    app.run(debug=True)
