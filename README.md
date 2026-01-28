# GitHub Webhook Listener (webhook-repo)

This repository contains a Flask application that listens to GitHub webhook events from another repository (`action-repo`) and displays the latest changes in a live UI.

---

## Features

- Captures **PUSH** events
- Captures **PULL REQUEST** events
- Detects **MERGE** events via `pull_request` payload (`merged: true`)
- Stores all events in **MongoDB**
- UI polls MongoDB every 15 seconds to display the latest events
- Minimal, clean, and functional UI

---

## Repositories

1. **action-repo**: Dummy repository used to trigger GitHub events via webhooks.  
   _All push, pull request, and merge events occur here._  

   Link: `https://github.com/mollika39/action-repo`

2. **webhook-repo**: This repository contains the backend Flask code, MongoDB logic, and UI to display events.  

   Link: `https://github.com/mollika39/webhook-repo`

---

## Project Structure
webhook-repo/
├─ app.py # Flask backend and webhook endpoint
├─ requirements.txt # Python dependencies
├─ templates/
│ └─ index.html # UI page
└─ static/
└─ script.js # JS polling /events endpoint
└─ README.md # This file


---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/webhook-repo.git
   cd webhook-repo
2. **Install dependencies**
   pip install -r requirements.txt
3. **Run Flask Server**
   python app.py
4. **Expose your local server to the internet** (optional for testing with GitHub Webhooks)
    ngrok http 5000

