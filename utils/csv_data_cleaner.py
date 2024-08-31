import re

class CSVDataCleaner:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.csv_content = None

    def read_csv(self):
        with open(self.input_file_path, 'r', encoding='utf-8') as file:
            self.csv_content = file.read()

    def fix_quotes(self):
        if self.csv_content is not None:
            self.csv_content = self.csv_content.replace('""', '"').replace("\\", "")
        else:
            raise ValueError("CSV content is not loaded. Please read the CSV file first.")

    def fix_braces(self):
        if self.csv_content is not None:
            self.csv_content = re.sub(r'}"[^{}]*"\'{', '}\n{', self.csv_content)
        else:
            raise ValueError("CSV content is not loaded. Please read the CSV file first.")

    def remove_unwanted_content(self):
        if self.csv_content is not None:
            self.csv_content = re.sub(r'^[^{]*{', '{', self.csv_content, count=1, flags=re.DOTALL)
            self.csv_content = re.sub(r'}[^}]*$', '}', self.csv_content, count=1, flags=re.DOTALL)
        else:
            raise ValueError("CSV content is not loaded. Please read the CSV file first.")

    def save_csv(self):
        if self.csv_content is not None:
            with open(self.output_file_path, 'w', encoding='utf-8') as file:
                file.write(self.csv_content)
        else:
            raise ValueError("CSV content is not loaded. Please read the CSV file first.")

    def clean_csv(self):
        self.read_csv()
        self.fix_quotes()
        self.fix_braces()
        self.remove_unwanted_content()
        return self.csv_content


# import re

# class CSVDataCleaner:
#     def __init__(self, input_file_path, output_file_path):
#         self.input_file_path = input_file_path
#         self.output_file_path = output_file_path
#         self.csv_content = None

#     def read_csv(self):
#         with open(self.input_file_path, 'r', encoding='utf-8') as file:
#             self.csv_content = file.read()

#     def fix_quotes(self):
#         if self.csv_content is not None:
#             self.csv_content = self.csv_content.replace('""', '"')
#         else:
#             raise ValueError("CSV content is not loaded. Please read the CSV file first.")

#     def fix_braces(self):
#         if self.csv_content is not None:
#             self.csv_content = re.sub(r'}"[^{}]*"\'{', '}\n{', self.csv_content)
#         else:
#             raise ValueError("CSV content is not loaded. Please read the CSV file first.")

#     def remove_unwanted_content(self):
#         if self.csv_content is not None:
#             self.csv_content = re.sub(r'^[^{]*{', '{', self.csv_content, count=1, flags=re.DOTALL)
#             self.csv_content = re.sub(r'}[^}]*$', '}', self.csv_content, count=1, flags=re.DOTALL)
#         else:
#             raise ValueError("CSV content is not loaded. Please read the CSV file first.")
        
#     def remove_content_quotes(self):
#         if self.csv_content is not None:
#             # Match the content value and remove internal quotes
#             def replace_quotes(match):
#                 content = match.group(1)
#                 content = content.replace('"', '')
#                 return f'"content": "{content}"'
            
#             self.csv_content = re.sub(r'"content":\s*"(.*?)"', replace_quotes, self.csv_content, flags=re.DOTALL)
#         else:
#             raise ValueError("CSV content is not loaded. Please read the CSV file first.")

#     def save_csv(self):
#         if self.csv_content is not None:
#             with open(self.output_file_path, 'w', encoding='utf-8') as file:
#                 file.write(self.csv_content)
#         else:
#             raise ValueError("CSV content is not loaded. Please read the CSV file first.")

#     def clean_csv(self):
#         self.read_csv()
#         self.fix_quotes()
#         self.fix_braces()
#         self.remove_unwanted_content()
#         # self.remove_content_quotes()
#         self.save_csv()

# if __name__ == "__main__":
#     file_path = '../src/API/PE/护卫舰/log.csv'
#     output_path = '../src/API/PE/护卫舰/fixed_log.csv'
    
#     processor = CSVDataCleaner(file_path, output_path)
#     processor.clean_csv()