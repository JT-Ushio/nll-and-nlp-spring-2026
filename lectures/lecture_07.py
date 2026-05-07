from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 06: 上下文无关文法在NLP中的应用")

    dependency_structure()
    assignment1()

def dependency_structure():
    text("### 依存句法分析")

    text("**依存句法分析（Dependency Parsing）**：分析句子中词语之间的依存关系，构建依存句法树。")
    text("- 依存句法树是一种有向无环图，其中每个节点代表一个词语，每条边代表两个词语之间的依存关系。")

    image("images/dep_tree_intro.png", width=600)

    text("- 常见的依存关系包括：")
    image("images/dep_relations.png", width=600)

    text("依存句法分析任务是NLP的关键基础任务之一")
    image("images/dep_parsing_task.png", width=600)

    text("### 依存句法分析有两种主流算法")

    text("1. 基于图的算法：将依存句法分析问题建模为一个图结构预测问题，使用最大生成树算法来寻找最优的依存树。")
    image("images/graph_based_parsing.png", width=600)

    text("- 其关键组件包括评分函数和解码算法")
    text("- 解码算法（如Chu-Liu/Edmonds算法，最大生成树算法）用于从所有可能的依存关系中找到得分最高的合法依存树。")

    image("images/biaffine_scoring.png", width=600)
    text("- 评分函数用于评估每条可能的依存关系的得分，通常使用双仿射（biaffine）模型来计算得分。")
    text("- 🤔：如何处理有向边？")
    text("- 🤔：如何预测依存关系？")
    text("- 评分函数也可以很复杂")
    image("images/gnn_parser.png", width=600)


    text("2. 基于转移系统的算法：通过定义一套转移操作（如Shift、Reduce、Left-Arc、Right-Arc等）来构建依存树。")
    image("images/transition_system.png", width=600)
    image("images/transition_based_parsing.png", width=400)

    text("- 其关键组件在于特征抽取")
    image("images/transition_system_features.png", width=400)
    text("- 栈特征")
    text("- 队列特征")
    text("- 动作历史")


    text("- 一些有价值特征会被忽略，例如")
    image("images/meaningful_features.png", width=600)

    text("- 结构无关的语义表示 + 结构相关的指示器特征（覆盖所有信息）")
    image("images/full_features.png", width=600)

    text("### 实验结果")
    image("images/dep_parsing_res.png", width=600)
    text("- 基于图的算法通常在准确率上优于基于转移系统的算法，但后者在速度上更快。")

    text("### 如何计算依存句法树的准确率？")
    text("- Unlabeled Attachment Score (UAS)：计算正确预测的依存关系数量占总依存关系数量的比例。")
    text("- Labeled Attachment Score (LAS)：计算正确预测的依存关系及其标签数量占总依存关系数量的比例。")
    text("- 为什么UAS和LAS会有差异？ 因为有些依存关系虽然正确预测了，但标签错误了。")
    text("- 树的形态对，但标签错误了")

    image("images/uas_las.png", width=600)
    text("✍️：预测结果的UAS和LAS分数分别是？")

    text("🤔：如果一条依存边，方向预测反了，UAS和LAS会如何？")
    text("🤔：LAS是否会大于UAS？")


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

    image("images/conllu_example.png", width=600)
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

    text("### 任务②：选择<mark>一种或多种语言</mark>，使用上述转移系统中的<mark>一种或多种</mark>，输入一个转移动作序列，输出一条UD样本(一颗完整的依存树)。")
    text("- 输入： 一个json对象，包含**转移系统名称**（大小写敏感）和对应的**转移动作序列**与**依存标签序列**")
    output_format = {
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
