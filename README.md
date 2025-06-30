# SmartCampus LLM Chat API

基于Flask框架的智能聊天后台API服务，支持与DeepSeek等LLM模型进行对话交互。

## 功能特性

- 🚀 基于Flask的轻量级Web API
- 💬 支持普通聊天和流式聊天
- 🔧 可配置的模型参数
- 📝 完整的日志记录
- 🌐 支持跨域请求
- 🏥 健康检查接口

## 项目结构

```
SmartCampus-py-backend/
├── app.py                 # Flask应用主文件
├── config.py              # 配置文件
├── requirements.txt       # 项目依赖
├── test_api.py           # API测试脚本
├── utils/                 # 工具模块
│   ├── __init__.py
│   └── llm_client.py     # LLM客户端工具类
└── llm-core/             # 原有LLM核心模块
    └── llm-request.py
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

创建 `.env` 文件（可选）：

```env
# OpenAI API配置
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.deepseek.com

# Flask应用配置
PORT=6666
DEBUG=False
LOG_LEVEL=INFO
```

### 3. 启动服务

```bash
python app.py
```

服务将在 `http://localhost:6666` 启动。

## API接口

### 1. 健康检查

**GET** `/`

```bash
curl http://localhost:6666/
```

响应示例：
```json
{
  "status": "success",
  "message": "SmartCampus LLM Chat API is running",
  "version": "1.0.0",
  "port": 6666
}
```

### 2. 普通聊天

**POST** `/api/chat`

请求体：
```json
{
  "message": "你好，请介绍一下你自己",
  "system_prompt": "你是一个智能助手，请用中文回答用户的问题。"
}
```

响应示例：
```json
{
  "status": "success",
  "data": {
    "message": "你好，请介绍一下你自己",
    "reply": "你好！我是一个智能助手...",
    "model": "deepseek-chat"
  }
}
```

### 3. 流式聊天

**POST** `/api/chat/stream`

请求体：
```json
{
  "message": "请写一首关于春天的诗",
  "system_prompt": "你是一个智能助手，请用中文回答用户的问题。"
}
```

响应格式：
```
data: 春天来了...
data: 万物复苏...
data: [DONE]
```

## 测试

运行测试脚本：

```bash
python test_api.py
```

## 配置说明

### 模型配置

在 `config.py` 中可以调整以下参数：

- `MODEL_NAME`: 使用的模型名称
- `MAX_TOKENS`: 最大生成token数
- `TEMPERATURE`: 生成温度（0-1）

### 日志配置

- `LOG_LEVEL`: 日志级别（DEBUG, INFO, WARNING, ERROR）

## 开发说明

### 添加新的API接口

1. 在 `app.py` 中添加新的路由
2. 在 `utils/` 目录下添加相应的工具类
3. 更新配置文件（如需要）

### 错误处理

项目包含完整的错误处理机制：
- 400: 请求参数错误
- 404: 接口不存在
- 500: 服务器内部错误

## 许可证

MIT License
