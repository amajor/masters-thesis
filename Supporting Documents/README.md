# Supporting Documents

## Spreadsheets

Information has been gathered and organized in Google Spreadsheets in order to
understand the data. You can find copies of the spreadsheets below.

* Filtered Repositories 
  * [Google Sheet](https://docs.google.com/spreadsheets/d/1qIyOSli28WGFCRCH7v7OL79zOm2wITmFz70vlBlPGN8/edit?usp=sharing)
  * [Excel Download Version](./Spreadsheets/Filtered%20Repositories.xlsx)
* Final Repository Set
  * [Google Sheet](https://docs.google.com/spreadsheets/d/14dJZ0UlfvQ-opwzeiR3mYqNDzONMj2Uqb6tDACKT-og/edit?usp=sharing)
  * [Excel Download Version](./Spreadsheets/Thesis%20Repositories.xlsx)

---

## [An Empirical Study of Lehman’s Law on Software Quality Evolution](./Reviewed/Yu_SoftwareQualityEvolution.pdf)

> Software systems must change to adapt to new functional requirements and nonfunctional requirements. According to Lehman’s laws of software evolution, on the one side, the size and the complexity of a software system will continually increase in its life time; on the other side, the quality of a software system will decrease unless it is rigorously maintained and adapted. Lehman’s laws of software evolution, especially of those on software size and complexity, have been widely validated. However, there are few empirical studies of Lehman’s law on software quality evolution, despite the fact that quality is one of the most important measurements of a software product. This paper defines a metric—accumulated defect density—to measure the quality of evolving software systems. We mine the bug reports and measure the size and complexity growth of four evolution lines of Apache Tomcat and Apache Ant projects. Based on these studies, Lehman’s law on software quality evolution is examined and evaluated.

---

## [Predicting Maintainability with Object-Oriented Metrics - An Empirical Comparison](./Reviewed/Jahnke03.pdf)

From Dr. Safwan Omari:

> Attached is a nice paper that does similar work on C/C++ and Java. Here a few notes.
> - The paper performs correlation analysis between OO metrics and software maintainability to find best metrics to predict maintainability, which is similar to what we are trying to do.
> - Authors used log history to quantify maintainability,  we kind of lowered the scope of our work to avoid having to do the same.
> - The paper performs the study on a few hand-picked software systems and log analysis appears to be manual. Our analysis is large-scale, should be  on the order 50 to 100 projects
> - Our work is more industry driven and oriented for practitioners, we use Pylint metrics and MI and these are tools/metrics used by practitioners.

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

## [Pylint](https://pylint.pycqa.org/en/latest/intro.html)

Pylint is a tool that can analyze code for best practices, following the 
[PEP 8 Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)

> Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code's complexity.

> Pylint will display a number of messages as it analyzes the code and it can also be used for displaying some statistics about the number of warnings and errors found in different files. The messages are classified under various categories such as errors and warnings.

> Last but not least, the code is given an overall mark, based on the number and severity of the warnings and errors.

### [Pylint Score](https://pylint.pycqa.org/en/latest/technical_reference/features.html#reports-options)

> Python expression which should return a score less than or equal to 10. You have access to the variables 'error', 'warning', 'refactor', and 'convention' which contain the number of messages in each category, as well as 'statement' which is the total number of statements analyzed. This score is used by the global evaluation report (RP0004).

Default Equation: 

    10.0 - ((float(5 * error + warning + refactor + convention) / statement) * 10)

### Refactor Score

- [Refactoring Checker](https://pylint.pycqa.org/en/latest/technical_reference/features.html#refactoring-checker)
  - max-nested-blocks (default: 5)
  - never-returning-functions (default: `sys.exit,argparse.parse_error`)
  - simplifiable-condition
  - condition-evals-to-constant
  - simplify-boolean-expression
  - consider-using-in
  - consider-merging-isinstance
  - consider-using-max-builtin
  - consider-using-min-builtin
  - consider-using-with
  - super-with-arguments
  - use-list-literal
  - etc.

---

## [PEP 8](https://www.python.org/dev/peps/pep-0008/)

> One of Guido's key insights is that code is read much more often than it is written. The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code. As PEP 20 says, "Readability counts".

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

> However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask!

---

## [Standardized code quality benchmarking for improving software maintainability](./Reviewed/Standardized-code-quality-benchmarking.pdf)

- Technical quality of source code impacts software maintainability
  1. how easy it is to determine where and how that change can be performed
  2. how easy it is to implement that change
  3. how easy it is to avoid unexpected effects of that change
  4. how easy it is to validate the changes performed
- "Measurement standardization greatly facilitates the collection of individual assessments in a structured repository."

- Paper sections:
  1. Introduction
  2. Measuring software via code metrics
  3. Standardized evaluation procedure
  4. Applications
  5. Case examples
  6. Discussion of the approach
  7. Related work
  8. Concluding remarks and future work

> We provide an overview of the approach developed by the Software Improvement Group for code analysis and quality consulting focused on software maintainability. The approach uses a standardized measurement model based on the ISO/IEC 9126 definition of maintainability and source code metrics. Procedural standardization in evaluation projects further enhances the comparability of results. Individual assessments are stored in a repository that allows any system at hand to be compared to the industry-wide state of the art in code quality and maintainability. When a minimum level of software maintainability is reached, the certification body of TUV Informationstechnik GmbH issues a Trusted Product Maintainability certificate for the software product.

---

## [ISO/IEC 9126-1:2001](https://www.iso.org/standard/22749.html)
### Software engineering — Product quality — Part 1: Quality model

- Status: Withdrawn
- Publication date: 2001-06
- Revised by ISO/IEC 25010:2011

## [ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html)
### Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models

> THIS STANDARD WAS LAST REVIEWED AND CONFIRMED IN 2017. 
> THEREFORE THIS VERSION REMAINS CURRENT.

ISO/IEC 25010:2011 defines:

1. A quality in use model composed of five characteristics (some of which are further subdivided into subcharacteristics) that relate to the outcome of interaction when a product is used in a particular context of use. This system model is applicable to the complete human-computer system, including both computer systems in use and software products in use.
2. A product quality model composed of eight characteristics (which are further subdivided into subcharacteristics) that relate to static properties of software and dynamic properties of the computer system. The model is applicable to both computer systems and software products.

Activities during product development that can benefit from the use of the quality models include:

- identifying software and system requirements;
- validating the comprehensiveness of a requirements definition;
- identifying software and system design objectives;
- identifying software and system testing objectives;
- identifying quality control criteria as part of quality assurance;
- identifying acceptance criteria for a software product and/or software-intensive computer system;
- establishing measures of quality characteristics in support of these activities.

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

## [How does code readability change during software evolution?](./Reviewed/How-does-code-readability-change-during-software-evolution.pdf)

Code readability can impact maintainability. In this article the authors found that within the sample that they reviewed, most source code was readable and a minority of commits changed the readability. They also provide guidelines for maintaining readiability, could be useful when building conclusions from the data.

> Code reading is one of the most frequent activities in software maintenance. Such an activity aims at acquiring information from the code and, thus, it is a prerequisite for program comprehension: developers need to read the source code they are going to modify before implementing changes. As the code changes, so does its readability; however, it is not clear yet how code readability changes during software evolution. To understand how code readability changes when software evolves, we studied the history of 25 open source systems. We modeled code readability evolution by defining four states in which a file can be at a certain point of time (non-existing, other-name, readable, and unreadable). We used the data gathered to infer the probability of transitioning from one state to another one. In addition, we also manually checked a significant sample of transitions to compute the performance of the state-of-the-art readability prediction model we used to calculate the transition probabilities. With this manual analysis, we found that the tool correctly classifies all the transitions in the majority of the cases, even if there is a loss of accuracy compared to the single-version readability estimation. Our results show that most of the source code files are created readable. Moreover, we observed that only a minority of the commits change the readability state. Finally, we manually carried out qualitative analysis to understand what makes code unreadable and what developers do to prevent this. Using our results we propose some guidelines (i) to reduce the risk of code readability erosion and (ii) to promote best practices that make code readable.

---

## [Measurement and refactoring for package structure based on complex network](./Reviewed/s41109-020-00298-8.pdf)

- "Refactoring, is one of powerful tools to improve software design and increase maintainability and usability for software systems (Fowler 1997)."
- Cohesion & Coupling
  - "Cohesion and coupling are correlated but not overlapped. Bias to any one metric is not good to measure software correctly. Based on the relation of cohesion and coupling metrics, we present an evaluation model of package structure, then update the refactoring algorithm."

> Software structure is the backbone for software systems. During the long time of software evolution, it is gradually weakened by continuous code modification and expansion driven by new requirements. Therefore, measuring software and refactoring codes are necessary to keep software structure stable and clean. In this paper, we propose two metrics of cohesion and coupling to characterize package structure. We consider not only the dependencies of intra-package and inter-package, but also the backward dependencies of inter-package. The two metrics are proved theoretically that they are satisfied with Briand’s four properties. Based on these metrics, a refactoring algorithm is presented to improve the quality of package structure. Through tests on ten open source software systems, the experiment result shows our metrics can measure software structure correctly and improve codes to fit for the rule of high cohesion and low coupling.

---

## [Impact of design patterns on software quality: a systematic literature review](./Reviewed/iet-sen.2018.5446.pdf)

- "The flexibility provided by design patterns becomes clear when the software is extended."
- "Changes performed in a class can be corrective, adaptive, perfective, or preventive. These changes can occur due to new requirements, debugging, changes that propagate from changes in other classes and refactoring."
  - "A class that changes more frequent than others might be because the class is easy to extend or because the class is correlated to other classes, which raises an alarm about the class modularity."
- "Our study has shown that the primary studies provide empirical evidence on the positive effect of documentation of designs pattern instances on programme comprehension, and therefore, maintainability."
- "...developers should pay more effort to add such documentation, even if in the form of simple comments in the source code."

---

## [Software Architecture Metrics: A Literature Review](./Reviewed/1901.09050.pdf)

> In Software Engineering, early detection of architectural issues is key. It helps mitigate the risk of poor performance, and lowers the cost of repairing these issues. Metrics give a quick overview of the project which helps designers with the detection of flaws or degradation in their architecture. Even though studies unveiled architectural metrics more than 25 years ago, they have not yet been embraced by the industry nor the open source community. In this study, we aim at conducting a review of existing metrics focused on the software architecture for evaluating quality, early in the design flow and throughout the project’s lifetime. We also give guidelines of their usage and study their relevance in different contexts.

- Early detection of architectural issues is key
  - Helps mitigate risk of poor performance
  - Lowers cost of repairing these issues
- Studies unveiled  architectural metrics 25 years ago
  - Industry and open source community have not embraced the metrics
- This study conducts review of existing metrics focused on software architecture for evaluating quality early in design flow AND throughout project's lifetime
- Provides guidelines of metric usage
- Studies relevance of metrics in different contexts

> **Maintainability**: It is very important that a software is easy to maintain. It must be easy to make changes in a software, either for the addition of a new feature, or for a bug fix. This means that changes must be possible locally, without impacting all of the software. Maintainability also means that it is possible for multiple developers to work on separate parts of the software without impacting each other, which enables parallel work. Maintainability is often synonym with sustainability, as it makes it possible for the software project to be used and updated for many years. For all these reasons, making a software maintainable is key for the future of the project.

> **Extensibility**: The ability for a software architecture to handle addition of new functionalities and components. It is very valuable in agile development as features are added throughout the life of the project.

---

## [A Beginner's Guide to Code Standards in Python - Pylint Tutorial](https://docs.pylint.org/en/1.6.0/tutorial.html)

This site appears to give a walkthrough of Pylint and how to use and understand it.

TODO: Review this site.

---

## [Software structure evolution and relation to subgraph defectiveness](./Reviewed/iet-sen.2018.5060.pdf)

- "...people are the key element in software production, and human mistakes are the main source of software faults. Good and reliable techniques for software fault prevention and early detection are one of the major concerns of organisations developing such systems."
- "It has been identified that the majority of faults are located in a minority of system modules/classes and that this minority of system modules/classes constitutes a minority of system share."
- "A network graph is a structural system property that is defined independently of static code properties or the software development properties and can be defined for any software code."
- "Analysing the evolution of software by representing the software system using the frequencies of subgraph types is beneficial because it allows for structural analysis involving communication patterns"

> Network analysis has been successfully applied in software engineering to understand structural effects in the software. System software is represented as a network graph, and network metrics are used to analyse system quality. This study is motivated by a previous study, which represents the software structure as three-node subgraphs and empirically identifies that software structure continuously evolves over system releases. Here, the authors extend the previous study to analyse the relation of structural evolution and the defectiveness of subgraphs in the software network graph. This study investigates the behaviour of subgraph defects through software evolution and their impact on system defectiveness. Statistical methods were used to study subgraph defectiveness across versions of the systems and across subgraph types. The authors conclude that software versions have similar behaviours in terms of average subgraph type defectiveness and subgraph frequency distributions. However, different subgraph types have different defectiveness distributions. Based on these conclusions, the authors motivate the use of subgraph-based software representation in defect predictions and software modelling. These promising findings contribute to the further development of the software engineering discipline and help software developers and quality management in terms of better modelling and focusing their testing efforts within the code structure represented by subgraphs.

---

## [Lab 2 Assignment](./Reviewed/Alison%20Major%20-%20Lab%202.pdf)

This was an assignment for the **Software Architecture** course at Lewis 
University. It was a brief study in several different quality and 
maintainability scores on three different repositories. The brief work on this
assignment led to the invitation to work on this new research paper for the
term paper (and which will ultimately be my thesis).

---
