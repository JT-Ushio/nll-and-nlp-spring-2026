from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)
    text("## 03: 正则语言与有限状态自动机")
    background()
    finite_automata()
    regular_language()

def background():
    text("### 形式语言与自动机")
    text("**输入输出 → 抽象计算设备**")
    text("- 一台计算设备能够完成什么任务？")
    text("- 一个问题如何转换成可计算的任务？")
    text("- → 计算思维")

    text("**自动机理论的先驱：Alan Turing (1912-1954)**")
    image("images/alan_turing.png", width=160)
    text("- 现代计算机科学之父")
    text("- 英国数学家")
    text("- 提出抽象计算模型 -- 图灵机，发明电子计算机")
    text("- 图灵测试")
    image("images/turing_mac.png", width=200)

    text("**图灵机（Turing Machines）**：具有无限内存的设备。")
    text("**下推自动机（push-down automata）**：可以以受限方式访问无限内存的设备。")
    text("**有穷自动机（finite automata）**：具有有限内存的设备。")

    text("**自动机要解决的“问题”**：示例")
    text("- 给定符号串s，它是否包含子符号串t？")
    text("- 给定一个自然语言句子，它属于哪种语言？")
    text("- 给定一个代码/句子，它是否有语法错误？")
    text("- 给定规则，创造一种语言（精灵语@魔戒，鱼人语@魔兽世界）")
    image("images/new_language.png", width=200)

    text("**形式语言（Formal Languages）**：由形式语法生成的语言。")
    text("- 我们将<mark>语言（Language）</mark>定义为<mark>字符串（String）</mark>的集合。")
    text("- 字符串定义为<mark>符号（Symbol）</mark>的序列，例如 cat，dog，house。")
    text("- 所有可能出现的符号是由这个语言的<mark>字母表（Alphabet，$\Sigma$）</mark>定义。")
    text("- if $\Sigma$ = {a, b}，则字符串可以是 a、b、aa、ab、ba、bb、aaa、aab、...")
    text("- 习惯上，我们会用 u，v，w 等靠后的字母表示字符串，例如 u = ab ，v = bbbaaa，w = abba 。")

    text("**字符串基本操作及其数学表示**")
    text("- 令$w=a_1 a_2 \cdots a_n, \quad v=b_1 b_2 \cdots b_m$")
    image("images/string_op.png", width=400)

    text("**定义字母表$\Sigma$的<mark>星闭包（Star Closure, $\Sigma^*$）</mark>**")
    text("- $\Sigma^*$ 是由$\Sigma$中的符号组成的所有可能字符串的集合。")
    text("- 例如，如果$\Sigma = \{a, b\}$，则$\Sigma^* = \{\epsilon, a, b, aa, ab, ba, bb, aaa, aab, \ldots\}$，其中$\epsilon$表示空字符串。")
    text("- 定义在 $\Sigma$ 上的语言是 $\Sigma$  中的符号组成的字符串的集合，")
    text("- → 定义在 $\Sigma$ 上的语言永远是 $\Sigma^*$ 的子集。")
    text(r"- 例如，如果$L = \\{a^n, b^n | n\ge 0\\}$，则$\epsilon/ab/aab/aabb$ $\in or\notin L$?")

    text("**语言相关操作的数学定义与表示**")
    image("images/language_op.png", width=400)

def finite_automata():
    text("### 有穷自动机（Finite Automata, FA）")
    text("- 有穷自动机是一个形式系统，它只记忆有限的信息量，这些信息量通过它的<mark>状态（State）</mark>表示。")
    text("- 当有<mark>输入（Input）</mark>给到有穷自动机的时候，它会相应地改变自己的状态。")
    text("- 告诉FA如何根据输入以及当前状态来改变到新状态的一系列规则，被称为<mark>转移函数（Transfer Function）</mark>")
    text("- 当FA转移到一个<mark>接受/终止状态（Accepting State）</mark>，我们就说这个输入被FA接受/FA终止了。")

    text("**例子：判断网球比赛输赢**")
    text("- 胜利规则有两条：至少要得 4 次分；还要比对手多得两次分。")
    text("- $\Sigma = \{s, o\}$，其中s表示东道主得分（server wins point），o表示对手得分（opponent wins point）。")
    text("- 大写字母$S^1$表示东道主赛点，$S^2$表示东道主胜利，$O^1$表示对手赛点，$O^2$表示对手胜利。")
    image("images/fa_graph.png", width=480)

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

    text("### ✍️：用五元组表示网球比赛")

    text("> 💡注意：DFA的转移函数$\delta$通常假设是完全定义的，即对于每个状态 $q \in Q$ 和每个输入符号 $a \in \Sigma$，必须有一个明确的下一个状态 $q^\prime = \delta(q, a)$。如果某些输入符号在某些状态下没有定义转移，可以引入一个特殊的“死状态”（dead state），所有未定义的转移都指向这个死状态，并且死状态的所有转移都指向自己。")
    image("images/fa_graph_w_deadnode.png", width=480)

    text("当前转移函数每次调用只能表示一次跳转")
    text("- 若输入字符串sososo之后进入状态p，需要写作$\delta(\delta(\delta(\delta(\delta(\delta(q, s), o), s), o), s), o)=p$")
    text("- 表示起来极其麻烦，定义一个扩展的转移函数")

    text("<mark>**定义**</mark>：递归定义 DFA 的**扩展转移函数（Extended Transfer Function）**：")
    image("images/ex_transition_func.png", width=400)

    text("### DFA的表示方法")
    text("1. 状态转换图：适用状态数比较**少**的时候")
    text("2. 转移表：适用状态数比较**多**的时候")
    text("3. 五元组：适用严格数学证明")

    image("images/transition_table.png", width=480)
    text("### ✍️：用五元组表示")

    text("### DFA的语言")
    text("<mark>**定义**</mark>：对于一个 DFA $M = (Q, \Sigma, \delta, q_0, F)$，")
    text("如果$\delta(q_0, w)\in F$，那么字符串$w$被$A$接收；")
    text(r"那么 M 能接受的所有字符串组成的集合为 DFA 的语言，记为 $L(M)=\\{w \mid \delta(q_0, w) \in F\\}$")

def regular_language():
    text("### 正则语言（Regular Language）")
    text("- 如果一个语言 L 可以由某个 DFA A 定义，即 L = L(A) ，则称语言 L 是正则语言（Regular Language）。")
    text("- 所有正则语言组成的集合称为正则语言类（Regular Languages），记为 RE 。")
    text(r"- $RE=\\{L \mid L=L(A), A\ is\ a\ DFA \\}$")

    text(r"🤔：$L = \\{0^n1^n|n\ge 1\\}$ 是不是正则语言？")
    text(r"✍️：$\Sigma=\\{0, 1\\}$，能被5整除的二进制串，能否用DFA表示，能的话列出DFA")

def Q_and_A():
    text("# 问答环节：欢迎大家提问！")
    image("images/stuff.png", width=600)


if __name__ == "__main__":
    main()
