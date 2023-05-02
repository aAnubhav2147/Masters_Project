This directory tracks the progress made towards my Master's capstone; course code - DSC520. The capstone is being done under the guidance of Prof. Ming Shao.

Final update: The usage of DeBERTa model yielded a Pearson Correlation Coefficient of ~0.84. The result can be checked here -> https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching/submissions

Project/Competition Synopsis:

In this competition, you will train your models on a novel semantic similarity dataset to extract relevant information by matching key phrases in patent documents. Determining the semantic similarity between phrases is critically important during the patent search and examination process to determine if an invention has been described before. For example, if one invention claims "television set" and a prior publication describes "TV set", a model would ideally recognize these are the same and assist a patent attorney or examiner in retrieving relevant documents. This extends beyond paraphrase identification; if one invention claims a "strong material" and another uses "steel", that may also be a match. What counts as a "strong material" varies per domain (it may be steel in one domain and ripstop fabric in another, but you wouldn't want your parachute made of steel). We have included the Cooperative Patent Classification as the technical domain context as an additional feature to help you disambiguate these situations.

Can you build a model to match phrases in order to extract contextual information, thereby helping the patent community connect the dots between millions of patent documents?


For more details: <https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching/overview>


References:

1.) "Attention Is All You Need" paper by Vaswani et al. (2017), https://arxiv.org/abs/1706.03762

2.) Google Patent Phrase Similarity: https://ai.googleblog.com/2022/08/announcing-patent-phrase-similarity.html?hl=ro&m=1

3.) Cooperative Patent Classification: https://www.cooperativepatentclassification.org/Archive

4.) The United States Patent & Trademark Office: https://www.uspto.gov/web/patents/classification/cpc/html/cpc.html

5.) Illustrated Transformer: http://jalammar.github.io/illustrated-transformer/

6.) A Gentle Introduction to Cross-Entropy Loss for Machine Learning: https://machinelearningmastery.com/cross-entropy-for-machine-learning/

7.) A Comprehensive Guide to Loss Functions in Machine Learning: https://heartbeat.fritz.ai/a-comprehensive-guide-to-loss-functions-in-machine-learning-55b5a2b4c8dd

8.) "Cross-Entropy Loss for Classification" by Andrew Ng: https://www.youtube.com/watch?v=LLux1SW--oM
