from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 03: 正则语言与有限状态自动机")

    background()
    finite_automata()
    regular_expression()

def background():
    text("### 形式语言与自动机")

    text("**形式语言（Formal Languages）**：由形式语法生成的语言。")
    text("- 我们将<mark>语言（Language）</mark>定义为<mark>字符串（String）</mark>的集合。")
    text("- 字符串定义为<mark>符号（Symbol）</mark>的序列，例如 cat，dog，house。")
    text("- 所有可能出现的符号是由这个语言的<mark>字母表（Alphabet，$\Sigma$）</mark>定义。")
    text("- if $\Sigma$ = {a, b}，则字符串可以是 a、b、aa、ab、ba、bb、aaa、aab、...")
    text("- 习惯上，我们会用 u，v，w 等靠后的字母表示字符串，例如 u = ab ，v = bbbaaa，w = abba 。")


def finite_automata():
    text("### 有穷自动机（Finite Automata, FA）")
    text("- 有穷自动机是一个形式系统，它只记忆有限的信息量，这些信息量通过它的<mark>状态（State）</mark>表示。")
    text("- 当有<mark>输入（Input）</mark>给到有穷自动机的时候，它会相应地改变自己的状态。")
    text("- 告诉FA如何根据输入以及当前状态来改变到新状态的一系列规则，被称为<mark>转移函数（Transfer Function）</mark>")
    text("- 当FA转移到一个<mark>接受/终止状态（Accepting State）</mark>，我们就说这个输入被FA接受/FA终止了。")

    text("- 有穷自动机的基本要素有：")
    text("1. 有限个状态（图上的结点）")
    text("2. 状态间的转移函数（图上的边）")
    text("3. 一个初始状态（图上start箭头指向的结点）")
    text("4. 一个或多个接受状态（图上的双环结点）")

    text("### 确定性有穷自动机（Deterministic Finite Automaton, DFA）")
    text("<mark>**定义**</mark>：确定性有穷自动机为一个五元组：")
    text("$$M = (Q, \Sigma, \delta, q_0, F)$$")
    text("- $Q$ 是一个有限状态集合。")
    text("- $\Sigma$ 是一个有限输入符号集合（字母表）。")
    text(r"- $\delta: Q \times \Sigma \rightarrow Q$ 是一个转移函数，定义了在状态 $q$ 接收输入符号 $a$ 后转移到哪个状态。")
    text("- $q_0 \in Q$ 是初始状态。")
    text("- $F \subseteq Q$ 是接受状态集合。")
    text("**DFA的工作原理**：")
    text("- DFA 从初始状态 $q_0$ 开始，逐个读取输入字符串中的符号。")
    text("- 对于每个输入符号 $a$，DFA 根据转移函数 $\delta$ 从当前状态 $q$ 转移到下一个状态 $q^\prime = \delta(q, a)$。")
    text("- 当输入字符串被完全读取后，如果DFA停在一个接受状态（即 $q \in F$），则输入字符串被接受；否则被拒绝。")

    text("✍️：习题：下列DFA识别什么语言？")
    image("images/dfa_example.png", width=600)

    text("### 非确定性有穷自动机（Nondeterministic Finite Automaton, NFA）")
    text("<mark>**定义**</mark>：非确定性有穷自动机为一个五元组：")
    text("$$M = (Q, \Sigma, \delta, q_0, F)$$")
    text("- $Q$ 是一个有限状态集合。")
    text("- $\Sigma$ 是一个有限输入符号集合（字母表）。")
    text(r"- $\delta: Q \times \Sigma \rightarrow \mathcal{Q}$ 是一个转移函数，定义了在状态 $q$ 接收输入符号 $a$ 后可以转移到<mark>哪些</mark>状态$\\{q_i, q_j, \cdots\\}$。")
    text(r"- 对于每个输入符号 $a$，NFA 根据转移函数 $\delta$ 从当前状态 $q$ 转移到下一组状态 $\delta(q, a)\to \\{q_i, q_j, \cdots\\}$。")
    text("- $q_0 \in Q$ 是初始状态。")
    text("- $F \subseteq Q$ 是接受状态集合。")

    text("**示例：在棋盘上移动**")
    text("- 有一个3*3的棋盘，棋子只能向红色（r）或向黑色（b）格子移动。")
    text("- 状态表示棋子所在的位置，输入符号表示移动的方向（r或b），起始位置是1，终止位置是9。")
    image("images/nfa_example_task.png", width=300)
    image("images/nfa_example_table.png", width=400)

    text("**NFA和DFA的关系**：")
    text("- NFA和DFA在表达能力上是等价的，即对于任何NFA，都存在一个DFA与其等价。")
    text("- 但是，NFA在某些情况下可以更简洁地表示语言。")
    text("**示例：所有以101结尾的{0, 1}上符号串**")
    text("- DFA实现")
    text("- NFA实现")
    text("| 模型 | 转移特性 | 完备性要求 | 接受条件 | 构造难度 | 实现特性 |\n| :---: | :---: | :---: | :---: | :---: | :---: |\n| DFA | 所有转换都是确定的；| 转移函数是全函数 | 最终停在F才被接受 | 构造较难，可能需要较多状态 | 可以直接实现，执行效率高 |\n| NFA | 转换可以是非确定的 | 并非所有输入符号的转换都需要显式定义 | 只要任一路径抵达F即接受 | 通常更容易构造，表达更紧凑 | 现实中实现可能受限 |\n")
    text("- ✍️：构造一个NFA识别包含“10110”的01串。")
    text("- ✍️：构造一个NFA识别不包含“10110”的01串。")

    text("NFA和DFA在表达能力上是等价的，即对于任何NFA，都存在一个DFA与其等价。")
    text("- DFA → NFA：显然，每个DFA都是一个特殊的NFA。")
    text("- NFA → DFA：子集构造法，在DFA中，将NFA的状态集合映射为DFA中的多个状态。「不要求掌握」")
    text("- DFA最小化算法：目标是用最少的状态表示同一个DFA。「不要求掌握」")

def regular_expression():
    text("## 04: 正则语言在NLP中的应用")
    text("### 正则表达式（Regular Expression）")
    text("- 正则表达式是一种描述正则语言的工具。")
    text("- 正则表达式由字母表中的符号以及一些特殊符号组成，用于描述字符串集合。")
    text("- 例如，正则表达式 `a(b|c)*d` 描述了以 `a` 开头，以 `d` 结尾，中间可以有任意数量的 `b` 或 `c` 的字符串集合。")
    text("- 正则表达式与有限自动机之间存在等价关系：对于每个正则表达式，都存在一个等价的NFA；对于每个NFA，都存在一个等价的正则表达式。")
    text("- 正则表达式的构造方法：")
    text("1. 基本正则表达式：对于每个符号 $a \in \Sigma$，正则表达式 $a$ 描述了包含单个符号 $a$ 的字符串集合；正则表达式 $\epsilon$ 描述了只包含空字符串的集合；正则表达式 $\emptyset$ 描述了不包含任何字符串的集合。")
    text("2. 连接：如果 $R$ 和 $S$ 是正则表达式，那么 $RS$ 是一个正则表达式，描述了所有可以由 $R$ 描述的字符串后跟 $S$ 描述的字符串组成的字符串集合。")
    text("3. 选择：如果 $R$ 和 $S$ 是正则表达式，那么 $R|S$ 是一个正则表达式，描述了所有可以由 $R$ 描述的字符串或 $S$ 描述的字符串组成的字符串集合。")
    text("4. 闭包：如果 $R$ 是一个正则表达式，那么 $R^*$ 是一个正则表达式，描述了所有可以由零个或多个 $R$ 描述的字符串组成的字符串集合。")
    text("- 正则表达式的应用：")
    text("1. 文本搜索和替换：广泛用于文本编辑器和编程语言中，用于搜索和替换文本模式。")
    text("2. 词法分析：编译器使用正则表达式来定义编程语言的词法规则，从而将源代码分解成标记（tokens）。")
    text("3. 数据验证：用于验证输入数据的格式，例如验证电子邮件地址、电话号码等。")
    text("4. 网络安全：用于检测和过滤恶意输入，例如SQL注入攻击、跨站脚本攻击等。")
    text("5. 其他领域：还被应用于生物信息学、数据挖掘等领域，用于模式匹配和数据分析。")

    text("- Linux 命令行工具：如 grep、sed、awk 等，都支持正则表达式，用于文本处理和模式匹配。")
    text("- 正则表达式基本语法：")
    text("| 元字符 | 描述 |\n| :---: | :---: |\n| `.` | 匹配除换行符以外的任意单个字符 |\n| `*` | 匹配前一个元素零次或多次 |\n| `+` | 匹配前一个元素一次或多次 |\n| `?` | 匹配前一个元素零次或一次 |\n| `^` | 匹配输入字符串的开始位置 |\n| `$` | 匹配输入字符串的结束位置 |\n| `[]` | 定义一个字符类，匹配其中的任一字符 |\n| `()` | 定义一个子表达式，用于分组和捕获 |\n| `|` | 选择符，匹配左侧或右侧的表达式 |\n")
    text("- 正则表达式的扩展语法：")
    text("| 元字符 | 描述 |\n| :---: | :---: |\n| `{n}` | 匹配前一个元素恰好 n 次 |\n| `{n,}` | 匹配前一个元素至少 n 次 |\n| `{n,m}` | 匹配前一个元素至少 n 次但不超过 m 次 |\n| `\d` | 匹配任意数字字符，等价于 `[0-9]` |\n| `\w` | 匹配任意字母、数字或下划线字符，等价于 `[A-Za-z0-9_]` |\n| `\s` | 匹配任意空白字符，包括空格、制表符、换行符等 |\n| `\D` | 匹配任意非数字字符，等价于 `[^0-9]` |\n| `\W` | 匹配任意非字母、数字或下划线字符，等价于 `[^A-Za-z0-9_]` |\n| `\S` | 匹配任意非空白字符，等价于 `[^ \t\r\n\f\v]` |\n")
    text("- 正则表达式使用示例：")
    text("1. 匹配以 `a` 开头，以 `d` 结尾，中间可以有任意数量的 `b` 或 `c` 的字符串：`a(b|c)*d`")
    text("2. 匹配一个或多个数字：`[0-9]+`")
    text("3. 匹配一个有效的电子邮件地址：`[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}`")
    text("**正则表达式对应的NFA五元组：**")
    text("- 状态集合 $Q$：由正则表达式的各个子表达式构造得到的状态集合")
    text("- 输入符号集合 $\Sigma$：正则表达式中出现的所有终结符")
    text("- 转移函数 $\delta$：由连接（concatenation）、并（|）、闭包（*）规则确定")
    text("- 初始状态 $q_0$：正则表达式的起始状态。")
    text("- 接受状态集合 $F$：正则表达式的结束状态。")
    text("- 例如，正则表达式 `a(b|c)*d` 对应的NFA可以表示为：")
    text("- 状态集合 $Q$：{q0, q1, q2}，其中 q0 是初始状态，q2 是接受状态。")
    text("- 输入符号集合 $\Sigma$：{a, b, c, d}。")
    text("- 转移函数 $\delta$：")
    text("1. $\delta(q0, a) = \\{q1\\}$")
    text("2. $\delta(q1, b) = \\{q1\\}$")
    text("3. $\delta(q1, c) = \\{q1\\}$")
    text("4. $\delta(q1, d) = \\{q2\\}$")
    text("5. 其他输入符号的转移都指向一个死状态。")
    text("- 初始状态 $q_0$：q0。")
    text("- 接受状态集合 $F$：{q2}。")


    def custom_nfa_for_regex():
        init_state = "q0"
        states = {"q0", "q1", "q2"}
        alphabet = {"a", "b", "c", "d"}
        accepting_states = {"q2"}
        transitions = {("q0", "a"): {"q1"}, ("q1", "b"): {"q1"}, ("q1", "c"): {"q1"}, ("q1", "d"): {"q2"}}
        return init_state, accepting_states, transitions

    def custom_regex_matches_string(init_state, accepting_states, transitions, string):
        current_states = {init_state}
        for symbol in string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in transitions:
                    next_states.update(transitions[(state, symbol)])
            current_states = next_states
        return any(state in accepting_states for state in current_states)

    def regex_matches_string(regex, string):
        import re
        pattern = re.compile(regex)
        return bool(pattern.fullmatch(string))


    text("**论文：[CL2025] TokenizationasFinite-StateTransduction**")
    image("images/bpe_dfa_paper.png", width=600)
    image("images/bpe_tokenize_algo.png", width=600)
    image("images/bpe_tokenize_ex.png", width=480)
    text("- BPE算法因为合并规则存在优先级、并不是自左向右扫描，所以被认为不能直接用DFA实现。")
    image("images/bpe_dfa_algo.png", width=600)
    text("- 更改BPE算法的遍历顺序，通过串行DFA实现BPE算法。")
    image("images/bpe_dfa_res.png", width=600)
    text("- 加速效果显著！")

def Q_and_A():
    text("# 问答环节：欢迎大家提问！")
    image("images/stuff.png", width=600)


if __name__ == "__main__":
    main()
