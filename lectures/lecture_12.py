from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 12: 语义角色标注")

    semantic_role_labeling()
    assignment1()

def semantic_role_labeling():
    text("### 语义角色标注")
    text("**语义角色标注（Semantic Role Labeling, SRL）**：是自然语言处理中的一项重要任务，旨在识别句子中每个谓词的语义角色，并为这些角色分配相应的标签。")
    text("- **形式定义**：给定一个句子和其中的谓词，SRL任务是为每个谓词识别其论元（arguments），并为每个论元分配一个语义角色标签。")
    text("- **通俗理解**：句子中谓词是对主语的陈述或说明，指出“做什么”、“是什么”或“怎么样，代表了一个事件的核心，跟谓词搭配的名词称为论元。语义角色是指论元在动词所指事件中担任的角色。")
    text("- **常见的语义角色标签**包括：施事者（Agent）、受事者（Patient）、客体（Theme）、经验者（Experiencer）、受益者（Beneficiary）、时间（Time）、工具（Instrument）、处所（Location）、目标（Goal）和来源（Source）等。")
    image("images/semantic_role_labeling.png", width=600)

    text("传统的SRL系统大多建立在句法分析基础之上，通常包括5个流程：")
    text("1. 构建一棵句法分析树。")
    text("2. 从句法树上识别出给定谓词的候选论元。")
    text("3. 候选论元剪除；一个句子中的候选论元可能很多，候选论元剪除就是从大量的候选项中剪除那些最不可能成为论元的候选项。")
    text("4. 论元识别：这个过程是从上一步剪除之后的候选中判断哪些是真正的论元，通常当做一个二分类问题来解决。")
    text("5. 对第4步的结果，通过多分类得到论元的语义角色标签。")
    image("images/dep_parsing4srl.png", width=600)

    text("可以看到，句法分析是基础，并且后续步骤常常会构造的一些人工特征，这些特征往往也来自句法分析。")

    text("🤔：依赖句法分析的缺点？")
    text("- 句法分析的错误会传播到后续的SRL步骤，导致整体性能下降。")
    text("- SRL只用了部分的句法树信息。")


    text("- 为了降低问题的复杂度，同时获得一定的句法结构信息，“浅层句法分析”的思想应运而生。")
    text("- 浅层句法分析也称为部分句法分析（partial parsing）或语块划分（chunking）。")
    text("- 基于语块的SRL方法将SRL作为一个序列标注问题来解决。")
    image("images/bio_srl_example.png", width=600)

    link(title="基于LLM的SRL方法", url="https://arxiv.org/pdf/2506.05385v1")
    image("images/llm_srl.png", width=600)
    image("images/llm_srl2.png", width=800)

    image("images/llm_srl_method1.png", width=400)
    image("images/llm_srl_method2.png", width=400)
    image("images/llm_srl_method3.png", width=400)

    image("images/llm_srl_method4.png", width=400)
    image("images/llm_srl_method5.png", width=400)
    image("images/llm_srl_method6.png", width=400)
    image("images/llm_srl_method7.png", width=400)

    image("images/llm_srl_method8.png", width=400)

    image("images/llm_srl_res1.png", width=600)
    image("images/llm_srl_res2.png", width=600)
    image("images/llm_srl_res3.png", width=600)


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
