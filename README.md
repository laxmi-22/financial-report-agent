# FinanceReportPipeline (ADK Project Template)

## Setup

1. Create a virtualenv: `python -m venv venv` & `source venv/bin/activate` (or on Windows `venv\Scripts\activate`)
2. `pip install -r requirements.txt`
3. Run the pipeline:
   `python main.py --ticker MSFT --start 2025-10-01 --end 2025-10-31`

Notes:
- The pipeline will try to use yfinance for real data; if unavailable it will use deterministic mock data.
- The Data Collector writes its output to `context['json_datacollector']` and Trend Analyzer reads the same key.

Related local notebook (uploaded):
`/mnt/data/capstone3.ipynb`
