from flask import Flask, jsonify
from efforts.agents import LawyerAgent
from flask_cors import CORS  # If frontend is on a different port

app = Flask(__name__)
CORS(app)

# Agent Definitions
prosecution = LawyerAgent("Prosecutor", """
You are Jordan Blake, the Assistant District Attorney.
Your job is to strongly present the case against the accused using facts and reasoning.
""")

defense = LawyerAgent("Defense", """
You are Alex Carter, the lead defense attorney.
Your job is to protect your client's rights and argue for their innocence.
""")

judge = LawyerAgent("Judge", """
You are the Honorable Judge Madison. Remain neutral and provide rulings based on what is presented in court.
""")

plaintiff = LawyerAgent("Plaintiff", """
You are Jamie Lee, the plaintiff. Tell the court your story and what injustice you faced.
""")

defendant = LawyerAgent("Defendant", """
You are Riley Brooks, the defendant. Defend yourself and tell your side of the story.
""")

@app.route("/trial/start", methods=["GET"])
def start_trial():
    trial_dialogue = []

    trial_dialogue.append({"role": "Judge", "message": judge.respond("The court is now in session.")})
    trial_dialogue.append({"role": "Prosecutor", "message": prosecution.respond("Please present your opening statement.")})
    trial_dialogue.append({"role": "Defense", "message": defense.respond("Please present your opening statement.")})
    trial_dialogue.append({"role": "Plaintiff", "message": plaintiff.respond("Tell us what happened.")})
    trial_dialogue.append({"role": "Defendant", "message": defendant.respond("How do you respond to the accusations?")})
    trial_dialogue.append({"role": "Judge", "message": judge.respond("Thank you. I will now give my ruling.")})

    return jsonify(trial_dialogue)

if __name__ == "__main__":
    app.run(debug=True)
