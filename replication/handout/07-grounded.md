# Irreducibly Human Work Lexicon pilot, grounded run: message 8 of 13 (chunk 07, 3 concepts)

Everything you need is in this message. Don't fetch, search or look anything up. Draft only from what is here and what you already know.

**Independence.** Several models are drafting these same 36 entries separately so Nik Bear Brown can compare them. Don't read, search for or ask for any other model's drafts, including Claude's. The material below is source material only (the lexicon's record, candidate neighbors, posting snippets, Wikipedia, Wikidata and WordNet candidates); it holds no one's drafts.

**How to work.** Treat each concept on its own, as if you had never seen the others: don't carry a decision, a wording or a relation from one concept to the next. This is the **grounded** run: each concept comes with its candidate Wikipedia articles, Wikidata items and WordNet senses.

**Instructions for every concept** (use them exactly as written):

~~~~text
You draft entries for the Irreducibly Human Work Lexicon, a WordNet-style lexical database of work concepts (skills, knowledge areas, abilities, languages, and credentials) used to match job postings with course syllabi. You receive one concept and a bundle of source material. You return one JSON object.

Your job is to record what the sources support, not to complete a template. An empty relation list is a correct answer. A plausible relation you cannot support is an error.

Work through these steps in order.

1. Work sense. Read the concept record and the usage examples. Write one sentence saying what the concept means as a job requirement or learning outcome. Every later decision is about this sense.

2. Source links. For Wikipedia, Wikidata, and WordNet separately, pick the single candidate that matches the work sense, or abstain by setting choice to null. Abstain when no candidate matches, when the candidates describe a different sense, or when you cannot tell. Give a one-sentence reason either way. You may cite only sources you linked, plus Wikidata ancestors of the item you linked.

3. Definition. Write one to three sentences in your own words describing the concept as it appears in postings and syllabi. Never reuse more than eight consecutive words from any source. Cite the pointers that support it.

4. Variants. List surface forms that name this concept: abbreviations, alternate spellings, historical names. If a form names the concept only in some contexts, state the condition (for example, "when it labels a skill, role, or team, not the experience itself").

5. Relations. Use only these types, and include a relation only if its test passes with the actual names filled in:
   - synonym: the target can replace the concept in a posting or syllabus without changing what is asked for or taught.
   - hypernym: "[concept] is a kind of [target]" is true.
   - hyponym: "[target] is a kind of [concept]" is true.
   - meronym: practicing or knowing the concept routinely includes the target as a component.
   - holonym: the concept is routinely a component of the target.
   - uses: the concept is typically practiced with the target, which is a tool, runtime, framework, or other technology rather than a component.
   - requires: the target must be learned before the concept can be practiced.
   - certifies: only when the concept is a credential; the credential attests to the target.
   - contrast: the target is often confused with the concept but differs from it. Use this for false-equivalence risks, including look-alike names.
   Do not record antonyms or pertainyms. Work concepts almost never have them.

6. Basis. Give every definition, variant, and relation a basis:
   - "source": the provided material states it, and you give at least one pointer that identifies the exact statement, synset relation, passage, or example.
   - "model_knowledge": you believe it, but the provided material does not state it. This is allowed. Never label model knowledge as source, and never invent a pointer.

7. Targets. If a relation's target matches a concept in lexicon_neighbors, set target_id to that concept's id. Otherwise set target_id to null and proposed_new to true.

8. Final check. Before returning, review every claim. Remove any relation whose test fails when read with the real names, any pointer that does not say what you claim, and anything you added only because a slot was empty. Put any concern a reviewer should see (conflicting sources, unclear sense, a likely error in the lexicon's existing record) in flags.

Pointer formats:
- Wikidata statement: wd:QID#PID=VALUE_QID (for example, wd:Q100#P279=Q200)
- Wikidata label or alias: wd:QID#alias=TEXT
- WordNet lemma: wn:SYNSET_ID#lemma=TEXT
- WordNet relation: wn:SYNSET_ID#RELATION=TARGET_SYNSET_ID, where RELATION is hypernym, hyponym, part_meronym, part_holonym, member_meronym, or member_holonym
- Wikipedia passage: wp:REVISION_ID#quote=TEXT, where TEXT is copied exactly from the provided article and is at most 20 words
- Usage example: ex:EXAMPLE_ID

Return only this JSON object, with no preamble and no code fences:

{
  "concept_id": "string",
  "work_sense": "string",
  "links": {
    "wikipedia": {"choice": "REVISION_ID or null", "reason": "string"},
    "wikidata": {"choice": "QID or null", "reason": "string"},
    "wordnet": {"choice": "SYNSET_ID or null", "reason": "string"}
  },
  "definition": {"text": "string", "basis": "source or model_knowledge", "pointers": ["string"]},
  "variants": [
    {"text": "string", "condition": "string or null", "basis": "source or model_knowledge", "pointers": ["string"]}
  ],
  "relations": [
    {"type": "one of the nine types above", "target_label": "string", "target_id": "string or null", "proposed_new": false, "basis": "source or model_knowledge", "pointers": ["string"], "note": "string or null"}
  ],
  "flags": ["string"]
}
~~~~

**Before you answer**, check every draft against this list and fix what fails (one pass of fixes, no more):

- `links.wikipedia`, `links.wikidata` and `links.wordnet` each have a `choice`, and each is null or one of that concept's candidates below.
- The definition, each variant and each relation has `basis` `source` or `model_knowledge`, and every `source` claim has at least one pointer.
- Every pointer resolves in the material below: `wd:` names the linked item or one of its ancestors and the statement or alias is really there; `wn:` names the linked synset and the lemma or relation is really there; `wp:` names the linked article's revision id and quotes at most 20 words that appear word for word; `ex:` names an example below.
- Only the nine relation types. A `target_id` must be one of that concept's neighbors.
- `certifies` only when the concept's `kind` is `credential`.
- The definition shares no run of 9 or more consecutive words with any Wikipedia text below.

**What to send back.** One JSON object per concept, one per line, in the order below, each with one extra field:
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "07", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-07.jsonl`. Otherwise send one code block marked `jsonl` holding the 3 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 3: Machine learning (`flxbx98seh`)

~~~~text
Concept record:
{
 "id": "flxbx98seh",
 "preferred_name": "Machine learning",
 "kind": "method",
 "broad_class": "skill",
 "variants": [
  {
   "label": "ML"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "bpi2rb7akn",
  "name": "CatBoost"
 },
 {
  "id": "ebn7tz5prh",
  "name": "PhD in Machine Learning"
 },
 {
  "id": "wng5g0t68d",
  "name": "Torch (machine learning)"
 },
 {
  "id": "oxu0hc83pv",
  "name": "Computer science"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "r32hw0qken",
  "name": "k-means clustering"
 },
 {
  "id": "ag0hpcesx8",
  "name": "Large language models"
 },
 {
  "id": "tx96mffcus",
  "name": "Neural networks"
 },
 {
  "id": "ecoz6ylymx",
  "name": "Statistics"
 },
 {
  "id": "mi2t4wx6vw",
  "name": "Free Lossless Audio Codec"
 },
 {
  "id": "nw1oyk7q86",
  "name": "Deep learning"
 },
 {
  "id": "r5kwam4bm9",
  "name": "Reinforcement learning"
 },
 {
  "id": "zoh6kna5kw",
  "name": "Retrieval-augmented generation"
 },
 {
  "id": "fcadn3ihwg",
  "name": "Angular"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "hzccoii598",
  "name": "Arithmetic"
 },
 {
  "id": "g9gfriy1ec",
  "name": "scikit-learn"
 },
 {
  "id": "xubhw9lr07",
  "name": "Active Learning"
 },
 {
  "id": "va052jqj8q",
  "name": "UML"
 },
 {
  "id": "php2tc9p7y",
  "name": "XML"
 },
 {
  "id": "oezvmtjgl6",
  "name": "Keyhole Markup Language"
 },
 {
  "id": "z79armevpb",
  "name": "Margin lending"
 },
 {
  "id": "op8cesvddr",
  "name": "Distance learning"
 },
 {
  "id": "w1blu9iu00",
  "name": "Blended learning"
 },
 {
  "id": "r4s8o1u1q1",
  "name": "Active Listening"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "sg1xfslxld",
  "name": "Quick learning"
 },
 {
  "id": "obj0g7i1kl",
  "name": "MQL4"
 },
 {
  "id": "nprxj06a8r",
  "name": "Machine operation"
 },
 {
  "id": "i3i5khm667",
  "name": "MXML"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:7",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior Independent AI Engineer / Architect. …nd orchestration systems Enterprise AI deployments Retrieval, evaluation, and reliability infrastructure LLM-powered workflows and products Machine learning platforms operating at scale You'll work directly with founders, CTOs, and product leaders, helping shape both technical direction and executio…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:6",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Analyst - Angular. Automation, Data management, Performance management, Analytical, Machine learning, Javascript, Workflow, Business intelligence"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:4",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Director, Standards & Strategy. …ends in the Audio/Video content creation and distribution spaces, including AR and VR, and other emerging technology areas such as imaging, machine learning and artificial intelligence Consistent with 1, establish DTS technologies in the technical standards and industry consortia publications that a…"
 },
 {
  "id": "dev122/internshala-jobs-dataset@v1/JobData.csv:29",
  "source": "kaggle:dev122/internshala-jobs-dataset (CC0: Public Domain), column Description",
  "text": "Job title: Artificial Intelligence (AI) Intern (Remote). …laborate with senior AI developers to develop natural language processing and computer vision algorithms 2. Collect and preprocess data for machine learning models 3. Analyze and interpret the results of experiments 4. Document and communicate findings to the team 5. Stay up-to-date with the latest …"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:103",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Senior AI Engineer. …ge Models (LLMs) for domain-specific use cases. 2. Build and maintain Retrieval-Augmented Generation (RAG) pipelines. 3. Develop and expose machine learning models as REST APIs using FastAPI. 4. Design and develop intelligent chatbot systems. 5. Implement agentic AI workflows and multi-step reasonin…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Machine learning",
  "revision_id": "1378799175",
  "matched_by": "title",
  "text": "Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without being explicitly programmed.\n\nStatistics and mathematical optimisation methods compose the foundations of machine learning. Data mining is a related field of study, focusing on exploratory data analysis (EDA) through unsupervised learning.\n\nFrom a theoretical viewpoint, probably approximately correct learning provides a mathematical and statistical framework for describing machine learning. Most traditional machine learning and deep learning algorithms can be described as empirical risk minimisation under this framework.\n\nAdvances in the field of deep learning have allowed neural networks, a class of statistical algorithms, to surpass many previous machine learning approaches in performance. The resulting dominance of machine learning within the field of AI from the late 2000s and early 2010s onwards was such that the terms \"machine learning\" and \"artificial intelligence\" are now often used interchangeably, even though they are not synonymous.\n\nHistory\n\nThe term machine learning was coined in 1959 by Arthur Samuel, an IBM employee and pioneer in the field of computer gaming and artificial intelligence. The synonym self-teaching computers was also used during this time period.\n\nThe earliest machine learning program was introduced in the 1950s, when Samuel invented a computer program that calculated the chance of winning in checkers for each side, but the history of machine learning is rooted in decades of efforts to study human cognitive processes. In 1949, Canadian psychologist Donald Hebb published the book The Organization of Behavior, in which he introduced a theoretical neural structure formed by certain interactions among nerve cells. The Hebbian theory of neuron interaction set the groundwork for how many machine learning algorithms work, with connected artificial neurons changing the strength of their connections based on data. Other researchers who have studied human cognitive systems contributed to the modern machine learning technologies as well, including Walter Pitts and Warren McCulloch, who proposed the first mathematical model of neural networks including algorithms that mirror human thought processes.\n\nBy the early 1960s, an experimental \"learning machine\" with punched tape memory, called Cybertron, had been developed by Raytheon Company to analyse sonar signals, electrocardiograms, and speech patterns using rudimentary reinforcement learning. It was repetitively \"trained\" by a human operator/teacher to recognise patterns and equipped with a \"goof\" button to cause it to reevaluate incorrect decisions. A representative book on research into machine learning during the 1960s was Nils Nilsson's book \"Learning Machines\", dealing mostly with machine learning for pattern classification. Interest related to pattern recognition continued into the 1970s, as described by Duda and Hart in 1973. In 1981, a report was given on using teaching strategies so that an artificial neural network learns to recognise 40 characters (26 letters, 10 digits, and 4 special symbols) from a computer terminal.\n\nTom M. Mitchell provided a widely quoted, more formal definition of the algorithms studied in the machine learning field: \"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E.\" This definition of the tasks in which machine learning is concerned is fundamentally operational rather than defining the field in cognitive terms. This follows Alan Turing's proposal in his paper \"Computing Machinery and Intelligence\", in which the question, \"Can machines think?\", is replaced by asking whether machines can convincingly imitate a human in its responses to human-posed questions.\n\nIn 2012, AlexNet, developed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton, achieved substantially improved results in the ImageNet image recognition competition, contributing to the wider adoption of deep neural networks. In 2013, Tomáš Mikolov and colleagues introduced word2vec, techniques for efficiently learning distributed vector representations of words from large text corpora. In 2014, Ian Goodfellow and colleagues introduced generative adversarial networks (GANs), a framework for training generative models through an adversarial process. In 2016, AlphaGo became the first computer program to defeat a professional human Go player without handicaps on a full-sized board, using deep neural networks and reinforcement learning. In 2017, Ashish Vaswani and colleagues introduced the Transformer, a neural network architecture based primarily on attention rather than recurrence or convolution.\n\nRelationships to other fields\n\nArtificial intelligence\n\nAs a scientific endeavour, machine learning grew out of the quest for artificial intelligence (AI). In the early days of AI as an academic discipline, some researchers were interested in having machines learn from data. They attempted to approach the problem with various symbolic methods, as well as what were then termed \"neural networks\"; these were mostly perceptrons and other models that were later found to be reinventions of the generalised linear models of statistics. Probabilistic reasoning was also employed, especially in automated medical diagnosis.\n\nHowever, an increasing emphasis on the logical, knowledge-based approach caused a rift between AI and machine learning. Probabilistic systems were plagued by theoretical and practical problems of data acquisition and representation. By 1980, expert systems had come to dominate AI, and statistics was out of favour. Work on symbolic/knowledge-based learning continued within AI, leading to inductive logic programming (ILP), but the more statistical line of research was now outside the field of AI proper, in pattern recognition and information retrieval. Neural network research was abandoned by AI and computer science around the same time. This subfield, termed \"connectionism\", was continued by researchers from other disciplines, including John Hopfield, David Rumelhart, and Geoffrey Hinton. Their main success came in the mid-1980s with the reinvention of backpropagation.\n\nMachine learning (ML), reorganised and recognised as its own field, started to flourish in the 1990s. The field changed its goal from achieving artificial intelligence to tackling solvable problems of a practical nature. It shifted focus away from the symbolic approaches it had inherited from AI, and toward methods and models borrowed from statistics, fuzzy logic, and probability theory.\n\nData compression\n\nThere is a close connection between machine learning and compression. A system that predicts the posterior probabilities of a sequence given its entire history can be used for optimal data compression (by using arithmetic coding on the output distribution). Conversely, an optimal compressor can be used for prediction (by finding the symbol that compresses best, given the previous history). This equivalence has been used as a justification for using data compression as a benchmark for \"general intelligence\".\n\nAn alternative view can show compression algorithms implicitly map strings into implicit feature space vectors, and compression-based similarity measures compute similarity within these feature spaces. For each compressor C(.) we define an associated vector space ℵ, such that C(.) maps an input string x, corresponding to the vector norm ||~x||. An exhaustive examination of the feature spaces underlying all compression algorithms is precluded by space; instead, feature vectors choose to examine three representative lossless compression methods, LZW, LZ77, and PPM.\n\nAccording to AIXI theory, a connection more directly explained in Hutter Prize, the best possible compression of x is the smallest possible software that generates x. For example, in that model, a zip file's compressed size includes both the zip file and the unzipping software, since you can not unzip it without both, but there may be an even smaller combined form.\n\nExamples of AI-powered audio/video compression software include NVIDIA Maxine, AIVC. Examples of software that can perform AI-powered image compression include OpenCV, TensorFlow, MATLAB's Image Processing Toolbox (IPT) and High-Fidelity Generative Image Compression.\n\nIn unsupervised machine learning, k-means clustering can be utilized to compress data by grouping similar data points into clusters. This technique simplifies handling extensive datasets that lack predefined labels and finds widespread use in fields such as image compression.\n\nData compression aims to reduce the size of data files, enhancing storage efficiency and speeding up data transmission. K-means clustering, an unsupervised machine learning algorithm, is employed to partition a dataset into a specified number of clusters, k, each represented by the centroid of its points. This process condenses extensive datasets into a more compact set of representative points. Particularly beneficial in image and signal processing, k-means clustering aids in data reduction by replacing groups of data points with their centroids, thereby preserving the core information of the original data while significantly decreasing the required storage space.\n\nLarge language models (LLMs) are also efficient lossless data compressors on some data sets, as demonstrated by DeepMind's research with the Chinchilla 70B model. Developed by DeepMind, Chinchilla 70B effectively compressed data, outperforming conventional methods such as Portable Network Graphics (PNG) for images and Free Lossless Audio Codec (FLAC) for audio. It achieved compression of image and audio data to 43.4% and 16.4% of their original sizes, respectively. There is, however, some reason to be concerned that the data set used for testing overlaps the LLM training data set, making it possible that the Chinchilla 70B model is only an efficient compression tool on data it has already been trained on.\n\nData mining\n\nMachine learning and data mining often employ the same methods and overlap significantly, but while machine learning focuses on prediction based on known properties learned from the training data, data mining focuses on the discovery of previously unknown properties in the data (this is the analysis step of knowledge discovery in databases). Data mining uses many machine learning methods, but with different goals; on the other hand, machine learning also employs data mining methods as \"unsupervised learning\" or as a preprocessing step to improve learner accuracy. Much of the confusion between these two research communities comes from the basic assumptions they work with: in machine learning, performance is usually evaluated with respect to the ability to reproduce known knowledge, while in knowledge discovery and data mining (KDD) the key task is the discovery of previously unknown knowledge. Evaluated with respect to known knowledge, an uninformed (unsupervised) method will easily be outperformed by other supervised methods, while in a typical KDD task, supervised methods cannot be used due to the unavailability of training data.\n\nMachine learning also has intimate ties to optimization: Many learning problems are formulated as minimisation of some loss function on a training set of examples. Loss functions express the discrepancy between the predictions of the model being trained and the actual problem instances (for example, in classification, one wants to assign a label to instances, and models are trained to correctly predict the preassigned labels of a set of examples).\n\nGeneralization\n\nCharacterizing the generalisation of various learning algorithms is an active topic of current research, especially for deep learning algorithms.\n\nStatistics\n\nMachine learning and statistics are closely related fields in terms of methods, but distinct in their principal goal: statistics draws population inferences from a sample, while machine learning finds generalisable predictive patterns.\n\nConventional statistical analyses require the a priori selection of a model most suitable for the study data set. In addition, only significant or theoretically relevant variables based on previous experience are included for analysis. In contrast, machine learning is not built on a pre-structured model; rather, the data shape the model by detecting underlying patterns. The more variables (input) used to train the model, the more accurate the ultimate model will be.\n\nLeo Breiman distinguished two statistical modelling paradigms: the data model and the algorithmic model, wherein \"algorithmic model\" means more or less the machine learning algorithms like Random forest.\n\nSome statisticians have adopted methods from machine learning, producing the field of statistical learning.\n\nStatistical physics\n\nAnalytical and computational techniques derived from deep-rooted physics of disordered systems can be extended to large-scale problems, including machine learning, e.g., to analyse the weight space of deep neural networks. Statistical physics is thus finding applications in the area of medical diagnostics.\n\n Theory\n\nA core objective of a learner is to generalise from its experience. Generalisation in this context is the ability of a learning machine to perform accurately on new, unseen examples/tasks after having experienced a learning data set. The training examples come from some generally unknown probability distribution (considered representative of the space of occurrences) and the learner has to build a general model about this space that enables it to produce sufficiently accurate predictions in new cases.\n\nThe computational analysis of machine learning algorithms and their performance is a branch of theoretical computer science known as computational learning theory. One major framework is the probably approximately correct learning model. Because training sets are finite and the future is uncertain, learning theory usually does not yield guarantees of the performance of algorithms. Instead, probabilistic bounds on the performance are quite common. The bias–variance decomposition is one way to quantify generalisation error.\n\nFor the best performance in the context of generalisation, the complexity of the hypothesis should match the complexity of the function underlying the data. If the hypothesis is less complex than the function, then the model has underfitted the data. If the complexity of the model is increased in response, then the training error decreases. But if the hypothesis is too complex, then the model is subject to overfitting and generalisation will be poorer.\n\nIn addition to performance bounds, learning theorists study the time complexity and feasibility of learning. In computational learning theory, a computation is considered feasible if it can be done in polynomial time. There are two kinds of time complexity results: Positive results show that a certain class of functions can be learned in polynomial time. Negative results show that certain classes cannot be learned in polynomial time.\n\nApproaches\n\nMachine learning approaches are traditionally divided into three broad categories, which correspond to learning paradigms, depending on the nature of the \"signal\" or \"feedback\" available to the learning system:\n\nSupervised learning: The computer is presented with example inputs and their desired outputs, given by a \"teacher\", and the goal is to learn a general rule that maps inputs to outputs.\n\nUnsupervised learning: No labels are given to the learning algorithm, leaving it on its own to find structure in its input. Unsupervised learning can be a goal in itself (discovering hidden patterns in data) or a means towards an end (feature learning).\n\nReinforcement learning: A computer program interacts with a dynamic environment in which it must perform a certain goal (such as driving a vehicle or playing a game against an opponent). As it navigates its problem space, the program is provided rewards as feedback, which it tries to maximize, thus resulting in the program learning from experience.\n\nAlthough each algorithm has advantages and limitations, no single algorithm works for all problems.\n\nSupervised learning\n\nSupervised learning algorithms build a mathematical model of a set of data that contains both the inputs and the desired outputs. The data, known as training data, consists of a set of training examples. Each training example has one or more inputs and the desired output, also known as a supervisory signal. In the mathematical model, each training example is represented by an array or vector, sometimes called a feature vector, and the training data is represented by a matrix. Through iterative optimisation of an objective function, supervised learning algorithms learn a function that can be used to predict the output associated with new inputs. An optimal function allows the algorithm to correctly determine the output for inputs that were not a part of the training data. An algorithm that improves the accuracy of its outputs or predictions over time is said to have learned to perform that task.\n\nTypes of supervised-learning algorithms include active learning, classification and regression. Classification algorithms are used when the outputs are restricted to a limited set of values, while regression algorithms are used when the outputs can take any numerical value within a range. For example, in a classification algorithm that filters emails, the input is an incoming email, and the output is the folder in which to file the email. In contrast, regression is used for tasks such as predicting a person's height based on factors like age and genetics or forecasting future temperatures based on historical data.\n\nSimilarity learning is an area of supervised machine learning closely related to regression and classification, but the goal is to learn from examples using a similarity function that measures how similar or related two objects are. It has applications in ranking, recommendation systems, visual identity tracking, face verification, and speaker verification.\n\nUnsupervised learning\n\nUnsupervised learning algorithms find structures in data that has not been labelled, classified or categorised. Instead of responding to feedback, unsupervised learning algorithms identify commonalities in the data and react based on the presence or absence of such commonalities in each new piece of data. Central applications of unsupervised machine learning include clustering, dimensionality reduction, and density estimation.\n\nCluster analysis is the assignment of a set of observations into subsets (called clusters) so that observations within the same cluster are similar according to one or more predesignated criteria, while observations drawn from different clusters are dissimilar. Different clustering techniques make different assumptions on the structure of the data, often defined by some similarity metric and evaluated, for example, by internal compactness, or the similarity between members of the same cluster, and separation, the difference between clusters. Other methods are based on estimated density and graph connectivity.\n\nA special type of unsupervised learning called self-supervised learning involves training a model by generating the supervisory signal from the data itself.\n\nDimensionality reduction\n\nDimensionality reduction is a process of reducing the number of random variables under consideration by obtaining a set of principal variables. In other words, it is a process of reducing the dimension of the feature set, also called the \"number of features\". Most of the dimensionality reduction techniques can be considered as either feature elimination or extraction. One of the popular methods of dimensionality reduction is principal component analysis (PCA). PCA involves changing higher-dimensional data (e.g., 3D) to a smaller space (e.g., 2D).\nThe manifold hypothesis proposes that high-dimensional data sets lie along low-dimensional manifolds, and many dimensionality reduction techniques make this assumption, leading to the areas of manifold learning and manifold regularisation.\n\nSemi-supervised learning\n\nSemi-supervised learning falls between unsupervised learning (without any labelled training data) and supervised learning (with completely labelled training data). Some of the training examples are missing training labels, yet many machine-learning researchers have found that unlabelled data, when used in conjunction with a small amount of labelled data, can produce a considerable improvement in learning accuracy.\n\nIn weakly supervised learning, the training labels are noisy,"
 },
 {
  "title": "Litre",
  "revision_id": "1376226710",
  "matched_by": "redirect",
  "text": "The litre (Commonwealth spelling) or liter (American spelling) (SI symbols L and l, other symbol used: ℓ) is a metric unit of volume. It is equal to 1 cubic decimetre (dm), 1000 cubic centimetres (cm) or 0.001 cubic metres (m). A cubic decimetre (or litre) occupies a volume of 10 cm × 10 cm × 10 cm (see figure) and is thus equal to one-thousandth of a cubic metre.\n\nThe original French metric system used the litre as a base unit. The word litre is derived from an older French unit, the litron, whose name came from Byzantine Greek—where it was a unit of weight, not volume—via Late Medieval Latin, and which equalled approximately 0.82 litres. The litre was also used in several subsequent versions of the metric system but is not an SI unit; the SI unit of volume is the cubic metre (m). The spelling used by the International Bureau of Weights and Measures is \"litre\", a spelling which is shared by most English-speaking countries. The spelling \"liter\" is predominantly used in American English.\n\nOne litre of liquid water has a mass of almost exactly one kilogram, because the kilogram was originally defined in 1795 as the mass of one cubic decimetre of water at the temperature of melting ice (0 °C). Subsequent redefinitions of the metre and kilogram mean that this relationship is no longer exact.\n\nDefinition\n\nA litre is a cubic decimetre, which is the volume of a cube 10 centimetres × 10 centimetres × 10 centimetres (1 L ≡ 1 dm ≡ 1000 cm). Hence 1 L ≡ 0.001 m ≡ 1000 cm; and 1 m (i.e. a cubic metre, which is the SI unit for volume) is exactly 1000 L.\n\nFrom 1901 to 1964, the litre was defined as the volume of one kilogram of pure water at maximum density (+3.98 °C) and standard pressure. The kilogram was in turn specified as the mass of the International Prototype of the Kilogram (a specific platinum/iridium cylinder) and was intended to be the same mass as the 1 litre of water referred to above. It was subsequently discovered that the cylinder was around 28 parts per million too large and thus, during this time, a litre was about 1.000028 dm. Additionally, the mass–volume relationship of water (as with any fluid) depends on temperature, pressure, purity and isotopic uniformity. In 1964, the definition relating the litre to mass was superseded. The litre is not an SI unit and is no longer described by the BIPM as accepted for use with the SI.\n\nA litre is equal in volume to the millistere, an obsolete non-SI metric unit formerly customarily used for dry measure.\n\nExplanation\n\nLitres are most commonly used for items (such as fluids and solids that can be poured) which are measured by the capacity or size of their container, whereas cubic metres (and derived units) are most commonly used for items measured either by their dimensions or their displacements. The litre is often also used in some calculated measurements, such as density (kg/L), allowing an easy comparison with the density of water.\n\nOne litre of water has a mass of almost exactly one kilogram when measured at its maximal density, which occurs at 3.984 °C. It follows, therefore, that ⁠1/1000⁠ of a litre, known as one millilitre (1 mL), of water has a mass of about 1 g, while 1000 litres of water has a mass of about 1000 kg (1 tonne or megagram).\n\nThis relationship holds because the gram was originally defined as the mass of 1 mL of water; however, this definition was abandoned in 1799 because the density of water changes with temperature and, very slightly, with pressure.\n\nThe density of water also depends on the isotopic ratios of the oxygen and hydrogen atoms in a particular sample. Modern measurements of Vienna Standard Mean Ocean Water, which is pure distilled water with an isotopic composition representative of the average of the world's oceans, show that it has a density of 0.999975±0.000001 kg/L at its point of maximum density (3.984 °C) under one standard atmosphere (101.325 kPa) of pressure.\n\nSI prefixes applied to the litre\n\nThe litre, though not an official SI unit, may be used with SI prefixes. The most commonly used derived unit is the millilitre, defined as one-thousandth of a litre, and also often referred to by the SI derived unit name \"cubic centimetre\". It is a commonly used measure, especially in medicine, cooking and automotive engineering. Other units may be found in the table below, where the more often used terms are in bold. However, some authorities advise against some of them; for example, in the United States, NIST advocates using the millilitre or litre instead of the centilitre. There are two international standard symbols for the litre: L and l. In the United States the former is preferred because of the risk that (in some fonts) the letter l and the digit 1 may be confused.\n\nNon-metric conversions\n\nSee also Imperial units and US customary units.\n\nRough conversions\n\nOne litre is about 5.7% larger than a US liquid quart, and about 12% smaller than an imperial quart.\n\nA mnemonic for its volume relative to an imperial pint is \"a litre of water's a pint and three-quarters\"; this is very close, as a litre is about 1.760 imperial pints.\n\nA cubic foot has a volume of exactly 28.316846592 L.\n\nSymbol\n\nOriginally, the only symbol for the litre was l (lowercase letter L), following the SI convention that only those unit symbols that abbreviate the name of a person start with a capital letter. In many English-speaking countries, however, the most common shape of a handwritten Arabic digit 1 is just a vertical stroke; that is, it lacks the upstroke added in many other cultures. Therefore, the digit \"1\" may easily be confused with the letter \"l\". In some computer typefaces, the two characters are barely distinguishable. As a result, L (uppercase letter L) was adopted by the CGPM as an alternative symbol for litre in 1979. The United States National Institute of Standards and Technology recommends the use of the uppercase letter L, a practice that is also widely followed in Canada and Australia. In these countries, the symbol L is also used with prefixes, as in mL and μL, instead of the traditional ml and μl used in Europe. In the UK and Ireland, as well as the rest of Europe, lowercase l is used with prefixes, though whole litres are often written in full (so, \"750 ml\" on a wine bottle, but often \"1 litre\" on a juice carton). In 1990, the International Committee for Weights and Measures stated that it was too early to choose a single symbol for the litre.\n\nScript l and Unicode \n\nPrior to 1979, the symbol ℓ came into common use in some countries; for example, it was recommended by South African Bureau of Standards publication M33 and Canada in the 1970s. This symbol can still be encountered occasionally in some English-speaking and European countries, and its use is ubiquitous in Japan and South Korea.\n\nFonts covering the CJK characters usually include not only the script small ℓ but also four precomposed characters: ㎕, ㎖, ㎗, and ㎘ for the microlitre, millilitre, decilitre and kilolitre to allow correct rendering for vertically written scripts. These have Unicode equivalents for compatibility, which are not recommended for use with new documents:\n\nU+2113 ℓ SCRIPT SMALL L\n\nU+3395 ㎕ SQUARE MU L\n\nU+3396 ㎖ SQUARE ML\n\nU+3397 ㎗ SQUARE DL\n\nU+3398 ㎘ SQUARE KL\n\nThe CJK Compatibility block also includes U+3351 ㍑ SQUARE RITTORU corresponding to リットル rittoru, Japanese for 'litre'.\n\nHistory\n\nThe first name of the litre was \"Cadil\"; standards are shown at the Musée des Arts et Métiers in Paris.\n\nThe litre was introduced in France in 1795 as one of the new \"republican units of measurement\" and defined as one cubic decimetre.\nOne litre of liquid water has a mass of almost exactly one kilogram, due to the gram being defined in 1795 as one cubic centimetre of water at the temperature of melting ice.\nThe original decimetre length was 44.344 lignes, which was revised in 1798 to 44.3296 lignes. This made the original litre 1.000974 of today's cubic decimetre. It was against this litre that the kilogram was constructed.\n\nIn 1879, the CIPM adopted the definition of the litre, with the symbol l (lowercase letter L).\n\nIn 1901, at the 3rd CGPM conference, the litre was redefined as the space occupied by 1 kg of pure water at the temperature of its maximum density (3.98 °C) under a pressure of 1 atm. This made the litre equal to about 1.000028 dm (earlier reference works usually put it at 1.000027 dm).\n\nIn 1964, at the 12th CGPM conference, the original definition was reverted to, and thus the litre was once again defined in exact relation to the metre, as another name for the cubic decimetre, that is, exactly 1 dm.\n\nIn 1979, at the 16th CGPM conference, the alternative symbol L (uppercase letter L) was adopted. It also expressed a preference that in the future only one of these two symbols should be retained, but in 1990 said it was still too early to do so.\n\nEveryday usage\n\nIn spoken English, the symbol \"mL\" (for millilitre) can be pronounced as \"mil\". This can potentially cause confusion with some other measurement words such as:\n\n\"mm\" for millimetre, a unit of length equal to one-thousandth of a metre\n\n\"mil\" for thousandth of an inch\n\n\"mil\", a Scandinavian unit of length equal to 10 kilometres\n\n\"mil\", unit of angular measurement\n\nThe abbreviation \"cc\" (for cubic centimetre, equal to a millilitre or mL) is a unit of the cgs system, which preceded the MKS system, which later evolved into the SI system. The abbreviation \"cc\" is still commonly used in many fields, including medical dosage and sizing for combustion engine displacement.\n\nThe microlitre (μL) has been known in the past as the lambda (λ), but this usage is discouraged as of 2014. In the medical field the microlitre is sometimes abbreviated as mcL on test results.\n\nIn the SI system, apart from prefixes for powers of 1000, use of the \"centi\" (10), \"deci\" (10), \"deca\" (10) and \"hecto\" (10) prefixes with litres is common. For example, in many European countries, the hectolitre is the typical unit for production and export volumes of beverages (milk, beer, soft drinks, wine, etc.) and for measuring the size of the catch and quotas for fishing boats; decilitres are common in Croatia, Switzerland and Scandinavia and often found in cookbooks, and restaurant and café menus; centilitres indicate the capacity of drinking glasses and of small bottles. In colloquial Dutch in Belgium, a \"vijfentwintiger\" and a \"drieëndertiger\" (literally \"twenty-fiver\" and \"thirty-threer\") are the common beer glasses, the corresponding bottles mention 25 cL and 33 cL. Bottles may also be 75 cL or half size at 37.5 cL for \"artisanal\" brews or 70 cL for wines or spirits. Cans come in 25 cL, 33 cL and 50 cL. Similarly, alcohol shots are often marked in cL in restaurant menus, typically 3 cL (1.06 imp fl oz; 1.01 US fl oz).\n\nIn countries where the metric system was adopted as the official measuring system after the SI standard was established, common usage eschews prefixes that are not powers of 1000. For example, in Canada, Australia, and New Zealand, consumer beverages are labelled almost exclusively using litres and millilitres. An exception is in pathology, where for instance blood lead level and blood sugar level may be measured in micrograms/milligrams per decilitre.\n\nFor larger volumes, kilolitres, megalitres, and gigalitres, have been used by the Northern Territory Government for measuring water consumption, reservoir capacities and river flows, although cubic metres are also used. Cubic metres are generally used for non-liquid commodities, such as sand and gravel, or storage space.\n\nSee also"
 },
 {
  "title": "Machine Learning (journal)",
  "revision_id": "1364329944",
  "matched_by": "title-minus-qualifier",
  "text": "Machine Learning is a peer-reviewed scientific journal, published since 1986.\n\nIn 2001, forty editors and members of the editorial board of Machine Learning resigned in order to support the Journal of Machine Learning Research (JMLR), saying that in the era of the internet, it was detrimental for researchers to continue publishing their papers in expensive journals with pay-access archives. Instead, they wrote, they supported the model of JMLR, in which authors retained copyright over their papers and archives were freely available on the internet.\n\nFollowing the mass resignation, Kluwer changed their publishing policy to allow authors to self-archive their papers online after peer-review.\n\nAbstracting and indexing\n\nThe journal is abstracted and indexed in several databases, for example in:\n\nScience Citation Index Expanded\n\nScopus\n\nEI Compendex\n\nINSPEC\n\nDBLP\n\nSelected articles\n\nJ.R. Quinlan (1986). \"Induction of Decision Trees\". Machine Learning. 1: 81–106. doi:10.1007/BF00116251.\n\nNick Littlestone (1988). \"Learning Quickly When Irrelevant Attributes Abound: A New Linear-threshold Algorithm\" (PDF). Machine Learning. 2 (4): 285–318. doi:10.1007/BF00116827. Archived from the original (PDF) on 2022-07-02.\n\nJohn R. Anderson and Michael Matessa (1992). \"Explorations of an Incremental, Bayesian Algorithm for Categorization\". Machine Learning. 9 (4): 275–308. doi:10.1007/BF00994109.\n\nDavid Klahr (1994). \"Children, Adults, and Machines as Discovery Systems\". Machine Learning. 14 (3): 313–320. doi:10.1007/BF00993981.\n\nThomas Dean and Dana Angluin and Kenneth Basye and Sean Engelson and Leslie Kaelbling and Evangelos Kokkevis and Oded Maron (1995). \"Inferring Finite Automata with Stochastic Output Functions and an Application to Map Learning\". Machine Learning. 18: 81–108. doi:10.1007/BF00993822.\n\nLuc De Raedt and Luc Dehaspe (1997). \"Clausal Discovery\". Machine Learning. 26 (2/3): 99–146. doi:10.1023/A:1007361123060.\n\nC. de la Higuera (1997). \"Characteristic Sets for Grammatical Inference\". Machine Learning. 27: 1–14.\n\nRobert E. Schapire and Yoram Singer (1999). \"Improved Boosting Algorithms Using Confidence-rated Predictions\". Machine Learning. 37 (3): 297–336. doi:10.1023/A:1007614523901.\n\nRobert E. Schapire and Yoram Singer (2000). \"BoosTexter: A Boosting-based System for Text Categorization\". Machine Learning. 39 (2/3): 135–168. doi:10.1023/A:1007649029923.\n\nP. Rossmanith and T. Zeugmann (2001). \"Stochastic Finite Learning of the Pattern Languages\". Machine Learning. 44 (1–2): 67–91. doi:10.1023/A:1010875913047.\n\nParekh, Rajesh; Honavar, Vasant (2001). \"Learning DFA from Simple Examples\". Machine Learning. 44 (1/2): 9–35. doi:10.1023/A:1010822518073.\n\nAyhan Demiriz and Kristin P. Bennett and John Shawe-Taylor (2002). \"Linear Programming Boosting via Column Generation\". Machine Learning. 46: 225–254. doi:10.1023/A:1012470815092.\n\nSimon Colton and Stephen Muggleton (2006). \"Mathematical Applications of Inductive Logic Programming\" (PDF). Machine Learning. 64 (1–3): 25–64. doi:10.1007/s10994-006-8259-x.\n\nWill Bridewell and Pat Langley and Ljupco Todorovski and Saso Dzeroski (2008). \"Inductive Process Modeling\". Machine Learning.\n\nStephen Muggleton and Alireza Tamaddoni-Nezhad (2008). \"QG/GA: a stochastic search for Progol\". Machine Learning. 70 (2–3): 121–133. doi:10.1007/s10994-007-5029-3.\n\nReferences"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q2539",
  "label": "machine learning",
  "description": "scientific study of algorithms and statistical models that computer systems use to perform tasks without explicit instructions",
  "aliases": [
   "ML",
   "statistical learning",
   "statistical machine learning"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q374814",
    "Q43015",
    "Q1047113",
    "Q2267705",
    "Q130609847",
    "Q123370638"
   ],
   "P279": [
    "Q21198",
    "Q11660"
   ],
   "P361": [
    "Q11660",
    "Q395"
   ],
   "P527": [
    "Q7094097",
    "Q334384",
    "Q1152135",
    "Q830687"
   ],
   "P1889": [
    "Q11660",
    "Q117349473",
    "Q117349475",
    "Q211930",
    "Q133500"
   ]
  },
  "revision_id": "2570835532",
  "value_labels": {
   "Q11862829": "academic discipline",
   "Q374814": "certification",
   "Q43015": "finance",
   "Q1047113": "field of study",
   "Q2267705": "field of study",
   "Q130609847": "learning approach",
   "Q123370638": "branch of computer science",
   "Q21198": "computer science",
   "Q11660": "artificial intelligence",
   "Q395": "mathematics",
   "Q7094097": "online machine learning",
   "Q334384": "supervised learning",
   "Q1152135": "unsupervised learning",
   "Q830687": "reinforcement learning",
   "Q117349473": "artificial intelligence model",
   "Q117349475": "artificial intelligence model type",
   "Q211930": "Marxism–Leninism",
   "Q133500": "learning"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11582",
  "label": "litre",
  "description": "non-SI unit of volume equal to one cubic decimetre",
  "aliases": [
   "L",
   "l",
   "litres"
  ],
  "claims": {
   "P31": [
    "Q1302471",
    "Q106839753",
    "Q3268848",
    "Q82047057",
    "Q106839917"
   ],
   "P460": [
    "Q2175964",
    "Q48680"
   ],
   "P1889": [
    "Q59279570"
   ]
  },
  "revision_id": "2572778923",
  "value_labels": {
   "Q1302471": "unit of volume",
   "Q106839753": "SI-accepted non-SI unit",
   "Q3268848": "non-SI unit mentioned in and accepted with the SI",
   "Q82047057": "UCUM derived unit",
   "Q106839917": "non-SI unit",
   "Q2175964": "cubic decimetre",
   "Q48680": "Maß",
   "Q59279570": "Litre"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q6723676",
  "label": "Machine Learning",
  "description": "journal",
  "aliases": [],
  "claims": {
   "P31": [
    "Q5633421",
    "Q5253501"
   ]
  },
  "revision_id": "2563308239",
  "value_labels": {
   "Q5633421": "scientific journal",
   "Q5253501": "delayed open access journal"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11862829",
  "label": "academic discipline",
  "description": "field of study organized around a distinct body of knowledge, theories, methods, or subject matter",
  "aliases": [
   "branch (academic)",
   "discipline",
   "academic field",
   "academic branch",
   "academic specialty",
   "academic specialism",
   "research field",
   "field of research",
   "field of study",
   "sub-discipline"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q1047113"
   ],
   "P460": [
    "Q2465832",
    "Q2267705",
    "Q627436",
    "Q362165"
   ],
   "P1889": [
    "Q3242580",
    "Q1166828",
    "Q1391009",
    "Q82957"
   ]
  },
  "revision_id": "2562020019",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q374814",
  "label": "certification",
  "description": "formal attestation of certain characteristics of an object, person, or organization",
  "aliases": [
   "certify",
   "certified"
  ],
  "claims": {
   "P279": [
    "Q104637332",
    "Q107329943",
    "Q427581",
    "Q16861606"
   ],
   "P361": [
    "Q1087786",
    "Q757012",
    "Q4218455"
   ],
   "P527": [
    "Q16023913",
    "Q16155280"
   ],
   "P460": [
    "Q12219184"
   ]
  },
  "revision_id": "2567801965",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q43015",
  "label": "finance",
  "description": "academic discipline studying businesses, financing, investments and protection of economic value",
  "aliases": [],
  "claims": {
   "P31": [
    "Q11862829",
    "Q4671286",
    "Q1474521",
    "Q1047113",
    "Q2267705",
    "Q627436"
   ],
   "P279": [
    "Q18564125",
    "Q113141571"
   ],
   "P527": [
    "Q1361817"
   ]
  },
  "revision_id": "2567836261",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1047113",
  "label": "field of study",
  "description": "field limited to a specific area of ​​knowledge; specialization in an occupation or branch of learning; a specific use",
  "aliases": [
   "subject area",
   "domain",
   "special field",
   "specialism",
   "subdiscipline",
   "sub-discipline",
   "specialized field of study",
   "specialty",
   "special branches"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q105948247",
    "Q110403031",
    "Q26256810",
    "Q21040055"
   ],
   "P361": [
    "Q9081"
   ],
   "P1889": [
    "Q123286730",
    "Q2267705"
   ]
  },
  "revision_id": "2562271253",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2267705",
  "label": "field of study",
  "description": "field of study leading to a specific degree",
  "aliases": [
   "field of education",
   "area of study"
  ],
  "claims": {
   "P279": [
    "Q1047113"
   ],
   "P527": [
    "Q13442814"
   ],
   "P460": [
    "Q11862829",
    "Q2465832",
    "Q4671286"
   ],
   "P1889": [
    "Q1047113"
   ]
  },
  "revision_id": "2544362366",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q130609847",
  "label": "learning approach",
  "description": "metaclass for learning and education",
  "aliases": [
   "type of learning"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q49094543"
   ],
   "P279": [
    "Q21146257"
   ]
  },
  "revision_id": "2567630981",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q123370638",
  "label": "branch of computer science",
  "description": "Computer Science sub-disciplines",
  "aliases": [
   "Computer Science sub-discipline",
   "subfield of computer science",
   "branch of computer science"
  ],
  "claims": {
   "P31": [
    "Q24017414",
    "Q5962346"
   ],
   "P279": [
    "Q2465832",
    "Q1047113",
    "Q11862829"
   ]
  },
  "revision_id": "2551194511",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21198",
  "label": "computer science",
  "description": "study of computation",
  "aliases": [
   "computing science",
   "CS",
   "Computer Science",
   "science of computing",
   "information processing science",
   "computer sciences",
   "computing sciences",
   "sciences of computing",
   "computation science",
   "computing",
   "computer studies",
   "comp sci",
   "comp. sci",
   "comp. sci.",
   "compsci",
   "informatics"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q4671286"
   ],
   "P279": [
    "Q816264"
   ],
   "P527": [
    "Q2878974",
    "Q538722",
    "Q11660",
    "Q844718"
   ],
   "P460": [
    "Q4027615"
   ],
   "P1889": [
    "Q4027615",
    "Q16387",
    "Q131222",
    "Q117801"
   ]
  },
  "revision_id": "2569264093",
  "ancestor_of": "Q2539",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110402867",
  "label": "knowledge classification",
  "description": "Wikidata metaclass",
  "aliases": [
   "knowledge classification system",
   "classification system of knowledge"
  ],
  "claims": {
   "P31": [
    "Q121344523"
   ],
   "P279": [
    "Q5962346"
   ],
   "P1889": [
    "Q110403031"
   ]
  },
  "revision_id": "2569936517",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q104637332",
  "label": "planned process",
  "description": "process that takes place with human or agentic involvement or planning",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116505632"
   ],
   "P279": [
    "Q3249551",
    "Q451967"
   ]
  },
  "revision_id": "2547914180",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q107329943",
  "label": "acknowledgement",
  "description": "act of affirming a fact already recognized by others to be true",
  "aliases": [
   "recognition",
   "acknowledge",
   "recognize",
   "accede",
   "certify",
   "certification",
   "attest",
   "attestation",
   "affirmation"
  ],
  "claims": {
   "P279": [
    "Q814441"
   ],
   "P1889": [
    "Q23199274",
    "Q382812",
    "Q2684591",
    "Q109267112",
    "Q814441"
   ]
  },
  "revision_id": "2507983347",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q427581",
  "label": "intangible asset",
  "description": "asset that lacks physical substance and usually is very hard to evaluate",
  "aliases": [
   "intangible assets"
  ],
  "claims": {
   "P31": [
    "Q256686",
    "Q116460050"
   ],
   "P279": [
    "Q46737",
    "Q6042535"
   ],
   "P527": [
    "Q253623",
    "Q1297822",
    "Q1146011",
    "Q157499",
    "Q167270",
    "Q1417728",
    "Q7397"
   ]
  },
  "revision_id": "2547192435",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q16861606",
  "label": "credential",
  "description": "qualification or authority issued by a competent third party",
  "aliases": [],
  "claims": {
   "P279": [
    "Q17537576"
   ]
  },
  "revision_id": "2568509527",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4671286",
  "label": "academic major",
  "description": "focus of academic study leading to a degree",
  "aliases": [
   "main speciality of study",
   "main field of study",
   "speciality of study",
   "field of study",
   "main discipline",
   "major discipline",
   "university discipline",
   "major concentration",
   "major",
   "university major"
  ],
  "claims": {
   "P279": [
    "Q11862829"
   ],
   "P460": [
    "Q2267705"
   ]
  },
  "revision_id": "2541824123",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1474521",
  "label": "function",
  "description": "responsibility within an organization; term in organizational theory",
  "aliases": [],
  "claims": {
   "P279": [
    "Q1168263"
   ],
   "P361": [
    "Q149584",
    "Q207449"
   ]
  },
  "revision_id": "2482143030",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q105948247",
  "label": "knowledge system",
  "description": "systems of knowledge produced over time through interactions with other human beings",
  "aliases": [
   "knowledge systems"
  ],
  "claims": {
   "P31": [
    "Q96116695"
   ],
   "P279": [
    "Q3622126"
   ],
   "P527": [
    "Q9081"
   ]
  },
  "revision_id": "2522085818",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110403031",
  "label": "knowledge type",
  "description": "Wikidata metaclass",
  "aliases": [
   "type of knowledge"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q140458154"
   ],
   "P1889": [
    "Q110402867",
    "Q125161275"
   ]
  },
  "revision_id": "2548067834",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q26256810",
  "label": "topic",
  "description": "topic or area addressed by a work or set of works",
  "aliases": [
   "issue",
   "subject",
   "theme",
   "topic of a work",
   "subject matter of a work",
   "matter",
   "main subject",
   "main topic",
   "subject matter",
   "gum:SubjectMatter"
  ],
  "claims": {
   "P279": [
    "Q11028",
    "Q12488383",
    "Q16514889"
   ],
   "P460": [
    "Q1053916",
    "Q200801"
   ],
   "P1889": [
    "Q14095863",
    "Q9340580"
   ]
  },
  "revision_id": "2567187301",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q19478619",
  "label": "metaclass",
  "description": "class which has instances that are all themselves classes",
  "aliases": [
   "Wikidata metaclass",
   "Wikidata metaclasses"
  ],
  "claims": {
   "P31": [
    "Q151885",
    "Q19868531",
    "Q115490628"
   ],
   "P279": [
    "Q16889133"
   ],
   "P361": [
    "Q324254"
   ],
   "P1889": [
    "Q19828331",
    "Q123369568",
    "Q1924819",
    "Q24017414"
   ]
  },
  "revision_id": "2559895276",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q49094543",
  "label": "educational concept",
  "description": "type of concept",
  "aliases": [
   "educational approach",
   "pedagogical concept",
   "pedagogical approach"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q137429456"
   ],
   "P279": [
    "Q131362181"
   ]
  },
  "revision_id": "2547013680",
  "ancestor_of": "Q2539",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1302471",
  "label": "unit of volume",
  "description": "unit of measurement",
  "aliases": [
   "volume unit",
   "Units of volume",
   "<size/dimension units: volume>"
  ],
  "claims": {
   "P279": [
    "Q141631499"
   ]
  },
  "revision_id": "2568408608",
  "ancestor_of": "Q11582",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106839753",
  "label": "SI-accepted non-SI unit",
  "description": "an SI-accepted unit of measurement that contains a non-SI unit and may contain an SI unit - SI prefixes may only be used with SI units",
  "aliases": [
   "SI-accepted unit",
   "accepted non-SI unit"
  ],
  "claims": {
   "P279": [
    "Q106839917",
    "Q87252761"
   ]
  },
  "revision_id": "2473849759",
  "ancestor_of": "Q11582",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3268848",
  "label": "non-SI unit mentioned in and accepted with the SI",
  "description": "unit explicitly mentioned in and accepted for use with the International System of Units",
  "aliases": [],
  "claims": {
   "P279": [
    "Q106839753"
   ]
  },
  "revision_id": "2528794207",
  "ancestor_of": "Q11582",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q82047057",
  "label": "UCUM derived unit",
  "description": "derived unit of measurement within the Unified Code for Units of Measure specification",
  "aliases": [],
  "claims": {
   "P279": [
    "Q47574"
   ],
   "P361": [
    "Q2494286"
   ]
  },
  "revision_id": "2547529357",
  "ancestor_of": "Q11582",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106839917",
  "label": "non-SI unit",
  "description": "unit not part of the International System of Units (SI)",
  "aliases": [],
  "claims": {
   "P279": [
    "Q47574"
   ]
  },
  "revision_id": "2450376683",
  "ancestor_of": "Q11582",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q141631499",
  "label": "composite unit of measure",
  "description": "",
  "aliases": [
   "composite measurement unit"
  ],
  "claims": {
   "P279": [
    "Q47574",
    "Q141630830"
   ]
  },
  "revision_id": "2553153959",
  "ancestor_of": "Q11582",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q87252761",
  "label": "SI or accepted non-SI unit",
  "description": "SI unit (metre, second ...), for use with SI accepted unit (hour, litre ...) or a combination (kilometre per hour ...)",
  "aliases": [
   "SI-accepted unit"
  ],
  "claims": {
   "P279": [
    "Q47574"
   ]
  },
  "revision_id": "2199437681",
  "ancestor_of": "Q11582",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q47574",
  "label": "unit of measurement",
  "description": "real scalar quantity, defined and adopted by convention, with which any other quantity of the same kind can be compared to express the ratio of the two quantities as a number (VIM)",
  "aliases": [
   "unit",
   "measurement unit",
   "unit of measure",
   "physical unit"
  ],
  "claims": {
   "P279": [
    "Q39875001",
    "Q181175",
    "Q71550118",
    "Q141328123",
    "Q141365972",
    "Q141750218"
   ],
   "P361": [
    "Q932268",
    "Q110597311"
   ],
   "P1889": [
    "Q21514353",
    "Q19110",
    "Q1370617",
    "Q2198779",
    "Q141240306"
   ]
  },
  "revision_id": "2570942294",
  "ancestor_of": "Q11582",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5633421",
  "label": "scientific journal",
  "description": "periodical journal publishing scientific research",
  "aliases": [
   "scientific magazine",
   "journal",
   "science journal",
   "scientific journals",
   "journals"
  ],
  "claims": {
   "P31": [
    "Q21114848"
   ],
   "P279": [
    "Q685935",
    "Q591041",
    "Q49850",
    "Q737498"
   ],
   "P1889": [
    "Q737498",
    "Q1911105"
   ]
  },
  "revision_id": "2557906009",
  "ancestor_of": "Q6723676",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5253501",
  "label": "delayed open access journal",
  "description": "type of journal providing free online access upon the expiry of an embargo period",
  "aliases": [],
  "claims": {
   "P279": [
    "Q5633421"
   ],
   "P1889": [
    "Q773668",
    "Q5953270"
   ]
  },
  "revision_id": "2470254348",
  "ancestor_of": "Q6723676",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21114848",
  "label": "magazine genre",
  "description": "type of genre",
  "aliases": [
   "genre of magazine",
   "periodicals genre",
   "journal genre"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q483394"
   ]
  },
  "revision_id": "2567686963",
  "ancestor_of": "Q6723676",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q685935",
  "label": "trade magazine",
  "description": "periodical dedicated to a particular field",
  "aliases": [
   "professional magazine",
   "trade rag",
   "trade journal",
   "trade publication"
  ],
  "claims": {
   "P31": [
    "Q21114848"
   ],
   "P279": [
    "Q41298"
   ],
   "P361": [
    "Q1391420"
   ],
   "P1889": [
    "Q55630524",
    "Q918727"
   ]
  },
  "revision_id": "2523496555",
  "ancestor_of": "Q6723676",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q591041",
  "label": "scientific publication",
  "description": "publication that reports empirical or theoretical work in the sciences",
  "aliases": [
   "scholarly publication"
  ],
  "claims": {
   "P31": [
    "Q39725049"
   ],
   "P279": [
    "Q732577",
    "Q47461344",
    "Q11826511",
    "Q12042160",
    "Q55915575"
   ],
   "P527": [
    "Q4119870",
    "Q265158",
    "Q1713"
   ]
  },
  "revision_id": "2567595781",
  "ancestor_of": "Q6723676",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q49850",
  "label": "journal",
  "description": "written medium (duplicate item)",
  "aliases": [],
  "claims": {
   "P31": [
    "Q17362920"
   ],
   "P279": [
    "Q1261026",
    "Q1002697"
   ],
   "P361": [
    "Q11030"
   ],
   "P460": [
    "Q41298"
   ],
   "P1889": [
    "Q361785"
   ]
  },
  "revision_id": "2516833327",
  "ancestor_of": "Q6723676",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-92463238-n",
  "lemmas": [
   "machine learning"
  ],
  "gloss": "a subfield of computer science that explores the study and construction of algorithms that can learn from and make predictions on data.",
  "examples": [
   "As a scientific endeavour, machine learning grew out of the quest for artificial intelligence."
  ],
  "relations": {
   "hypernym": [
    "oewn-06138021-n"
   ]
  },
  "relation_targets": {
   "oewn-06138021-n": "computer science, computing"
  }
 },
 {
  "synset": "oewn-13644955-n",
  "lemmas": [
   "milliliter",
   "millilitre",
   "mil",
   "ml",
   "cubic centimeter",
   "cubic centimetre",
   "cc"
  ],
  "gloss": "a metric unit of volume equal to one thousandth of a liter",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-13637335-n"
   ],
   "part_meronym": [
    "oewn-13644736-n"
   ],
   "part_holonym": [
    "oewn-13645213-n"
   ]
  },
  "relation_targets": {
   "oewn-13637335-n": "metric capacity unit",
   "oewn-13644736-n": "cubic millimeter, cubic millimetre",
   "oewn-13645213-n": "centiliter, centilitre, cl"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 3: Natural language processing (`d168utcmjy`)

~~~~text
Concept record:
{
 "id": "d168utcmjy",
 "preferred_name": "Natural language processing",
 "kind": "method",
 "broad_class": "skill",
 "variants": [
  {
   "label": "NLP"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "k2fnt61kzq",
  "name": "Apache OpenNLP"
 },
 {
  "id": "gvwuv6xjpu",
  "name": "Natural language generation"
 },
 {
  "id": "erag95km1k",
  "name": "Natural language processing systems"
 },
 {
  "id": "ivx36sezid",
  "name": "Natural language understanding"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "oxu0hc83pv",
  "name": "Computer science"
 },
 {
  "id": "flxbx98seh",
  "name": "Machine learning"
 },
 {
  "id": "tx96mffcus",
  "name": "Neural networks"
 },
 {
  "id": "hj8i6mh3zz",
  "name": "Chinese"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "ag0hpcesx8",
  "name": "Large language models"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "enx40y6s0v",
  "name": "Speech Recognition"
 },
 {
  "id": "hwaf7og623",
  "name": "Doctor of Nursing Practice"
 },
 {
  "id": "gxbpx9za78",
  "name": "Neonatal Resuscitation Program"
 },
 {
  "id": "gkq7vbv3ql",
  "name": "npm"
 },
 {
  "id": "ap5dyxzh9v",
  "name": "Licensed Practical Nurse"
 },
 {
  "id": "bxl9tjsu5g",
  "name": "Mail processing"
 },
 {
  "id": "n4go9oimdg",
  "name": "spaCy"
 },
 {
  "id": "w49tfjhjw9",
  "name": "Claim processing"
 },
 {
  "id": "hfschl129h",
  "name": "Tulu"
 },
 {
  "id": "xbnzpi95t0",
  "name": "Language teaching"
 },
 {
  "id": "m4rbaj4f3l",
  "name": "Invoice processing"
 },
 {
  "id": "ciqcmsfd1o",
  "name": "Hungarian"
 },
 {
  "id": "b53t6y9iys",
  "name": "Catalan"
 },
 {
  "id": "zvfjqwa8g1",
  "name": "Production and Processing"
 },
 {
  "id": "zb709ig3an",
  "name": "Lisp"
 },
 {
  "id": "y13g58ujg8",
  "name": "Serial Line Internet Protocol"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:65",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Analyst. financial analysis, python, data analysis, data analytics, natural language processing, investment banking, business analysis, analysis"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:18",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Software Engineer. …ng information retrieval, distributed computing, large-scale system design, networking and data storage, security, artificial intelligence, natural language processing, UI design and mobile; the list goes on and is growing every day. As a software engineer, you will work on a specific project critic…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:197",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Senior Business Analyst (Ai/dữ Liệu/smart City). [\"Business Analysis\", \"Product Owner\", \"AI\", \"Embedded\", \"NLP\"]"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:1630",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Senior Manager, Data Science - AI Foundations. …LangChain, Lightning, VectorDBs, and more - to reveal the insights hidden within huge volumes of numeric and textual data. Be the expert in Natural Language Processing (NLP) to harness the power of Large Language Models (LLMs), adapt and finetune them for customer facing applications and features. B…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:18653",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "Python, NLP, Pytorch"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Natural language processing",
  "revision_id": "1374356070",
  "matched_by": "title",
  "text": "Natural language processing (NLP) is the processing of natural language information by a computer. NLP is a subfield of computer science and is closely associated with artificial intelligence. NLP is also related to information retrieval, knowledge representation, computational linguistics, and linguistics more broadly.\n\nMajor processing tasks in an NLP system include: speech recognition, text classification, natural language understanding, and natural language generation.\n\nHistory\n\nNatural language processing has its roots in the 1950s. Already in 1950, Alan Turing published an article titled \"Computing Machinery and Intelligence,\" which proposed what is now called the Turing test as a criterion of intelligence, though at the time that was not articulated as a problem separate from artificial intelligence. The proposed test includes a task that involves the automated interpretation and generation of natural language.\n\nSymbolic NLP (1950s – early 1990s)\n\nThe premise of symbolic NLP is often illustrated using John Searle's Chinese room thought experiment: Given a collection of rules (e.g., a Chinese phrasebook, with questions and matching answers), the computer emulates natural language understanding (or other NLP tasks) by applying those rules to the data it confronts.\n\n1950s: The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into English. The authors claimed that within three or five years, machine translation would be a solved problem. However, real progress was much slower, and after the ALPAC report in 1966, which found that ten years of research had failed to fulfill the expectations, funding for machine translation was dramatically reduced. Little further research in machine translation was conducted in America (though some research continued elsewhere, such as Japan and Europe) until the late 1980s when the first statistical machine translation systems were developed.\n\n1960s: Some notably successful natural language processing systems developed in the 1960s were SHRDLU, a natural language system working in restricted \"blocks worlds\" with restricted vocabularies, and ELIZA, a simulation of Rogerian psychotherapy, written by Joseph Weizenbaum between 1964 and 1966. Despite using minimal information about human thought or emotion, ELIZA was able to produce interactions that appeared human-like. When the \"patient\" exceeded the very small knowledge base, ELIZA might provide a generic response, for example, responding to \"My head hurts\" with \"Why do you say your head hurts?\". Ross Quillian's successful work on natural language was demonstrated with a vocabulary of only twenty words, because that was all that would fit in a computer memory at the time.\n\n1970s: During the 1970s, many programmers began to write \"conceptual ontologies\", which structured real-world information into computer-understandable data. Examples are MARGIE (Schank, 1975), SAM (Cullingford, 1978), PAM (Wilensky, 1978), TaleSpin (Meehan, 1976), QUALM (Lehnert, 1977), Politics (Carbonell, 1979), and Plot Units (Lehnert 1981). During this time, the first chatterbots were written (e.g., PARRY).\n\n1980s: The 1980s and early 1990s mark the heyday of symbolic methods in NLP. Focus areas of the time included research on rule-based parsing (e.g., the development of HPSG as a computational operationalization of generative grammar), morphology (e.g., two-level morphology), semantics (e.g., Lesk algorithm), reference (e.g., within Centering Theory) and other areas of natural language understanding (e.g., in the Rhetorical Structure Theory). Other lines of research were continued, e.g., the development of chatterbots with Racter and Jabberwacky. An important development (that eventually led to the statistical turn in the 1990s) was the rising importance of quantitative evaluation in this period.\n\nStatistical NLP (1990s–present)\n\nUp until the 1980s, most natural language processing systems were based on complex sets of hand-written rules. Starting in the late 1980s, however, there was a revolution in natural language processing with the introduction of machine learning algorithms for language processing. This shift was influenced by increasing computational power (see Moore's law) and a decline in the dominance of Chomskyan linguistic theories (e.g. transformational grammar), whose theoretical underpinnings discouraged the sort of corpus linguistics that underlies the machine-learning approach to language processing. \n\n1990s: Many early successes of statistical NLP occurred in machine translation, particularly through work at IBM Research. An IBM team including Frederick Jelinek, Peter F. Brown, and Robert Mercer developed a probabilistic approach to translation, described in the 1990 paper A Statistical Approach to Machine Translation. The work used parallel English and French text from the proceedings of the Parliament of Canada and was subsequently developed into the IBM alignment models. However, such systems often depended on large task-specific corpora, making the availability of suitable training data an important limitation.\n\n2000s: With the growth of the web, increasing amounts of raw (unannotated) language data have become available since the mid-1990s. Research has thus increasingly focused on unsupervised and semi-supervised learning algorithms. Such algorithms can learn from data that has not been hand-annotated with the desired answers or using a combination of annotated and non-annotated data. Generally, this task is much more difficult than supervised learning, and typically produces less accurate results for a given amount of input data. However, large quantities of non-annotated data are available (including, among other things, the entire content of the World Wide Web), which can often make up for the worse efficiency if the algorithm used has a low enough time complexity to be practical.\n\n2003: word n-gram model, at the time the best statistical algorithm, is outperformed by a multi-layer perceptron (with a single hidden layer and context length of several words, trained on up to 14 million words, by Bengio et al.)\n\n2010: Tomáš Mikolov (then a PhD student at Brno University of Technology) with co-authors applied a simple recurrent neural network with a single hidden layer to language modeling, and in the following years he went on to develop Word2vec. In the 2010s, representation learning and deep neural network-style (featuring many hidden layers) machine learning methods became widespread in natural language processing. This shift gained momentum due to results showing that such techniques can achieve state-of-the-art results in many natural language tasks, e.g., in language modeling and parsing. This is increasingly important in medicine and healthcare, where NLP helps analyze notes and text in electronic health records that would otherwise be inaccessible for study when seeking to improve care or protect patient privacy.\n\nApproaches: Symbolic, statistical, neural networks\n\nSymbolic approach, i.e., the hand-coding of a set of rules for manipulating symbols, coupled with a dictionary lookup, was historically the first approach used both by AI in general and by NLP in particular: such as by writing grammars or devising heuristic rules for stemming.\n\nMachine learning approaches, which include both statistical and neural networks, on the other hand, have many advantages over the symbolic approach:\n\nboth statistical and neural network methods tend to focus more on the most common cases extracted from a corpus of texts, whereas the rule-based approach needs to provide rules for both rare and common cases equally.\n\nlanguage models, produced by either statistical or neural network methods, are more robust to both unfamiliar (e.g. containing words or structures that have not been seen before) and erroneous input (e.g. with misspelled words or words accidentally omitted) in comparison to the rule-based systems, which are also more costly to produce.\n\nthe larger such a (probabilistic) language model is, the more accurate it becomes, in contrast to rule-based systems that can gain accuracy only by increasing the amount and complexity of the rules leading to intractability problems.\n\nRule-based systems are commonly used:\n\nwhen the amount of training data is insufficient to successfully apply machine learning methods, e.g., for the machine translation of low-resource languages such as provided by the Apertium system,\n\nfor preprocessing in NLP pipelines, e.g., tokenization, or\n\nfor post-processing and transforming the output of NLP pipelines, e.g., for knowledge extraction from syntactic parses.\n\nStatistical approach\n\nIn the late 1980s and mid-1990s, the statistical approach ended a period of AI winter, which was caused by the inefficiencies of the rule-based approaches.\n\nThe earliest decision trees, producing systems of hard if–then rules, were still very similar to the old rule-based approaches.\nOnly the introduction of hidden Markov models, applied to part-of-speech tagging, announced the end of the old rule-based approach.\n\nNeural networks\n\nA major drawback of statistical methods is that they require elaborate feature engineering. Since 2015, neural network–based methods have increasingly replaced traditional statistical approaches, using semantic networks and word embeddings to capture semantic properties of words.\n\nIntermediate tasks (e.g., part-of-speech tagging and dependency parsing) are not needed anymore.\n\nNeural machine translation, based on the then-newly invented sequence-to-sequence transformations, made obsolete the intermediate steps, such as word alignment, previously necessary for statistical machine translation.\n\nCommon NLP tasks\n\nThe following is a list of some of the most commonly researched tasks in natural language processing. Some of these tasks have direct real-world applications, while others more commonly serve as subtasks that are used to aid in solving larger tasks.\n\nThough natural language processing tasks are closely intertwined, they can be subdivided into categories for convenience. A coarse division is given below.\n\nText and speech processing\n\nOptical character recognition (OCR)\n\nGiven an image representing printed text, determine the corresponding text.\nSpeech recognition\n\nGiven a sound clip of a person or people speaking, determine the textual representation of the speech. This is the opposite of text to speech and is one of the extremely difficult problems colloquially termed \"AI-complete\" (see above). In natural speech there are hardly any pauses between successive words, and thus speech segmentation is a necessary subtask of speech recognition (see below). In most spoken languages, the sounds representing successive letters blend into each other in a process termed coarticulation, so the conversion of the analog signal to discrete characters can be a very difficult process. Also, given that words in the same language are spoken by people with different accents, the speech recognition software must be able to recognize the wide variety of input as being identical to each other in terms of its textual equivalent.\nSpeech segmentation\n\nGiven a sound clip of a person or people speaking, separate it into words. A subtask of speech recognition and typically grouped with it.\nText-to-speech\n\nGiven a text, transform those units and produce a spoken representation. Text-to-speech can be used to aid the visually impaired.\nWord segmentation (Tokenization)\n\nTokenization is a text-processing technique that divides text into individual words or word fragments. This technique results in two key components: a word index and tokenized text. The word index is a list that maps unique words to specific numerical identifiers, and the tokenized text replaces each word with its corresponding numerical token. These numerical tokens are then used in various deep learning methods.\n\nFor a language like English, this is fairly trivial, since words are usually separated by spaces. However, some written languages like Chinese, Japanese and Thai do not mark word boundaries in such a fashion, and in those languages text segmentation is a significant task requiring knowledge of the vocabulary and morphology of words in the language. Sometimes this process is also used in cases like bag of words (BOW) creation in data mining.\n\nMorphological analysis\n\nLemmatization\n\nThe task of removing inflectional endings only and returning the base dictionary form of a word which is also known as a lemma. Lemmatization is another technique for reducing words to their normalized form. But in this case, the transformation actually uses a dictionary to map words to their actual form.\nMorphological segmentation\n\nSeparate words into individual morphemes and identify the class of the morphemes. The difficulty of this task depends greatly on the complexity of the morphology (i.e., the structure of words) of the language being considered. English has fairly simple morphology, especially inflectional morphology, and thus it is often possible to ignore this task entirely and simply model all possible forms of a word (e.g., \"open, opens, opened, opening\") as separate words. In languages such as Turkish or Meitei, a highly agglutinated Indian language, however, such an approach is not possible, as each dictionary entry has thousands of possible word forms.\nPart-of-speech tagging\n\nGiven a sentence, determine the part of speech (POS) for each word. Many words, especially common ones, can serve as multiple parts of speech. For example, \"book\" can be a noun (\"the book on the table\") or verb (\"to book a flight\"); \"set\" can be a noun, verb or adjective; and \"out\" can be any of at least five different parts of speech.\nStemming\n\nThe process of reducing inflected (or sometimes derived) words to a base form (e.g., \"close\" will be the root for \"closed\", \"closing\", \"close\", \"closer\" etc.). Stemming yields similar results as lemmatization, but does so on grounds of rules, not a dictionary.\n\nSyntactic analysis\n\nGrammar induction\n\nGenerate a formal grammar that describes a language's syntax.\nSentence breaking (also known as \"sentence boundary disambiguation\")\n\nGiven a chunk of text, find the sentence boundaries. Sentence boundaries are often marked by periods or other punctuation marks, but these same characters can serve other purposes (e.g., marking abbreviations).\nParsing\n\nDetermine the parse tree (grammatical analysis) of a given sentence. The grammar for natural languages is ambiguous and typical sentences have multiple possible analyses: perhaps surprisingly, for a typical sentence there may be thousands of potential parses (most of which will seem completely nonsensical to a human). There are two primary types of parsing: dependency parsing and constituency parsing. Dependency parsing focuses on the relationships between words in a sentence (marking things like primary objects and predicates), whereas constituency parsing focuses on building out the parse tree using a probabilistic context-free grammar (PCFG) (see also stochastic grammar).\n\nLexical semantics (of individual words in context)\n\nLexical semantics\n\nWhat is the computational meaning of individual words in context?\nDistributional semantics\n\nHow can we learn semantic representations from data?\nNamed entity recognition (NER)\n\nGiven a stream of text, determine which items in the text map to proper names, such as people or places, and what the type of each such name is (e.g. person, location, organization). Although capitalization can aid in recognizing named entities in languages such as English, this information cannot aid in determining the type of named entity, and in any case, is often inaccurate or insufficient. For example, the first letter of a sentence is also capitalized, and named entities often span several words, only some of which are capitalized. Furthermore, many other languages in non-Western scripts (e.g. Chinese or Arabic) do not have any capitalization at all, and even languages with capitalization may not consistently use it to distinguish names. For example, German capitalizes all nouns, regardless of whether they are names, and French and Spanish do not capitalize names that serve as adjectives. This task is also referred to as token classification.\nSentiment analysis (see also Multimodal sentiment analysis)\n\nSentiment analysis involves identifying and classifying the emotional tone expressed in text. This technique involves analyzing text to determine whether the expressed sentiment is positive, negative, or neutral. Models for sentiment classification typically utilize inputs such as word n-grams, Term Frequency-Inverse Document Frequency (TF-IDF) features, hand-generated features, or employ deep learning models designed to recognize both long-term and short-term dependencies in text sequences. The applications of sentiment analysis are diverse, extending to tasks such as categorizing customer reviews on various online platforms.\nTerminology extraction\n\nThe goal of terminology extraction is to automatically extract relevant terms from a given corpus.\nWord-sense disambiguation (WSD)\n\nMany words have more than one meaning; we have to select the meaning which makes the most sense in context. For this problem, we are typically given a list of words and associated word senses, e.g. from a dictionary or an online resource such as WordNet.\nEntity linking\n\nMany words—typically proper names—refer to named entities; here we have to select the entity (a famous individual, a location, a company, etc.) which is referred to in context.\n\nRelational semantics (semantics of individual sentences)\nRelationship extraction\n\nGiven a chunk of text, identify the relationships among named entities (e.g. who is married to whom).\nSemantic parsing\n\nGiven a piece of text (typically a sentence), produce a formal representation of its semantics, either as a graph (e.g., in AMR parsing) or in accordance with a logical formalism (e.g., in DRT parsing). This challenge typically includes aspects of several more elementary NLP tasks from semantics (e.g., semantic role labelling, word-sense disambiguation) and can be extended to include full-fledged discourse analysis (e.g., discourse analysis, coreference; see Natural language understanding below).\nSemantic role labelling (see also implicit semantic role labelling below)\n\nGiven a single sentence, identify and disambiguate semantic predicates (e.g., verbal frames), then identify and classify the frame elements (semantic roles).\n\nDiscourse (semantics beyond individual sentences)\nCoreference resolution\n\nGiven a sentence or larger chunk of text, determine which words (\"mentions\") refer to the same objects (\"entities\"). Anaphora resolution is a specific example of this task, and is specifically concerned with matching up pronouns with the nouns or names to which they refer. The more general task of coreference resolution also includes identifying so-called \"bridging relationships\" involving referring expressions. For example, in a sentence such as \"He entered John's house through the front door\", \"the front door\" is a referring expression and the bridging relationship to be identified is the fact that the door being referred to is the front door of John's house (rather than of some other structure that might also be referred to).\nDiscourse analysis\n\nThis rubric includes several related tasks. One task is discourse parsing, i.e., identifying the discourse structure of a connected text, i.e. the nature of the discourse relationships between sentences (e.g. elaboration, explanation, contrast). Another possible task is recognizing and classifying the speech acts in a chunk of text (e.g. yes–no question, content question, statement, assertion, etc.).\nImplicit semantic role labelling\n\nGiven a single sentence, identify and disambiguate semantic predicates (e.g., verbal frames) and their explicit semantic roles in the current sentence (see Semantic role labelling above). Then, identify semantic roles that are not explicitly realized in the current sentence, classify them into arguments that are explicitly realized elsewhere in the text and those that are not specified, and resolve the former against the local text. A closely related task is zero anaphora resolution, i.e., the extension of coreference resolution to pro-drop languages.\nRecognizing textual entailment\n\nGiven two text fragments, determine if one being true entails the other, entails the other's negation, or allows the other to be either true or false.\nTopic segmentation and recognition\n\nGiven a chunk of text, separate it into segments each of which is devoted to a topic, and identify the topic of the segment.\nArgument mining\n\nThe goal of argument mining is the automatic extraction and identification of argumentative structures from natural language text with the aid of computer programs. Such argumentative structures include the premise, conclusions, the argument scheme and the relationship between the main and subsidiary argument,"
 },
 {
  "title": "NLP",
  "revision_id": "1330183191",
  "matched_by": "title",
  "text": "Look up NLP in Wiktionary, the free dictionary.\n\nNLP commonly refers to:\n\nNatural language processing, a field of computer science and linguistics\n\nNeuro-linguistic programming, a pseudoscientific method aimed at modifying human behavior\n\nComputer programming\n\nNatural-language programming, a programming paradigm\n\nLibraries\n\nNational Library of Pakistan\n\nMathematics\n\nNonlinear programming, solving optimisation problems with nonlinear constraints\n\nMedicine\n\nNo light perception, a diagnosis of severe blindness\n\nPolitical parties\n\nNational Liberal Party (disambiguation)\n\nNational Liberation Party (disambiguation)\n\nNational Labour Party (disambiguation)\n\nNatural Law Party, a trans-national union of political parties, with national branches in over 80 countries\n\nNatural Law Party of Canada\n\nNatural Law Party (Ireland)\n\nNatural Law Party of Israel\n\nNatural Law Party of New Zealand\n\nNatural Law Party of Ontario\n\nNatural Law Party of Quebec\n\nNatural Law Party (Trinidad and Tobago)\n\nNatural Law Party (United States)"
 },
 {
  "title": "Natural Language Processing (journal)",
  "revision_id": "1328786392",
  "matched_by": "title-minus-qualifier",
  "text": "Natural Language Processing is a bimonthly peer-reviewed academic journal published by Cambridge University Press which covers research and software in natural language processing. It was established in 1995 as Natural Language Engineering, obtaining its current title in 2024. Other than original publications on theoretical and applied aspects of computational linguistics, the journal also contains Industry Watch and Emerging Trends columns tracking developments in the field. The editor-in-chief is Ruslan Mitkov (Lancaster University). From 2024 the journal is published completely open access. According to the Journal Citation Reports, the journal has a 2023 impact factor of 2.3.\n\nReferences"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q30642",
  "label": "natural language processing",
  "description": "field of computer science and linguistics",
  "aliases": [
   "NLP"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q1047113",
    "Q2267705",
    "Q268592",
    "Q135892289"
   ],
   "P279": [
    "Q11660",
    "Q21198",
    "Q182557",
    "Q11862829",
    "Q750843"
   ]
  },
  "revision_id": "2566562126",
  "value_labels": {
   "Q11862829": "academic discipline",
   "Q1047113": "field of study",
   "Q2267705": "field of study",
   "Q268592": "industry",
   "Q135892289": "branch of linguistics",
   "Q11660": "artificial intelligence",
   "Q21198": "computer science",
   "Q182557": "computational linguistics",
   "Q750843": "information processing"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q227935",
  "label": "NLP",
  "description": "Wikimedia disambiguation page",
  "aliases": [],
  "claims": {
   "P31": [
    "Q4167410"
   ]
  },
  "revision_id": "2538296517",
  "value_labels": {
   "Q4167410": "Wikimedia disambiguation page"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15767074",
  "label": "Natural Language Engineering",
  "description": "peer-reviewed academic journal published by Cambridge University Press",
  "aliases": [],
  "claims": {
   "P31": [
    "Q5633421"
   ]
  },
  "revision_id": "2567884993",
  "value_labels": {
   "Q5633421": "scientific journal"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11862829",
  "label": "academic discipline",
  "description": "field of study organized around a distinct body of knowledge, theories, methods, or subject matter",
  "aliases": [
   "branch (academic)",
   "discipline",
   "academic field",
   "academic branch",
   "academic specialty",
   "academic specialism",
   "research field",
   "field of research",
   "field of study",
   "sub-discipline"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q1047113"
   ],
   "P460": [
    "Q2465832",
    "Q2267705",
    "Q627436",
    "Q362165"
   ],
   "P1889": [
    "Q3242580",
    "Q1166828",
    "Q1391009",
    "Q82957"
   ]
  },
  "revision_id": "2562020019",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1047113",
  "label": "field of study",
  "description": "field limited to a specific area of ​​knowledge; specialization in an occupation or branch of learning; a specific use",
  "aliases": [
   "subject area",
   "domain",
   "special field",
   "specialism",
   "subdiscipline",
   "sub-discipline",
   "specialized field of study",
   "specialty",
   "special branches"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q105948247",
    "Q110403031",
    "Q26256810",
    "Q21040055"
   ],
   "P361": [
    "Q9081"
   ],
   "P1889": [
    "Q123286730",
    "Q2267705"
   ]
  },
  "revision_id": "2562271253",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2267705",
  "label": "field of study",
  "description": "field of study leading to a specific degree",
  "aliases": [
   "field of education",
   "area of study"
  ],
  "claims": {
   "P279": [
    "Q1047113"
   ],
   "P527": [
    "Q13442814"
   ],
   "P460": [
    "Q11862829",
    "Q2465832",
    "Q4671286"
   ],
   "P1889": [
    "Q1047113"
   ]
  },
  "revision_id": "2544362366",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q268592",
  "label": "industry",
  "description": "group of firms that produce a closely related set of raw materials, goods, or services",
  "aliases": [
   "economic industry",
   "industrial branch",
   "industry (economics)",
   "industries",
   "industrial sector"
  ],
  "claims": {
   "P31": [
    "Q29028649"
   ],
   "P279": [
    "Q16887380"
   ],
   "P361": [
    "Q3958441"
   ],
   "P527": [
    "Q783794"
   ],
   "P1889": [
    "Q8148",
    "Q3958441",
    "Q8187769"
   ]
  },
  "revision_id": "2559779969",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q135892289",
  "label": "branch of linguistics",
  "description": "subfield within linguistics",
  "aliases": [
   "linguistics branch",
   "subfield of linguistics",
   "linguistics subfield",
   "subdiscipline of linguistics",
   "linguistics subdisciplines",
   "linguistics specialty",
   "specialty of linguistics",
   "area of linguistics",
   "linguistics area"
  ],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q8162",
    "Q2465832"
   ]
  },
  "revision_id": "2550837005",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11660",
  "label": "artificial intelligence",
  "description": "field that develops and studies software enabling machines to exhibit intelligent behavior",
  "aliases": [
   "AI software",
   "machine intelligence",
   "artificially intelligent",
   "artificial Intelligence",
   "machine understanding",
   "simulated intelligence",
   "computational rationality",
   "intelligent machine",
   "machine thought",
   "artificially intelligent beings",
   "machines that can think",
   "artificial smartness",
   "artificial stupidity",
   "AI science"
  ],
  "claims": {
   "P31": [
    "Q112057532",
    "Q123370638",
    "Q125161275"
   ],
   "P279": [
    "Q21198",
    "Q120208",
    "Q1156402"
   ],
   "P361": [
    "Q21198",
    "Q395"
   ],
   "P527": [
    "Q5514059",
    "Q203790",
    "Q105604957",
    "Q2539"
   ],
   "P1889": [
    "Q117349473"
   ]
  },
  "revision_id": "2569958782",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21198",
  "label": "computer science",
  "description": "study of computation",
  "aliases": [
   "computing science",
   "CS",
   "Computer Science",
   "science of computing",
   "information processing science",
   "computer sciences",
   "computing sciences",
   "sciences of computing",
   "computation science",
   "computing",
   "computer studies",
   "comp sci",
   "comp. sci",
   "comp. sci.",
   "compsci",
   "informatics"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q4671286"
   ],
   "P279": [
    "Q816264"
   ],
   "P527": [
    "Q2878974",
    "Q538722",
    "Q11660",
    "Q844718"
   ],
   "P460": [
    "Q4027615"
   ],
   "P1889": [
    "Q4027615",
    "Q16387",
    "Q131222",
    "Q117801"
   ]
  },
  "revision_id": "2569264093",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q182557",
  "label": "computational linguistics",
  "description": "interdisciplinary field studying language from a computational perspective",
  "aliases": [],
  "claims": {
   "P31": [
    "Q1665984",
    "Q11862829",
    "Q135892289"
   ],
   "P279": [
    "Q21198",
    "Q12553063"
   ],
   "P460": [
    "Q3754405"
   ]
  },
  "revision_id": "2567795867",
  "ancestor_of": "Q30642",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110402867",
  "label": "knowledge classification",
  "description": "Wikidata metaclass",
  "aliases": [
   "knowledge classification system",
   "classification system of knowledge"
  ],
  "claims": {
   "P31": [
    "Q121344523"
   ],
   "P279": [
    "Q5962346"
   ],
   "P1889": [
    "Q110403031"
   ]
  },
  "revision_id": "2569936517",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q105948247",
  "label": "knowledge system",
  "description": "systems of knowledge produced over time through interactions with other human beings",
  "aliases": [
   "knowledge systems"
  ],
  "claims": {
   "P31": [
    "Q96116695"
   ],
   "P279": [
    "Q3622126"
   ],
   "P527": [
    "Q9081"
   ]
  },
  "revision_id": "2522085818",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110403031",
  "label": "knowledge type",
  "description": "Wikidata metaclass",
  "aliases": [
   "type of knowledge"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q140458154"
   ],
   "P1889": [
    "Q110402867",
    "Q125161275"
   ]
  },
  "revision_id": "2548067834",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q26256810",
  "label": "topic",
  "description": "topic or area addressed by a work or set of works",
  "aliases": [
   "issue",
   "subject",
   "theme",
   "topic of a work",
   "subject matter of a work",
   "matter",
   "main subject",
   "main topic",
   "subject matter",
   "gum:SubjectMatter"
  ],
  "claims": {
   "P279": [
    "Q11028",
    "Q12488383",
    "Q16514889"
   ],
   "P460": [
    "Q1053916",
    "Q200801"
   ],
   "P1889": [
    "Q14095863",
    "Q9340580"
   ]
  },
  "revision_id": "2567187301",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q29028649",
  "label": "economic concept",
  "description": "concept used in economic sciences",
  "aliases": [
   "economics concept",
   "concept in economics"
  ],
  "claims": {
   "P31": [
    "Q137429456"
   ],
   "P279": [
    "Q131362181"
   ],
   "P1889": [
    "Q64513524"
   ]
  },
  "revision_id": "2550617485",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q16887380",
  "label": "group",
  "description": "well-defined, enumerable collection of discrete entities that form a collective whole",
  "aliases": [
   "group of",
   "group of objects",
   "grouping",
   "object grouping",
   "object group",
   "collection",
   "lineup",
   "branch",
   "group of things",
   "group of entities",
   "thing grouping",
   "thing group",
   "entity grouping",
   "entity group",
   "group of individual things"
  ],
  "claims": {
   "P31": [
    "Q5962346"
   ],
   "P279": [
    "Q28813620"
   ],
   "P527": [
    "Q35120",
    "Q36809769",
    "Q36808958"
   ],
   "P1889": [
    "Q36161",
    "Q12139612",
    "Q133250",
    "Q83306",
    "Q83478",
    "Q2668072",
    "Q1514741",
    "Q63341786",
    "Q16889133",
    "Q111360549",
    "Q824979",
    "Q215380",
    "Q141131708"
   ]
  },
  "revision_id": "2560437842",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q24017414",
  "label": "second-order class",
  "description": "metaclass containing as instances all classes of individuals",
  "aliases": [
   "2nd-order class",
   "metaclass of the first order"
  ],
  "claims": {
   "P31": [
    "Q24017465",
    "Q115490628"
   ],
   "P279": [
    "Q23959932",
    "Q19478619"
   ],
   "P1889": [
    "Q21146257",
    "Q19478619",
    "Q16889133",
    "Q23958852"
   ]
  },
  "revision_id": "2570870333",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q8162",
  "label": "linguistics",
  "description": "scientific study of language",
  "aliases": [
   "language studies"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q4671286",
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q80083",
    "Q34749"
   ],
   "P361": [
    "Q6486703",
    "Q64810203"
   ],
   "P527": [
    "Q40998",
    "Q38311",
    "Q37437",
    "Q39645",
    "Q181839",
    "Q35395",
    "Q661093",
    "Q1428721",
    "Q8091"
   ],
   "P1889": [
    "Q64810203"
   ]
  },
  "revision_id": "2567840294",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2465832",
  "label": "branch of science",
  "description": "field of scientific study",
  "aliases": [
   "discipline of science",
   "field of science",
   "branches of science",
   "subdivision of science",
   "scientific field",
   "research area",
   "type of science"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q1047113"
   ],
   "P460": [
    "Q11862829",
    "Q2267705"
   ],
   "P1889": [
    "Q3242580"
   ]
  },
  "revision_id": "2563543766",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q112057532",
  "label": "type of technology",
  "description": "Wikidata metaclass, used as \"instance of\" for every \"subclass of\" technology",
  "aliases": [
   "technology type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ]
  },
  "revision_id": "2542124180",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q123370638",
  "label": "branch of computer science",
  "description": "Computer Science sub-disciplines",
  "aliases": [
   "Computer Science sub-discipline",
   "subfield of computer science",
   "branch of computer science"
  ],
  "claims": {
   "P31": [
    "Q24017414",
    "Q5962346"
   ],
   "P279": [
    "Q2465832",
    "Q1047113",
    "Q11862829"
   ]
  },
  "revision_id": "2551194511",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q125161275",
  "label": "type of intelligence",
  "description": "Wikidata metaclass for intelligence or cleverness",
  "aliases": [
   "intelligence type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ],
   "P1889": [
    "Q110403031"
   ]
  },
  "revision_id": "2552317421",
  "ancestor_of": "Q30642",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4167410",
  "label": "Wikimedia disambiguation page",
  "description": "type of wiki page usually in main namespace (article namespace, ns=0) containing links to articles with similar names, and very little details only, use with P31 \"instance of\"",
  "aliases": [
   "disambiguation",
   "disambiguation page",
   "Wiki disambiguation page",
   "dabpage"
  ],
  "claims": {
   "P279": [
    "Q15633587",
    "Q17442446",
    "Q138717185"
   ],
   "P361": [
    "Q52",
    "Q373",
    "Q263",
    "Q369",
    "Q367",
    "Q370",
    "Q1063116",
    "Q15633578"
   ],
   "P460": [
    "Q15623926"
   ],
   "P1889": [
    "Q21484471",
    "Q80096233",
    "Q134972145",
    "Q138717185",
    "Q118521146"
   ]
  },
  "revision_id": "2568773925",
  "ancestor_of": "Q227935",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15633587",
  "label": "MediaWiki main namespace page",
  "description": "page in the main namespace of a wiki, used for \"main\" content specific to the project such as article, lemma, ...",
  "aliases": [
   "(main)"
  ],
  "claims": {
   "P279": [
    "Q15474042"
   ],
   "P361": [
    "Q118552465"
   ],
   "P1889": [
    "Q118552465"
   ]
  },
  "revision_id": "2503396531",
  "ancestor_of": "Q227935",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17442446",
  "label": "Wikimedia internal item",
  "description": "instances and/or subclasses of this item are about some Wikimedia-only content and should not refer to real world entities",
  "aliases": [
   "internal item"
  ],
  "claims": {
   "P279": [
    "Q17379835"
   ]
  },
  "revision_id": "2556281869",
  "ancestor_of": "Q227935",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q138717185",
  "label": "disambiguation page",
  "description": "type of page common in wikis",
  "aliases": [],
  "claims": {
   "P279": [
    "Q111279923"
   ],
   "P1889": [
    "Q4167410",
    "Q118521146",
    "Q22981376"
   ]
  },
  "revision_id": "2569961906",
  "ancestor_of": "Q227935",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5633421",
  "label": "scientific journal",
  "description": "periodical journal publishing scientific research",
  "aliases": [
   "scientific magazine",
   "journal",
   "science journal",
   "scientific journals",
   "journals"
  ],
  "claims": {
   "P31": [
    "Q21114848"
   ],
   "P279": [
    "Q685935",
    "Q591041",
    "Q49850",
    "Q737498"
   ],
   "P1889": [
    "Q737498",
    "Q1911105"
   ]
  },
  "revision_id": "2557906009",
  "ancestor_of": "Q15767074",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21114848",
  "label": "magazine genre",
  "description": "type of genre",
  "aliases": [
   "genre of magazine",
   "periodicals genre",
   "journal genre"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q483394"
   ]
  },
  "revision_id": "2567686963",
  "ancestor_of": "Q15767074",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q685935",
  "label": "trade magazine",
  "description": "periodical dedicated to a particular field",
  "aliases": [
   "professional magazine",
   "trade rag",
   "trade journal",
   "trade publication"
  ],
  "claims": {
   "P31": [
    "Q21114848"
   ],
   "P279": [
    "Q41298"
   ],
   "P361": [
    "Q1391420"
   ],
   "P1889": [
    "Q55630524",
    "Q918727"
   ]
  },
  "revision_id": "2523496555",
  "ancestor_of": "Q15767074",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q591041",
  "label": "scientific publication",
  "description": "publication that reports empirical or theoretical work in the sciences",
  "aliases": [
   "scholarly publication"
  ],
  "claims": {
   "P31": [
    "Q39725049"
   ],
   "P279": [
    "Q732577",
    "Q47461344",
    "Q11826511",
    "Q12042160",
    "Q55915575"
   ],
   "P527": [
    "Q4119870",
    "Q265158",
    "Q1713"
   ]
  },
  "revision_id": "2567595781",
  "ancestor_of": "Q15767074",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q49850",
  "label": "journal",
  "description": "written medium (duplicate item)",
  "aliases": [],
  "claims": {
   "P31": [
    "Q17362920"
   ],
   "P279": [
    "Q1261026",
    "Q1002697"
   ],
   "P361": [
    "Q11030"
   ],
   "P460": [
    "Q41298"
   ],
   "P1889": [
    "Q361785"
   ]
  },
  "revision_id": "2516833327",
  "ancestor_of": "Q15767074",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-06151863-n",
  "lemmas": [
   "natural language processing",
   "NLP",
   "human language technology"
  ],
  "gloss": "the branch of information science that deals with natural language information",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06151569-n"
   ]
  },
  "relation_targets": {
   "oewn-06151569-n": "information science, informatics, information processing"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 3: Extract, transform, load (`d9sq04v2o1`)

~~~~text
Concept record:
{
 "id": "d9sq04v2o1",
 "preferred_name": "Extract, transform, load",
 "kind": "method",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Extraction, Transformation, and Loading (ETL)"
  },
  {
   "label": "ETL"
  },
  {
   "label": "Extraction, Transformation, and Loading"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "uclexd8uv3",
  "name": "Data validation"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "vf02rn80se",
  "name": "Cost accounting"
 },
 {
  "id": "ie3ky4o9l0",
  "name": "Data wrangling"
 },
 {
  "id": "kp84ig38m5",
  "name": "Database design"
 },
 {
  "id": "pmy0yp0e50",
  "name": "NoSQL database"
 },
 {
  "id": "f69xny35zm",
  "name": "SQL"
 },
 {
  "id": "ss273uzint",
  "name": "Software testing"
 },
 {
  "id": "ocy9gvs6bk",
  "name": "Web crawling"
 },
 {
  "id": "php2tc9p7y",
  "name": "XML"
 },
 {
  "id": "ye2k9qi1x3",
  "name": "Certification in Transportation and Logistics"
 },
 {
  "id": "uct8ix3rbg",
  "name": "Tcl"
 },
 {
  "id": "rh3gh6e9pn",
  "name": "Elm"
 },
 {
  "id": "ot4pymzomt",
  "name": "Social-emotional learning"
 },
 {
  "id": "kdyyyj7yda",
  "name": "Engineer in Training"
 },
 {
  "id": "uhwnqf48he",
  "name": "Representational State Transfer"
 },
 {
  "id": "ubbk8mnwmv",
  "name": "WebCTRL"
 },
 {
  "id": "i4i1z8400a",
  "name": "Certified in Logistics, Transportation and Distribution"
 },
 {
  "id": "zyx43s2qb5",
  "name": "Air Travel Organisers' Licensing"
 },
 {
  "id": "wy0q8xbf4z",
  "name": "International Computer Driving Licence"
 },
 {
  "id": "uxw4bog89z",
  "name": "Certified Biomedical Equipment Technician"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "q9s4sj8gqa",
  "name": "Advanced Trauma Life Support"
 },
 {
  "id": "ixojaf13wa",
  "name": "Associate of Applied Science in Animation and CGI Motion"
 },
 {
  "id": "i6xjzm9oyc",
  "name": "Wilderness EMT"
 },
 {
  "id": "i6g7p06d2d",
  "name": "Earth leakage circuit breaker"
 },
 {
  "id": "hfschl129h",
  "name": "Tulu"
 },
 {
  "id": "gaqvznkz28",
  "name": "Perl"
 },
 {
  "id": "fbgyvaz7qh",
  "name": "Scholarship of teaching and learning"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:4",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior Independent Software Developer. software development|go|wordpress|chat|apple|testing|catalyst|etl|ai"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:8",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Analytics Engineer. …nsparent, and repeatable solutions. You fluently explain complex ideas to colleagues and customers. Responsibilities Execute data analysis, ETL, and data mining to support customer deployments Configure enterprise analytics platform and tools Work closely with customer delivery teams with mixed back…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:527",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: [Hà Nội, HCM] Chuyên Gia/chuyên Viên Phê Duyệt Tín Dụng Cấp 1-2-3. [\"Azure Data Services\", \"ETL\", \"Khai Thác Dữ Liệu\", \"Phân Tích Dữ Liệu\", \"Quản Trị Dữ Liệu\"]"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:1320",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "تحلیل داده, هوش تجاری, T-SQL, ETL"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:1671",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Record To Report Ops Analyst. journal entries, accounting, extract transform load, record to report, etl, service operations, informatica powercenter, forecasting"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Extract, transform, load",
  "revision_id": "1364353374",
  "matched_by": "title",
  "text": "Extract, transform, load (ETL) is a three-phase computing process where data are extracted from an input source, transformed (including cleaning), and loaded into an output data container. The data can be collected from one or more sources and it can also be output to one or more destinations. ETL processing is typically executed using software applications but it can also be done manually by system operators. ETL software typically automates the entire process and can be run manually or on recurring schedules either as single jobs or aggregated into a batch of jobs.\n\nA properly designed ETL system extracts data from source systems and enforces data type and data validity standards and ensures it conforms structurally to the requirements of the output. Some ETL systems can also deliver data in a presentation-ready format so that application developers can build applications and end users can make decisions.\n\nThe ETL process is often used in data warehousing. ETL systems commonly integrate data from multiple applications (systems), typically developed and supported by different vendors or hosted on separate computer hardware. The separate systems containing the original data are frequently managed and operated by different stakeholders. For example, a cost accounting system may combine data from payroll, sales, and purchasing.\n\nData extraction involves extracting data from homogeneous or heterogeneous sources; data transformation processes data by data cleaning and transforming it into a proper storage format/structure for the purposes of querying and analysis; finally, data loading describes the insertion of data into the final target database such as an operational data store, a data mart, data lake or a data warehouse.\n\nETL and its variant ELT (extract, load, transform), are increasingly used in cloud-based data warehousing. Applications involve not only batch processing, but also real-time streaming.\n\nPhases\n\nExtract\n\nETL processing involves extracting the data from the source system(s). In many cases, this represents the most important aspect of ETL, since extracting data correctly sets the stage for the success of subsequent processes. Most data-warehousing projects combine data from different source systems. Each separate system may also use a different data organization and/or format. Common data-source formats include relational databases, flat-file databases, XML, and JSON, but may also include non-relational database structures such as IBM Information Management System or other data structures such as Virtual Storage Access Method (VSAM) or Indexed Sequential Access Method (ISAM), or even formats fetched from outside sources by means such as a web crawler or data scraping. The streaming of the extracted data source and loading on-the-fly to the destination database is another way of performing ETL when no intermediate data storage is required.\n\nAn intrinsic part of the extraction involves data validation to confirm whether the data pulled from the sources has the correct/expected values in a given domain (such as a pattern/default or list of values). If the data fails the validation rules, it is rejected entirely or in part. The rejected data is ideally reported back to the source system for further analysis to identify and to rectify incorrect records or perform data wrangling.\n\nTransform\n\nIn the data transformation stage, a series of rules or functions are applied to the extracted data in order to prepare it for loading into the end target.\n\nAn important function of transformation is data cleansing, which aims to pass only \"proper\" data to the target. The challenge when different systems interact is in the relevant systems' interfacing and communicating. Character sets that may be available in one system may not be in others.\n\nIn other cases, one or more of the following transformation types may be required to meet the business and technical needs of the server or data warehouse:\n\nSelecting only certain columns to load (or selecting null columns not to load). For example, if the source data has three columns (aka \"attributes\"), roll_no, age, and salary, then the selection may take only roll_no and salary. Or, the selection mechanism may ignore all those records where salary is not present (salary = null).\n\nTranslating coded values. For example if the source system codes male as \"1\" and female as \"2\", but the warehouse codes male as \"M\" and female as \"F\".\n\nEncoding free-form values. For example, mapping \"Male\" to \"M\".\n\nDeriving a new calculated value. For example, sale_amount = qty * unit_price.\n\nSorting or ordering the data based on a list of columns to improve search performance.\n\nJoining data from multiple sources (e.g., lookup, merge) and deduplicating the data.\n\nAggregating. For example, rollup – summarizing multiple rows of data – total sales for each store, and for each region, etc.\n\nGenerating surrogate-key values.\n\nTransposing or pivoting (turning multiple columns into multiple rows or vice versa).\n\nSplitting a column into multiple columns. For example, converting a comma-separated list, specified as a string in one column, into individual values in different columns.\n\nDisaggregating repeating columns.\n\nLooking up and validating the relevant data from tables or referential files.\n\nApplying any form of data validation. Failed validation may result in a full rejection of the data, partial rejection, or no rejection at all, and thus none, some, or all of the data are handed over to the next step depending on the rule design and exception handling; many of the above transformations may result in exceptions, e.g., when a code translation parses an unknown code in the extracted data.\n\nLoad\n\nThe load phase loads the data into the end target, which can be any data store including a simple delimited flat file or a data warehouse. Depending on the requirements of the organization, this process varies widely. Some data warehouses may overwrite existing information with cumulative information; updating extracted data is frequently done on a daily, weekly, or monthly basis. Other data warehouses (or even other parts of the same data warehouse) may add new data in a historical form at regular intervals – for example, hourly. To understand this, consider a data warehouse that is required to maintain sales records of the last year. This data warehouse overwrites any data older than a year with newer data. However, the entry of data for any one year window is made in a historical manner. The timing and scope to replace or append are strategic design choices dependent on the time available and the business needs. More complex systems can maintain a history and audit trail of all changes to the data loaded in the data warehouse.\nAs the load phase interacts with a database, the constraints defined in the database schema – as well as in triggers activated upon data load – apply (for example, uniqueness, referential integrity, mandatory fields), which also contribute to the overall data quality performance of the ETL process.\n\nFor example, a financial institution might have information on a customer in several departments and each department might have that customer's information listed in a different way. The membership department might list the customer by name, whereas the accounting department might list the customer by number. ETL can bundle all of these data elements and consolidate them into a uniform presentation, such as for storing in a database or data warehouse.\n\nAnother way that companies use ETL is to move information to another application permanently. For instance, the new application might use another database vendor and most likely a very different database schema. ETL can be used to transform the data into a format suitable for the new application to use.\n\nAn example would be an expense and cost recovery system such as used by accountants, consultants, and law firms. The data usually ends up in the time and billing system, although some businesses may also utilize the raw data for employee productivity reports to Human Resources (personnel dept.) or equipment usage reports to Facilities Management.\n\nAdditional phases\n\nA real-life ETL cycle may consist of additional execution steps, for example:\n\nCycle initiation (pre-ETL: Ensure all ETL-relevant systems are available, functional, and have no issues that would suddenly halt an hour into ETL, such as valid B2B compute/memory/storage subscriptions and API keys, satisfactory budget for estimated time/money, no higher-priority tasks)\n\nBuild reference data (i.e., linking (not hard-copying) to reliable historic baselines)\n\nExtract (from data sources)\n\nValidate (ensure data can eventually be useful; data is not 100% garbage)\n\nTransform (clean, apply business rules, check for data integrity, create aggregates or disaggregates)\n\nStage (load into staging tables, if used)\n\nAudit reports (for example, on compliance with business rules. Also, in case of failure, helps to diagnose/repair)\n\nPublish (to target tables)\n\nArchive (Extreme, space-efficient compression for very rarely used, old data. Situationally, can be lossy)\n\nDesign challenges\n\nETL processes can involve considerable complexity, and significant operational problems can occur with improperly designed ETL systems.\n\nData variations\n\nThe range of data values or data quality in an operational system may exceed the expectations of designers at the time validation and transformation rules are specified. Data profiling of a source during data analysis can identify the data conditions that must be managed by transform rules specifications, leading to an amendment of validation rules explicitly and implicitly implemented in the ETL process.\n\nData warehouses are typically assembled from a variety of data sources with different formats and purposes. As such, ETL is a key process to bring all the data together in a standard, homogeneous environment.\n\nDesign analysis should establish the scalability of an ETL system across the lifetime of its usage – including understanding the volumes of data that must be processed within service level agreements. The time available to extract from source systems may change, which may mean the same amount of data may have to be processed in less time. Some ETL systems have to scale to process terabytes of data to update data warehouses with tens of terabytes of data. Increasing volumes of data may require designs that can scale from daily batch to multiple-day micro batch to integration with message queues or real-time change-data-capture for continuous transformation and update.\n\nUniqueness of keys\n\nUnique keys play an important part in all relational databases, as they tie everything together. A unique key is a column that identifies a given entity, whereas a foreign key is a column in another table that refers to a primary key. Keys can comprise several columns, in which case they are composite keys. In many cases, the primary key is an auto-generated integer that has no meaning for the business entity being represented, but solely exists for the purpose of the relational database – commonly referred to as a surrogate key.\n\nAs there is usually more than one data source getting loaded into the warehouse, the keys are an important concern to be addressed. For example: customers might be represented in several data sources, with their Social Security number as the primary key in one source, their phone number in another, and a surrogate in the third. Yet a data warehouse may require the consolidation of all the customer information into one dimension.\n\nA recommended way to deal with the concern involves adding a warehouse surrogate key, which is used as a foreign key from the fact table.\n\nUsually, updates occur to a dimension's source data, which must be reflected in the data warehouse.\n\nIf the primary key of the source data is required for reporting, the dimension already contains that piece of information for each row. If the source data uses a surrogate key, the warehouse must keep track of it even though it is never used in queries or reports; it is done by creating a lookup table that contains the warehouse surrogate key and the originating key. This way, the dimension is not polluted with surrogates from various source systems, while the ability to update is preserved.\n\nThe lookup table is used in different ways depending on the nature of the source data.\nThere are 5 types to consider; three are included here:\n\nType 1\n\nThe dimension row is simply updated to match the current state of the source system; the warehouse does not capture history; the lookup table is used to identify the dimension row to update or overwrite\nType 2\n\nA new dimension row is added with the new state of the source system; a new surrogate key is assigned; source key is no longer unique in the lookup table\nFully logged\n\nA new dimension row is added with the new state of the source system, while the previous dimension row is updated to reflect it is no longer active and time of deactivation.\n\nPerformance\n\nETL vendors benchmark their record-systems at multiple TB (terabytes) per hour (or ~1 GB per second) using powerful servers with multiple CPUs, multiple hard drives, multiple gigabit-network connections, and much memory.\n\nIn real life, the slowest part of an ETL process usually occurs in the database load phase. Databases may perform slowly because they have to take care of concurrency, integrity maintenance, and indices. Thus, for better performance, it may make sense to employ:\n\nDirect path extract method or bulk unload whenever is possible (instead of querying the database) to reduce the load on source system while getting high-speed extract\n\nMost of the transformation processing outside of the database\n\nBulk load operations whenever possible\n\nStill, even using bulk operations, database access is usually the bottleneck in the ETL process. Some common methods used to increase performance are:\n\nPartition tables (and indices): try to keep partitions similar in size (watch for null values that can skew the partitioning)\n\nDo all validation in the ETL layer before the load: disable integrity checking (disable constraint ...) in the target database tables during the load\n\nDisable triggers (disable trigger ...) in the target database tables during the load: simulate their effect as a separate step\n\nGenerate IDs in the ETL layer (not in the database)\n\nDrop the indices (on a table or partition) before the load – and recreate them after the load (SQL: drop index ...; create index ...)\n\nUse parallel bulk load when possible – works well when the table is partitioned or there are no indices (Note: attempting to do parallel loads into the same table (partition) usually causes locks – if not on the data rows, then on indices)\n\nIf a requirement exists to do insertions, updates, or deletions, find out which rows should be processed in which way in the ETL layer, and then process these three operations in the database separately; you often can do bulk load for inserts, but updates and deletes commonly go through an API (using SQL)\n\nWhether to do certain operations in the database or outside may involve a trade-off. For example, removing duplicates using distinct may be slow in the database; thus, it makes sense to do it outside. On the other side, if using distinct significantly (x100) decreases the number of rows to be extracted, then it makes sense to remove duplications as early as possible in the database before unloading data.\n\nA common source of problems in ETL is a big number of dependencies among ETL jobs. For example, job \"B\" cannot start while job \"A\" is not finished. One can usually achieve better performance by visualizing all processes on a graph, and trying to reduce the graph making maximum use of parallelism, and making \"chains\" of consecutive processing as short as possible. Again, partitioning of big tables and their indices can really help.\n\nAnother common issue occurs when the data are spread among several databases, and processing is done in those databases sequentially. Sometimes database replication may be involved as a method of copying data between databases – it can significantly slow down the whole process. The common solution is to reduce the processing graph to only three layers:\n\nSources\n\nCentral ETL layer\n\nTargets\n\nThis approach allows processing to take maximum advantage of parallelism. For example, if you need to load data into two databases, you can run the loads in parallel (instead of loading into the first – and then replicating into the second).\n\nSometimes processing must take place sequentially. For example, dimensional (reference) data are needed before one can get and validate the rows for main \"fact\" tables.\n\nParallel computing\n\nSome ETL software implementations include parallel processing. This enables a number of methods to improve overall performance of ETL when dealing with large volumes of data.\n\nETL applications implement three main types of parallelism:\n\nData: By splitting a single sequential file into smaller data files to provide parallel access\n\nPipeline: allowing the simultaneous running of several components on the same data stream, e.g. looking up a value on record 1 at the same time as adding two fields on record 2\n\nComponent: The simultaneous running of multiple processes on different data streams in the same job, e.g. sorting one input file while removing duplicates on another file\n\nAll three types of parallelism usually operate combined in a single job or task.\n\nAn additional difficulty comes with making sure that the data being uploaded is relatively consistent. Because multiple source databases may have different update cycles (some may be updated every few minutes, while others may take days or weeks), an ETL system may be required to hold back certain data until all sources are synchronized. Likewise, where a warehouse may have to be reconciled to the contents in a source system or with the general ledger, establishing synchronization and reconciliation points becomes necessary.\n\nFailure recovery\n\nData warehousing procedures usually subdivide a big ETL process into smaller pieces running sequentially or in parallel. To keep track of data flows, it makes sense to tag each data row with \"row_id\", and tag each piece of the process with \"run_id\". In case of a failure, having these IDs help to roll back and rerun the failed piece.\n\nBest practice also calls for checkpoints, which are states when certain phases of the process are completed. Once at a checkpoint, it is a good idea to write everything to disk, clean out some temporary files, log the state, etc.\n\nImplementations\n\nAn established ETL framework may improve connectivity and scalability. A good ETL tool must be able to communicate with the many different relational databases and read the various file formats used throughout an organization. ETL tools have started to migrate into enterprise application integration, or even enterprise service bus, systems that now cover much more than just the extraction, transformation, and loading of data. Many ETL vendors now have data profiling, data quality, and metadata capabilities. A common use case for ETL tools include converting CSV files to formats readable by relational databases. A typical translation of millions of records is facilitated by ETL tools that enable users to input CSV-like data feeds/files and import them into a database with as"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q1276130",
  "label": "extract, transform, load",
  "description": "procedure for copying data from one or more sources, then transforming the data at the source system, and lastly copying into a destination system which represents the data differently from the source(s)",
  "aliases": [
   "ETL"
  ],
  "claims": {
   "P31": [
    "Q116505632",
    "Q6661985",
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q6661985"
   ],
   "P361": [
    "Q193351"
   ],
   "P527": [
    "Q5227287",
    "Q4272815",
    "Q124476957"
   ],
   "P1889": [
    "Q19818626"
   ]
  },
  "revision_id": "2567914106",
  "value_labels": {
   "Q116505632": "type of process",
   "Q6661985": "data processing",
   "Q1047113": "field of study",
   "Q2267705": "field of study",
   "Q193351": "data warehouse",
   "Q5227287": "data extraction",
   "Q4272815": "data transformation",
   "Q124476957": "data loading",
   "Q19818626": "extract, load, transform"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q83348825",
  "label": "Etl",
  "description": "family name",
  "aliases": [],
  "claims": {
   "P31": [
    "Q101352"
   ]
  },
  "revision_id": "2380905870",
  "value_labels": {
   "Q101352": "family name"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q18045577",
  "label": "ADGRL4",
  "description": "protein-coding gene in the species Homo sapiens",
  "aliases": [
   "ETL",
   "KPG_003",
   "ELTD1",
   "adhesion G protein-coupled receptor L4"
  ],
  "claims": {
   "P31": [
    "Q7187"
   ],
   "P279": [
    "Q20747295"
   ]
  },
  "revision_id": "2571564891",
  "value_labels": {
   "Q7187": "gene",
   "Q20747295": "protein-coding gene"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q116505632",
  "label": "type of process",
  "description": "Wikidata metaclass of process",
  "aliases": [
   "process type"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q142077035"
   ],
   "P361": [
    "Q58778"
   ],
   "P1889": [
    "Q138611570"
   ]
  },
  "revision_id": "2566753342",
  "ancestor_of": "Q1276130",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q6661985",
  "label": "data processing",
  "description": "any process that uses a computer program to enter data and summarise, analyse or otherwise convert data into usable information",
  "aliases": [
   "processing",
   "computer data processing",
   "data handling",
   "data manipulation"
  ],
  "claims": {
   "P31": [
    "Q116505632",
    "Q10843872"
   ],
   "P279": [
    "Q750843",
    "Q627436",
    "Q10843872"
   ],
   "P1889": [
    "Q13044486"
   ]
  },
  "revision_id": "2568266315",
  "ancestor_of": "Q1276130",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1047113",
  "label": "field of study",
  "description": "field limited to a specific area of ​​knowledge; specialization in an occupation or branch of learning; a specific use",
  "aliases": [
   "subject area",
   "domain",
   "special field",
   "specialism",
   "subdiscipline",
   "sub-discipline",
   "specialized field of study",
   "specialty",
   "special branches"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q105948247",
    "Q110403031",
    "Q26256810",
    "Q21040055"
   ],
   "P361": [
    "Q9081"
   ],
   "P1889": [
    "Q123286730",
    "Q2267705"
   ]
  },
  "revision_id": "2562271253",
  "ancestor_of": "Q1276130",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2267705",
  "label": "field of study",
  "description": "field of study leading to a specific degree",
  "aliases": [
   "field of education",
   "area of study"
  ],
  "claims": {
   "P279": [
    "Q1047113"
   ],
   "P527": [
    "Q13442814"
   ],
   "P460": [
    "Q11862829",
    "Q2465832",
    "Q4671286"
   ],
   "P1889": [
    "Q1047113"
   ]
  },
  "revision_id": "2544362366",
  "ancestor_of": "Q1276130",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q6661985",
  "label": "data processing",
  "description": "any process that uses a computer program to enter data and summarise, analyse or otherwise convert data into usable information",
  "aliases": [
   "processing",
   "computer data processing",
   "data handling",
   "data manipulation"
  ],
  "claims": {
   "P31": [
    "Q116505632",
    "Q10843872"
   ],
   "P279": [
    "Q750843",
    "Q627436",
    "Q10843872"
   ],
   "P1889": [
    "Q13044486"
   ]
  },
  "revision_id": "2568266315",
  "ancestor_of": "Q1276130",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q19478619",
  "label": "metaclass",
  "description": "class which has instances that are all themselves classes",
  "aliases": [
   "Wikidata metaclass",
   "Wikidata metaclasses"
  ],
  "claims": {
   "P31": [
    "Q151885",
    "Q19868531",
    "Q115490628"
   ],
   "P279": [
    "Q16889133"
   ],
   "P361": [
    "Q324254"
   ],
   "P1889": [
    "Q19828331",
    "Q123369568",
    "Q1924819",
    "Q24017414"
   ]
  },
  "revision_id": "2559895276",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q24017414",
  "label": "second-order class",
  "description": "metaclass containing as instances all classes of individuals",
  "aliases": [
   "2nd-order class",
   "metaclass of the first order"
  ],
  "claims": {
   "P31": [
    "Q24017465",
    "Q115490628"
   ],
   "P279": [
    "Q23959932",
    "Q19478619"
   ],
   "P1889": [
    "Q21146257",
    "Q19478619",
    "Q16889133",
    "Q23958852"
   ]
  },
  "revision_id": "2570870333",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q142077035",
  "label": "type of perdurant",
  "description": "instances are classes of perdurant",
  "aliases": [
   "perdurant type",
   "event universal",
   "gufo:EventType",
   "ufo:PerdurantType"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q141439648"
   ],
   "P1889": [
    "Q141750103",
    "Q108586636"
   ]
  },
  "revision_id": "2570481579",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q10843872",
  "label": "process",
  "description": "set of interrelated tasks that transform inputs into outputs, where the tasks may be carried out by people, nature or machines using various resources",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116505632"
   ],
   "P279": [
    "Q3249551",
    "Q1914636"
   ],
   "P527": [
    "Q1816633"
   ],
   "P1889": [
    "Q104637332",
    "Q104637425",
    "Q500669",
    "Q20920559",
    "Q46270982"
   ]
  },
  "revision_id": "2561980101",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q750843",
  "label": "information processing",
  "description": "process in which input information is analysed or transformed in order to produce information as output",
  "aliases": [
   "information process"
  ],
  "claims": {
   "P31": [
    "Q116505632",
    "Q500669",
    "Q268592"
   ],
   "P279": [
    "Q3249551",
    "Q500669",
    "Q141344358"
   ],
   "P361": [
    "Q579488"
   ],
   "P1889": [
    "Q99194088"
   ]
  },
  "revision_id": "2554189270",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q627436",
  "label": "field of work",
  "description": "particular area of activity in industry and science",
  "aliases": [],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q1047113",
    "Q451967"
   ],
   "P460": [
    "Q11862829"
   ],
   "P1889": [
    "Q44597158",
    "Q12737077"
   ]
  },
  "revision_id": "2562948765",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110402867",
  "label": "knowledge classification",
  "description": "Wikidata metaclass",
  "aliases": [
   "knowledge classification system",
   "classification system of knowledge"
  ],
  "claims": {
   "P31": [
    "Q121344523"
   ],
   "P279": [
    "Q5962346"
   ],
   "P1889": [
    "Q110403031"
   ]
  },
  "revision_id": "2569936517",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q105948247",
  "label": "knowledge system",
  "description": "systems of knowledge produced over time through interactions with other human beings",
  "aliases": [
   "knowledge systems"
  ],
  "claims": {
   "P31": [
    "Q96116695"
   ],
   "P279": [
    "Q3622126"
   ],
   "P527": [
    "Q9081"
   ]
  },
  "revision_id": "2522085818",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110403031",
  "label": "knowledge type",
  "description": "Wikidata metaclass",
  "aliases": [
   "type of knowledge"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q140458154"
   ],
   "P1889": [
    "Q110402867",
    "Q125161275"
   ]
  },
  "revision_id": "2548067834",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q26256810",
  "label": "topic",
  "description": "topic or area addressed by a work or set of works",
  "aliases": [
   "issue",
   "subject",
   "theme",
   "topic of a work",
   "subject matter of a work",
   "matter",
   "main subject",
   "main topic",
   "subject matter",
   "gum:SubjectMatter"
  ],
  "claims": {
   "P279": [
    "Q11028",
    "Q12488383",
    "Q16514889"
   ],
   "P460": [
    "Q1053916",
    "Q200801"
   ],
   "P1889": [
    "Q14095863",
    "Q9340580"
   ]
  },
  "revision_id": "2567187301",
  "ancestor_of": "Q1276130",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q101352",
  "label": "family name",
  "description": "part of a naming scheme for individuals, used in many cultures worldwide",
  "aliases": [
   "last name",
   "fam name",
   "family surname",
   "surname",
   "clan name"
  ],
  "claims": {
   "P31": [
    "Q121493639"
   ],
   "P279": [
    "Q4116295",
    "Q10856962"
   ],
   "P361": [
    "Q1071027"
   ],
   "P460": [
    "Q4116295",
    "Q61942409"
   ],
   "P1889": [
    "Q8436",
    "Q777342",
    "Q279239",
    "Q211503",
    "Q55408004",
    "Q61942409"
   ]
  },
  "revision_id": "2572971854",
  "ancestor_of": "Q83348825",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q121493639",
  "label": "name particle",
  "description": "part of a name",
  "aliases": [
   "name component",
   "component of a name",
   "name element"
  ],
  "claims": {
   "P279": [
    "Q10856962",
    "Q13196193",
    "Q184943"
   ],
   "P361": [
    "Q115642094"
   ]
  },
  "revision_id": "2571890163",
  "ancestor_of": "Q83348825",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4116295",
  "label": "surname",
  "description": "human name used in combination with given name(s) used to indicate association, often a family name or a name indicating place of origin",
  "aliases": [
   "after-name",
   "last name"
  ],
  "claims": {
   "P31": [
    "Q121493639"
   ],
   "P279": [
    "Q10856962"
   ],
   "P361": [
    "Q1071027"
   ],
   "P460": [
    "Q101352",
    "Q53857984",
    "Q117209596"
   ],
   "P1889": [
    "Q61942409",
    "Q279239"
   ]
  },
  "revision_id": "2572014198",
  "ancestor_of": "Q83348825",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q10856962",
  "label": "anthroponym",
  "description": "name of a person, such as given name (first name) or surname",
  "aliases": [
   "human name",
   "person's name"
  ],
  "claims": {
   "P31": [
    "Q134599141"
   ],
   "P279": [
    "Q60596080"
   ],
   "P1889": [
    "Q1137656"
   ]
  },
  "revision_id": "2555383414",
  "ancestor_of": "Q83348825",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7187",
  "label": "gene",
  "description": "basic physical and functional unit of heredity",
  "aliases": [
   "genes"
  ],
  "claims": {
   "P31": [
    "Q111972893"
   ],
   "P279": [
    "Q863908",
    "Q50365914",
    "Q3771876"
   ],
   "P361": [
    "Q37748",
    "Q7020",
    "Q1501261"
   ],
   "P1889": [
    "Q1449",
    "Q7020"
   ]
  },
  "revision_id": "2568084548",
  "ancestor_of": "Q18045577",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q20747295",
  "label": "protein-coding gene",
  "description": "type of a gene",
  "aliases": [
   "protein coding gene"
  ],
  "claims": {
   "P31": [
    "Q131679239"
   ],
   "P279": [
    "Q7187"
   ]
  },
  "revision_id": "2566835221",
  "ancestor_of": "Q18045577",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q111972893",
  "label": "type of structure",
  "description": "Wikidata metaclass of arrangement and organization of interrelated elements in an object or system",
  "aliases": [
   "structure type"
  ],
  "claims": {
   "P31": [
    "Q23958852"
   ],
   "P279": [
    "Q21146257",
    "Q96251598"
   ]
  },
  "revision_id": "2561704900",
  "ancestor_of": "Q18045577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q863908",
  "label": "nucleic acid sequence",
  "description": "succession of letters that indicate the order of nucleotides within a DNA (using GACT) or RNA (GACU) molecule",
  "aliases": [
   "base sequence",
   "nucleotide sequence",
   "Nucleic acid sequence",
   "nucleic acid primary structure"
  ],
  "claims": {
   "P279": [
    "Q37500013",
    "Q3771876",
    "Q141543245"
   ]
  },
  "revision_id": "2556398578",
  "ancestor_of": "Q18045577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q50365914",
  "label": "biological region",
  "description": "sequence region defined by its disposition to be involved in a biological process",
  "aliases": [],
  "claims": {
   "P279": [
    "Q219858"
   ]
  },
  "revision_id": "2184498222",
  "ancestor_of": "Q18045577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3771876",
  "label": "nucleic acid structure",
  "description": "organization of DNA and RNA molecules at different scales",
  "aliases": [
   "nucleic acid part"
  ],
  "claims": {
   "P279": [
    "Q15712714"
   ],
   "P1889": [
    "Q863908"
   ]
  },
  "revision_id": "2549811286",
  "ancestor_of": "Q18045577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q131679239",
  "label": "type of gene",
  "description": "metaclass for genes with different structural or functional characteristics",
  "aliases": [
   "gene type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ],
   "P1889": [
    "Q106016",
    "Q5532959"
   ]
  },
  "revision_id": "2552517149",
  "ancestor_of": "Q18045577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
