import pandas as pd
import os
print("当前工作目录:", os.getcwd())
def clean_housing_data(input_csv, output_csv):
    # 读取数据
    df = pd.read_csv(input_csv)

    # 删除全缺列
    df.drop(columns=['latitude', 'longitude'], inplace=True)

    # 价格列转数值，去掉$和逗号
    df['price'] = df['price'].str.replace(r'[\$,]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # 缺失值填充
    for col in ['bedroom_count', 'bathroom_count', 'parking_count']:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

    # 日期转换
    df['RunDate'] = pd.to_datetime(df['RunDate'], errors='coerce')
    df['open_date'] = pd.to_datetime(df['open_date'], errors='coerce', format='%Y-%m-%d')

    # 字符串统一格式
    for col in ['city', 'state', 'location_name', 'property_type']:
        df[col] = df[col].str.strip().str.lower()

    # 删除缺失严重的列
    df.drop(columns=['building_size', 'land_size', 'preferred_size'], inplace=True)

    # 保存清洗后数据
    df.to_csv(output_csv, index=False)

    print(f"数据清洗完成，保存为 {output_csv}")

def preview_cleaned_data(cleaned_csv):
    df_cleaned = pd.read_csv(cleaned_csv)
    print("清洗后数据预览:")
    print(df_cleaned.head())

if __name__ == "__main__":
    input_path = '/Users/sherry/Desktop/python/australian_housing.csv'
    output_path = 'australian_housing_cleaned.csv'

    clean_housing_data(input_path, output_path)
    preview_cleaned_data(output_path)