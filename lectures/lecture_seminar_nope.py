from execute_util import link, image, text
from lecture_util import article_link

import tiktoken

def main():
    text("# 立足AI原住民，铸就顶尖外语家")
    
    image("images/speaker.png", width=400)
    text("- 复旦外文-助理教授-纪焘")
    text("- 2013年信息学奥赛保送生")
    text("- 本硕博 & 博后均在计算机系，研究方向为自然语言处理、计算语言学")
    text("- 博士论文《多语言依存句法分析》")
    text("- 外语+计算机融合课程：《自然语言处理与语言习得》《面向语言信息处理的语言逻辑理论》等")

    intro()
    what_can_ai_do()
    how_cfll_plus_cs()

    Q_and_A()

    

def intro():
    text("## AI的兴起与发展")
    text("### AI的首次出圈是AlphaGo")
    image("images/go1.jpg", width=600)
    text("- 2016年AlphaGo 4:1 战胜围棋世界冠军李世石")
    image("images/go2.jpg", width=600)
    text("- 2017年AlphaGo 3:0 战胜围棋世界冠军柯洁")

    text("### 2024年 AI主导的研究获得了诺贝尔物理学奖、化学奖")
    image("images/nbe1.png", width=600)
    text("- 诺贝尔物理学奖表彰“利用人工神经网络实现机器学习的基础性发现和发明”")
    image("images/nbe2.jpg", width=600)
    text("- 诺贝尔化学奖表彰“利用人工智能在复杂化学反应预测中的突破性贡献”")

    text("### AI正在成为新的生产力工具")
    image("images/aivshuman.png", width=600)
    text("- AI正从各个能力维度上全面超越人类的表现")

    image("images/aiiq.png", width=600)
    text("- 人工智能的IQ测试得分领先显著。")
    
    image("images/math.png", width=600)
    text("- 大型语言模型(LLM)在国际数学奥林匹克(IMO)2025中取得了相当于金牌的成绩。")
    
    image("images/acmicpc1.png", width=400)
    text("- 大型语言模型(LLM)在2025年ACM国际大学生程序设计竞赛(ACM-ICPC)中表现出色，达到了世界级水平。")
    image("images/acmicpc2.png", width=900)
    text("- 12道题里11道题OpenAI都是一次提交就通过，只有最难的G题，花了9次才提交通过。 ")
    image("images/acmicpc3.png", width=600)
    text("- A题：编程设计一个数据结构：斜堆（skew heap）......")

    image("images/useai.png", width=600)
    text("- 使用AI的公司逐渐增多，特别是近年来生成式AI的兴起，使得AI在各行各业的应用变得更加广泛和深入。")

    image("images/usvschina.png", width=600)
    text("- 中美之间AI的差距在逐渐缩小，中国在AI领域的进展和创新也非常显著。")

    image("images/smallllm.png", width=600)
    text("- 达到相同智能所需的模型体量逐渐减小，AI变得更加高效和易于应用。")

    text("### 挑战：AI减少了就业机会")
    image("images/aijob.png", width=400)
    text("- 美国就业市场过去一年里，科技行业的就业萎靡。")
    text("- 公司通过减少人员编制展现AI的高效应用。")

    text("### 立足AI时代")
    text("- 成为AI的原住民：➊创造好的AI工具，➋用好AI工具")
    text("- 幸运的是，生成式AI的核心是大语言模型(LLM)，而LLM是计算语言学的产物，我们语言学家有天然的优势！")
    text("- 当前生成式AI的成功主要是计算机科学通过“暴力求解”推进，然而瓶颈已经显现。")
    text("- 语言学家能够解释“为什么有用/没用？”，从而指示正确的优化方向，未来需要计算语言复合人才来推动AI的发展和应用。")


def what_can_ai_do():
    text("### AI是国际话语权、国家综合实力的新高地")
    text("### 当前的生成式AI是以语言为中心")
    text("### 中美模型最大的差距在于基于人类反馈的强化学习(RLHF)")
    image("images/6-sft-rlhf.png", width=600)
    text("- “暴力求解”只适用于通用、数据量大、数据质量高的任务")
    text("- 语言学家能够帮助设计更有效的反馈机制，从而提升AI的专业性和适应性")
    text("- 例如：创造一个会说脱口秀的AI")

    text("- 危机：“暴力求解”但互联网数据已经用完")
    image("images/usvschina.png", width=600)
    text("- 语言学家能够帮助合成有价值的数据，解决数据危机")


def how_cfll_plus_cs():
    
    text("### AI通识大课、外语+计算机融合课、外语/计算机专业课")
    text("- CFFF国内高校最大的AI计算集群")
    image("images/cfff1.png", width=400)
    image("images/cfff2.png", width=400)
    text("- 复旦自然语言处理实验室：复旦语言学本科+计算机直博：徐凝雨博士")
    image("images/ff_nlp1.jpg", width=400)
    image("images/ff_nlp2.jpg", width=400)
    text("- 国际权威期刊《美国科学院院刊》（PNAS）发表论文，揭示大语言模型中的类人概念表征。")
    text("- 复旦大学自然语言处理实验室黄萱菁教授、邱锡鹏教授，现代语言学研究院、智能复杂体系实验室张梦翰研究员共同担任通讯作者。")

def Q_and_A():
    text("# 问答环节：欢迎大家提问！")


if __name__ == "__main__":
    main()
