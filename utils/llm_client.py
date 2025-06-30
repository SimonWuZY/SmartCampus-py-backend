from openai import OpenAI
from config import Config
import logging

logger = logging.getLogger(__name__)

class LLMClient:
    """LLM客户端类"""
    
    def __init__(self):
        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY,
            base_url=Config.OPENAI_BASE_URL
        )
    
    def chat(self, message, system_prompt="你是一个智能助手，请用中文回答用户的问题。"):
        """普通聊天接口"""
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
            
            response = self.client.chat.completions.create(
                model=Config.MODEL_NAME,
                messages=messages,
                stream=False,
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"LLM聊天错误: {str(e)}")
            raise e
    
    def chat_stream(self, message, system_prompt="你是一个智能助手，请用中文回答用户的问题。"):
        """流式聊天接口"""
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
            
            stream = self.client.chat.completions.create(
                model=Config.MODEL_NAME,
                messages=messages,
                stream=True,
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            return stream
            
        except Exception as e:
            logger.error(f"LLM流式聊天错误: {str(e)}")
            raise e 