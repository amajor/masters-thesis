# Supporting Documents

## [Lab 2 Assignment](./Reviewed/Alison%20Major%20-%20Lab%202.pdf)

This was an assignment for the **Software Architecture** course at Lewis 
University. It was a brief study in several different quality and 
maintainability scores on three different repositories. The brief work on this
assignment led to the invitation to work on this new research paper for the
term paper (and which will ultimately be my thesis).

---

## [Enabling Empirical Research: A Corpus of Large-Scale Python Systems](./Reviewed/conference_041818.pdf)

The work done in this paper involves collecting a sub-set of Python projects
that can be used for further research. The bulk of the effort in this paper is
in determining which classifiers to use to pare down the public set of Python
systems into a reasonable set for further analysis.

> The Python programming language has been picking up traction in Industry for the past few years in virtually all application domains. Python is known for its high calibre and passionate community of developers. Empirical research on Python systems has potential to promote a healthy environment, where claims and beliefs held by the community are supported by data. To facilitate such research, a corpus of 132 open source python projects have been identified, basic information, quality as well as complexity metrics has been collected and organized into CSV files. Collectively, the list consists of 36, 635 python modules, 59, 532 classes, 253, 954 methods and 84, 892 functions. Projects in the selected list span various application domains including Web/APIs, Scientific Computing, Security and more.

---

## [A Large-Scale Study of Programming Languages and Code Quality in GitHub](./Reviewed/baishakhi17.pdf)

This study begins by programmatically collecting a sample set of projects in 
GitHub that vary in languages. Then the set is appropriately culled, resulting
in a final set used for review. The results are then a study of the impact that
different programming languages may have on the code quality of a project.

> What is the effect of programming languages on software quality? This question has been a topic of much debate for a very long time. In this study, we gather a very large data set from GitHub (728 projects, 63 million SLOC, 29,000 authors, 1.5 million commits, in 17 languages) in an attempt to shed some empirical light on this question. This reasonably large sample size allows us to use a mixed-methods approach, combining multiple regression modeling with visualization and text analytics, to study the effect of language features such as static versus dynamic typing and allowing versus disallowing type confusion on software quality. By triangulating findings from different methods, and controlling for confounding effects such as team size, project size, and project history, we report that language design does have a significant, but modest effect on software quality. Most notably, it does appear that disallowing type confusion is modestly better than allowing it, and among functional languages, static typing is also somewhat better than dynamic typing. We also find that functional languages are somewhat better than procedural languages. It is worth noting that these modest effects arising from language design are overwhelmingly dominated by the process factors such as project size, team size, and commit size. However, we caution the reader that even these modest effects might quite possibly be due to other, intangible process factors, for example, the preference of certain personality types for functional, static languages that disallow type confusion.

---

## [Software Architecture in Practice: Third Edition](https://www.oreilly.com/library/view/software-architecture-in/9780132942799/)

By Len Bass, Paul Clements, and Rick Kazman

### Chapter 18

- "If you go to the trouble of creating a strong architecture, one that you expect to stand the test of time, then you _must_ go to the trouble of describing it in enough detail, without ambiguity, and organizing it so that others can quickly find and update needed information." (pg 327)
- Documentation holds the results of major design decisions as they are confirmed (pg 328)
- Architecture documentation is used for several purposes
  - Means of education (pg 328)
  - Primary vehicle for communication among stakeholders (pg 329)
  - Basis for system analysis and construction (pg 329)
- _Combined View_ - combination of two views to show strong association between them (pg 343)
- "The architect should plan to issue releases of the documentation to support major project milestones, which usually means far enough ahead of the milestone to give developers time to put the architecture to work." (pg 350)
- "Explaining the choice of approach is likely to include a discussion about the satisfaction of quality attribute requirements and tradeoffs incurred." (pg 355)

---

## [Software structure evolution and relation to subgraph defectiveness](./Reviewed/iet-sen.2018.5060.pdf)

- "...people are the key element in software production, and human mistakes are the main source of software faults. Good and reliable techniques for software fault prevention and early detection are one of the major concerns of organisations developing such systems."
- "It has been identified that the majority of faults are located in a minority of system modules/classes and that this minority of system modules/classes constitutes a minority of system share."
- "A network graph is a structural system property that is defined independently of static code properties or the software development properties and can be defined for any software code."
- "Analysing the evolution of software by representing the software system using the frequencies of subgraph types is beneficial because it allows for structural analysis involving communication patterns"

> Network analysis has been successfully applied in software engineering to understand structural effects in the software. System software is represented as a network graph, and network metrics are used to analyse system quality. This study is motivated by a previous study, which represents the software structure as three-node subgraphs and empirically identifies that software structure continuously evolves over system releases. Here, the authors extend the previous study to analyse the relation of structural evolution and the defectiveness of subgraphs in the software network graph. This study investigates the behaviour of subgraph defects through software evolution and their impact on system defectiveness. Statistical methods were used to study subgraph defectiveness across versions of the systems and across subgraph types. The authors conclude that software versions have similar behaviours in terms of average subgraph type defectiveness and subgraph frequency distributions. However, different subgraph types have different defectiveness distributions. Based on these conclusions, the authors motivate the use of subgraph-based software representation in defect predictions and software modelling. These promising findings contribute to the further development of the software engineering discipline and help software developers and quality management in terms of better modelling and focusing their testing efforts within the code structure represented by subgraphs.

---
