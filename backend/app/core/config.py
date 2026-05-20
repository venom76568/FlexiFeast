from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FlexiFeast"
    API_V1_STR: str = "/api"
    DATABASE_URL: str = "sqlite:///./flexifeast.db" # fallback
    
    # Swiggy MCP configuration
    SWIGGY_MCP_API_URL: str | None = None
    SWIGGY_MCP_API_KEY: str | None = None
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
