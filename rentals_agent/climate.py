import pandas as pd

def clean_climate_data(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    print(f"读取 {input_csv} 基本信息:")
    print(df.info())
    print("缺失值统计:")
    print(df.isnull().sum())

    # 统一风向字段小写去空格
    wind_dir_cols = ['WindGustDir', 'WindDir9am', 'WindDir3pm']
    for col in wind_dir_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()

    # 降雨标志转二进制
    for col in ['RainToday', 'RainTomorrow']:
        if col in df.columns:
            df[col] = df[col].map({'No': 0, 'Yes': 1})

    # 数值字段填充缺失值
    numeric_cols = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm',
                    'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
                    'Temp9am', 'Temp3pm']
    for col in numeric_cols:
        if col in df.columns:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)

    # 新增气温差特征
    if 'MaxTemp' in df.columns and 'MinTemp' in df.columns:
        df['TempRange'] = df['MaxTemp'] - df['MinTemp']

    df.to_csv(output_csv, index=False)
    print(f"清洗完成，保存为 {output_csv}")

if __name__ == "__main__":
    input_train = '/Users/sherry/Desktop/python/Aus weather/Weather Training Data.csv'
    output_train = 'Weather_Training_Cleaned.csv'
    clean_climate_data(input_train, output_train)

    input_test = '/Users/sherry/Desktop/python/Aus weather/Weather Test Data.csv'
    output_test = 'Weather_Test_Cleaned.csv'
    clean_climate_data(input_test, output_test)