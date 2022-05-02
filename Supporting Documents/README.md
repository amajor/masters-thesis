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

## [Design Principles and Design Patterns](./Reviewed/DesignPrinciplesAndPatterns.pdf)

> The immediate cause of the degradation of the design is well understood. The requirements have been changing in ways that the initial design did not anticipate. Often these changes need to be made quickly, and may be made by engineers who are not familiar with the original design philosophy. 

_From [Wikipedia](https://en.wikipedia.org/wiki/SOLID):_

The SOLID ideas are:

1. The **single-responsibility principle**: "There should never be more than one reason for a class to change." In other words, every class should have only one responsibility.
2. The **open–closed principle**: "Software entities ... should be open for extension, but closed for modification."
3. The **Liskov substitution principle**: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it." See also design by contract.
4. The **interface segregation principle**: "Many client-specific interfaces are better than one general-purpose interface."
5. The **dependency inversion principle**: "Depend upon abstractions, not concretions."

The SOLID acronym was introduced later, around 2004, by Michael Feathers.

### [Single Responsibility Principle](./Reviewed/RobertMartin_SingleResponsibilityPrinciple.pdf)

> This principle was described in the work of Tom DeMarco and Meilir Page-Jones. They called it cohesion.

> SRP: The Single Responsibility Principle
> THERE SHOULD NEVER BE MORE THAN ONE REASON FOR A CLASS TO CHANGE.

---

## [Review of approaches to manage architectural knowledge in Agile Global Software Development](./Reviewed/iet-sen.2016.0197.pdf)

> Nowadays, Agile and Global Software Development (AGSD) has brought benefits and new challenges to the software industry. Among the main challenges is Architecture Knowledge Management (AKM), due to the following reasons: (i) in Agile Software Development team members prefer to convey knowledge in a face-to-face manner, over transmitting it through formal documents; and (ii) an efficient AKM in Global Software Development involves managing explicit knowledge. These opposite paradigms turn AKM into an unsolved issue in AGSD. In this study, the authors present a systematic mapping review about AKM in AGSD. From this review, they identified nine approaches that AGSD companies use to overcome the AKM challenge, which are grouped in three areas: (i) documentation artefact-based, (ii) communication-based, and (iii) methodological-based. Also, they found that the selected papers evenly support the three phases of the integrated knowledge management cycle (creation/capture, sharing/dissemination and acquisition/application), although only 7% of them support the capture of architectural knowledge in a formalised way. Finally, they conclude proposing critical points to consider in the implementation of AKM solutions in AGSD, and presenting their directions of future work.

---

## [A systematic literature review of open source software quality assessment models](./Reviewed/A-systematic-literature-review-of-open-source-software-quality-assessment-models.pdf)

_Refers to [ISO 25010](https://www.iso.org/standard/35733.html)._

> **Background:** Many open source software (OSS) quality assessment models are proposed and available in the literature. However, there is little or no adoption of these models in practice. In order to guide the formulation of newer models so they can be acceptable by practitioners, there is need for clear discrimination of the existing models based on their specific properties. Based on this, the aim of this study is to perform a systematic literature review to investigate the properties of the existing OSS quality assessment models by classifying them with respect to their quality characteristics, the methodology they use for assessment, and their domain of application so as to guide the formulation and development of newer models. Searches in IEEE Xplore, ACM, Science Direct, Springer and Google Search is performed so as to retrieve all relevant primary studies in this regard. Journal and conference papers between the year 2003 and 2015 were considered since the first known OSS quality model emerged in 2003.

> **Results:** A total of 19 OSS quality assessment model papers were selected. To select these models we have developed assessment criteria to evaluate the quality of the existing studies. Quality assessment models are classified into five categories based on the quality characteristics they possess namely: single-attribute, rounded category, community-only attribute, non-community attribute as well as the non-quality in use models. Our study reflects that software selection based on hierarchical structures is found to be the most popular selection method in the existing OSS quality assessment models. Furthermore, we found that majority (47%) of the existing models do not specify any domain of application.

> **Conclusions:** In conclusion, our study will be a valuable contribution to the community and helps the quality assessment model developers in formulating newer models and also to the practitioners (software evaluators) in selecting suitable OSS in the midst of alternatives.

This study has a lot of interesting data points about the process quality model characteristics (found in ISO 25010) and how maintainability is the most important attribute being measured in Open Source Software (OSS) in the different quality assessment models out there.

### [The SQO-OSS Quality Model: Measurement Based Open Source Software Evaluation](./Reviewed/Samoladas2008_Chapter_TheSQO-OSSQualityModelMeasurem.pdf)

> Software quality evaluation has always been an important part of software business. The quality evaluation process is usually based on hierarchical quality models that measure various aspects of software quality and deduce a characterization of the product quality being evaluated. The particular nature of open source software has rendered existing models inappropriate for detailed quality evaluations. In this paper, we present a hierarchical quality model that evaluates source code and community processes, based on automatic calculation of metric values and their correlation to a set of predefined quality profiles.

---

## [Gamification for software process improvement: a practical approach](./Reviewed/iet-sen.2018.5120.pdf)

> Gamification is a research field that is intended to increase motivation, so it is especially indicated in human capital intensive environments such as the software industry. Within Software Engineering, one of the main issues regarding software process improvement (SPI) is personnel motivation in specific SPI initiatives. These issues are stronger in small and medium software development companies where employees have to deal with the pressure of deadlines and occasional work overload. To address the adoption of SPI initiatives, the researchers implemented a defined gamification framework for deployment in SPI efforts in order to increase motivation among software workers and to enhance SPI results. The framework was rolled out in a small Spanish software development organisation, which is conducting internal SPI initiatives. To validate the effectiveness of the implemented framework, a controlled experiment was carried out in which an experimental group adopted SPI improvements using a gamification approach. The implementation results show that the application of the framework does not increase personnel motivation in SPI tasks although it contributes to enhancing the SPI tasks performance. This study discusses the limitations and recommendations to implement appropriately the SPI-gamification framework in the scope of small and medium software development companies.

While an interesting topic, this paper is about implementing gamefication within an organization and does not directly apply to the open source systems that we're reviewing. It is an interesting idea, but does not directly correlate with Maintainability Index and software evolution.

---

## [Understanding software evolution with software cities](./Reviewed/1473871612438785.pdf)

> Software cities are visualizations of software systems in the form of virtual cities. They are used as platforms to integrate a large variety of product- and process-related analysis data. Their usability, however, for real-world software development often suffers from their inability to appropriately deal with software changes. Even small structural changes can disrupt the overall structure of the city, which in turn corrupts the mental maps of its users. In this article we describe a systematic approach to utilize the city metaphor for the visualization of evolving software systems as growing software cities. The main contribution is a new layout approach which explicitly takes the development history of software systems into account. The approach has two important effects: first, it creates a stable gestalt of software cities even when the underlying software systems evolve; thus, by preserving its users’ mental maps these cities are especially suitable for use during ongoing system development. Second, it makes history directly visible in the city layouts, which allows for supporting novel analysis scenarios. We illustrate such scenarios by presenting several thematic cities’ maps, each capturing specific development history aspects.

Systematic approach to utilize the city metaphor:
1. Creates a stable gestalt of software cities even when the underlying software systems evolve
2. It makes history directly visible in the city layouts

The EvoStreets approach follows 3 models to build up the map:
1. The **primary model** for software cities captures structural and analysis data.
    - Structural data refer to the static software structure, i.e. the decomposition into subsystems and modules, as well as dependencies among modules.
2. The secondary model is a 2.5D **geometric model**, representing primary model data
    - captures the main structural and evolutionary properties of the software system
    - provides a specific, stable gestalt for each software system
      - mainly influenced by the particular layout of the system elements
3. **Thematic tertiary models**
    - designed to support specific application scenarios by visualizing particular aspects of a given software system and its development history

> The EvoStreets approach particularly focuses on aspects of evolution by capturing the information about the creation time of system elements in the layout and by creating stable layout sequences during the evolution of systems. This allows for supporting several application scenarios which are based on information about the history of development activities and their effects on the system structure. Typical questions developers and project managers in this context ask are “How did this component evolve?”, “Who is working on what?”,29 or “Who owns a piece of code?” and “What is the history of a piece of code?”.

---

## [A Systematic Literature Review of Machine Learning Techniques for Software Maintainability Prediction](./Reviewed/Alsolai_Roper_IST_2019_A_systematic_literature_review_of_machine_learning_techniques.pdf)

> **Context:** Software maintainability is one of the fundamental quality attributes of software engineering. The accurate prediction of software maintainability is a significant challenge for the effective management of the software maintenance process. 

> **Objective:** The major aim of this paper is to present a systematic review of studies related to the prediction of maintainability of object-oriented software systems using machine learning techniques. This review identifies and investigates a number of research questions to comprehensively summarize, analyse and discuss various viewpoints concerning software maintainability measurements, metrics, datasets, evaluation measures, individual models and ensemble models. 

> **Method:** The review uses the standard systematic literature review method applied to the most common computer science digital database libraries from January 1991 to July 2018. 

> **Results:** We survey 56 relevant studies in 35 journals and 21 conference proceedings. The results indicate that there is relatively little activity in the area of software maintainability prediction compared with other software quality attributes. CHANGE maintenance effort and the maintainability index were the most commonly used software measurements (dependent variables) employed in the selected primary studies, and most made use of class-level product metrics as the independent variables. Several private datasets were used in the selected studies, and there is a growing demand to publish datasets publicly. Most studies focused on regression problems and performed k-fold cross-validation. Individual prediction models were employed in the majority of studies, while ensemble models relatively rarely. 

> **Conclusion:** Based on the findings obtained in this systematic literature review, ensemble models demonstrated increased accuracy prediction over individual models, and have been shown to be useful models in predicting software maintainability. However, their application is relatively rare and there is a need to apply these, and other, models to an extensive variety of datasets with the aim of improving the accuracy and consistency of results.

---

## [An Extensive Analysis of Machine Learning Based Boosting Algorithms for Software Maintainability Prediction](./Reviewed/ijimai7_2_9_0.pdf)

_Refers to [ISO 25010](https://www.iso.org/standard/35733.html)._

> Software Maintainability is an indispensable factor to acclaim for the quality of particular software. It describes the ease to perform several maintenance activities to make a software adaptable to the modified environment. The availability & growing popularity of a wide range of Machine Learning (ML) algorithms for data analysis further provides the motivation for predicting this maintainability.

> This study would open new doors for the software developers for carrying out comparatively more precise predictions well in time and hence reduce the overall maintenance costs.

---

## [Programs, Life Cycles, and Laws of Software Evolution](./Reviewed/lehman.pdf)

> By classifying programs according to their relationship to the environment in which they are executed, the paper identities the sources of evolutionary pressure on computer applications and programs and shows why this results in a process of never ending maintenance activity. The resultant life cycle processes are then briefly discussed. The paper then introduces laws of Program Evolution that have been formulated following quantitative studies of the evolution of a number of different systems. Finally an example is provided of the application of Evolution Dynamics models to program release plnnning.

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

_Refers to [ISO 9126](https://www.iso.org/standard/22749.html), which becomes [ISO 25010](https://www.iso.org/standard/35733.html)._

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

_Refers to [ISO 25010](https://www.iso.org/standard/35733.html)._

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
