
#  **Ollama Setup Guide for Hiring Assistant**

## *What is Ollama*?

Ollama is a local LLM server that allows you to run large language models on your own machine without needing external API keys or internet connectivity.

##  **Quick Setup**

### 1. *Install Ollama*

*Windows:*
```bash
# Download from https://ollama.ai/download
# Or use winget:
winget install Ollama.Ollama
```

*macOS:*
```bash
# Download from https://ollama.ai/download
# Or use Homebrew:
brew install ollama
```

*Linux:*
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. **Start Ollama**

```bash
ollama serve
```

### 3. **Pull a Model**

Choose one of these models (recommended in order):

```bash
# Option 1: Llama2 (7B parameters, good balance)
ollama pull llama2

# Option 2: Mistral (7B parameters, excellent performance)
ollama pull mistral

# Option 3: CodeLlama (specialized for code)
ollama pull codellama

# Option 4: Llama2 (13B parameters, better quality but slower)
ollama pull llama2:13b
```

### 4. Verify Installation

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Test a model
ollama run llama2 "Hello, how are you?"
```

## **Model Recommendations**

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| `llama2` | 7B | Fast | Good | General use |
| `mistral` | 7B | Fast | Excellent | Best overall |
| `codellama` | 7B | Fast | Good | Technical questions |
| `llama2:13b` | 13B | Slower | Better | Higher quality |

##  **Configuration**

The application is configured to use `llama2` by default. To change the model:

1. Edit `config.py`
2. Change the `OPENAI_MODEL` variable:
   ```python
   OPENAI_MODEL = "mistral"  # or "codellama", "llama2:13b", etc.
   ```

## **Running the Application**

1. *Start Ollama:*
   ```bash
   ollama serve
   ```

2. *Install Python dependencies:*
   ```bash
   pip install -r requirements.txt
   ```

3. *Run the application:*
   ```bash
   streamlit run app.py
   ```

##  Benefits of Local LLMs

###  **Advantages:**
- *No API costs* - Completely free to use
- *Privacy* - All data stays on your machine
- *Offline* - Works without internet connection
- *No rate limits* - Use as much as you want
- *Customizable* - Fine-tune models for your needs

###  **Considerations:**
- *Hardware requirements* - Needs decent RAM and CPU/GPU
- *Model quality* - May be slightly lower than cloud models
- *Setup time* - Initial download and setup required

##  **System Requirements**

### **Minimum Requirements:**
- *RAM:* 8GB (16GB recommended)
- *Storage:* 4GB free space
- *CPU:* Modern multi-core processor
- *OS:* Windows 10+, macOS 10.15+, or Linux

### **Recommended Requirements:**
- *RAM:* 16GB or more
- *GPU:* NVIDIA GPU with 8GB+ VRAM (optional but recommended)
- *Storage:* SSD with 10GB+ free space

##  **Troubleshooting**

### *Common Issues*:

1. *"Cannot connect to Ollama"*
```bash
# Check if Ollama is running
ollama serve

# Check if port 11434 is available
netstat -an | grep 11434
```

2. *"Model not found"*
```bash
# List available models
ollama list

# Pull the model again
ollama pull llama2
```

3. *"Out of memory"*
- Try a smaller model: `ollama pull llama2:7b`
- Close other applications
- Increase system RAM

4. *"Slow responses"*
- Use a smaller model
- Ensure you have enough RAM
- Consider using a GPU (if available)

##  Success!

Once Ollama is running and you've pulled a model, the TalentScout Hiring Assistant will work completely offline with no external dependencies!

##  Additional Resources

- [Ollama Documentation](https://ollama.ai/docs)
- [Model Library](https://ollama.ai/library)
- [Community Models](https://ollama.ai/library?sort=newest)
=======
#  **Ollama Setup Guide for Hiring Assistant**

## *What is Ollama*?

Ollama is a local LLM server that allows you to run large language models on your own machine without needing external API keys or internet connectivity.

##  **Quick Setup**

### 1. *Install Ollama*

*Windows:*
```bash
# Download from https://ollama.ai/download
# Or use winget:
winget install Ollama.Ollama
```

*macOS:*
```bash
# Download from https://ollama.ai/download
# Or use Homebrew:
brew install ollama
```

*Linux:*
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. **Start Ollama**

```bash
ollama serve
```

### 3. **Pull a Model**

Choose one of these models (recommended in order):

```bash
# Option 1: Llama2 (7B parameters, good balance)
ollama pull llama2

# Option 2: Mistral (7B parameters, excellent performance)
ollama pull mistral

# Option 3: CodeLlama (specialized for code)
ollama pull codellama

# Option 4: Llama2 (13B parameters, better quality but slower)
ollama pull llama2:13b
```

### 4. Verify Installation

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Test a model
ollama run llama2 "Hello, how are you?"
```

## **Model Recommendations**

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| `llama2` | 7B | Fast | Good | General use |
| `mistral` | 7B | Fast | Excellent | Best overall |
| `codellama` | 7B | Fast | Good | Technical questions |
| `llama2:13b` | 13B | Slower | Better | Higher quality |

##  **Configuration**

The application is configured to use `llama2` by default. To change the model:

1. Edit `config.py`
2. Change the `OPENAI_MODEL` variable:
   ```python
   OPENAI_MODEL = "mistral"  # or "codellama", "llama2:13b", etc.
   ```

## **Running the Application**

1. *Start Ollama:*
   ```bash
   ollama serve
   ```

2. *Install Python dependencies:*
   ```bash
   pip install -r requirements.txt
   ```

3. *Run the application:*
   ```bash
   streamlit run app.py
   ```

##  Benefits of Local LLMs

###  **Advantages:**
- *No API costs* - Completely free to use
- *Privacy* - All data stays on your machine
- *Offline* - Works without internet connection
- *No rate limits* - Use as much as you want
- *Customizable* - Fine-tune models for your needs

###  **Considerations:**
- *Hardware requirements* - Needs decent RAM and CPU/GPU
- *Model quality* - May be slightly lower than cloud models
- *Setup time* - Initial download and setup required

##  **System Requirements**

### **Minimum Requirements:**
- *RAM:* 8GB (16GB recommended)
- *Storage:* 4GB free space
- *CPU:* Modern multi-core processor
- *OS:* Windows 10+, macOS 10.15+, or Linux

### **Recommended Requirements:**
- *RAM:* 16GB or more
- *GPU:* NVIDIA GPU with 8GB+ VRAM (optional but recommended)
- *Storage:* SSD with 10GB+ free space

##  **Troubleshooting**

### *Common Issues*:

1. *"Cannot connect to Ollama"*
```bash
# Check if Ollama is running
ollama serve

# Check if port 11434 is available
netstat -an | grep 11434
```

2. *"Model not found"*
```bash
# List available models
ollama list

# Pull the model again
ollama pull llama2
```

3. *"Out of memory"*
- Try a smaller model: `ollama pull llama2:7b`
- Close other applications
- Increase system RAM

4. *"Slow responses"*
- Use a smaller model
- Ensure you have enough RAM
- Consider using a GPU (if available)

##  Success!

Once Ollama is running and you've pulled a model, the TalentScout Hiring Assistant will work completely offline with no external dependencies!

##  Additional Resources

- [Ollama Documentation](https://ollama.ai/docs)
- [Model Library](https://ollama.ai/library)
- [Community Models](https://ollama.ai/library?sort=newest)
>>>>>>> a431973a36876c8ecd0f0f8a507c1f34b563384c
- [Performance Tips](https://ollama.ai/docs/advanced/performance) 