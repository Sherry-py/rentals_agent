# config_reader module
# 需要安装PyYAML: pip install pyyaml
import os
from typing import Dict, Optional

import yaml


class ConfigReader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self._config: Optional[Dict] = None

    def get_config(self) -> Dict:
        """获取配置字典，如果尚未加载则先加载配置"""
        if self._config is None:
            self._load_config()
        return self._config

    def _load_config(self) -> None:
        """加载并解析YAML配置文件"""
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                # 使用safe_load避免安全风险
                self._config = yaml.safe_load(f)
                # 处理空文件情况，返回空字典
                if self._config is None:
                    self._config = {}
        except FileNotFoundError:
            raise FileNotFoundError(f"配置文件 '{self.config_path}' 不存在")
        except yaml.YAMLError as e:
            raise ValueError(f"YAML文件解析错误: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"读取配置文件时发生错误: {str(e)}")


# 示例用法
if __name__ == "__main__":
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构造配置文件路径
    config_path = os.path.join(current_dir, "user_config.yaml")
    reader = ConfigReader(config_path)
    try:
        config = reader.get_config()
        print("配置加载成功:")
        print(config)
    except Exception as e:
        print(f"发生错误: {e}")
