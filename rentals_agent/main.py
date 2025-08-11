from housing import load_housing_data, filter_houses

def main():
    # 数据文件路径
    file_path = '/Users/Sherry/Desktop/python/Housing.xlsx'  # 改为你的路径

    # 读取数据
    df = load_housing_data(file_path)

    # === 条件筛选设置 ===
    min_price = 10000000      # 最低价格
    max_price = 15000000      # 最高价格
    min_bedrooms = 3          # 至少卧室数
    airconditioning = "yes"   # 是否有空调: "yes" / "no" / None
    furnishingstatus = "furnished"  # 家具状态: "furnished" / "semi-furnished" / "unfurnished" / None

    # 筛选
    results = filter_houses(
        df,
        min_price=min_price,
        max_price=max_price,
        min_bedrooms=min_bedrooms,
        airconditioning=airconditioning,
        furnishingstatus=furnishingstatus
    )

    # 输出
    print(f"符合条件的房源（共 {len(results)} 套）：")
    print(results)

    # 保存
    output_file = 'filtered_houses.xlsx'
    results.to_excel(output_file, index=False)
    print(f"筛选结果已保存到 {output_file}")

if __name__ == "__main__":
    main()