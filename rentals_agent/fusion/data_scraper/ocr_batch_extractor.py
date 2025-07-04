import os
import pytesseract
from PIL import Image
import pandas as pd


# 可选: Mac Brew 安装通常自动配置，无需设置路径
# 如果报错找不到 tesseract，可取消注释并修改路径
# pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def extract_text_from_images(folder_path='screenshots'):
    extracted_data = []

    if not os.path.exists(folder_path):
        print(f"❌ 文件夹 {folder_path} 不存在，请先将截图放入该文件夹。")
        return

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        print(f"⚠️ 未检测到截图文件，请将房源截图放入 {folder_path} 后重试。")
        return

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"🔍 正在处理: {image_file}")

        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image, lang='eng')
            extracted_data.append({'filename': image_file, 'text': text})
        except Exception as e:
            print(f"❌ 无法处理 {image_file}: {e}")

    df = pd.DataFrame(extracted_data)
    output_csv = os.path.join(folder_path, 'ocr_extracted_texts.csv')
    df.to_csv(output_csv, index=False)
    print(f"✅ 提取完成，已保存到 {output_csv}")


if __name__ == '__main__':
    extract_text_from_images('screenshots')  # 可根据需要修改截图路径