import json

class DataTransformer:
    def __init__(self, json_data):
        self.data = json_data
        # print(self.data)

    def transform_to_qa_format(self):
        qa_data = []
        for vessel in self.data:
            vessel_name = vessel.get("Vessel_Name")
            identification_features = vessel.get("Identification_features") or vessel.get("Identificationfeatures") or vessel.get("Identification features")
            feature_explanation = vessel.get("Feature_explanation") or vessel.get("Feature explanation")
            identification_process = vessel.get("Identification_process", {}).get("content")

            # 检查关键字段是否存在
            if not (vessel_name and identification_features and feature_explanation and identification_process):
                print(f"Warning: Missing data in entry {vessel}")
                continue

            # 创建判读特征及其重要性得分的问答对
            features_qa = {
                "input": f"{vessel_name}的识别特征有哪些？哪些识别特征更重要？",
                "output": "；".join([f"{feature_info['feature']}，满分5分的话，该特征的重要性得分为{feature_info['score']}"
                               for feature_info in identification_features.values()])
            }

            # 创建特征描述的问答对
            explanation_qa = {
                "input": f"进行详细分析，帮助我理解{vessel_name}的识别特征",
                "output": "；".join([f"{info['feature']}：{feature_explanation[info_id]}"
                               for info_id, info in identification_features.items()])
            }

            # 创建判读流程的问答对
            process_qa = {
                "input": f"{vessel_name}的识别流程是什么？",
                "output": identification_process
            }

            # # 将问答对加入到列表中
            # qa_data.append(features_qa)
            # qa_data.append(explanation_qa)
            # qa_data.append(process_qa)

            # 将问答对封装到conversation字段中
            qa_data.append({
                "conversation": [features_qa]
            })
            qa_data.append({
                "conversation": [explanation_qa]
            })
            qa_data.append({
                "conversation": [process_qa]
            })
        
        return qa_data

    def save_json(self, output_path, json_data):
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)


# import json

# class DataTransformer:
#     def __init__(self, json_data):
#         self.data = json_data

#     def transform_to_qa_format(self):
#         qa_data = []
#         for vessel in self.data:
#             vessel_name = vessel["Vessel_Name"]
#             identification_features = vessel["Identification_features"]
#             feature_explanation = vessel["Feature_explanation"]
#             identification_process = vessel["Identification_process"]["content"]

#             # 创建判读特征及其重要性得分的问答对
#             features_qa = {
#                 "input": f"{vessel_name}的识别特征有哪些？哪些识别特征更重要？",
#                 "output": "；".join([f"{feature_info['feature']}，满分5分的话，该特征的重要性得分为{feature_info['score']}"
#                                for feature_info in identification_features.values()])
#             }

#             # 创建特征描述的问答对
#             explanation_qa = {
#                 "input": f"进行详细分析，帮助我理解{vessel_name}的识别特征",
#                 "output": "".join([f"{info['feature']}：{feature_explanation[info_id]}"
#                                for info_id, info in identification_features.items()])
#             }

#             # 创建判读流程的问答对
#             process_qa = {
#                 "input": f"{vessel_name}的识别流程是什么？",
#                 "output": identification_process
#             }

#             # 将问答对加入到列表中
#             qa_data.append(features_qa)
#             qa_data.append(explanation_qa)
#             qa_data.append(process_qa)
        
#         return qa_data

#     def save_json(self, output_path, json_data):
#         with open(output_path, 'w', encoding='utf-8') as json_file:
#             json.dump(json_data, json_file, ensure_ascii=False, indent=4)
