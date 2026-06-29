import os

from dotenv import load_dotenv


load_dotenv()



class Settings:


    # =====================
    # Application
    # =====================

    APP_NAME = os.getenv(
        "APP_NAME",
        "bit-ueh-multi-agent"
    )


    ENV = os.getenv(
        "ENV",
        "development"
    )



    # =====================
    # LLM Provider
    # =====================

    LLM_PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "openai"
    )


    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )


    GOOGLE_API_KEY = os.getenv(
        "GOOGLE_API_KEY",
        ""
    )



    # =====================
    # Model
    # =====================

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gpt-4.1-mini"
    )


    TEMPERATURE = float(
        os.getenv(
            "TEMPERATURE",
            0.2
        )
    )



    # =====================
    # Session
    # =====================

    SESSION_EXPIRE_MINUTES = int(
        os.getenv(
            "SESSION_EXPIRE_MINUTES",
            30
        )
    )


    MAX_HISTORY = int(
        os.getenv(
            "MAX_HISTORY",
            20
        )
    )



settings = Settings()