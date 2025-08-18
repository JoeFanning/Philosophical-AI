# Egalitarian-AI 

## Abstract<br>
The development of a benevolent AI is an essential endeavour for humanity. This immense task is coupled by two important questions. 

1.How to decide on what is benevolent for humanity? What is ethical, moral and just for all? How to make the world a better place?

2.How to define these decisions into metrics for computation in AI?

These are not questions that just have to be asked. They are questions that must be answer. The question is can we answer these questions for AI before it has the ability to answer these questions incorrectly? 

## ​Global and Intergovernmental Frameworks

At the time of this writing a wide array of frameworks exist to address the complex ethical and justice challenges of dynamic AI systems. While many of them share similar core principles, they often focus on different sectors or levels of governance.

​These frameworks aim to provide a broad set of principles for nations and international organizations to follow.

[**​UNESCO Recommendation on the Ethics of Artificial Intelligence**](https://www.unesco.org/en/articles/recommendation-ethics-artificial-intelligence) 

This is the first global standard-setting instrument on AI ethics, adopted by 193 member states. It outlines core values and principles, including proportionality, safety, fairness, and human oversight, and promotes multi-stakeholder governance.

​[**The EU AI Act**](https://artificialintelligenceact.eu/) 

This is a risk-based legal framework that regulates the development and deployment of AI in the European Union. It categorizes AI systems based on their potential to cause harm and imposes stricter requirements on higher-risk systems. It aims to create a global standard for trustworthy AI, impacting any company that wants to operate within the EU.

[**OECD AI Principles**](https://www.oecd.org/en/topics/sub-issues/ai-principles.html) 

These principles, adopted by 42 countries, provide a set of recommendations for policymakers to promote human-centered and trustworthy AI that respects human rights and democratic values.

### ​Academic and Industry Frameworks**

​These frameworks are often developed by researchers, non-profits, or technology companies to guide their own practices or to propose new models for governance.

Companies like:<br>
[IBM (AIF360)](https://research.ibm.com/blog/ai-fairness-360),<br>
[Microsoft (Fairlearn)](https://fairlearn.org/v0.12/about/index.html),<br>
[Google (What-If Tool)](https://research.google/pubs/the-what-if-tool-interactive-probing-of-machine-learning-models/)<br> 
have developed toolkits: "fairness toolkits" or "bias mitigation toolkits" which implement ethical governance over AI models.

[​**DILEMA Project (Designing International Law and Ethics into Military AI)**](https://www.asser.nl/DILEMA?hl=en-gb) 

This project focuses specifically on the ethical and legal challenges of AI in military applications. It aims to ensure that human agency is maintained over military AI systems and that they comply with international law.

​[**The Montreal Declaration for Responsible AI**](https://montrealdeclaration-responsibleai.com/) 

This declaration, developed through a collaborative, public process, outlines principles for the ethical development and deployment of AI, with a strong emphasis on well-being, social justice, and democracy.

## Egalitarianism a Philosophy for a Benevolent AI

### ​Egalitarianism

Egalitarianism is a school of thought rooted in the belief that all people are fundamentally equal and should be treated as such. It is a philosophy that prioritizes social equality and the removal of inequalities, particularly in political, economic, and social life. 
​The word ["egalitarianism"](https://joefanning.github.io/Egalitarian-AI/researchresources.md)comes from the French word "égal," which means "equal" or "level." It emerged during the French Revolution in the late 18th century when people were fighting for a society where everyone had the same rights and opportunities, no matter their background.

## Egalitarian AI 
Egalitarian AI derives it's name from egalitarianism. Egalitarian AI would be considered an encompassing higher order for [Ethical AI](https://www.google.com/search?q=what+is+ethical+ai&oq=what+is+ethical+Ai&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgATSAQk3NDUyajBqMjmoAgCwAgE&client=ms-android-huawei-rev1&sourceid=chrome-mobile&ie=UTF-8) .
It's not just a set of rules for a model to adhere too, but a framework designed on a philosophy that guides the design and purpose of the entire AI system and its integration into society. It asks, "Does this system contribute to a more equal and just society? Is it helping to dismantle systemic inequalities?". 

## Technical Development and Deployment 

### Defining a structural implementation with Egalitarian-AI 

In machine learning an egalitarian model would operate at a higher level of abstraction than an ethical model.
All the models of the AI system would be processed individually by the Ethical AI. Then all these processed models would be collectively analysed and processed by the Egalitarian-AI. 

It would also self adapt it's structure and functionality based on dynamic information from its own data and from external data.
This self adaption is done with
[Adaptive machine learning models] (resources/Adaptive_Machine_Learning_Algorithms:_Improving_Efficiency_through_Dynamic_Model_Adjustment.pdf) it would adjust its parameters and structure as it's exposed to new data, allowing it to handle changing information or environments.

#### Stage 1: The Ethical AI Layer (Individual Model Processing)

​This is the "local" or "micro" level of analysis. In this stage, each individual machine learning model or component within the larger AI system would be rigorously audited to ensure it meets a set of predefined ethical standards. This would be a form of automated quality control for fairness, transparency, and accountability.
​Technically, this would involve a suite of automated tools and metrics applied to each model:
​Bias Detection and Fairness Audits: Before a model is deployed, an Ethical AI layer would run a series of fairness tests. It would use metrics for example like [Disparate Impact, Equal Opportunity Difference, or Statistical Parity](https://joefanning.github.io/Egalitarian-AI/ethicalbiasmodels.md) to check for bias across different demographic subgroup. These metrics are used in algorithms in<br>
[IBM AI Fairness 360 (AIF360) toolkit](https://research.ibm.com/blog/ai-fairness-360).<br>
IBM AI Fairness 360 (AIF360) on [Github](https://github.com/Trusted-AI/AIF360)


**​Explainability (XAI)** 

The layer would produce a detailed explainability report for each model using techniques like SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations). This would ensure that an operator can understand why a particular model is making its decisions.

**Security**

​Privacy and Robustness Checks: Automated scans would check for vulnerabilities like data leakage or susceptibility to adversarial attacks. The goal is to ensure the model is secure and protects user data. 
​This stage ensures that every single component of the AI system is "ethically sound" on its own, like checking that every individual part of a car is working correctly before assembly.

#### Stage 2: The Egalitarian AI Layer (Collective Analysis)

​This is the "global" or "macro" level of analysis. The Egalitarian-AI layer operates at a higher level of abstraction, taking the ethically-vetted models and analyzing their collective impact on the system and society as a whole.

Even though past results do not determine future events. 
It must identify where past results have changed society and reimplement the positive ones and retract the negative ones. 

For example:<br>
[Intersectionality](https://researchguides.library.syr.edu/fys101/intersectionality) 
<br>
While Ethical AI can help reduce explicit biases related to single attributes (like race or gender), addressing intersectional bias—where multiple, overlapping identities create unique and compounded forms of discrimination—is far more complex. The core issue is that intersectional bias isn't just a simple combination of individual biases; it's often a unique harm that doesn't appear when looking at individual groups separately. 
Research has already been done in this area:<br>
[An Intersectional Definition of Fairness](https://ui.adsabs.harvard.edu/abs/2018arXiv180708362F/abstract) 

One of Egalitarian-AI's functions would be to identify these compounded forms of discrimination.

A theoretical real world example:
Three ethically processed models:
A loan approval model, a job application approval rating model and a car insurance quote estimation model.
let's say the loan approval model is less likely to approve loans for people in certain neighborhoods, the job application model favors candidates with addresses in wealthier areas, and the car insurance model gives higher rates to people living in specific zip codes. Even if each model seems fair on its own, when you look at them together, you might find that people from lower-income neighborhoods are consistently facing disadvantages across the board.

**Where past results shouldn't define future decisions**
If the data truthfully reflects that Black people, on average, have lower credit scores than white people, it's not the data itself that's the problem—it's the underlying socioeconomic conditions that caused this disparity. An AI model trained on this data will learn this pattern and, as a result, will likely continue to deny loans or charge higher interest rates to Black applicants, even if they are individually creditworthy.
​The issue is that the credit scoring system, and the data it produces, are deeply intertwined with historical and systemic inequalities.
​The Roots of the Disparity
​Redlining: For decades, the Federal Housing Administration and other institutions used a practice called "redlining" to refuse to guarantee home loans in Black communities. This deprived Black families of a key way to build wealth and good credit.
​Income and Wealth Gaps: Due to historical and ongoing discrimination in employment and housing, Black households have significantly lower median income and wealth than white households. This makes it harder to pay bills on time, save money, and maintain a low credit utilization ratio, all of which are key factors in credit scores.
​Credit "Invisibility": Many people in historically marginalized communities are "credit invisible," meaning they don't have enough credit history to generate a score. They may pay their bills on time (rent, utilities, etc.), but that information isn't typically included in traditional credit reports.
​The Unfairness
​The unfairness isn't that the AI is "lying" about the data. The unfairness is that the data itself is a reflection of a system that has historically disadvantaged a group of people. If an AI model simply learns to replicate that system, it automates and perpetuates a historical injustice.
​The goal of creating "fair" AI isn't to pretend that these disparities don't exist. It's to build a system that can look beyond the raw, biased data and make decisions based on an individual's true creditworthiness, rather than on the systemic disadvantages they face.

**Calibrating the structure of the system**
The Egalitarian-AI could also use the data from these three models to perform [ensemble learning](https://www.google.com/search?q=ensemble+learning+in+computer+science&oq=ensemble+learning+in+computer+science&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHjIICAoQABgWGB4yCAgLEAAYFhgeMggIDBAAGBYYHjIICA0QABgWGB4yCAgOEAAYFhge0gEJMjE4NjlqMGo0qAIOsAIB8QW_RZ0sa6bcKg&client=ms-android-huawei-rev1&sourceid=chrome-mobile&ie=UTF-8)
It would identify relationships between the models data cleaning, exploring, and modeling. It would then perform comparative analyse of the three models [model training, and evaluation](https://www.google.com/search?q=model+training+and+evaluation&oq=model+training+and+evaluation&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIICAIQABgFGB4yCAgDEAAYBRgeMggIBBAAGAgYHjIICAUQABgIGB4yCAgGEAAYCBgeMggIBxAAGAgYHjIICAgQABgIGB4yCAgJEAAYCBgeMggIChAAGAgYHjIICAsQABgIGB7SAQkxOTc5NmowajeoAg-wAgHxBVW1XJkouRqp8QVVtVyZKLkaqQ&client=ms-android-huawei-rev1&sourceid=chrome-mobile&ie=UTF-8). It could identify models structural relationships and where one model could be improved structurally in relationship to another or others, or how many models could be improved in relation to one. 

**​Systemic Feedback Loop Analysis**

The Egalitarian-AI would monitor its real-world deployments. Successful deployments would be replicated, and the data they generate would be integrated to optimize or scale solutions for equivalent or analogous problems. The system would also generalize these learnings to improve other, unrelated components, thereby enhancing its overall functionality.

The structural functionality should adapt and improve depending on successfull metrics and the successful metrics should adapt and improve depending on tbe successfull structural functionality. 

​**External Data Integration and Impact Measurement**

This is a key differentiator. The Egalitarian-AI would not just use internal data but would also integrate with external, real-world data streams (e.g., census data, public health records, economic indicators). It would then analyze the system's overall impact. For example, "Is the deployment of our educational AI system actually narrowing the academic achievement gap, or is it only benefiting students in well-resourced schools?"

​**Resource and Opportunity Allocation** 

If the AI system is a suite of services, the Egalitarian-AI would ensure the distribution of these services is equitable. It might actively shift resources or prioritize service access for historically underserved communities to correct for systemic imbalances.

​**Macro-Level Optimization** 

The Egalitarian-AI's objective function would not be a simple metric like accuracy or fairness score, but a complex, multi-variable function that seeks to maximize social equality. It might recommend re-calibrating individual models or re-configuring the entire system to achieve a better societal outcome.
​Analogy: A City's Infrastructure
​This two-tiered technical structure can be likened to the way a city's infrastructure is planned and maintained:
​Ethical AI: An ethical approach would be like a building inspector. They would ensure that each individual building (an AI model) is constructed to code, is safe, and has proper access for people with disabilities.
​Egalitarian AI: An egalitarian approach would be like the city planner. They would look at all the buildings together and ask: "Are we building a city where everyone has equal access to housing, jobs, and parks? Are we building a city that actively promotes equity and breaks down historical segregation, or are we just making sure that the new construction doesn't violate existing rules?"

​Technically the Egalitarian-AI will dynamically enhance it's own functionality based on metrics constructed from a philosophy called Egalitarianism. Not on a functionality using metrics purely based on profit or power optimisation.

​Egalitarian AI is a benevolent AI to promote and establish local ethics and global justice.

Joe Fanning Den Haag Centrum Aug 2025

Resourses to read:
An Intersectional Definition of Fairness:<br>
https://ui.adsabs.harvard.edu/abs/2018arXiv180708362F/abstract
