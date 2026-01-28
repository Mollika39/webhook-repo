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

   Link: `https://github.com/<your-username>/action-repo`

2. **webhook-repo**: This repository contains the backend Flask code, MongoDB logic, and UI to display events.  

   Link: `https://github.com/<your-username>/webhook-repo`

---

## Project Structure

