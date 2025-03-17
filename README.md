# agentic_ai
<!-- streamlit -->
1. pip install streamlit
2. pip install -U pip setuptools wheel
3. pip install -U spacy
4. streamlit run app.py

<!-- ollama install -->
1. https://ollama.com/download 
2. ollama run llama3.2 - Excels in multilingual text processing
3. control + d to exit chat
4. ollama run deepseek-r1:7b - focus on reasoning tasks, it excels in mathematical problem-solving and code generation
5. control + d to exit chat

<!-- install packages -->
1. conda create -n agenticAI python=3.10.0
2. conda activate agenticAI
3. pip install 'crewai[tools]'
4. conda install -n agenticAI ipykernel --update-deps --force-reinstall
5. pip install databathing
6. pip install sqlite-utils



<!-- crewai project -->
1. crewai create crew DataAssistant
