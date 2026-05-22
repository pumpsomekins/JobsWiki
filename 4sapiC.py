import os
import time
import openai

# 基础配置
api_key = "sk-eO6YaNyvsoXPlU9plEDi57MaQMF9RxZle2Y9XhsfH07HoFpc"
base_url = "https://4sapi.com/v1"
model_list = ["deepseek-v4-pro"]

client = openai.OpenAI(api_key=api_key, base_url=base_url)

input_filename = "4sapi命令.txt"
output_filename = "4sapi回答.md"

# 1. 严格检查并读取生产指令文件
if not os.path.exists(input_filename):
    print(f"❌ 生产环境错误：未找到输入文件【{input_filename}】。请先创建并写入指令。")
    exit(1)

with open(input_filename, "r", encoding="utf-8") as f:
    prompt = f.read().strip()

if not prompt:
    print(f"❌ 生产环境错误：【{input_filename}】内容为空，终止执行。")
    exit(1)

# 2. 核心生产管线：读取指令 -> 计时请求 -> 导出生产结果
# 投产推荐使用 'w' 模式，每次运行自动刷新为最新的命令回答（如需历史累加可改为 'a'）
with open(output_filename, "w", encoding="utf-8") as out_file:
    
    for model_name in model_list:
        print(f"🚀 正在处理生产指令 [模型节点: {model_name}] ...")
        
        try:
            # 精准记录生产耗时开始
            start_time = time.time()

            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,        # 投产使用 0 确保输出结果的高确定性和稳定性
                max_tokens=10000      # 预留足够的极限输出空间
            )

            # 精准记录生产耗时结束
            elapsed_time = time.time() - start_time
            reply = response.choices[0].message.content

            # 结构化同步到本地生产文件
            out_file.write(f"# 🤖 生产任务输出报告\n\n")
            out_file.write(f"* **执行模型:** {model_name}\n")
            out_file.write(f"* **任务用时:** {elapsed_time:.2f} 秒\n\n")
            out_file.write(f"--- \n\n")
            out_file.write(f"## 📝 最终回答内容\n\n{reply}\n")

            print(f"✅ 任务处理成功！用时: {elapsed_time:.2f} 秒")

        except Exception as e:
            error_msg = f"❌ 生产任务执行失败 [模型: {model_name}]: {e}"
            print(error_msg)
            out_file.write(f"# ❌ 生产任务执行失败\n\n**错误细节:** {e}\n")

print(f"🎉 生产任务流程结束，结果已写入: 【{output_filename}】")