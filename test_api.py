#!/usr/bin/env python3
"""
SmartCampus LLM Chat API 测试脚本
"""

import requests
import json

# API基础URL
BASE_URL = "http://localhost:6666"

def test_health_check():
    """测试健康检查接口"""
    print("=== 测试健康检查接口 ===")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"状态码: {response.status_code}")
        print(f"响应: {response.json()}")
        print()
    except Exception as e:
        print(f"错误: {e}")
        print()

def test_chat_api():
    """测试聊天接口"""
    print("=== 测试聊天接口 ===")
    try:
        data = {
            "message": "你好，请介绍一下你自己",
            "system_prompt": "你是一个智能助手，请用中文回答用户的问题。"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/chat",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"状态码: {response.status_code}")
        print(f"请求数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
        print(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        print()
    except Exception as e:
        print(f"错误: {e}")
        print()

def test_stream_chat_api():
    """测试流式聊天接口"""
    print("=== 测试流式聊天接口 ===")
    try:
        data = {
            "message": "请写一首关于春天的诗",
            "system_prompt": "你是一个智能助手，请用中文回答用户的问题。"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/chat/stream",
            json=data,
            headers={"Content-Type": "application/json"},
            stream=True
        )
        
        print(f"状态码: {response.status_code}")
        print(f"请求数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
        print("流式响应:")
        
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    content = line_str[6:]  # 移除 'data: ' 前缀
                    if content == '[DONE]':
                        print("=== 流式响应结束 ===")
                        break
                    print(content, end='', flush=True)
        print()
        print()
    except Exception as e:
        print(f"错误: {e}")
        print()

if __name__ == "__main__":
    print("开始测试SmartCampus LLM Chat API...")
    print()
    
    # 运行测试
    test_health_check()
    test_chat_api()
    test_stream_chat_api()
    
    print("测试完成！") 