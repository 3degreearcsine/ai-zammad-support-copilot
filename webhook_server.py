from flask import Flask, request, jsonify
from ai_analyzer import analyze_ticket
from zammad_client import add_note

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.json

    try:
        ticket = data.get("ticket", {})
        ticket_id = ticket.get("id")
        title = ticket.get("title")

        print(f"Received ticket {ticket_id}: {title}")

        analysis = analyze_ticket(title)

        note = f"""
        🤖🧠 AI Analysis (Auto-triggered):

        {analysis}
        """

        add_note(ticket_id, note)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000)
