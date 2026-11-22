"""Local configuration."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    temperature: float = 0.0

    # Local paths
    data_dir = BASE_DIR / "data"
    input_dir = data_dir / "input"
    templates_dir = data_dir / "templates"
    output_dir = data_dir / "output"

    pdf_path = input_dir / "annual_report.pdf"
    template_path = templates_dir / "creditlens_template.xlsx"
    output_path = output_dir / "spreading_output.xlsx"

    # Page selection defaults
    first_n_pages = 10
    max_selected_pages = 20

def get_settings() -> Settings:
    return Settings()
