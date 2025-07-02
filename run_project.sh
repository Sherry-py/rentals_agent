#!/bin/bash

# 项目根目录（根据你实际路径改）
PROJECT_ROOT="/Users/sherry/Desktop/python/PythonProject"

# 虚拟环境路径（根据你实际路径改）
VENV_PATH="$PROJECT_ROOT/.venv"

# 激活虚拟环境
if [ -d "$VENV_PATH" ]; then
  source "$VENV_PATH/bin/activate"
  echo "虚拟环境已激活"
else
  echo "未找到虚拟环境，跳过激活"
fi

# 切换到项目根目录
cd "$PROJECT_ROOT" || { echo "切换目录失败"; exit 1; }
echo "已切换到项目目录：$PROJECT_ROOT"

# 设置PYTHONPATH
export PYTHONPATH="$PROJECT_ROOT"
echo "PYTHONPATH 设置为 $PROJECT_ROOT"

# 运行模块（你可以改成你想跑的模块或测试）
python3 -m rentals_agent.config.strategy_engine

# 你也可以用下面命令运行所有测试（取消注释即可）
# python3 -m unittest discover -s rentals_agent -p "test_*.py"