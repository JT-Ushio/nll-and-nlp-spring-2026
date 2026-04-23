from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 07: 上下文有关文法与线性有界自动机")

    context_sensitive_grammar()
    assignment1()

def context_sensitive_grammar():
    text("### 上下文有关文法")
    image("images/chomsky_language.png", width=400)
    text("**上下文有关文法（Context-Sensitive Grammar, CSG）**：是一种形式文法，其中的产生式规则允许在非终结符的两侧都有上下文。")
    text("- 形式定义：一个上下文有关文法G是一个四元组($G = (N, \Sigma, P, S)$)，其中$N$是非终结符集合，$\Sigma$ 是终结符集合，$P$ 是产生式规则集合，$S$ 是开始符号。")
    text(r"- 产生式规则的形式：$\alpha \to \beta$，其中 $\alpha$ 和 $\beta$ 都是由非终结符和终结符组成的字符串，并且 $\alpha$ 至少包含一个非终结符。")
    text("- 上下文有关文法比上下文无关文法更强大，可以描述更多的语言，但也更复杂。")

    text("**示例：一个CSG文法无法用CFG描述**")
    text(r"- 语言$L = \\{a^n b^n c^n | n \geq 1\\}$，即由相同数量的a、b、c组成的字符串集合。")
    text("- 该语言可以由以下CSG文法生成：")
    text("S → abc | aSQ")
    text("bQc → bbcc")
    text("cQ → Qc")
    text("- 该语言无法由任何CFG生成，因为CFG无法同时保证a、b、c的数量相同。")
    image("images/csg_example.png", width=600)

    text(r"✍️：有以下文法：$G = (\{S,B,C\},\{a,b,c\},P, S)$,其中$P=$")
    text("```json\n{\n\tS → aSBC | abC, \n\tCB → BC, \n\tbB → bb, \n\tbC → bc, \n\tcC → cc\n}\n```")
    text("这个<mark>CSG</mark>文法生成的语言是什么？")

    text("质数长度语言：{$a^p$ | p is a prime number}")
    text(r"重复字符串语言：{$ww | w \in \\{a, b\\}^+$}")
    text("NLP中的一些语言现象，如中心嵌套结构（center embedding）和非投影依赖（cross-serial dependencies），也可以用CSG来描述。")


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
    text("<mark>**DDL：5月20日 24:00**</mark>")


def Q_and_A():
    text("# 问答环节：欢迎大家提问！")
    image("images/stuff.png", width=600)


if __name__ == "__main__":
    main()
