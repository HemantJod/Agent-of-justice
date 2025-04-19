# Agent-of-justice 

Courtroom Simulation with Multi-Agent AI
========================================

An interactive courtroom trial simulator featuring AI agents representing a judge, defense, prosecution, plaintiff, defendant, and witness. Powered by large language models via Hugging Face.

--------------------------
Features
--------------------------
- Fully autonomous courtroom roleplay
- Modular agent architecture
- Based on real trial structure
- Easily extendable for new roles or trial types

--------------------------
Requirements
--------------------------
Run the following to install dependencies:

    pip install -r requirements.txt

Create a `.env` file using the template below and add your Hugging Face API token:

    HF_API_TOKEN=your_huggingface_api_token

--------------------------
Setup Instructions
--------------------------
Clone the repository and set up your environment:

    git clone https://github.com/yourname/courtroom-simulation.git
    cd courtroom-simulation
    cp .env.example .env

Install the dependencies:

    pip install -r requirements.txt

--------------------------
Running the Demo
--------------------------

**CLI Version:**

    python demo/cli_demo.py

**Notebook Version:**

    Open the file `demo/notebook_demo.ipynb` using Jupyter Notebook or any compatible IDE.


--------------------------
Sample Case & Output
--------------------------

**Input JSON Example:**

    {
      "title": "Trade Secret Theft",
      "summary": "John Doe is accused of stealing proprietary algorithms...",
      "evidence": ["server_logs", "resignation_letter"]
    }

**Output Snapshot (TXT):**

    ==== Opening Statements ====
    Prosecution:
    "As the Assistant District Attorney..."

    Defense:
    "My client, Mr. Doe, maintains his innocence..."

    Witness Testimony:
    "I saw no physical act of copying, but I did notice..."

    Judge's Verdict:
    "Based on the evidence presented..."

--------------------------
Architecture Overview
--------------------------

- CourtAgent: A wrapper class around Hugging Face's InferenceClient
- System Prompts: Guides behavior for each courtroom role
- Prompt Format: Structured messages using role-based tags
- AI Model: Default is 'microsoft/Phi-3-mini-4k-instruct' (can be changed)
