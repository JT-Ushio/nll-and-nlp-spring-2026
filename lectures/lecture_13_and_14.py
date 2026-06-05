from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 13: 思维链与大语言模型中的逻辑涌现")

    chain_of_thought()
    assignment1()

def chain_of_thought():
    text("### 思维链")
    text("**思维链（Chain of Thought, CoT）**：是一种在大语言模型中引导模型进行复杂推理的技术，通过生成中间推理步骤来提高模型解决复杂问题的能力。")
    text("- **基本思想**：在回答复杂问题时，直接生成最终答案可能会导致模型跳过重要的推理步骤，或者在推理过程中犯错。思维链通过引导模型生成一系列中间步骤，使得模型能够逐步推理，从而提高最终答案的准确性。")
    text("- **实现方式**：通常通过在提示中加入示例，展示如何从问题出发，逐步推理到答案。例如，在数学问题中，可以展示如何从题目中的已知条件出发，逐步进行计算，最终得出答案。")
    text("- **效果**：研究表明，使用思维链技术可以显著提高大语言模型在数学推理、逻辑推理等复杂任务上的表现。")

    link(title="思维链的原始论文，Google Brain，2023", url="https://arxiv.org/pdf/2201.11903")
    image("images/zero_shot.png", width=600)
    image("images/chain_of_thought.jpg", width=600)
    image("images/chain_of_thought2.jpg", width=600)

    image("images/cot_intro.png", width=480)
    image("images/cot_multi_tasks.png", width=480)

    image("images/cot_res1.png", width=480)
    image("images/cot_res2.png", width=480)
    image("images/cot_res3.png", width=480)
    image("images/cot_res4.png", width=600)
    image("images/cot_res5.png", width=480)

    link(title="零样本思维链，Google Brain+东京大学，2023", url="https://arxiv.org/pdf/2405.14101")
    image("images/zero_shot_cot1.jpg", width=600)
    image("images/zero_shot_cot2.jpg", width=600)

    image("images/zero_cot_res1.png", width=600)
    image("images/zero_cot_res2.png", width=600)
    image("images/zero_cot_res3.png", width=600)

    link(title="自我纠正+投票机制，Google Brain，2023", url="https://arxiv.org/abs/2203.11171")

    image("images/vote_cot.jpg", width=600)

    image("images/vote_cot_res1.png", width=600)
    image("images/vote_cot_res1.png", width=600)
    image("images/vote_cot_res1.png", width=600)

    text("🤔：你还能想到哪些其他的思维链变体吗？")
    link(title="思维链的其他变体", url="https://vxc3hj17dym.feishu.cn/wiki/IPoVw9QBRiJNPdkowUBcYWdTn1e")


    text("### 心理学的类比")
    text("- 在《思考，快与慢》（Thinking, Fast and Slow）一书中，丹尼尔・卡尼曼（Daniel Kahneman 基于「认知双系统理论」（dual process theory），将人类的思维方式划分为两种模式：快思考和慢思考")
    text("- 快思考（System 1）是自动的、快速的、无意识的思维过程，适用于日常生活中的简单决策和反应。")
    text("- 慢思考（System 2）是有意识的、缓慢的、需要努力的思维过程，适用于复杂问题的分析和推理。")
    text("- 由于快速思维易于启动且更为省力，它往往成为决策主导，但这通常以牺牲准确性与逻辑性为代价。它天然依赖于人脑的「认知捷径」（即启发式方法 heuristics），进而容易产生错误与偏差。而通过有意识地放慢思维速度，给予更多反思、改进与分析的时间，可以激活慢速思维，挑战直觉，从而做出更具理性与准确性的决策。")

    text("### 计算是一种资源")
    text("- 神经网络可以通过它们在一次前向推理中可以访问的计算量和存储量来表征")
    text("- 优化过程（如梯度下降）将确定如何将这些资源组织成计算和信息存储的电路。")
    text("- 如果设计一个在测试时能进行更多计算的架构或系统，并训练它有效地使用这个资源，它将会很有效。")
    text("- Transformer 模型中，模型为每个生成的 token 所做的计算量（flops）大约是参数数量的 2 倍。")
    text("- 对于稀疏模型（如专家混合模型MoE），每次前向推理中只有一部分参数被使用，因此计算量 = 2 * 参数 / 稀疏度，其中稀疏度是激活的专家的比例。")
    text("- **思维链**使模型能够对它试图计算的答案的每个标记执行更多的浮点运算。它有一个很好的特性，允许模型根据问题的难度使用不同数量的计算。")

    text("### 通过Token来思考")
    text("- 早期的 CoT 推理改进工作涉及对人类编写的推理轨迹或经过答案正确性筛选的模型编写轨迹进行监督学习，后者可以被视为一种原始的强化学习（RL）形式")
    text("- 更直接的，强化学习微调")

    text("### RLHF（Reinforcement Learning with Human Feedback）")
    text("- RLHF 是一种训练方法，结合了强化学习和人类反馈，以优化模型的行为，使其更符合人类的期望和需求。")
    text("- 过去几年里各种 LLM 根据人类输入提示 (prompt) 生成多样化文本的能力令人印象深刻。然而，对生成结果的评估是主观和依赖上下文的.")
    text("- 例如，我们希望模型生成一个有创意的故事、一段真实的信息性文本，或者是可执行的代码片段，这些结果难以用现有的基于规则的文本生成指标来衡量。")
    text("- 现有的预训练语言模型通常以预测下一个单词的方式和简单的损失函数 (如交叉熵) 来建模，没有显式地引入人的偏好和主观意见。")

    text("- 用生成文本的人工反馈作为性能衡量标准，或者更进一步用该反馈作为损失来优化模型，这就是 RLHF 的思想")
    text("- RLHF 使得在一般文本数据语料库上训练的语言模型能和复杂的人类价值观对齐。")
    image("images/rlhf_intro.png", width=600)
    image("images/rlhf_res.png", width=600)

    text("- RLHF的步骤：")
    text("1. 预训练&SFT：首先在大规模文本数据上预训练一个语言模型，使其具备基本的语言理解和生成能力。")
    text("2. 收集人类反馈：通过让人类评审员对模型生成的文本进行评价，收集关于文本质量、相关性、创造性等方面的反馈。这些反馈可以是评分、排名或者具体的改进建议。")
    text("3. 训练奖励模型：使用收集到的人类反馈来训练一个奖励模型，该模型能够预测人类对生成文本的评价。奖励模型的输入是模型生成的文本，输出是一个分数，表示文本的质量或相关性。")
    text("4. 强化学习优化：使用强化学习算法（如 Proximal Policy Optimization, PPO）来优化语言模型，使其生成的文本能够获得更高的奖励模型分数。通过不断迭代，模型逐渐学会生成更符合人类期望的文本。")
    image("images/rlhf_steps.png", width=600)
    image("images/rm_training_loss.png", width=600)
    image("images/reward_func.png", width=600)

    text("🤔：为什么会有后面这一项？")

    text("- 避免RL偏离：RLHF的一个挑战是，强化学习优化可能会导致模型生成的文本偏离预训练阶段学到的语言模式，从而产生不自然或不连贯的文本。")
    text("- PPO=**近端**策略优化（Proximal Policy Optimization），是一种强化学习算法，旨在通过限制每次更新的幅度来避免模型生成文本的质量下降。")

    image("images/rlhf_res2.png", width=600)
    image("images/rlhf_res3.png", width=600)
    image("images/rlhf_res4.png", width=600)
    image("images/rlhf_res5.png", width=600)
    image("images/rlhf_label.png", width=800)
    image("images/rlhf_human.png", width=480)

    image("images/pretraining.png", width=600)
    image("images/reward-model.png", width=600)
    image("images/rlhf.png", width=600)

    image("images/smol-r1.png", width=600)
    image("images/smol-r1-2.png", width=600)
    image("images/smol-r1-res1.png", width=600)
    image("images/smol-r1-res2.png", width=600)
    image("images/smol-r1-res3.png", width=600)



def assignment1():
    text("## Assignment 1: 基于转移系统的依存句法树序列化")

    text("### 数据集：[Universal Dependencies 2.7](https://huggingface.co/datasets/albertvillanova/universal_dependencies) (UDv2.7)树库")
    link(title="[通用依存树库项目]", url="https://universaldependencies.org/")
    text("- 104种语言")
    text("- 依存句法树以[CoNLL-U格式](https://universaldependencies.org/format.html#syntactic-annotation)提供，每行包含一个词语及其相关信息（如词性、依存关系等）。")
    text("数据集加载环境（tested）：")
    text("```python\n pip install datasets==2.17.1 \n pip install conllu==6.0.0 \n```\n")

    text("### 四种**可选**转移系统的定义")
    text("1. Arc-Standard系统：使用Shift、Left-Arc、Right-Arc三种操作来构建依存树。")
    image("images/arc_standard.png", width=400)

    text("2. Arc-Eager系统：使用Shift、Left-Arc、Right-Arc、Reduce四种操作来构建依存树。")
    image("images/arc_eager.png", width=400)

    text("3. Arc-Hybrid系统：使用Shift、Left-Arc、Right-Arc三种操作来构建依存树，但在某些情况下允许提前建立依存关系。")
    image("images/arc_hybrid.png", width=400)

    text("4. Non-Projective Arc-Hybrid系统：在Arc-Hybrid系统的基础上增加了处理非投影依存关系的能力。")
    image("images/np_arc_hybrid.png", width=400)

    text("✍️：示例依存树分别对应的四种转移系统序列是？")

    text("### 任务①：选择<mark>一种或多种语言</mark>，使用上述转移系统中的<mark>一种或多种</mark>，将UD树库中的依存句法树序列化为转移操作序列。")
    text("即：输入一条UD样本(一颗完整的依存树)，输出其对应的转移操作动作序列。")
    text("- 输入： `dataset['test'][0]` ")
    text("- 输出： 一个json对象，包含**转移系统名称**（大小写敏感）和对应的**转移动作序列**与**依存标签序列**")
    output_format = {
        "transition_system": "Arc-Standard",
        "actions": ["sh", "la", "sh", "sh", "ra", ...],
        "labels": ["", "nsubj", "", "", "obj", ...],
    } # @inspect output_format

    text("### 任务②：选择<mark>一种或多种语言</mark>，输入一个转移动作序列，输出一条UD样本(一颗完整的依存树)。")
    text("- 输入： 一个json对象，包含**转移系统名称**（大小写敏感）和对应的**转移动作序列**与**依存标签序列**")
    input_format = {
        "transition_system": "Arc-Standard",
        "actions": ["sh", "la", "sh", "sh", "ra", ...],
        "labels": ["", "nsubj", "", "", "obj", ...],
    } # @inspect output_format
    text("- 输出： `dataset['test'][0]` ")

    text("提交：飞书文档包含**实验配置**和**转移操作动作序列生成代码**")
    text("实验报告包含至少<mark>2个结论</mark>")
    text("可探究问题：")
    text("- 不同语言、不同领域的依存关系分布是否存在差异？")
    text("- 不同长度范围下，依存关系分布是否存在差异？")
    text("- 不同转移系统的成功率如何？若存在失败的句子，可以手动分析一条例句，解释为什么失败")
    text("🤔：什么情况下会出现失败？")
    text("- 统计平均依存距离（Average Dependency Distance）在不同语言、不同领域、不同标签范围下的分布情况。")
    text("- 统计不同依存标签的平均出现时刻比例，为什么有些依存关系比其他关系更早出现？")
    text("- ......")
    text("输入输出格式检查脚本：下次课提供")
    text("Copilot CLI作业演示：下次课提供")
    text("<mark>**DDL：5月27日 24:00**</mark>")


def Q_and_A():
    text("# 问答环节：欢迎大家提问！")
    image("images/stuff.png", width=600)


if __name__ == "__main__":
    main()
