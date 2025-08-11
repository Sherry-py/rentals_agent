import pandas as pd

def main():
    # 读取清洗后的房源数据
    housing_df = pd.read_csv('australian_housing_cleaned.csv')

    # 统一城市名格式（小写，去空格）
    housing_df['city'] = housing_df['city'].str.strip().str.lower()

    # 指定目标城市
    target_city = 'rosebery'  # 你可以改成其他有效城市名

    # 筛选目标城市的房源
    city_houses = housing_df[housing_df['city'] == target_city]

    print(f"{target_city} 区域共有房源：{len(city_houses)} 套")

    if city_houses.empty:
        print("没有符合条件的房源")
    else:
        # 过滤价格缺失的房源
        filtered_houses = city_houses.dropna(subset=['price'])
        print(f"过滤后共有房源：{len(filtered_houses)} 套")
        print(filtered_houses[['address_1', 'price', 'bedroom_count', 'bathroom_count']].head())

if __name__ == "__main__":
    main()