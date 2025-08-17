# Egalitarian-AI 
The development of a benevolent AI is an essential endeavour for humanity. This immense task is coupled by two important high level questions. 

1.How to decide on what is benevolent for humanity? What is ethical, moral and just for all? How to make the world a better place?

2.How to define these decisions into metrics for computation in AI?

These are not questions that just have to be asked. They are questions that must be answer. The question is can we answer these questions for AI before it has the ability to answer these questions incorrectly? 

## ​Global and Intergovernmental Frameworks

At the time of this writing a wide array of frameworks exist to address the complex ethical and justice challenges of dynamic AI systems. While many of them share similar core principles, they often focus on different sectors or levels of governance.

​These frameworks aim to provide a broad set of principles for nations and international organizations to follow.

**​UNESCO Recommendation on the Ethics of Artificial Intelligence** 

This is the first global standard-setting instrument on AI ethics, adopted by 193 member states. It outlines core values and principles, including proportionality, safety, fairness, and human oversight, and promotes multi-stakeholder governance.

​**The EU AI Act**

This is a risk-based legal framework that regulates the development and deployment of AI in the European Union. It categorizes AI systems based on their potential to cause harm and imposes stricter requirements on higher-risk systems. It aims to create a global standard for trustworthy AI, impacting any company that wants to operate within the EU.

**OECD AI Principles**

These principles, adopted by 42 countries, provide a set of recommendations for policymakers to promote human-centered and trustworthy AI that respects human rights and democratic values.

**​Academic and Industry Frameworks**

​These frameworks are often developed by researchers, non-profits, or technology companies to guide their own practices or to propose new models for governance.
Companies like IBM (AIF360), Microsoft (Fairlearn), Google (What-If Tool) and other companies and entities. Their "fairness toolkits" or "bias mitigation toolkits" are an example of trying to create benevolent AI.

​**DILEMA Project (Designing International Law and Ethics into Military AI)** 

This project focuses specifically on the ethical and legal challenges of AI in military applications. It aims to ensure that human agency is maintained over military AI systems and that they comply with international law.

​**The Montreal Declaration for Responsible AI**

This declaration, developed through a collaborative, public process, outlines principles for the ethical development and deployment of AI, with a strong emphasis on well-being, social justice, and democracy.

**​A Dynamic Governance Model for AI** 

This model, proposed by academics, advocates for an adaptive, public-private partnership approach to AI governance. It suggests that a collaborative, multi-stakeholder framework is necessary to keep pace with the rapid evolution of AI technology.

## Egalitarianism a Philosophy for a Benevolent AI

### ​Egalitarianism

Egalitarianism is a school of thought rooted in the belief that all people are fundamentally equal and should be treated as such. It is a philosophy that prioritizes social equality and the removal of inequalities, particularly in political, economic, and social life. 
​The word ["egalitarianism"](https://joefanning.github.io/Egalitarian-AI/researchresources.md)comes from the French word "égal," which means "equal" or "level." It emerged during the French Revolution in the late 18th century when people were fighting for a society where everyone had the same rights and opportunities, no matter their background.

Egalitarian AI derives it's name from egalitarianism. Egalitarian AI would be considered an encompassing higher order for [Ethical AI](https://www.google.com/search?q=what+is+ethical+ai&oq=what+is+ethical+Ai&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgATSAQk3NDUyajBqMjmoAgCwAgE&client=ms-android-huawei-rev1&sourceid=chrome-mobile&ie=UTF-8) .
It's not just a set of rules for a model to adhere too, but a framework designed on a philosophy that guides the design and purpose of the entire AI system and its integration into society. It asks, "Does this system contribute to a more equal and just society? Is it helping to dismantle systemic inequalities?". 

## Technical Development and Deployment 

### Defining a structural implementation with Egalitarian-AI 

In machine learning an egalitarian model would operate at a higher level of abstraction than an ethical model.
All the models of the AI system would be processed individually by the Ethical AI. Then all these processed models would be collectively analysed and processed by the Egalitarian-AI. 

#### Stage 1: The Ethical AI Layer (Individual Model Processing)

​This is the "local" or "micro" level of analysis. In this stage, each individual machine learning model or component within the larger AI system would be rigorously audited to ensure it meets a set of predefined ethical standards. This would be a form of automated quality control for fairness, transparency, and accountability.
​Technically, this would involve a suite of automated tools and metrics applied to each model:
​Bias Detection and Fairness Audits: Before a model is deployed, an Ethical AI layer would run a series of fairness tests. It would use metrics like [Disparate Impact, Equal Opportunity Difference, or Statistical Parity](https://joefanning.github.io/Egalitarian-AI/ethicalbiasmodels.md) to check for bias across different demographic subgroup. These metrics are used in toolkits like IBM AI Fairness 360 (AIF360) toolkit. 

**​Explainability (XAI)** 

The layer would produce a detailed explainability report for each model using techniques like SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations). This would ensure that an operator can understand why a particular model is making its decisions.

**Security**

​Privacy and Robustness Checks: Automated scans would check for vulnerabilities like data leakage or susceptibility to adversarial attacks. The goal is to ensure the model is secure and protects user data.

​This stage ensures that every single component of the AI system is "ethically sound" on its own, like checking that every individual part of a car is working correctly before assembly.

#### Stage 2: The Egalitarian AI Layer (Collective Analysis)

​This is the "global" or "macro" level of analysis. The Egalitarian-AI layer operates at a higher level of abstraction, taking the ethically-vetted models and analyzing their collective impact on the system and society as a whole. Its goal is to optimize for a more just and equal outcome, rather than just local fairness.

An example:
Three ethically processed models:
A loan approval model, a job application approval rating model and a car insurance quote estimation model.
let's say the loan approval model is less likely to approve loans for people in certain neighborhoods, the job application model favors candidates with addresses in wealthier areas, and the car insurance model gives higher rates to people living in specific zip codes. Even if each model seems fair on its own, when you look at them together, you might find that people from lower-income neighborhoods are consistently facing disadvantages across the board.

The Egalitarian-AI could also use all the data from these three models to perform [ensemble learning](https://www.google.com/search?q=ensemble+learning+in+computer+science&oq=ensemble+learning+in+computer+science&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHjIICAoQABgWGB4yCAgLEAAYFhgeMggIDBAAGBYYHjIICA0QABgWGB4yCAgOEAAYFhge0gEJMjE4NjlqMGo0qAIOsAIB8QW_RZ0sa6bcKg&client=ms-android-huawei-rev1&sourceid=chrome-mobile&ie=UTF-8)
It would identify data relationships between the models data in cleaning, exploring, and modeling of the data. It would then perform comparative analyse of the three models [model training, and evaluation](https://www.google.com/search?q=model+training+and+evaluation&oq=model+training+and+evaluation&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIICAIQABgFGB4yCAgDEAAYBRgeMggIBBAAGAgYHjIICAUQABgIGB4yCAgGEAAYCBgeMggIBxAAGAgYHjIICAgQABgIGB4yCAgJEAAYCBgeMggIChAAGAgYHjIICAsQABgIGB7SAQkxOTc5NmowajeoAg-wAgHxBVW1XJkouRqp8QVVtVyZKLkaqQ&client=ms-android-huawei-rev1&sourceid=chrome-mobile&ie=UTF-8). It could identify model relationships and where one model could be improved in relationship to another or others, or how many models could be improved in relation to one. 

**​Systemic Feedback Loop Analysis**

The Egalitarian-AI would monitor its real-world deployments. Successful deployments would be replicated, and the data they generate would be integrated to optimize or scale solutions for equivalent or analogous problems. The system would also generalize these learnings to improve other, unrelated components, thereby enhancing its overall functionality.

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

