from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)

    text("| 单位 | 专业/部门 | 经历 | 研究方向 |\n| :---: | :---: | :---: | :---: |\n| 华东师范大学 | 计算机科学与技术 | 学士（保送） | 《基于循环神经网络的依存句法分析》 |\n| 华东师范大学 | 计算机科学与技术 | 博士（硕博连读） | 《多语言依存句法分析》 |\n| 复旦大学 | 自然语言处理实验室 | 博士后研究人员 |  |\n| **复旦大学** | **外文学院** | **助理教授** | **计算语言学与大语言模型** |\n| **上海人工智能实验室** | **大模型中心** | **算法顾问（兼）** | |\n")

    text("- ACL/NeurIPS/ICLR/EMNLP等自然语言处理和深度学习顶会发表论文30余篇")
    text("- TA@《统计自然语言处理》，TA@《深度学习导论》，代课教师@《自然语言处理导论》")
    text("- 网页编译框架来源Stanford CS336课程")

    why_language_and_cs_matter()
    intro()
    todo()

    Q_and_A()

def why_language_and_cs_matter():
    image("images/block_news.png", width=600)
    text("- **利润增长 → 裁员近半 → 股价飙升** "), link(title="[WallStreet]", url="https://wallstreetcn.com/articles/3766301")
    text("- **AI时代下，企业通过裁员来突出效率与价值**")
    text("---")
    image("images/hc_devlop.png", width=600)
    text("- **软件开发行业**的青年就业岗位持续萎缩 "), link(title="[Stanford Report, Fig 1]", url="https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf")
    text("---")
    image("images/hc_custom_service.png", width=600)
    text("- **社会服务行业**的青年就业岗位持续萎缩 "), link(title="[Stanford Report, Fig 1]", url="https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf")
    text("---")
    image("images/hc_other_job.png", width=600)
    text("- **销售经理、产线员工、护理师**等AI不可替代（目前）行业的就业岗位正常增长 "), link(title="[Stanford Report, Fig A2]", url="https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf")
    text("---")
    image("images/swe_bench.png", width=600)
    text("- **基础软件开发能力评测集**性能突飞猛进：4.4%(2023) → 71.7%(2024) "), link(title="[AI Index Report 2025, Fig 2.5.4]", url="https://arxiv.org/pdf/2504.07139")
    text("---")
    image("images/math_hard_case.png", width=600)
    image("images/math_hard_bench.png", width=600)
    text("- **前沿数学问题解题**性能显著提升 "), link(title="[AI Index Report 2025, Fig 2.6.7]", url="https://arxiv.org/pdf/2504.07139")
    text("---")
    image("images/math.png", width=600)
    text("- 大型语言模型(LLM)在国际数学奥林匹克(IMO)2025中取得了相当于金牌的成绩。")
    image("images/acmicpc1.png", width=400)
    text("- 大型语言模型(LLM)在2025年ACM国际大学生程序设计竞赛(ACM-ICPC)中表现出色，达到了世界级水平。")
    image("images/acmicpc2.png", width=900)
    text("- 12道题里11道题OpenAI都是一次提交就通过，只有最难的G题，花了9次才提交通过。 ")
    image("images/acmicpc3.png", width=600)
    text("- A题：编程设计一个数据结构：斜堆（skew heap）......")
    text("---")
    text("### AI作为生产力工具，难替代、全栈、善用AI的求职者具有竞争力")
    text("#### 回顾：AI的首次出圈是AlphaGo")
    image("images/go1.jpg", width=600)
    text("- 2016年AlphaGo 4:1 战胜围棋世界冠军李世石")
    image("images/go2.jpg", width=600)
    text("- 2017年AlphaGo 3:0 战胜围棋世界冠军柯洁")
    image("images/go_and_ai.png", width=600)
    text("=> 棋手利用AI快速提升水平 "), link(title="[LizzieYzy]", url="https://blog.csdn.net/gitblog_00913/article/details/158304469")

    text("### AI确实很重要，但为什么外语+计算机？🤔")
    text("#### 举例：中美模型最大的差距在于基于人类反馈的强化学习(RLHF)")
    image("images/6-sft-rlhf.png", width=600)
    text("- 大规模预训练 → 指令微调 → 基于人类反馈的强化学习")
    text("- “暴力求解”只适用于通用、数据量大、数据质量高的任务")
    text("- 语言学家能够帮助设计更有效的反馈机制，从而提升AI的专业性和适应性")
    text("- 例如：创造一个会说脱口秀的AI")

    text("- 危机：“暴力求解”但互联网数据已经用完")
    image("images/limits_of_llm_data.png", width=600)
    text("- 语言学家能够帮助合成有价值的数据，解决数据危机")
    text("### 自然语言处理（NLP）是一门交叉学科，深度融合了计算机科学、语言学、统计学等多个领域的知识和技术。")
    text("- **AI应用**的研究依赖交叉学科的思维与技能")
    text("- **AI进步**的研究依赖交叉学科的思维与技能")


def intro():
    text("- 逻辑推理作为AI的核心能力之一，始终在NLP和AI领域的研究中占据举足轻重的地位。")
    text("- 自20世纪50年代计算机科学和人工智能诞生之初，逻辑推理就被视为构建智能系统的基石。")
    image("images/logic_mac.png", width=600)
    link(title="[Logic Theory Machine]", url="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1056797")
    text("- 形式逻辑与符号推理 → 模拟人类的思考过程 → 实现类似人类的智能。")
    text("- 形式逻辑推理在70年代成为人工智能研究的主导领域。")
    text("- 80年代，随着数据驱动方法和神经网络的兴起，机器学习算法取得了令人瞩目的成果。")
    text("- 逻辑推理与数据驱动学习相结合 → 更强大、健壮和可解释的人工智能系统")
    image("images/logic_devlop.png", width=800)
    link(title="[大模型逻辑推理研究综述]", url="https://aclanthology.org/2024.ccl-2.3.pdf")

    text("### 显式逻辑结构与隐式逻辑结构")
    text("1. 语义角色标注任务（Semantic Role Labeling, SRL）")
    image("images/srl_case.png", width=600)
    text("SRL以句子为单位，以句子的谓词为中心，研究句子中各成分与谓词之间的关系，并且用语义角色来描述他们之间的关系。")

    text("2. 组合范畴文法（Combinatory Categorial Grammar, CCG）")
    image("images/ccg_case.png", width=600)
    text("CCG使用组合范畴来表示词汇和短语的语法信息，然后使用这些组合范畴之间的组合规则来生成句子的结构")

    text("3. 抽象语义图（Abstract Meaning Representation, AMR）")
    image("images/amr_case.png", width=600)
    text("AMR是一种基于图结构的语义表示方法，用于捕捉句子的语义信息。AMR将句子中的实体、事件和关系表示为一个有向图，其中节点表示实体或事件，边表示它们之间的关系。")

    text("4. 篇章分析（Discourse Analysis）")
    image("images/discourse_case1.png", width=600)
    image("images/discourse_case2.png", width=600)
    text("篇章分析关注文本中句子之间的关系和结构，研究如何理解和生成连贯的文本。篇章分析涉及到文本的组织结构、信息流动、指代关系等方面的研究。")

    text("5. 指代消解（Coreference Resolution）"), link(title="[CCL2024]", url="https://aclanthology.org/anthology-files/pdf/ccl/2024.ccl-1.55.pdf")
    image("images/coreference_case.png", width=600)
    text("指代消解旨在识别文本中指代词（如代词、名词短语等）所指代的实体或事件。")

    text("6. 自然语言推断（Natural Language Inference, NLI）"), link(title="[XNLI]", url="https://github.com/facebookresearch/XNLI")
    image("images/nli_case.png", width=600)
    text("- 前提（premise）：已知为真的句子")
    text("- 假设（hypothesis）：需要判断与前提关系的句子")

    text("- 蕴含（Entailment）：如果前提为真，则假设必然为真。")
    text("> 前提“一个男孩在踢球。” 假设“有人在运动。” → 蕴含")
    text("- 矛盾（Contradiction）：如果前提为真，则假设必然为假。")
    text("> 前提“一个男孩在踢球。” 假设“没有人在踢球。” → 矛盾")
    text("- 中立（Neutral）：前提和假设之间没有必然的蕴含或矛盾关系。")
    text("> 前提“一个男孩在踢球。” 假设“男孩在公园里踢球。” → 中立")

    text("#### 基础任务 → 下游任务")
    image("images/logic_bench.png", width=600)
    image("images/logic_case.png", width=1080)
    link(title="[LogiQA]", url="https://arxiv.org/abs/2007.08124")

    text("### 🤔：这些显式逻辑结构对下游任务是否有帮助？")
    text("- 大多数情况下，显式逻辑结构对下游任务的帮助有限，甚至可能有害。")
    text("- 实践中显式逻辑结构也需要预测，无法保证预测的准确性。")

    text("### 显式逻辑结构与隐式逻辑结构")
    text("- 鸡蛋是**圆的**")
    text("- 12*3+9=**45**")
    text("- 我们把香蕉给猴子，因为它们饿了。它们是指____")
    text("- 我们把香蕉给猴子，因为它们熟透了。它们是指____")
    text("- 长颈鹿的声带很特殊，其声带中有一个浅沟，发声的时候就比较困难，而且要肺部、胸腔以及膈肌的共同帮助下它才可以发声，但是由于其脖子很长的缘故，所以这些器官相隔就挺远的，所以它也就没有办法____")
    text("#### 💡：只学习预测下一个单词，模型就能学会隐式的逻辑结构")

    text("🤔：大规模训练中见过数据（背诵） or 真正学会了自然语言逻辑（推理）？")
    link(title="[Transformers as Soft Reasoners over Language]", url="https://arxiv.org/abs/2002.05867")
    image("images/multi_hop_nli.png", width=600)
    image("images/main-results.png", width=600)
    image("images/logic-and-transformers.png", width=400)

    text("- 隐式逻辑结构难以解释，没有显式结构直观")
    text("- 隐式逻辑结构并不总是有效，大模型存在“幻觉”现象，可能会生成不符合逻辑的内容")
    image("images/hallucination.png", width=600)
    image("images/symbolic_add_nn.png", width=600)
    text("- 结合显式逻辑结构与隐式逻辑结构 → 更强大、健壮和可解释的人工智能系统")
    image("images/symbolic_vs_nn.png", width=600)

    text("### 课程大纲")
    image("images/course_outline.png", width=600)

    text("### 课程考核")
    text("- 出勤 & 课堂表现：20%")
    text("- 课程实践：30%（两次）")
    text("- 期末考试：50%")

    text("- CFFF国内高校最大的AI计算集群")
    image("images/cfff1.png", width=400)
    image("images/cfff2.png", width=400)

    text("### 参考教材")
    text("- Barbara H. Partee, Alice ter Meulen, and Robert E. Wall"), link(title="《语言学中的数学方法》", url="http://www.lingviko.net/feng/ml.pdf")
    text("- John E. Hopcroft, Rajeev Motwani, and Jeffrey D. Ullman"), link(title="《自动机理论、语言和计算导论》", url="http://www.lingviko.net/feng/ml.pdf")


def todo():
    text("[ ] 注册"), link(title="Github", url="https://github.com/"), text("账号")
    text("[ ] 申请学生认证，获得一系列开发工具"), link(title="GitHub Education", url="https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student")
    text("[ ] 使用GitHub Copilot"), link(title="GitHub Copilot", url="https://github.com/copilot")

def Q_and_A():
    text("# 问答环节：欢迎大家提问！")
    image("images/stuff.png", width=600)


if __name__ == "__main__":
    main()
