# Financial Report Agent – Capstone Project
🚀 Overview
This project demonstrates an automated financial analysis system using multi-agent orchestration and a Streamlit UI.
It generates dynamic financial reports, validates evaluation criteria, and provides a defense-ready workflow with transparent safeguards.

🧩 Features
- Agent-based architecture (agents/, tools/, orchestrator/)
- Dynamic ticker selection via curated nse_bse_tickers.csv
- Evaluation agent that parses metrics, applies thresholds, and flags failures
- Streamlit UI with dropdowns, banners, and interactive reports
- Cloud deployment on Streamlit Community Cloud
- Defense-ready documentation with reproducibility and transparency

**Application URL :** https://financial-report-agent-usne9wbrnz7lfrypgr4sbz.streamlit.app/

**Demo Video :** https://youtu.be/sKlGTjcW6vE

📂 Project Structure

   ├── agents/                       # Agent definition
   
   ├── orchestrator/                  # Workflow orchestration
   
   ├── tools/                        # Helper utilities

   ├── app.py                       # Streamlit entry point
   
   ├── nse_bse_tickers.csv  # Curated NSE/BSE tickers
   
   ├── requirements.txt # Python dependencies
   
   ├── README.md        # Project documentation
   
   └── .gitignore       # Ignore cache & sensitive files



⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


2. Install Dependencies
pip install -r requirements.txt


3. Environment Variables
Create a .env file in the root directory:
GOOGLE_API_KEY=XXXX
(Replace XXXX with your actual key when running locally. On Streamlit Cloud, use Secrets Management to store keys securely.)

4. Run Locally
streamlit run app.py


🌐 Deployment
This project is deployed on Streamlit Community Cloud.
To reproduce deployment:
- Push code to GitHub
- Connect repo to Streamlit Cloud
- Select app.py as entry point
- Add secrets (e.g., GOOGLE_API_KEY) under Settings → Secrets
- Deploy → get a public URL

🧠 Evaluation Criteria
- Why: To showcase automated financial analysis with transparency and defense-ready safeguards
- What: Multi-agent orchestration, dynamic ticker input, evaluation logic, Streamlit UI
- How: Modular architecture, reproducible workflows, cloud deployment, professional documentation

🔒 Security
- .gitignore excludes __pycache__, .env, and other sensitive files
- API keys are managed via environment variables and Streamlit Secrets

📜 License
This project is for academic capstone purposes. Adapt as needed for production use.


