from dotenv import load_dotenv
import os

load_dotenv()

# =====================
# API Keys
# =====================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# =====================
# Provider Configuration
# =====================

DEFAULT_PROVIDER = os.getenv(
    "DEFAULT_PROVIDER",
    "groq"
)

# =====================
# Models
# =====================

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

# =====================
# Generation Settings
# =====================

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        0.2
    )
)