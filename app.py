from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from dateutil import parser

app = Flask(__name__)

# MongoDB connection (replace with your Atlas URI)
client = MongoClient("mongodb+srv://github:dasmodonjoli2001@cluster0.jsmmdxp.mongodb.net/?appName=Cluster0")
db = client.github_events
collection = db.events


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")

    event = {}

    try:
        if event_type == "push":
            event = {
                "type": "PUSH",
                "author": data["pusher"]["name"],
                "from_branch": None,
                "to_branch": data["ref"].split("/")[-1],
                "timestamp": parser.parse(data["head_commit"]["timestamp"])
            }

        elif event_type == "pull_request":
            pr = data["pull_request"]

            # MERGE EVENT
            if pr.get("merged") is True:
                    event = {
                    "type": "MERGE",
                    "author": pr["merged_by"]["login"] if pr.get("merged_by") else pr["user"]["login"],
                    "from_branch": pr["head"]["ref"],
                    "to_branch": pr["base"]["ref"],
                    "timestamp": parser.parse(pr["merged_at"])
                    }

    # PULL REQUEST CREATED
            else:
                event = {
                "type": "PULL_REQUEST",
                "author": pr["user"]["login"],
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": parser.parse(pr["created_at"])
                }


        if event:
            collection.insert_one(event)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/events")
def get_events():
    # Fetch only latest 15 seconds data
    fifteen_sec_ago = datetime.utcnow().timestamp() - 15

    events = collection.find({
        "timestamp": {"$gte": datetime.fromtimestamp(fifteen_sec_ago)}
    }).sort("timestamp", -1)

    response = []
    for e in events:
        response.append({
            "type": e["type"],
            "author": e["author"],
            "from_branch": e.get("from_branch"),
            "to_branch": e.get("to_branch"),
            "timestamp": e["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")
        })

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
