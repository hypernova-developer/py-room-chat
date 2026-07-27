# Contributing to Network Chat System

First off, thank you for considering contributing to this project! Contributions like yours are what make open-source software such an incredible space to learn, inspire, and create.

Please take a moment to review this document to keep the project structured, clean, and easy to maintain.

---

## 🛠️ How Can You Contribute?

### 1. Reporting Bugs
If you find a bug or unexpected behavior while running the server or client:
* Check existing issues to see if it has already been reported.
* If not, open a new issue describing:
  * What you expected to happen vs. what actually happened.
  * Steps to reproduce the issue.
  * Your operating system and Python version.

### 2. Suggesting Features
Got ideas to improve the room management, socket handling, or UI?
* Open an issue with the tag `enhancement`.
* Explain clearly why this feature would be useful and how it should work.

### 3. Pull Requests
We welcome Pull Requests for bug fixes, code refactoring, and new feature additions!

---

## 🚀 Getting Started with Development

### Prerequisites
* **Python 3.8+** installed on your system.
* Standard Python libraries (`socket`, `threading`, `datetime`, `random`, `os`).

### Setup Local Environment
1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/PROJECT_NAME.git](https://github.com/YOUR_USERNAME/PROJECT_NAME.git)
   cd PROJECT_NAME

```

3. Create a new feature branch for your changes:
```bash
git checkout -b feature/your-feature-name

```



---

## 📋 Code Conventions & Best Practices

To keep the codebase clean and maintainable, please follow these guidelines:

* **Type Hints:** Use explicit Python type annotations (e.g., `def create_room(room_id: str) -> Room:`).
* **Thread Safety:** Always utilize `threading.Lock()` when mutating global states like `connections` or shared `Room` objects to avoid race conditions.
* **Error Handling:** Ensure network sockets clean up properly (`conn.close()`) in case of unexpected disconnects or protocol exceptions.
* **Clean Code:** Write readable, self-documenting code. Avoid adding unnecessary comments.

---

## 📥 Submitting a Pull Request (PR)

1. Commit your changes locally with clear commit messages:
```bash
git commit -m "Add room authorization validation logic"

```


2. Push your changes to your fork:
```bash
git push origin feature/your-feature-name

```


3. Open a **Pull Request** against the `main` branch of the original repository.
4. Describe your changes clearly in the PR description and link any relevant issues.

Thank you for your contributions! ⚡
