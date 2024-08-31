import json
import re

class JSONProcessor:
    def __init__(self, csv_data):
        self.json_content = csv_data

    def fix_multiline_content(self):
        # 使用正则表达式修复多行内容
        content_pattern = re.compile(r'"content":\s*"([^"]*?)"\s*[,}]')
        def replace_newlines(match):
            content = match.group(1)
            content_fixed = content.replace('\n', '').replace('\r', '')
            return f'"content": "{content_fixed}"' + match.group(0)[-1]
        self.json_content = content_pattern.sub(replace_newlines, self.json_content)

    def clean_content(self):
        self.json_content = self.json_content.replace('\n', '').replace('\r', '')
        # 使用正则表达式替换任意长度的空格为空
        self.json_content = re.sub(r'\s+', '', self.json_content)

    def split_json_objects(self):
        json_objects = self.json_content.split('}{')
        json_objects = [json_objects[0] + '}'] + ['{' + obj + '}' for obj in json_objects[1:-1]] + ['{' + json_objects[-1]]
        json_array_content = '[' + ','.join(json_objects) + ']'
        return json_array_content

    def process(self):
        print("Original JSON Content:", self.json_content[:1000], '\n')  # Debugging information
        self.fix_multiline_content()
        print("After fixing multiline content:", self.json_content[:1000], '\n')  # Debugging information
        self.clean_content()
        print("After cleaning content:", self.json_content[:1000], '\n')  # Debugging information
        json_array_content = self.split_json_objects()
        print("Final JSON array content:", json_array_content[:3000], '\n')  # Debugging information

        try:
            # Try to load the JSON data
            json_data = json.loads(json_array_content)
            return json_data
        except json.JSONDecodeError as e:
            # Print detailed error information with context
            error_position = e.pos
            context_start = max(0, error_position - 50)
            context_end = min(len(json_array_content), error_position + 50)
            error_context = json_array_content[context_start:context_end]
            
            # Print error message and the surrounding context
            print(f"Error decoding JSON at position {error_position}: {e}")
            print(f"Error context: {error_context}\n")
            return None

# import re
# import json

# class JSONProcessor:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def read_file(self):
#         with open(self.file_path, 'r', encoding='utf-8') as file:
#             self.json_content = file.readlines()

#     def fix_multiline_content(self):
#         start_marker = '"content":'
#         end_marker = '。"\n'
#         start_index = self.json_content.find(start_marker) + len(start_marker)
#         end_index = self.json_content.find(end_marker, start_index)

#         if start_index != -1 and end_index != -1:
#             multi_line_content = self.json_content[start_index:end_index]
#             single_line_content = multi_line_content.replace('\n', '')
#             self.json_content = self.json_content[:start_index] + single_line_content + self.json_content[end_index:]

#     def clean_content(self):
#         self.json_content = self.json_content.replace('\n', '').replace('\r', '').replace(' ', '').replace('\\', '')

#     def split_json_objects(self):
#         json_objects = self.json_content.split('}{')
#         json_objects = [json_objects[0] + '}'] + ['{' + obj + '}' for obj in json_objects[1:-1]] + ['{' + json_objects[-1]]
#         json_array_content = '[' + ','.join(json_objects) + ']'
#         return json_array_content

#     def save_json(self, json_array_content, output_path):
#         with open(output_path, 'w', encoding='utf-8') as file:
#             file.write(json_array_content)

#     def process(self, output_path):
#         self.read_file()
#         print("Initial JSON Content:", " ".join(self.json_content)[:1000], "...")  # 调试信息，仅打印前1000个字符
#         self.fix_multiline_content()
#         print("After fixing multiline content:", " ".join(self.json_content)[:1000], "...")  # 调试信息，仅打印前1000个字符
#         self.clean_content()
#         print("After cleaning content:", " ".join(self.json_content)[:1000], "...")  # 调试信息，仅打印前1000个字符
#         json_array_content = self.split_json_objects()
#         print("Final JSON Array Content:", json_array_content[:1000], "...")  # 调试信息，仅打印前1000个字符

#         try:
#             json.loads(json_array_content)
#             self.save_json(json_array_content, output_path)
#         except json.JSONDecodeError as e:
#             print(f"Error decoding JSON: {e}")
#             error_position = e.pos
#             context = json_array_content[max(0, error_position - 50):min(len(json_array_content), error_position + 50)]
#             print(f"Error context: {context}")


# if __name__ == "__main__":
#     file_path = '../src/API/PE/护卫舰/fixed_log.csv'
#     output_path = '../src/API/PE/护卫舰/fixed_log.json'
    
#     processor = JSONProcessor(file_path)
#     processor.process(output_path)

