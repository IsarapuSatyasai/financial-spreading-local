# Financial Spreading - Local Version

Local, runnable version of the LangGraph financial spreading workflow.
Uses standard OpenAI (`ChatOpenAI`) instead of Azure. No Databricks dependencies.

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-...
   ```
4. Place your files:
   - Annual report PDF → `data/input/annual_report.pdf`
   - CreditLens Excel template → `data/templates/creditlens_template.xlsx`

## Run

Open and run `financial_spreading_test_run.ipynb` (or execute the cells).

Output Excel will be written to `data/output/`.

## Structure

See the folder layout in the repository.
