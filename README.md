# 💬 Py-Room-Chat

A lightweight, multi-threaded TCP socket chat server and client application built in Python using native socket and threading libraries.

This project demonstrates low-level network programming, concurrent connection handling, thread-safe message broadcasting, and room-based access control.

---

## 🌟 Key Features

* **Room Management:** Dynamic creation of individual chat rooms with custom IDs.
* **Password Protection:** Secure private rooms with room-level password authentication.
* **Multi-threading:** Non-blocking architecture handling multiple client connections simultaneously.
* **Thread Safety:** Implements `threading.Lock()` to prevent race conditions during state mutation and broadcasting.
* **Console UI Refresher:** Clean terminal output rendering on the client side using ANSI escape codes.
* **Automated Logging:** Saves activity logs for the server and isolated chat histories per room in the `logs/` directory.

---

## 📁 Repository Structure

```text
py-room-chat/
├── .gitignore
├── README.md
└── src/
    ├── server.py
    └── client.py
```

## 🚀 Getting Started
Prerequisites

    Python 3.8 or higher installed on your machine.
    No external third-party dependencies required (uses built-in Python standard libraries).

Running the Server
    Open your terminal and navigate to the project root directory.
    Run the server script:
    Bash
    python src/server.py
    The server will start listening on port 40000 by default.

Running the Client
    Open a new terminal instance.
    (Optional) Update the SERVER_IP variable inside src/client.py if running across different devices on a local network.
    Launch the client application:

    Bash
    python src/client.py
    Follow the on-screen prompts to enter your nickname, room ID, and password.

## 🔒 Protocol & Handshake Flow
    Authentication: Client sends a fixed 16-byte nickname to the server.
    Room Request: Client sends room ID (16 bytes) and password (16 bytes).
    Validation:
        If the room exists and the password matches -> Connection is granted (OK).
        If the room does not exist -> Server responds with NO. The client can choose to issue a create signal (CRT) to spin up a new room dynamically.
    Chat Loop: Once connected, messages are broadcasted to all other active members in the room in real time.

## 📜 Commands (Client Side)
    /exit, /quit, or /q — Safely disconnect from the chat room and terminate the client session.


🚧 Upcoming Updates & Roadmap
    [ ] Byte-Level Padding Fix: Transition from string formatting to byte-array padding to safely support multi-byte UTF-8 characters.
    [ ] Enhanced Status Codes: Granular error handling (WRONG_PASS vs NOT_FOUND) during authentication.
    [ ] TLS/SSL Encryption: Add secure socket wrapping for encrypted client-server traffic.
