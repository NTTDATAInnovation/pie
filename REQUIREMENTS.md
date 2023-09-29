## PIE (Personal Information Eraser)

### Case description, tl;dr
A client have a lot of unstructured text data in Danish. Some of it contain PII which is a problem under GDPR. Either the client has to discard the data or remove/mask the PII.
We want to offer a microservice API that can
1.	Take in text data
2.	Identify the PII
3.	Replace the PII with tags, such as {NAME}, {LOCATION}, {PHONE}, {EMAIL} etc
    - Note: We don’t want to replace tokens like “SnapChat” or ”FIFA”.
4.	Return the modified text to the user.

### Client concerns
•	Recall: We are more concerned with masking all PII than occasionally masking tokens that are not PII.
•	Efficiency: Although the microservice isn’t supposed to run in real-time (e.g,. on every message in a live chat), we are still concerned about latency.
•	OpEx: Insofar as possible, we would like to keep the operational expenditures (running monthly cost) as low as possible (obviously).

### Proposed process
1.	Writing a python implementation using the IBM SDK
2.	Evaluate if LLMs are required
3.  Pick and optimize the model (For LLMs: Reducing size, quantization, prompt tuning.) to improve performance and reduce operational expenditures
3.	Run evaluation on the test data
4.	Deploy the solution (Including authentication etc.)

**I will supply you with**
-	This repo with
    - Documented template source code (Including evaluation notebook),
    - A virtual environment configuration file (poetry) and
    - An instructive README.md (This file)
-	Gold-labelled Danish test data (About 800 examples)
