# James AI Roadmap Chatbot

A simple AI chatbot web application built with Flask that provides AI learning roadmaps. The backend is powered by Python and integrated with the Groq AI API. The frontend is served via Flask templates.

---

## Features

- Conversational AI chatbot interface
- Dark and light mode themes with animations
- Download chat history as PDF
- Responsive design for desktop and mobile
- Hosted on Render for free 24/7 uptime

---

## Project Structure

```

├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend HTML template
├── static/
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
└── README.md               # Project documentation

````

---

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- Groq AI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-roadmap-chatbot.git
   cd ai-roadmap-chatbot
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
````
3. Set environment variable for API key (Linux/macOS):

   ```bash
   export GROQ_API_KEY="your_api_key_here"
   ```

   On Windows (PowerShell):

   ```powershell
   setx GROQ_API_KEY "your_api_key_here"
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://localhost:10000` (or the port specified in `app.py`).

---

## Deployment

This app is configured to deploy on [Render](https://render.com):

* Build Command: `pip install -r requirements.txt`
* Start Command: `python app.py`
* Environment Variable: `GROQ_API_KEY`

---

## Usage

* Start chatting with the AI chatbot on the homepage.
* Choose AI domains to get customized learning roadmaps.
* Download your chat history as PDF.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

## License

This project is licensed under the MIT License.

---

## Contact

Naidu Rapeta - [Mail](mailto:rapetanaidu478@gmail.com)
Project Link: [https://github.com/yourusername/ai-roadmap-chatbot](https://github.com/naidu2342/ai-roadmap-chatbot)

```
```
