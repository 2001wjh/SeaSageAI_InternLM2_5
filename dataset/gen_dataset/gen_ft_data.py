import logging
from utils.csv_data_cleaner import CSVDataCleaner
from utils.csv_to_json import JSONProcessor
from utils.json_data_transformer import DataTransformer

# 配置日志
logging.basicConfig(level=logging.INFO)

ship_list = [
    '航母', 
    '两栖攻击舰', 
    '驱逐舰', 
    '护卫舰', 
    '补给舰'
]

def main(input_csv_path, output_json_path):
    try:
        # Step 1: Clean CSV data
        cleaner = CSVDataCleaner(input_csv_path)
        cleaned_csv_data = cleaner.clean_csv()
        # logging.info(f"Cleaned CSV Data (first 5 rows): {cleaned_csv_data[:5]}")  # Debugging

        # Step 2: Convert cleaned CSV data to JSON
        processor = JSONProcessor(cleaned_csv_data)
        json_data = processor.process()
        # logging.info(f"JSON Data (first 5 entries): {json_data[:5]}")  # Debugging

        # Step 3: Transform JSON data to QA format
        transformer = DataTransformer(json_data)
        qa_data = transformer.transform_to_qa_format()

        # Step 4: Save the transformed data to a JSON file
        transformer.save_json(output_json_path, qa_data)
        logging.info(f"Data successfully saved to {output_json_path}")

        # Step 5: Print a success message
        logging.info(f"数据整理成功，已保存到 {output_json_path} 文件中")

    except Exception as e:
        logging.error(f"An error occurred during data processing: {str(e)}")

def get_paths(ship_type):
    paths = {
        '航母': {
            'csv': './src/API/PE/航母/log.csv',
            'json': './dataset/航母/instruction_fine_tuning_data.json'
        },
        '两栖攻击舰': {
            'csv': './src/API/PE/两栖攻击舰/log.csv',
            'json': './dataset/两栖攻击舰/instruction_fine_tuning_data.json'
        },
        '驱逐舰': {
            'csv': './src/API/PE/驱逐舰/log.csv',
            'json': './dataset/驱逐舰/instruction_fine_tuning_data.json'
        },
        '护卫舰': {
            'csv': './src/API/PE/护卫舰/log.csv',
            'json': './dataset/护卫舰/instruction_fine_tuning_data.json'
        },
        '补给舰': {
            'csv': './src/API/PE/补给舰/log.csv',
            'json': './dataset/补给舰/instruction_fine_tuning_data.json'
        }
    }

    # 当舰艇类型不合法时，给出提示并返回 None
    if ship_type in paths:
        return paths[ship_type]
    else:
        logging.warning(f"Invalid ship type: {ship_type}")
        return None

if __name__ == "__main__":
    ship_type = int(input("请输入你要整理的舰艇类型（航母 1 | 两栖攻击舰 2 | 驱逐舰 3 | 护卫舰 4 | 补给舰 5）："))

    paths = get_paths(ship_list[ship_type - 1])
    if paths:
        input_csv_path = paths['csv']
        output_json_path = paths['json']
        main(input_csv_path, output_json_path)
        
    else:
        logging.error("输入的舰艇类型无效，请输入正确的舰艇类型。")
