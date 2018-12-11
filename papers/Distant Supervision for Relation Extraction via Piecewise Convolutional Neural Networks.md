## paper profile
>- 论文名称：Distant Supervision for Relation Extraction via Piecewise Convolutional Neural Networks
>- 论文信息：Zeng et al. 2015 EMNLP
>- 模型名称：PCNN
>- 论文内容：非常经典的文章，分段式的max pooling。后面做的文章都要引用这篇文章。
>- 原文地址：http://aclweb.org/anthology/D/D15/D15-1203.pdf
___
## Introduction  
>The distant supervision strategy is an effctive method of automatically labeling >trainning data. However it has two shortcomings when used for relation extraction.
>  1. the distant supervision assumption is too strong and causes wrong label problem.
>  2. previous methods have typically applied supervised models to elaborately >designed features when obtained the labeled data through distant supervision. These >errors may lead to error propagation or accumulation.  

  **太容易产生错误的标记。**
  **错误会积累会传播。**

>A sentence is inherently divided into three segments according to the two given entities. The internal context includes the characters inside
the two entities, and the external context involves the characters around the two entities (Zhang etal., 2006).

**根据被提供的两个实体，将句子分成三段。实体内部，就是实体本身包括的字符；实体外部就是其他的上下文。**

>The contributions of this paper can be summarized as follows.  
  - We explore the feasibility of performing distant supervised relation extraction without hand-designed features. PCNNS are proposed to automatically learn features without complicated NLP preprocessing.
  - To address the wrong label problem, we develop innovative solutions that incorporate multi-instance learning into the PCNNS for distant supervised relation extraction.
  - In the proposed network, we devise a piecewise max pooling layer, which aims to capture structural information between two entities.

- **不使用手工创建的特征，探索远程监督关系抽取的可行性。不使用复杂NLP手段的情况下，用PCNNS来自动学习特征。**
- **为了解决错误的标签问题，开发了创新的解决方案，将多实例学习结合PCNNS，用于远程监督关系提取。**
- **设计一个*分段最大池化层*，用来捕获两个实体间的结构信息**

## related work

>Performance strongly depends on the quality of the designed features, so most existing studies have concentrated on extracting features to identify the relations between two entities.

**由于效果比较依赖特征的质量，所以现在大部分研究都是关于提取特征以识别两个实体之间的关系。**

>Previous methods can be generally categorized into two types:
>  - feature-based methods
>  - kernel-based methods.

>In feature-based methods, a diverse set of strategies is exploited to convert classification clues (e.g., sequences, parse trees) into feature vectors.

**在基于特征的方法中，利用各种策略将分类线索（例如，序列，解析树）转换为特征向量。**

>Kernel-based methods provide a natural alternative to exploit rich representations of input classification clues, such as syntactic parse trees. Kernelbased methods enable the use of a large set of features without needing to extract them explicitly.

**基于内核的方法提供了一种利用输入分类线索的丰富表示的自然选择方法，例如语义树。该方法可以使用大量的特征集，不用明确的提取它们。**

>The author think NLP work is difficult to get high-quality features in the last of this section, ok, network now.
**别整着乱七八糟的啦，用神经网络自动学吧。**

## methodology
>Distant supervised relation extraction is formulated as multi-instance problem. In this section, we present innovative solutions that incorporate multi-instance learning into a convolutional neural network to fulfill this task. PCNNs are proposed for the automatic learning of features without complicated NLP preprocessing. Figure 3 shows our neural network architecture for distant supervised relation extraction. It illustrates the procedure that handles one instance of a bag. This procedure includes four main parts: Vector Representation, Convolution, Piecewise Max Pooling and Softmax Output. We describe these parts in detail below.

**远程监督关系抽取为解决多例问题而制定。在本节中，我们提出了创新的解决方案，将多实例学习结合到卷积神经网络中以完成此任务。 PCNN自动学习特征而无需复杂的NLP处理。 图3显示了我们用于远程监督关系提取的神经网络架构。 它说明了处理一个包实例的过程。 此过程包括四个主要部分：向量表示，卷积，分段最大池和Softmax输出。 我们在下面详细描述这些部分。**

## 3.1  Vector Representation
