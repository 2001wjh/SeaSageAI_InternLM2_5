import os
os.environ["no_proxy"] = "localhost,127.0.0.1,::1"

import openai
import gradio as gr
from dotenv import load_dotenv, find_dotenv
import requests 

# 定义全局变量，用于区分五种不同类型的舰艇
naval_vessels = ["航母", "两栖攻击舰", "驱逐舰", "护卫舰", "补给舰"]

# Google Custom Search API 配置
google_api_key = os.getenv("GOOGLE_API_KEY")
google_cse_id = os.getenv("GOOGLE_CSE_ID")

# 设置代理
proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897",
}

def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx={google_cse_id}&q={query}"
    try:
        response = requests.get(url, proxies=proxies, timeout=30)
        response.raise_for_status()
        # print("Raw response from Google Custom Search API:", response.json())
        search_results = response.json().get('items', [])
        return search_results
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    return []

def format_search_results(results):
    formatted_results = "\n\n".join([f"Title: {result['title']}\nSnippet: {result['snippet']}" for result in results])
    return formatted_results

# 定义从消息中获取回复的函数
def get_completion(messages, model="gpt-4o"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        if response and response.choices:
            message = response.choices[0].message
            if message:
                return message.content
            else:
                print("没有返回消息内容。")
        else:
            print("无效的回复或未返回选择。")
    except Exception as e:
        print(f"发生错误: {e}")
    return "对不起，发生了错误。"

# 从文件中读取系统提示内容的函数
def read_system_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 定义处理聊天输入的函数
def chat(user_input):
    print(f"用户输入: {user_input}")

    # 指定系统提示文件的路径
    system_prompt_file = f"../../../prompts/{naval_vessels[0]}/description-one-shot.txt"

    # 读取系统提示内容
    system_prompt_content = read_system_prompt(system_prompt_file)
    # print(system_prompt_content)

    # 进行Google搜索
    search_results = google_search(user_input)
    if not search_results:
        return "搜索过程中发生错误，请稍后再试。"

    formatted_results = format_search_results(search_results)
    print(formatted_results)

    # 第一次调用：整合搜索结果
    integration_context = [
        {'role': 'system', 'content': f"请整合以下内容与用户的问题相关的信息：\n{formatted_results}"},
        {'role': 'user', 'content': user_input}
    ]
    integration_response = get_completion(integration_context)

    if integration_response == "对不起，发生了错误。":
        return integration_response

    # 第二次调用：基于整合后的信息生成最终结果
    final_context = [
        {'role': 'system', 'content': system_prompt_content},
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': integration_response}
    ]
    final_response = get_completion(final_context)

    if final_response == "对不起，发生了错误。":
        return final_response

    print(f"AI 回复: {final_response}")
    return final_response

if __name__ == "__main__":
    # 加载环境变量
    _ = load_dotenv(find_dotenv(), override=True)

    client = openai.OpenAI()

    # 创建 Gradio 界面
    interface = gr.Interface(
        fn=chat,
        inputs=gr.Textbox(lines=7, label="请输入你的消息:"),
        outputs=gr.Textbox(label="回复:"),
        flagging_dir=naval_vessels[0],
        title="SeaSageAI 海军专家",
        description="与一位精通舰船分类和识别的 AI 助手聊天。"
    )

    # 启动界面
    interface.launch()
