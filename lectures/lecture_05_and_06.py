from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 04: 正则语言在NLP中的应用")

    seq_labeling()
    context_free()
    constitunent_structure()
    pushdown_automata()

def seq_labeling():
    text("### 命名实体识别（Named Entity Recognition, NER）")

    text("**命名实体识别（NER）**：识别文本中具有特定意义的实体，如人名、地名、组织名等。")
    text("- 我们将<mark>实体（Entity）</mark>定义为具有特定意义的词或短语。")
    text("- 实体类型包括\<PER\>人名（Person）\<PER\>、\<LOC\>地名（Location）\<LOC\>、\<ORG\>组织名（Organization）\<ORG\>等。")
    text("- 例如，在句子“重庆张雪机车工业有限公司的国产820RR-RS赛车，在锦标赛葡萄牙站中取得冠军。”中：")
    text("- \<ORG\>重庆张雪机车工业有限公司\<ORG\>")
    text("- \<LOC\>葡萄牙\<LOC\>")

    text("**预测目标**：")
    text("1. 给定句子中的一个文本片段，预测它是否是一个实体。→ 多分类问题（类别固定）")
    text("$$P(\\text{实体类型} | \\text{任意的文本片段})$$，非实体片段的实体类型为None。")

    text("2. 给定一个实体类型，预测它在句子中的起始位置和结束位置。→ 多分类问题（类别不固定）")
    text("$$P(\\text{起始位置, 结束位置} | \\text{实体类型})$$，若句子中不存在该实体，则起始位置为-1，结束位置为-1。")

    text("3. 给定一个句子，预测它的BIO标签 → 序列标注问题（也是分类问题，类别固定）")
    text("$$P(\\text{BIO标签序列} | \\text{句子序列})$$，BIO标签包括B-实体类型、I-实体类型、O（非实体）。")
    text("例如，在句子“重庆张雪机车工业有限公司的国产820RR-RS赛车，在世界超级摩托车锦标赛葡萄牙站中取得冠军。”中：")
    text("| 词语 | BIO标签 |\n| :---: | :---: |\n| 重庆 | B-ORG |\n| 张雪 | I-ORG |\n| 机车 | I-ORG |\n| 工业 | I-ORG |\n| 有限公司 | I-ORG |\n| 的 | O |\n| 国产 | O |\n| 820RR-RS | O |\n| 赛车 | O |\n| ， | O |\n| 在 | O |\n| 世界 | O |\n| 超级 | O |\n| 摩托车 | O |\n| 锦标赛 | O |\n| 葡萄牙 | B-LOC |\n| 站 | O |\n| 中 | O |\n| 取得 | O |\n| 冠军 | O |\n")

    text("**三种方式的优缺点**：")
    text("| 方式 | 标签数量 | 执行次数 |\n| :---: | :---: | :---: |\n| 1. 实体类型预测 | 实体类型数量 + 1（None） | L*L |\n| 2. 起始位置和结束位置预测 | L+L | 2 |\n| 3. BIO标签序列预测 | 实体类型数量*2 + 1 | L |\n")

    text("🤔：如果一个句子里有多个相同类型的实体，三种方式会怎么样？")
    text("🤔：如果训练和测试的句子不同长度（测试>训练中的最大长度），方案2会怎么样？")
    text("🤔：如果发生实体嵌套（比如张雪也是人名），三种方式会怎么样？")
    text("🤔：如果发生实体交叉，三种方式会怎么样？")

    text("**预测非法**：")
    text("- 方案2：预测的起始位置或结束位置超出句子长度，或者起始位置大于结束位置。")
    text("- 方案3：预测的BIO标签序列中存在不合法的标签组合，例如I-ORG前面是O或者B-PER。")
    text("**DFA 实现方案3**：")
    text("- 模型的输出可以看做一个基于BIO字母表的字符串，DFA可以用来验证这个字符串是否接受，若接受则合法。")
    text("✍️：如何构造？")

    text("**Viterbi解码**")
    text("- 方案3中，模型输出的BIO标签序列可能不合法，我们可以使用Viterbi算法在DFA上进行解码，找到最可能的合法BIO标签序列。")
    text("- Viterbi算法是一种动态规划算法，用于在DFA状态转移系统中找到分数最高的合法序列。")
    text("- 具体步骤：")
    text("1. 初始化：对于DFA的每个状态，初始化一个分数，表示从初始状态到该状态的最高分数路径的分数。初始状态的分数为0，其他状态的分数为负无穷。")
    text("2. 递推计算：对于输入序列中的每个位置，对于DFA的每个状态，计算从前一个位置的每个状态转移到当前状态的分数，并更新当前状态的分数为最高分数。")
    text("3. 终止：在输入序列的最后一个位置，找到分数最高的接受状态，并从该状态回溯到初始状态，得到最可能的合法BIO标签序列。")

    text("### 词性标注（Part-of-Speech Tagging）")
    text("**词性标注（POS Tagging）**：为句子中的每个词语分配一个词性标签，如名词、动词、形容词等。")
    text("- 预测目标：")
    text("$$P(\\text{词性标签序列} | \\text{句子序列})$$")
    text("- 例如，在句子“我喜欢吃苹果。”中：")
    text("| 词语 | 词性标签 |\n| :---: | :---: |\n| 我 | PRON |\n| 喜欢 | VERB |\n| 吃 | VERB |\n| 苹果 | NOUN |\n| 。 | PUNCT |\n")
    text("- 词性标注也可以看做一个序列标注问题，可以使用类似于NER的DFA和Viterbi算法进行解码。")
    text("🤔：类似限定词后再接限定词这种不可能出现的情况？")
    text("🤔：基于词和基于Token的区别？")


def context_free():
    text("## 05: 上下文无关文法和下推自动机")

    text("### 上下文无关文法")
    text("- 上下文无关文法（Context-Free Grammar, CFG）是一种形式文法，用于描述上下文无关语言。")
    text("- 上下文无关文法由一个四元组 $(V, \Sigma, R, S)$ 组成：")
    text("1. $V$ 是一个有限的非终结符集合。")
    text("2. $\Sigma$ 是一个有限的终结符集合，且 $V \cap \Sigma = \emptyset$。")
    text("3. $R$ 是一个有限的产生式集合。")
    text("4. $S$ 是一个开始符号，属于 $V$。")
    text("- 产生式的形式为 $A \\rightarrow \\alpha$，其中 $A \in V$ 是一个非终结符，$\\alpha \in (V \cup \Sigma)^*$ 是一个由非终结符和终结符组成的字符串。")
    text(r"- 上下文无关文法的语言由开始符号 $S$ 生成的所有字符串组成，即 $L(G) = \\{ w \in \Sigma^* | S \Rightarrow^* w \\}$，其中 $\Rightarrow^*$ 表示通过零次或多次应用产生式从 $S$ 推导出 $w$。")
    text("- 展开（expand） : 从一个非终结符开始，根据产生式规则替换非终结符，直到得到一个由终结符组成的字符串。")
    text("- 折叠（reduce） : 从一个由终结符和非终结符组成的字符串开始，根据产生式规则替换一个子串为一个非终结符，直到得到开始符号 $S$。")

    text("以两个简单的例子来说明什么是上下文无关语法")
    text("- 例子1：假设有一种非常非常原始的语言，它的句子只有： **主语** **谓语** **宾语** 这样一种结构")
    text("- **主语** 中只有 **我**、 **你**、 **他** 三个词， **谓语** 中只有 **吃** 一个词， **宾语** 中只有 **饭**、 **菜** 两个词。")
    text("- 这个语言的上下文无关文法 $G$ 定义如下：")
    text(r"- 非终结符集合 $V = \\{S, 主语, 谓语, 宾语\\}$")
    text(r"- 终结符集合 $\Sigma = \\{我, 你, 他, 吃, 饭, 菜\\}$")
    text("- 产生式集合 $R = \\{S \\rightarrow 主语 谓语 宾语, 主语 \\rightarrow 我 | 你 | 他, 谓语 \\rightarrow 吃, 宾语 \\rightarrow 饭 | 菜\\}$")

    text("- 例子2，文法 $G$ 定义如下：")
    text(r"- 非终结符集合 $V = \\{S\\}$")
    text(r"- 终结符集合 $\Sigma = \\{a, b\\}$")
    text(r"- 产生式集合 $R = \\{S \\rightarrow aSb, S \\rightarrow \\epsilon\\}$")
    text(r"- 开始符号 $S$")
    text(r"- 这个文法生成的语言 $L(G)$ 包含所有形式为 $a^n b^n$ 的字符串，其中 $n \\geq 0$。例如：")
    text(r"- $\\epsilon$（当 $n=0$）")
    text(r"- $ab$（当 $n=1$）")
    text(r"- $aabb$（当 $n=2$）")
    text(r"- $aaabbb$（当 $n=3$）")
    text("- 以此类推。")

    text(r"✍️：构造上下文无关文法用以产生 $\\{a_1a_2...a_na_n...a_2a_1|a_i\in\\{0,1\\}, 1\le i\le n\\}$。")
    text(r"✍️：构造一个上下文无关文法，生成语言 $L = \\{a^n b^m c^n | n, m \\geq 0\\}$。")

    text("**例子3，简单算术运算**：")
    text(r"- 非终结符集合 $V = \\{E, op\\}$")
    text(r"- 终结符集合 $\Sigma = \\{0-9, +, -, *, /, (, )\\}$")
    text(r"- 产生式集合 $R = \\{E \\rightarrow E\ op\ E\ |\ (E)\ |\ \\text{[0-9]+},\\quad op \\rightarrow +\ |\ -\ |\ *\ |\ /\\}$")

    text("**语法分析**：给定一个句子和一个上下文无关文法，判断该句子是否属于该文法生成的语言，并且如果属于，给出一个或多个推导树（parse tree）。")
    text("- 例如，对于句子 12 + (53 - 7) 和上述文法，我们可以构造如下的推导树")
    image("images/syntax_3.png", width=400)
    text("- 12 + 53 * 7：分析树并不唯一")
    image("images/syntax_5.png", width=400)

    text("自上而下的语法分析：从开始符号 $S$ 开始，尝试使用产生式规则展开，直到得到输入句子。")
    text("自下而上的语法分析：从输入句子开始，尝试使用产生式规则折叠，直到得到开始符号 $S$。")
    text("- 例如，对于句子 12 + (53 - 7)，自上而下的分析可能会先尝试将 $E$ 展开为 $E op E$，然后将第一个 $E$ 展开为 $[0-9]+$，第二个 $E$ 展开为 $(E)$，以此类推。")
    text("- 对于同一句子，自下而上的分析可能会先将 $12$ 折叠为 $E$，将 $53$ 折叠为 $E$，将 $7$ 折叠为 $E$，然后将 $E - E$ 折叠为 $E$，最后将 $E + E$ 折叠为 $E$。")
    text("✍️：设文法 G 由如下规则定义：S → AB, A → Aa|bB, B → a|Sb。")
    text("- 给出下列句子形式的**推导树/解析树/分析树**: (1)baabaab (2)bBABb")

    text("**最左推导**：")
    text("- 每次选择最左边的非终结符进行展开，得到的推导树称为最左推导树。")
    text("**最右推导**：")
    text("- 每次选择最右边的非终结符进行折叠，得到的推导树称为最右推导树。")
    text("- 对于某些文法，最左推导树和最右推导树可能不同，这种现象称为文法的二义性/歧义性（ambiguity）。")
    text("- 即：存在一个字符串，它可以由两个或者更多的解析树产出。")
    text("**定理**：解析树、最左推导和最右推导是可以相互转化的，它们的表达能力是等价的。")

    text("**无法推导的变量**：")
    text("- 在上下文无关文法中，如果一个非终结符无法通过任何产生式推导出一个由终结符组成的字符串，那么这个非终结符被称为无法推导的变量。")
    text("- 例如，在文法 $G = (\\{S, A\\}, \\{a\\}, R, S)$ 中，产生式集合 $R = \\{S \\rightarrow aS | A, A \\rightarrow Aa\\}$ 中，非终结符 $A$ 无法推导出任何由终结符组成的字符串，因此 $A$ 是一个无法推导的变量。")

    text("**删除无用的符号**")
    text("- 在上下文无关文法中，如果一个符号（非终结符或终结符）无法出现在任何由开始符号推导出的字符串中，那么这个符号被称为无用的符号。")

    text("**去除空串**")
    text("- 在上下文无关文法中，如果一个非终结符 $A$ 可以推导出空串 $\epsilon$，我们可以通过以下步骤去除空串：")
    text(r"1. 找到所有可以推导出空串的非终结符，记为 $N_\\epsilon$。")
    text(r"2. 对于每个产生式 $A \\rightarrow \\alpha$，如果 $\\alpha$ 中包含 $N_\\epsilon$ 中的非终结符，我们可以生成新的产生式，通过删除 $\\alpha$ 中的这些非终结符来创建新的产生式。")
    text(r"3. 删除所有直接推导出空串的产生式 $A \\rightarrow \\epsilon$，以及所有包含 $N_\\epsilon$ 中非终结符的产生式。")
    text(r"- 例如，在文法 $G = (\\{S, A\\}, \\{a\\}, R, S)$ 中，产生式集合 $R = \\{S \\rightarrow aS | A, A \\rightarrow Aa | \\epsilon\\}$ 中，非终结符 $A$ 可以推导出空串 $\epsilon$，因此我们可以生成新的产生式 $S \\rightarrow aS | A | a$，并删除 $A \\rightarrow \\epsilon$ 和 $A \\rightarrow Aa$，最终得到新的文法 $G' = (\\{S, A\\}, \\{a\\}, R', S)$，其中 $R' = \\{S \\rightarrow aS | A | a, A \\rightarrow Aa\\}$。")

    text("**去除单元产生式**")
    text("- 在上下文无关文法中，如果一个产生式 $A \\rightarrow B$ 满足 $A$ 和 $B$ 都是非终结符，且 $B$ 可以推导出一个由终结符组成的字符串，那么这个产生式被称为单元产生式。")
    text("- 去除单元产生式的步骤：")
    text(r"1. 找到所有单元产生式。")
    text(r"2. 对于每个单元产生式 $A \\rightarrow B$，如果 $B$ 可以推导出一个由终结符组成的字符串，我们可以用 $B$ 的所有产生式替换 $A \\rightarrow B$。")
    text(r"3. 删除所有单元产生式。")

    text("**乔姆斯基范式**")
    text("- 乔姆斯基范式（Chomsky Normal Form, CNF）是一种特殊的上下文无关文法形式，其中每个产生式要么是 $A \\rightarrow BC$ 的形式（两个非终结符），要么是 $A \\rightarrow a$ 的形式（一个终结符）。")
    text("- 将任意上下文无关文法转换为乔姆斯基范式的过程包括：")
    text(r"1. 去除空串。")
    text(r"2. 去除单元产生式。")
    text(r"3. 将其他产生式转换为适当的格式。")
    text(r"- 例如，在文法 $G = (\\{S, A\\}, \\{a\\}, R, S)$ 中，产生式集合 $R = \\{S \\rightarrow aS | A, A \\rightarrow Aa | \\epsilon\\}$ 中，非终结符 $A$ 可以推导出空串 $\epsilon$，因此我们可以生成新的产生式 $S \\rightarrow aS | A | a$，并删除 $A \\rightarrow \\epsilon$ 和 $A \\rightarrow Aa$，最终得到新的文法 $G' = (\\{S, A\\}, \\{a\\}, R', S)$，其中 $R' = \\{S \\rightarrow aS | A | a, A \\rightarrow Aa\\}$。")

    text("**练习：判断文法是否为CNF**：")
    text(r"1. $G_1 = (\\{S, A, B\\}, \\{a, b\\}, R_1, S)$，其中 $R_1 = \\{S \\rightarrow AB, A \\rightarrow a, B \\rightarrow b\\}$")
    text(r"2. $G_2 = (\\{S, A\\}, \\{a\\}, R_2, S)$，其中 $R_2 = \\{S \\rightarrow AA, A \\rightarrow aA | a\\}$")
    text(r"3. $G_3 = (\\{S, A, B\\}, \\{a, b\\}, R_3, S)$，其中 $R_3 = \\{S \\rightarrow AB | a, A \\rightarrow a, B \\rightarrow b\\}$")


def constitunent_structure():
    text("### 句法分析（Constituent Structure）")
    text("- 句法分析是自然语言处理中的一个重要任务，旨在分析句子的结构，识别句子中的成分（constituents）以及它们之间的关系。")
    text("- 句法分析的结果通常表示为一个树形结构，称为句法树（parse tree），其中每个节点代表一个成分，每个边代表成分之间的关系。")
    text("- 例如:")
    image("images/constituent_tree_ex.png", width=600)
    text("- 句法树中的每个节点代表一个成分，例如：")
    text("- S：句子（Sentence）")
    text("- NP：名词短语（Noun Phrase）")
    text("- VP：动词短语（Verb Phrase）")
    text("- 根据不同成分之间是否可以进行相互替代而不会影响句子语法正确性，可以进一步地将成分进行分类，某一类短语就属于一个句法范畴（Syntactic Category）。")
    text("- 比如“一本小说”、“一所大学”等都属于一个句法范畴：名词短语（None Phrase，NP）。")
    text("- 句法范畴不仅仅包含名词短语（NP）、动词短语（VP）、介词短语（PP）等短语范畴，也包含名词（N）、动词（V）、形容词（Adj）等词汇范畴。除此之外还包含功能范畴（包括冠词、助动词等）。")
    text("- 句法范畴之间不是完全对等的，而是具有层级关系。")
    text("- 例如：一个句子可以由一个名词短语和一个动词短语组成，一个名词短语可以由一个限定词和一个名词组成，一个动词短语又可以由一个动词和一个名词短语组成。")
    text("- 句法分析可以帮助我们理解句子的结构和意义，例如：")
    text("- 识别主语、谓语和宾语等基本成分。")
    text("- 理解句子中的修饰关系，例如形容词修饰名词，副词修饰动词等。")
    text("- 解析复杂句子中的从句和主句之间的关系。")

    text("CYK 算法（CYK 是 Cocke–Younger–Kasami 的缩写，有时也称为 CKY）是基于动态规划思想的自底向上语法分析算法")
    text("- CYK算法要求所使用的语法必须符合乔姆斯基范式")
    text("- 根据 CNF 语法形式，句法树的叶子节点为单词，单词的父节点为词性符号，在词性符号层之上每一个非终结符都有两个子节点。因此 CYK 算法采用了二维矩阵对整个树结构进行编码。")
    text("- 对于一个长度为 n 的句子，构造一个 (n + 1) × (n + 1) 的**二维矩阵 T**")
    text("- 矩阵主对角线以下全部为 0，主对角线上的元素由输入句子的终结符号(单词)构成")
    text("- **主对角线以上的元素T[i,j]**包含由文法G的非终结符构成的集合，这个集合表示输入句子中横跨在位置i到j之间的单词的组成成分。")

    image("images/cky_algo.png", width=600)

    text("- 输入句子中索引从0开始，索引位于输入句子的单词之间，也可以看成单词之间的间隔指针")
    text("例如：0 她 1 喜欢 2 跳 3 芭蕾 4")
    image("images/cky_step.png", width=600)


    text("**移进-归约成分句法分析算法**：")
    text("- 基本思想是从左到右扫描输入的包含单词词性对的句子，使用堆栈和一系列的移进（Shift）和归约（Reduce）操作序列构建句法树")
    text("- 算法初始时堆栈S为空，队列Q中包含整个句子所有单词。在算法结束时堆栈S中包含一个完整的句法树，队列Q为空。所采用的操作包含以下四个：")
    text("1. 移进（Shift）：将非空队列Q最左端的单词移入堆栈S中。")
    text("2. 归约（Reduce）：根据推导规则，根据推导规则右侧所包含非终结符数量，将堆栈S中的最顶端相应数量元素移出，然后将利用推导规则产生的新结构压入堆栈中.")
    text("3. 接受（Accept）：队列中所有单词都已被移到堆栈中，并且堆栈中只剩下一个由非终结符S为根的树，表示分析成功，算法结束。")
    text("4. 拒绝（Reject）：队列中所有单词都已被移到堆栈中，但是堆栈中并非只有一个以非终结符S为根的树，并且无法继续归约，表示分析失败，算法结束。")
    image("images/transition_parsing.png", width=600)

    text("🤔：为了判断当前应该执行什么动作，你会如何抽取特征？")

def pushdown_automata():
    text("### 下推自动机")
    text("- 下推自动机（Pushdown Automaton, PDA）是一种比有限自动机更强大的计算模型，可以识别上下文无关语言。")
    text("- 下推自动机由一个七元组 $(Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$ 组成：")
    text("1. $Q$ 是一个有限**状态**集合。")
    text("2. $\Sigma$ 是一个有限**输入符号**集合（字母表）。")
    text("3. $\Gamma$ 是一个有限**栈符号**集合。")
    text("4. $\delta$ 是一个**转移函数**，定义了在状态 $q$ 接收输入符号 $a$（或空输入 $\epsilon$）并且栈顶符号为 $X$ 时，可以转移到哪些状态并且对栈进行什么操作。")
    text(r"$$\delta: Q \times (\Sigma \cup \\{\\epsilon\\}) \times \Gamma \rightarrow \\mathcal{P}(Q \times \\Gamma^*)$$")
    text("转移函数接收 3 个参数：")
    text("- 一个状态 $q\in Q$，表示当前状态。")
    text("- 一个输入符号 $a\in\Sigma\cup\{\epsilon\}$，表示当前读取的输入。")
    text("- 一个栈顶符号 $Z\in\Gamma$，表示当前栈顶的符号。")
    text(r"$$\delta(q, a, Z)=\{(p, \alpha) \mid p \in Q, \alpha \in \Gamma^*\}$$")
    text("表示PDA可以在处于状态$q$，接收输入$a$，并且观察到栈顶元素为$Z$的时候：")
    text("- 状态更新为$p$")
    text("- 从输入首部接收一个字符$a$。")
    text(r"- 栈顶元素$Z$替换为序列$\alpha$")
    text("5. $q_0 \in Q$ 是**初始状态**。")
    text("6. $Z_0 \in \Gamma$ 是**初始栈符号**。")
    text("7. $F \subseteq Q$ 是**接受状态**集合。")

    image("images/pda_demo.png", width=600)

    text("- 下推自动机的运行：")
    text("1. 初始状态为 $q_0$，初始栈符号为 $Z_0$。")
    text("2. 在每一步，自动机根据当前状态、输入符号（或空输入）和栈顶符号，根据转移函数 $\delta$ 转移到新的状态，并且对栈进行相应的操作（如弹出栈顶符号、推入新的符号等）。")
    text("3. 当输入字符串被完全读取，并且自动机处于接受状态时，输入字符串被接受。")

    text("- 下推自动机可以用来识别上下文无关语言，例如：")
    text(r"1. 语言 $L = \\{0^n 1^n | n \\geq 1\\}$ 可以由一个下推自动机识别，该自动机会在读取 $0$ 时将一个符号推入栈中，在读取 $1$ 时弹出一个符号，最后当输入被完全读取且栈为空时接受。")
    text("- 状态转移图如下：")
    image("images/pda_example1.png", width=600)

    text("- PDA接收输入示例如下：")
    image("images/pda_example2.png", width=600)

    text("接收过程也可以用列表表达式描述：")
    text(r"$$\left(q, 000111, Z_0\right) \vdash\left(q, 00111, X Z_0\right) \vdash\left(q, 0111, X X Z_0\right) \vdash\left(q, 111, X X X Z_0\right) $$")
    text(r"$$\vdash\left(p, 11, X X Z_0\right) \vdash\left(p, 1, X Z_0\right) \vdash\left(p, \varepsilon, Z_0\right) \vdash\left(f, \varepsilon, Z_0\right)$$")

    text("✍️：如果输入字符串为 `0001111` 呢？")
    text("🤔：S → 0S1 | 01，这种产生式形式如何用下推自动机实现？")

    text(r"2. ✍️：语言 $L = \\{a^n b^m c^n | n, m \\geq 0\\}$ 可以由一个下推自动机识别，该自动机会在读取 $a$ 时将一个符号推入栈中，在读取 $b$ 时不对栈进行操作，在读取 $c$ 时弹出一个符号，最后当输入被完全读取且栈为空时接受。")


def Q_and_A():
    text("# 问答环节：欢迎大家提问！")
    image("images/stuff.png", width=600)


if __name__ == "__main__":
    main()
