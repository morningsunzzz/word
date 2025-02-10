import pandas as pd
import openpyxl 
import os

try:
    # 检查文件是否存在
    file_path = 'Irregular verbs不规则动词变形表.xlsx'
    if not os.path.exists(file_path):
        print(f"错误：文件 '{file_path}' 不存在！")
        print(f"当前工作目录：{os.getcwd()}")
        exit(1)

    # 读取Excel文件
    df = pd.read_excel(file_path)
    
    verbs_data = []
    for index, row in df.iterrows():
        verb = {
            "word": row['原形'],
            "type": "v.",
            "forms": {
                "original": row['原形'],
                "original_phonetic": row['原形音标'],
                "past": row['过去式'],
                "past_phonetic": row['过去式音标'],
                "pastParticiple": row['过去分词'],
                "pastParticiple_phonetic": row['过去分词音标']
            },
            "definition": row['释义'],
            "tags": ["不规则动词"]
        }
        verbs_data.append(verb)

    # 输出数据
    print(f"成功处理了 {len(verbs_data)} 个动词")
    print(verbs_data)
    
    # 如果需要保存为json文件，可以取消下面的注释
    import json
    with open('verbs_data.json', 'w', encoding='utf-8') as f:
        json.dump(verbs_data, f, ensure_ascii=False, indent=4)

except Exception as e:
    print(f"发生错误：{str(e)}")