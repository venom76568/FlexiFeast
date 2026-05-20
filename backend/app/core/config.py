from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FlexiFeast"
    API_V1_STR: str = "/api"
    DATABASE_URL: str = "sqlite:///./flexifeast.db" # fallback
    
    # Swiggy MCP configuration
    SWIGGY_MCP_API_URL: str | None = None
    SWIGGY_MCP_API_KEY: str | None = None
    
    # Security and Integration
    API_KEY: str = "default_api_key" # Change in production
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]
    TWILIO_ACTIVE: bool = False
    TWILIO_ACCOUNT_SID: str | None = None
    TWILIO_AUTH_TOKEN: str | None = None
    SLACK_BOT_TOKEN: str | None = None
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
