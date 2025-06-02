# 🔍 Research Assistant Using CrewAI
- A powerful research assistant built with CrewAI, Exa, and Streamlit that helps you research any topic using AI Agents.

![App Screenshot](./assets/frontend.png)

---

# 🌟 Features

- 🤖 Multiple LLM Support
- 🔍 Advanced answering capabilities using Exa
- 📊 Real-time research process visualization
- 📝 Structured research reports
- 🎯 Topic-focused research and analysis
- 🔒 Secure API key management
- 📱 Responsive and modern UI

---
# 🏗️ Architecture
research-assistant/
│
├── app.py
├── .env
├── requirements.txt
├── pyproject.toml
│
├── .streamlit/
│   └── secrets.toml
│
├── assets/
│   └── (your static files go here)
│
├── experiment/
│   └── run.py
│
├── src/
│   ├── __init__.py
│   ├── crew.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   └── agent.py
│   │
│   ├── llms/
│   │   ├── __init__.py
│   │   └── init_llms.py
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   └── task.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── custum_tool.py
│   │
│   ├── UI/
│   │   ├── __init__.py
│   │   └── sidebar.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── output_handler.py

---

# ⚙️ Installing Dependencies

### Create Virtual Python-3.12 Environment
```bash
uv venv --python 3.12
```

### Activating the Virtual Environment 

- macOS/Linux
```bash
source .venv/bin/activate
```

- Windows (PowerShell)

```bash
.venv\Scripts\Activate
```
---


### Single Packages
```bash
uv pip install <package_name>
```

### From a requirements.txt File
```bash
uv pip install -r requirements.txt
```
---

### To recreate your environment elsewhere (e.g. on CI or another machine), install exactly what’s in the lockfile:

```bash
uv sync
```
---

### To capture the exact versions of all installed packages, generate a lockfile:
```bash
uv lock
```

--- 

# 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# 🙏 Acknowledgments

- [CrewAI](https://crewai.com) for the AI agent framework
- [Exa](https://exa.ai) for advanced search capabilities
- [Streamlit](https://streamlit.io) for the web interface

---

Made by Dhruv Saxena using CrewAI, Exa, and Streamlit
