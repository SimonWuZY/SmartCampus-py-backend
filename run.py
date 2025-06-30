"""
SmartCampus LLM Chat API 启动脚本
"""

import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """检查依赖是否已安装"""
    try:
        import flask
        import openai
        import dotenv
        print("✅ 所有依赖已安装")
        return True
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install -r requirements.txt")
        return False

def create_env_file():
    """创建.env文件（如果不存在）"""
    env_file = Path(".env")
    if not env_file.exists():
        print("📝 创建.env配置文件...")
        env_content = """# OpenAI API配置
OPENAI_API_KEY=sk-79d7980164854184a37a8f6e2be6a3d6
OPENAI_BASE_URL=https://api.deepseek.com

# Flask应用配置
PORT=6666
DEBUG=False
LOG_LEVEL=INFO
"""
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ .env文件已创建")
    else:
        print("✅ .env文件已存在")

def main():
    """主函数"""
    print("🚀 SmartCampus LLM Chat API 启动器")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 创建配置文件
    create_env_file()
    
    print("\n🎯 启动选项:")
    print("1. 启动API服务器")
    print("2. 运行API测试")
    print("3. 安装依赖")
    print("4. 退出")
    
    while True:
        choice = input("\n请选择操作 (1-4): ").strip()
        
        if choice == "1":
            print("\n🚀 启动API服务器...")
            print("服务将在 http://localhost:6666 启动")
            print("按 Ctrl+C 停止服务")
            print("-" * 50)
            try:
                subprocess.run([sys.executable, "app.py"])
            except KeyboardInterrupt:
                print("\n👋 服务已停止")
            break
            
        elif choice == "2":
            print("\n🧪 运行API测试...")
            try:
                subprocess.run([sys.executable, "test_api.py"])
            except Exception as e:
                print(f"测试失败: {e}")
            break
            
        elif choice == "3":
            print("\n📦 安装依赖...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
                print("✅ 依赖安装完成")
            except Exception as e:
                print(f"❌ 依赖安装失败: {e}")
            break
            
        elif choice == "4":
            print("👋 再见！")
            sys.exit(0)
            
        else:
            print("❌ 无效选择，请重新输入")

if __name__ == "__main__":
    main() 