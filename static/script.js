async function renderEvents() {
  try {
    const res = await fetch("/events");
    const data = await res.json();

    const list = document.getElementById("events");
    list.innerHTML = "";

    data.forEach(e => {
      let text = "";

      if (e.type === "PUSH") {
        text = `${e.author} pushed to ${e.to_branch} on ${e.timestamp}`;
      } 
      else if (e.type === "PULL_REQUEST") {
        text = `${e.author} submitted a pull request from ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
      } 
      else if (e.type === "MERGE") {
        text = `${e.author} merged branch ${e.from_branch} to ${e.to_branch} on ${e.timestamp}`;
      }

      const li = document.createElement("li");
      li.innerText = text;
      list.appendChild(li);
    });
  } catch (err) {
    console.error("Failed to fetch events:", err);
  }
}

// run immediately
renderEvents();

// poll every 15 seconds
setInterval(renderEvents, 15000);
