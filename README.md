# K-Anonymist
## Inspiration

Medical data is a goldmine for research, but privacy laws like GDPR (Europe) and HIPAA (USA) create "data silos." Doctors want to share insights, but the manual process of anonymizing records is slow and prone to human error. 

To bridge this gap, we built k-anonymist: a "Privacy Orchestrator" that doesn't just mask text, but actually reasons through local laws and contextual risks. Our goal is to empower healthcare providers to instantly transform sensitive clinical narratives into high-utility, anonymized datasets. 

By automating the intersection of legal compliance and data science, k-anonymist ensures that life-saving information can flow freely to researchers while keeping patient identities mathematically and legally secure.

## What it does

**Entity Risk Assessment:** The system identifies entities like names, IDs, and cities. It queries a Context Vault to retrieve specific risk percentages (exposure risk) for each value. For example, a rare city name might show a 90% risk, while a major metropolis shows 5%.

**Legal Validation:** Using ES|QL, the system pulls mandatory handling rules from a Compliance Vault. It checks the patient's jurisdiction (e.g., Netherlands) to see if specific laws, like Dutch UAVG Article 46, require full redaction or just masking for that data type.

**Contextual Transformation:** The agent synthesizes the risk percentage and the legal rule to apply the smartest transformation. It might fully redact a high-risk name but "generalize" a medium-risk location to keep the data useful for geographic research.

## How we built it

📂**Data Integration:** We utilized a specialized Context Vault containing specific entities (e.g., city names, hospital titles) mapped to their re-identification risk percentages. This data allows the system to quantitatively assess how easily a patient could be "exposed" based on their specific location or attributes.

⚡**Elastic as the Core Engine:** Elastic is the project's backbone. We utilized Elasticsearch to store our risk and compliance databases, leveraging ES|QL (Elasticsearch Query Language) to perform high-speed, grounded lookups that verify every entity's exposure risk in real-time.

🤖**Agentic Intelligence:** The project is driven by an Elastic AI Agent (Claude 4.5), which functions as a reasoning engine. It autonomously determines which tools to call—comparing the entity risk values against legal rules—to apply the most effective anonymization strategy.

## Challenges we ran into

**Logic Chain Stability:** Ensuring the agent consistently followed a three-step process—retrieving entity risk, checking legal rules, and applying transformations—without skipping steps or "hallucinating" risks.

**Cumulative Risk Management:** Teaching the agent that multiple low-risk entities (like a city and a month) can combine to create a high-risk unique identifier.

**ES|QL Precision:** Mapping unstructured medical text to structured ES|QL queries to fetch accurate risk percentages and legal actions from our vaults.

**Response Parsing:** Building a robust system to clean and split the complex JSON responses from the Elastic Agent into a user-friendly "Reasoning Trace" and "Audit Table."

## Accomplishments that we're proud of

**Precision Generalization:** Our system moves beyond simple masking to "Generalize" data—preserving research utility by keeping regional and temporal trends intact while securing patient identities.

**Elastic-Agent Synergy:** We achieved a seamless integration between Claude 4.5 and ES|QL, allowing the agent to perform grounded, real-time database lookups to justify every privacy decision.

**Automated Legal Mapping:** We successfully mapped complex statutes (like the Dutch UAVG) into machine-actionable logic, automating a high-stakes process that usually takes hours of manual legal review.

## What we learned

We learned that privacy is a spectrum; single data points might be low-risk, but their combination creates a unique "fingerprint" that requires agentic, holistic analysis.

**Grounded Reliability:** Integrating ES|QL proved that grounding LLMs in a structured "system of truth" prevents hallucinations and ensures legally defensible decisions.

**Utility vs. Privacy:** We discovered that "Generalization" (e.g., changing a city to a region) is superior to redaction for maintaining data value for researchers.

**Legal Translation:** We successfully bridged the gap between abstract law and code by mapping statutes like the Dutch UAVG into actionable AI logic.

## What's next for k-anonymist

⏱️**Real-time Implementation:** Integrating k-anonymist into live clinical workflows, allowing for "on-the-fly" anonymization as doctors type or dictated notes are processed.

🌍**Global Scaling:** Expanding our Compliance Vault to ingest and map international privacy statutes beyond GDPR and HIPAA, creating a universal "Privacy Translator" for cross-border research.

📦**Bulk Data Processing:** Optimizing our Elastic-Agent pipeline to handle massive, multi-terabyte datasets (Big Data), enabling entire hospital databases to be safely prepared for research in minutes.
