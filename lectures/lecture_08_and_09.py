from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 07: 上下文有关文法与线性有界自动机")

    context_sensitive_grammar()
    turing_machine()
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
    text("S→aSA∣bSB∣aA∣bB")
    text("Aa→aA,Ab→bA,Ba→aB,Bb→bB")
    text("A→a,B→b")
    text("NLP中的一些语言现象，如非投影依赖（non-projective dependencies），也可以用CSG来描述。")
    text("自然语言的一部分现象超出了 CFG 的表达能力，尤其是非投影依赖、某些长距离一致性等")

    text("### 线性有界自动机")
    text("**线性有界自动机（Linear Bounded Automaton, LBA）**：是一种图灵机，其工作带的长度被输入字符串的长度线性限制。")
    text("- 形式定义：一个线性有界自动机是一个七元组($M = (Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$)，其中$Q$是状态集合，$\Sigma$是输入符号集合，$\Gamma$是带符号集合，$\delta$是转移函数，$q_0$是初始状态，$q_{accept}$是接受状态，$q_{reject}$是拒绝状态。")
    text("- LBA的工作带长度被输入字符串的长度线性限制，即工作带的长度不超过输入字符串长度的某个常数倍。")
    text("- LBA可以识别上下文有关语言，但不能识别所有的递归可枚举语言。")

def turing_machine():
    text("### 图灵机")
    text("**图灵机（Turing Machine）**：是一种抽象计算模型，用于定义可计算性和复杂性。")
    image("images/turing_machine.png", width=600)
    image("images/Turing_Machine_Model_Davey_2012.jpg", width=600)

    text("- **形式定义：**")
    image("images/turing_define.png", width=600)

    text("例子：给定一个图灵机向右扫描它的输入，寻找一个 1：")
    text("如果它找到了一个 0，继续向右扫描；")
    text("如果它找到了一个 1，将这个 1 改成 0，进入终止状态；")
    text("如果它到达了一个空符号，将空符号改成 1，然后向左移动一格，之后继续向右。")
    text("形式化的构造如下：")
    text("状态集合：$Q = \\{q_0, q_1, q_{accept}, q_{reject}\\}$")
    text("输入符号集合：$\Sigma = \\{0, 1\\}$")
    text("带符号集合：$\Gamma = \\{0, 1, \\sqcup\\}$")
    text("初始状态：$q_0$")
    text("接受状态：$q_{accept}$")
    text("拒绝状态：$q_{reject}$")
    text("转移函数：")
    text("$$\n\\delta(q_0, 0) = (q_0, 0, R)$$")
    text("$$\delta(q_0, 1) = (q_1, 0, R)$$")
    text("$$\delta(q_0, \\sqcup) = (q_0, 1, R)$$")
    text("$$\delta(q_1, 0) = (q_1, 0, R)$$")
    text("$$\delta(q_1, 1) = (q_1, 1, R)$$")

    image("images/turing_case1.png", width=600)
    text("到最后，一步也不能动了（没有对应的规则），这个图灵机停机并接受输入。")

    text("✍️：构建一个图灵机来接收语言 $$L={a^n b^n | n≥0}$$")
    text("**解决思路**是先从最左边删除一个 a，再从最右边删除一个 b，再回到最左边删除一个 a，再回到最右边删除一个 b，如此重复，如果恰好能够删光则可接受")
    image("images/turing_case2.png", width=600)

    text("✍️：构造一个图灵机，将输入字符串循环右移一位。")
    text("abba → aabb")

    text("### 递归可枚举语言（Recursively Enumerable Languages，RE）")
    text("定义停机问题（Halting Problem）如下：")
    text("输入：一个图灵机M和一个输入字符串w")
    text("问题：M在输入 w 时是否停机？")
    text("停机问题是不可判定的，也就是说，不存在一个算法能够对所有图灵机 M 和输入字符串 w 的组合，正确判断 M 在 w 上是否会停机。")

    text("证明：采用反证法。")
    text("假设存在一台图灵机 H，它可以判定停机问题。对于任意图灵机 M 和输入 x，H 都能正确判断：")
    text("如果 M 在输入 x 上会停机，那么 H 接受 ⟨M, x⟩；")
    text("如果 M 在输入 x 上不会停机，那么 H 拒绝 ⟨M, x⟩。")

    text("现在构造一台新的图灵机 H'。它的输入是某台图灵机的编码 ⟨M⟩。")
    text("H' 的行为如下：先让 H 判断 M 在输入 ⟨M⟩ 时是否会停机。")
    text("如果 H 判断“会停机”，那么 H' 就进入死循环；")
    text("如果 H 判断“不会停机”，那么 H' 就立刻停机。")
    text("也就是说，H' 的行为与 H 的判断结果正好相反。")

    text("接下来考虑让 H' 接受自己的编码 ⟨H'⟩ 作为输入。")
    text("也就是问：H' 在输入 ⟨H'⟩ 时是否会停机？")

    text("如果 H' 在输入 ⟨H'⟩ 时停机，那么根据 H 的判断，H 应该认为 H' 会停机。")
    text("但按照 H' 的定义，只要 H 认为会停机，H' 就应该进入死循环，而不应该停机。")
    text("这就产生了矛盾。")

    text("如果 H' 在输入 ⟨H'⟩ 时不停机，那么根据 H 的判断，H 应该认为 H' 不会停机。")
    text("但按照 H' 的定义，只要 H 认为不会停机，H' 就应该停机，而不应该不停机。")
    text("这同样产生了矛盾。")

    text("因此，无论哪种情况都会导致矛盾，说明最初假设的图灵机 H 不存在。")
    text("所以，停机问题是不可判定的。")

    image("images/full_picture.png", width=600)

    text("### 复杂度")
    text("**时间复杂度（Time Complexity）**：指算法执行所需的时间随输入规模的增长而增长的函数。常用大O符号表示，如 O(n)、O($n^2$) 等。")
    text("**空间复杂度（Space Complexity）**：指算法执行所需的空间（内存）随输入规模的增长而增长的函数。也用大O符号表示。")
    text("经典分析：各种排序算法的时间复杂度和空间复杂度。")


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
