# rentals_agent 项目

## 一、项目背景
`rentals_agent` 是一个用于澳大利亚房屋租售数据分析和智能筛选的 Python 项目，核心目标是：  

1. 对房屋数据和气候数据进行整合  
2. 提供训练/测试数据用于机器学习模型  
3. 实现交互式房源筛选功能  
4. 支持自然语言条件解析，方便用户查询  

项目可用于：
- 房源分析与推荐  
- 智能筛选和条件匹配  
- 机器学习建模和预测  

---

## 二、文件结构PythonProject/
│
├─ README.md                     # 项目说明文件
├─ rentals_agent/                # 项目核心代码
│  ├─ init.py
│  ├─ main.py
│  ├─ climate.py
│  ├─ climatemapping.py
│  ├─ housing.py
│  ├─ mergeoutput.py             # 合并房屋与气候数据
│  ├─ interactive_filter.py      # 交互式房源筛选
│  └─ …
├─ .venv/                        # Python 虚拟环境
└─ config/ docs/ fusion/          # 其他项目文件夹
---

## 三、数据文件
- `Weather_climateA.csv` / `Weather_climateB.csv`：清洗后的气象站数据  
- `australian_housing_cleaned.csv`：清洗后的房屋基础信息  
- 合并生成：
  - `houses_with_climateA_B.csv`：房屋数据 + 气候特征  
  - `houses_train.csv` / `houses_test.csv`：训练集 / 测试集  

---

## 四、主要功能

### 1. 数据清洗与整合
- 对原始房屋数据和气候数据进行格式化、缺失值处理  
- 映射房屋与气候信息（按城市或区域匹配）  
- 输出完整的 CSV 供模型使用或筛选  

### 2. 训练/测试数据拆分
- 使用 `sklearn.model_selection.train_test_split` 拆分训练集和测试集  
- 提供标准化数据用于机器学习模型训练与验证  
- 保证模型泛化能力  

### 3. 房源条件筛选
- 支持实时交互式输入条件（价格区间、卧室数量、雨量、温度等）  
- 自然语言解析示例：价格 50万到80万，卧室 3，雨量小于 2mm
- 脚本自动解析并筛选符合条件的房源  
- 可选择使用 `climateA` 或 `climateB` 数据源  

---

## 五、项目操作步骤与历史记录

### 1. 初期
- 导入和清洗房屋数据  
- 清洗气候数据并统一列名  

### 2. 映射房屋与气候数据
- 按城市或区域匹配气候数据  
- 为每个房屋增加气候特征，如 `RainToday`, `TempRange`  

### 3. 数据合并
- 使用 `mergeoutput.py` 合并房屋与气候数据  
- 输出 `houses_with_climateA_B.csv`  

### 4. 训练/测试集拆分
- 使用 `train_test_split` 拆分训练集和测试集  
- 输出 `houses_train.csv` 和 `houses_test.csv`  

### 5. 交互式筛选功能
- 实现 `interactive_filter.py` 脚本  
- 支持自然语言条件输入  
- 实时输出符合条件的房源  
- 可以指定使用 `climateA` 或 `climateB` 数据源  

### 6. 今日操作（2025-08-14）
- 统一云端文件路径，整理气候与房屋 CSV  
- 完成训练集 / 测试集生成  
- 优化交互式筛选功能  
- 确保 PyCharm 可直接操作和 Git push  

---

## 六、使用方法

1. 克隆仓库：
```bash
git clone git@github.com:Sherry-py/rentals_agent.git
cd rentals_agent
	2.	安装依赖：pip install pandas scikit-learn
  	3.	合并数据：python mergeoutput.py
    	4.	生成训练集和测试集：python mergeoutput.py --split
      	5.	交互式筛选：python interactive_filter.py
        	•	根据提示输入条件（价格区间、卧室数量、雨量等）
	•	脚本自动返回符合条件的房源
七、注意事项
	1.	文件路径统一放在云端（iCloud）或项目根目录
	2.	确保 Python 环境已安装 pandas 和 scikit-learn
	3.	README.md 在仓库根目录，rentals_agent/ 仅存放代码

⸻

八、成果
	•	完整房屋与气候数据整合
	•	训练/测试数据可直接用于机器学习
	•	支持自然语言交互式房源筛选
	•	项目文件路径和 Git 仓库管理问题已理顺
