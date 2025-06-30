import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """应用配置类"""
    
    # OpenAI配置
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-79d7980164854184a37a8f6e2be6a3d6")
    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.deepseek.com")
    
    # Flask配置
    PORT = int(os.getenv("PORT", 6666))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    HOST = "0.0.0.0"
    
    # 日志配置
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # 模型配置
    MODEL_NAME = "deepseek-chat"
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7 