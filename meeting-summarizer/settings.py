class settings:
    def __init__(self):
        self.openai_api_key = "your_openai_api_key_here"
        self.openai_api_base = "https://api.openai.com/v1"
        self.openai_model = "gpt-4o-mini"

    def load_from_env(self):
        import os
        from dotenv import load_dotenv

        load_dotenv()
        self.openai_api_key = os.getenv("OPENAI_API_KEY", self.openai_api_key)
        self.openai_api_base = os.getenv("OPENAI_API_BASE", self.openai_api_base)
        self.openai_model = os.getenv("OPENAI_MODEL", self.openai_model)