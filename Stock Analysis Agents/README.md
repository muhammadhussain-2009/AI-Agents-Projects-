# Stock Analysis Agents

A powerful AI-driven stock analysis system built with **CrewAI**, leveraging multi-agent collaboration to provide comprehensive stock market insights and analysis.

## 📋 Table of Contents

- [About CrewAI Framework](#about-crewai-framework)
- [Installation Guidelines](#installation-guidelines)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Contribution Guidelines](#contribution-guidelines)

## 🤖 About CrewAI Framework

**CrewAI** is a framework for orchestrating role-playing autonomous AI agents. It enables you to create a crew of specialized agents that collaborate to accomplish complex tasks.

### Key Features:

- **Agent Collaboration**: Multiple AI agents work together, each with specialized roles and skills
- **Task Management**: Define and organize tasks that agents execute sequentially or in parallel
- **Memory & Context**: Agents maintain context and learn from previous interactions
- **Tool Integration**: Seamlessly integrate external APIs, databases, and tools
- **Flexible LLM Support**: Works with OpenAI's GPT models, open-source models via Ollama, and more

### How It Works in Stock Analysis:

In this project, we use CrewAI to create a team of specialized agents:
- **Stock Analyst Agent**: Researches and analyzes stock performance
- **Financial Advisor Agent**: Provides investment recommendations
- **Risk Assessment Agent**: Evaluates market risks and volatility
- **Report Writer Agent**: Compiles findings into comprehensive reports

These agents work together to deliver thorough stock analysis by combining their expertise.

---

## 💻 Installation Guidelines

### Prerequisites

- Python 3.10 or higher
- [UV Package Manager](https://docs.astral.sh/uv/)

### Step 1: Install UV

UV is a fast Python package installer and resolver. Install it using:

**On macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows (using PowerShell):**
```powershell
powershell -ExecutionPolicy BypassCurrentUser -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/muhammadhussain-2009/AI-Agents-Projects-.git
cd AI-Agents-Projects-
cd "Stock Analysis Agents"
```

### Step 3: Create Virtual Environment with UV

```bash
uv venv
```

Activate the virtual environment:

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
uv pip install -r requirements.txt
```

Or install specific packages:
```bash
uv pip install crewai langchain python-dotenv
```

---

## ⚙️ Configuration

### Option 1: Using GPT-3.5 (OpenAI)

#### Setup:

1. **Get your OpenAI API Key:**
   - Go to [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Copy the key

2. **Create a `.env` file** in the project root:
   ```bash
   touch .env
   ```

3. **Add your API key to `.env`:**
   ```env
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL_NAME=gpt-3.5-turbo
   ```

4. **Update `crewai_config.py` or your main script:**
   ```python
   from langchain_openai import ChatOpenAI
   
   llm = ChatOpenAI(
       model_name="gpt-3.5-turbo",
       temperature=0.7,
       api_key=os.getenv("OPENAI_API_KEY")
   )
   ```

#### Cost Considerations:
- GPT-3.5 is cost-effective and suitable for production use
- Monitor your API usage on the OpenAI dashboard

---

### Option 2: Using Local Models with Ollama

#### Setup:

1. **Install Ollama:**
   - Download from [Ollama Official Site](https://ollama.ai)
   - Follow platform-specific installation instructions

2. **Pull a Model:**
   ```bash
   ollama pull mistral
   # or
   ollama pull neural-chat
   ```

3. **Start Ollama Server:**
   ```bash
   ollama serve
   ```
   The server runs on `http://localhost:11434` by default

4. **Create a `.env` file** with Ollama configuration:
   ```env
   OLLAMA_MODEL_NAME=mistral
   OLLAMA_BASE_URL=http://localhost:11434
   ```

5. **Update your script to use Ollama:**
   ```python
   from langchain_ollama import ChatOllama
   
   llm = ChatOllama(
       model=os.getenv("OLLAMA_MODEL_NAME", "mistral"),
       base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
       temperature=0.7
   )
   ```

#### Recommended Models:
- **Mistral** (7B): Fast and efficient, good for general tasks
- **Neural Chat** (7B): Optimized for chat and analysis
- **Llama 2** (13B): More powerful, requires more resources

#### Advantages:
- ✅ Completely free
- ✅ Runs locally (no API calls)
- ✅ Privacy-preserving
- ✅ No rate limiting

#### Disadvantages:
- ⚠️ Requires significant computational resources
- ⚠️ Slower response times than cloud APIs
- ⚠️ Smaller models may have limited reasoning capacity

---

## 🚀 Running the Main Script

### Basic Execution:

```bash
python main.py
```

### With Command-Line Arguments:

```bash
python main.py --stock AAPL --mode analysis
```

### Example Usage:

```bash
# Analyze Apple stock
python main.py --stock AAPL

# Analyze Tesla with detailed report
python main.py --stock TSLA --detailed

# Compare multiple stocks
python main.py --stock AAPL MSFT GOOGL
```

### Expected Output:

```
🤖 Starting Stock Analysis Crew...
📊 Analyzing AAPL...
✅ Stock Analyst Agent: [Analysis complete]
📈 Financial Advisor Agent: [Recommendations ready]
⚠️  Risk Assessment Agent: [Risk evaluation complete]
📄 Report Writer Agent: [Report generated]

Final Report:
===============================
[Comprehensive stock analysis report]
===============================
```

### Output Files:

Results are typically saved to:
```
./reports/
├── analysis_AAPL_<timestamp>.txt
├── analysis_AAPL_<timestamp>.json
└── recommendations.md
```

### Troubleshooting:

**Issue: API Key Not Found**
```
Solution: Ensure .env file exists and OPENAI_API_KEY is set correctly
```

**Issue: Ollama Connection Error**
```
Solution: 
1. Ensure Ollama is running: ollama serve
2. Check URL is correct in .env (default: http://localhost:11434)
```

**Issue: Memory or Performance Issues**
```
Solution:
1. Use a smaller Ollama model (Mistral 7B instead of larger models)
2. Reduce batch size or limit analysis scope
3. Consider using GPT-3.5 for better performance
```

---

## 🤝 Contribution Guidelines

We welcome contributions! Follow these guidelines to help improve the project:

### Getting Started:

1. **Fork the repository**
   ```bash
   Click the "Fork" button on GitHub
   ```

2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Agents-Projects-.git
   cd AI-Agents-Projects-
   cd "Stock Analysis Agents"
   ```

3. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Development Workflow:

1. **Install development dependencies:**
   ```bash
   uv pip install -r requirements-dev.txt
   ```

2. **Make your changes:**
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Update docstrings for functions and classes

3. **Test your changes:**
   ```bash
   python -m pytest tests/
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add description of your feature"
   ```

   Follow conventional commits format:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `refactor:` for code refactoring
   - `test:` for tests

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request:**
   - Go to the original repository
   - Click "New Pull Request"
   - Describe your changes clearly
   - Link any related issues

### Code Standards:

- **Language**: Python 3.10+
- **Style Guide**: PEP 8
- **Type Hints**: Use type hints for function arguments and returns
- **Documentation**: Include docstrings for all functions and classes
- **Testing**: Write tests for new features

### Example Contribution Ideas:

- 🆕 Add new stock analysis agents (Sentiment Analysis, Dividend Analyst)
- 📊 Integrate additional data sources (Yahoo Finance, Alpha Vantage, Finnhub)
- 🎨 Improve report formatting and visualization
- 🐛 Bug fixes and performance improvements
- 📚 Documentation and examples
- 🧪 Additional test coverage

### Reporting Bugs:

If you find a bug, please:
1. Check if it's already reported in [Issues](https://github.com/muhammadhussain-2009/AI-Agents-Projects-/issues)
2. Create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs. actual behavior
   - Your environment details

### Contact & Questions:

- 📧 Create an issue for questions
- 💬 Discussions are welcome for feature ideas

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a star! ⭐

---

**Happy analyzing! 📈**
