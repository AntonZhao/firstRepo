### 论文名称：Distant Supervision for Relation Extraction via Piecewise Convolutional Neural Networks

论文信息：Zeng et al. 2015 EMNLP

模型名称：PCNN

论文内容：非常经典的文章，分段式的max pooling。后面做的文章都要引用这篇文章。

原文地址：http://aclweb.org/anthology/D/D15/D15-1203.pdf



### 论文名称：Bidirectional Recurrent Convolutional Neural Network for Relation Classification

作者信息：Rui Cai 2016 ACL

模型名称：BRCNN

### 论文内容：本文提出了一个基于最短依赖路径（SDP）的深度学习关系分类模型，文中称为双向递归卷积神经网络模型（BRCNN）

原文地址：http://www.aclweb.org/anthology/P/P16/P16-1072.pdf



### 论文名称：End-to-End Relation Extraction using LSTMs on Sequences and Tree Structures

作者信息：Miwa et al. 2016

模型名称：BiLSTM SPTree

论文内容：用了一种树形的结构

原文地址：http://www.aclweb.org/anthology/P/P16/P16-1105.pdf



### 论文名称：Attention-Based Bidirectional Long Short-Term Memory Networks for Relation Classification

作者信息：中科大自动化所 Zhou ACL 2016

模型名称：BLSTM + ATT

论文内容：简单有效。使用BLSTM对句子建模，并使用word级别的attention机制。

原文地址：http://www.aclweb.org/anthology/P16-2034



### 论文名称：Neural Relation Extraction with Selective Attention over Instances

作者信息：清华 Lin et al. 2016

模型名称：CNN+ATT / PCNN+ATT

论文内容：使用CNN/PCNN作为sentence encoder, 并使用句子级别的attention机制。近几年标杆的存在，国内外新论文都要把它拖出来吊打一遍。

原文地址：http://www.aclweb.org/anthology/P16-1200







### 论文名称：NUERAL RELATION EXTRACTION WITH MULTI-LINGUAL ATTENTION

作者信息：清华 Lin et al. 2017

模型简称：MNRE

论文内容：很有意思也很有用。单语言语料的信息如果不够，就要用到多语言的语料。NLP任务中多语言之间的信息利用是今年研究比较多的一个。不过实际做起来难度是比较大的，最主要原因还是数据比较难以采集。本文使用

(P)CNN+ATT(上面那篇)扩展到多语言语料库上，利用多语言之间的信息 https://zhuanlan.zhihu.com/p/29970617。性能提升比较客观。应该也只有一些大公司才有能力将这种算法落地使用。



### 论文名称：Deep Residual Learning forWeakly-Supervised Relation Extraction

作者信息：Yi Yao Huang 台湾国立大学 EMNLP 2017

模型名称：ResCNN-9

论文内容：本文使用浅层（9）ResNet作为sentence encoder, 在不使用piecewise pooling 或者attention机制的情况下，性能和PCNN+ATT 接近。这就证明使用更fancy的CNN网络作为sentence encoder完全是有可能有用的。不光光可以在本任务中验证，其他的NLP任务同样可以使用。本文在github上有源代码，强烈推荐。我写的知乎笔记： https://zhuanlan.zhihu.com/p/31689694。 顺带一提的是，本文的工程实现还存在可以改进的地方。





### 论文名称：Overcoming Limited Supervision in Relation Extraction: A Pattern-enhanced Distributional Representation Approach

作者信息：ACM 2016
模型名称：REPEL

论文内容：这篇文章思路比较有意思，非常值得一看。没有用深度学习，而是两个朴素的模型互相迭代，运用了半监督学习的思想。不过没有代码，如果实验结果可以复现，那么意义还是比较大的。https://zhuanlan.zhihu.com/p/32364723。





### 论文名称：Cross-Sentence N-ary Relation Extraction with Graph LSTMs

作者信息：ACL 2017
模型名称：Graph LSTM

论文内容：这个就是提出了一种图形LSTM结构，本质上还是利用了SDP等可以利用的图形信息。别的部分没有什么特别的。https://zhuanlan.zhihu.com/p/32541447



### 论文名称：Distant Supervision for Relation Extraction with Sentence-Level Attention and Entity Descriptions

作者信息：Ji 2017 中科院自动化所 AAAI 2017

模型名称：APCNNs(PCNN + ATT) + D

论文内容：引入实体描述信息，个人认为没什么亮点，引入外部信息固然有效，但是很多时候实际问题中遇到的实体大多是找不到实体描述信息的。 https://zhuanlan.zhihu.com/p/35051652



### 论文名称：Large Scaled Relation Extraction with Reinforcement Learning

作者信息： Zeng 2018 中科院自动化所 AAAI 2018

模型名称：PE + REINF

论文内容：提出强化学习用于RE任务，个人感觉挺牵强的，效果也很一般。文中提到的PE不知道是不是我代码写错了，试出来就是没什么用。  https://zhuanlan.zhihu.com/p/34811735





### 论文名称： Learning with Noise: Enhance Distantly Supervised Relation Extraction with Dynamic Transition Matrix
作者信息： ACL 2017 Luo 北大
模型名称：CNN + ATT + TM （这名字是我给起的）



论文内容：文章出发点很好。既然远程监督数据集最大的问题在于噪音非常之多，那么对于噪音进行描述则是非常有意义的。本文创新点有两个。第一个是，我们让模型先学习从输入空间到真实标签空间的映射，再用一个转移矩阵学习从真实标签空间到数据集标签空间的错误转移概率矩阵。这不是本文提出的方法，本文在此基础之上进行改进，将该矩阵从全局共享转化为跟输入相关的矩阵，也就是文中提到的动态转移矩阵，性能有提升。第二个出创新点在于使用了课程学习。课程学习的出发点在于模型如果先学习简单样本再学习难样本，这样一种先易后难的学习方式比随机顺序学习更好。最终在NYT数据集上有小小的提升，但是本文的思路非常值得借鉴。可只可惜没有源代码。建议读博的大佬们尝试一下，我觉得很好玩。 https://zhuanlan.zhihu.com/p/36527644





### 论文名称： Effectively Combining RNN and CNN for Relation Classification and Extraction

作者信息： SemEval 2018 四项任务 三项第一，一项第二  ETH Zurich

模型名称：作者没起名字

论文内容：这是一篇打比赛的文章，工程性的内容很多。核心技巧在于使用CNN, RNN模型集成。文中还提到了多种方法，不择手段提升最终模型的性能。虽然该模型训练速度可以说是非常慢了，但是还是有很多地方可以借鉴。 https://zhuanlan.zhihu.com/p/35845948
