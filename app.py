from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from config import Config
from utils.llm_client import LLMClient

# 配置日志
logging.basicConfig(level=getattr(logging, Config.LOG_LEVEL))
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 初始化LLM客户端
llm_client = LLMClient()

@app.route('/')
def index():
    """健康检查接口"""
    return jsonify({
        "status": "success",
        "message": "SmartCampus LLM Chat API is running",
        "version": "1.0.0",
        "port": Config.PORT
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """LLM聊天接口"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "请求数据不能为空"}), 400
        
        message = data.get('message', '')
        if not message:
            return jsonify({"error": "消息内容不能为空"}), 400
        
        # 获取系统提示词（可选）
        system_prompt = data.get('system_prompt', "你是一个智能助手，请用中文回答用户的问题。")
        
        # 调用LLM API
        reply = llm_client.chat(message, system_prompt)
        
        logger.info(f"用户消息: {message}")
        logger.info(f"AI回复: {reply}")
        
        return jsonify({
            "status": "success",
            "data": {
                "message": message,
                "reply": reply,
                "model": Config.MODEL_NAME
            }
        })
        
    except Exception as e:
        logger.error(f"聊天接口错误: {str(e)}")
        return jsonify({
            "error": "服务器内部错误",
            "message": str(e)
        }), 500

@app.route('/api/chat/stream', methods=['POST'])
def chat_stream():
    """流式LLM聊天接口"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "请求数据不能为空"}), 400
        
        message = data.get('message', '')
        if not message:
            return jsonify({"error": "消息内容不能为空"}), 400
        
        # 获取系统提示词（可选）
        system_prompt = data.get('system_prompt', "你是一个智能助手，请用中文回答用户的问题。")
        
        def generate():
            try:
                # 调用流式LLM API
                stream = llm_client.chat_stream(message, system_prompt)
                
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        yield f"data: {chunk.choices[0].delta.content}\n\n"
                
                yield "data: [DONE]\n\n"
                
            except Exception as e:
                logger.error(f"流式聊天错误: {str(e)}")
                yield f"data: 错误: {str(e)}\n\n"
        
        return app.response_class(
            generate(),
            mimetype='text/plain'
        )
        
    except Exception as e:
        logger.error(f"流式聊天接口错误: {str(e)}")
        return jsonify({
            "error": "服务器内部错误",
            "message": str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({
        "status": "healthy",
        "service": "SmartCampus LLM Chat API",
        "version": "1.0.0"
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "接口不存在"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "服务器内部错误"}), 500

if __name__ == '__main__':
    logger.info(f"启动SmartCampus LLM Chat API服务器，端口: {Config.PORT}")
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG) 