import pandas as pd
import re

# 读取 OCR 提取结果
df = pd.read_csv('screenshots/ocr_extracted_texts.csv')

# 准备结果列表
structured_data = []

for idx, row in df.iterrows():
    filename = row['filename']
    text = row['text']

    # 地址提取
    address_match = re.search(r'(\d{1,4}[A-Z]?/.*?Rosebery NSW 2018)', text)
    address = address_match.group(1) if address_match else ''

    # 租金价格
    price_match = re.search(r'\$([0-9]{3,4})\s*pw', text)
    price_pw = price_match.group(1) if price_match else ''

    # 卧室
    bedrooms_match = re.search(r'(\d+)Bed', text)
    bedrooms = bedrooms_match.group(1) if bedrooms_match else ''

    # 浴室
    bathrooms_match = re.search(r'(\d+)Bath', text)
    bathrooms = bathrooms_match.group(1) if bathrooms_match else ''

    # 车位
    car_match = re.search(r'(\d+)Car', text)
    car_spaces = car_match.group(1) if car_match else ''

    # 可入住日期
    available_match = re.search(r'from:\s*(\w+ \d+)', text)
    available_from = available_match.group(1) if available_match else ''

    # 押金
    bond_match = re.search(r'Rental bond:\s*\$([\d,]+)', text)
    bond = bond_match.group(1) if bond_match else ''

    structured_data.append({
        'filename': filename,
        'address': address,
        'price_pw': price_pw,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'car_spaces': car_spaces,
        'available_from': available_from,
        'bond': bond
    })

# 转为 DataFrame 并保存
structured_df = pd.DataFrame(structured_data)
structured_df.to_csv('screenshots/structured_rental_list.csv', index=False)

print('✅ 结构化提取完成，已保存为 screenshots/structured_rental_list.csv')