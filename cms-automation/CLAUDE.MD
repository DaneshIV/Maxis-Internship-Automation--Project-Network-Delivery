# CMS Automation

Automates end-to-end data entry from Excel into the CMS web system, with an AI prediction module that fills missing fields using historical ACR data.

---

## Project Structure

```
cms-automation/
├── config/
│   ├── field_mapping.yaml       # Excel → CMS field mapping (update after CMS access)
│   └── .env.example             # Environment variable template
│
├── src/
│   ├── parser/
│   │   └── excel_parser.py      # Reads and validates Excel data
│   ├── automation/
│   │   └── cms_automation.py    # Playwright browser automation for CMS
│   ├── ai/
│   │   ├── train.py             # Model training pipeline
│   │   └── predict.py           # Inference — predicts missing CMS fields
│   └── utils/
│       ├── config_loader.py     # Loads field_mapping.yaml and .env
│       └── logger.py            # Shared logging module
│
├── tests/
│   ├── test_parser/
│   ├── test_automation/
│   └── test_ai/
│
├── data/
│   ├── raw/                     # Source Excel files (gitignored)
│   └── processed/               # Cleaned data output (gitignored)
│
├── models/                      # Saved trained models (gitignored)
├── logs/                        # Runtime logs (gitignored)
├── docs/                        # Technical documentation
│
├── main.py                      # Entry point — runs the full pipeline
├── requirements.txt
└── .gitignore
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/cms-automation.git
cd cms-automation
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure environment
```bash
cp .env.example .env
# Edit .env and fill in CMS credentials and ACR access details
```

### 5. Update field mapping
```
config/field_mapping.yaml
```
Fill in the `cms_field` values once CMS access is granted.

---

## Running the Pipeline

```bash
python main.py
```

---

## Modules

| Module | Status | Description |
|---|---|---|
| `excel_parser.py` | 🔲 In progress | Reads and validates Excel rows |
| `config_loader.py` | ✅ Done | Loads YAML config and .env |
| `logger.py` | 🔲 In progress | Shared logging across all modules |
| `cms_automation.py` | 🔲 Pending CMS access | Playwright automation for CMS form |
| `train.py` | 🔲 Pending ACR data | AI model training pipeline |
| `predict.py` | 🔲 Pending ACR data | AI inference for missing fields |

---

## Status

> **Current phase:** Pre-access setup — building all modules that don't require CMS or ACR access.
> CMS access and ACR data pending approval.

---

## Tech Stack

| Purpose | Tool |
|---|---|
| Language | Python 3.11+ |
| Excel parsing | pandas, openpyxl |
| Web automation | Playwright |
| AI / ML | scikit-learn, XGBoost |
| Config | PyYAML, python-dotenv |
| Version control | Git / GitHub |
| API testing | Insomnia |
