## InsightLens – Problem, Solution & Cost Analysis

_InsightLens is a serverless platform that collects, analyses, and visualises customer reviews using AWS Lambda, Comprehend, DynamoDB, S3, and QuickSight, enabling SMEs to track sentiment trends, recurring issues, and take proactive action on feedback!_

---

### Problem Statement

SMEs face fragmented customer feedback across multiple platforms. Manual analysis is slow, error-prone, and offers little insight into sentiment trends, recurring issues, or brand health. Businesses struggle to take timely, data-driven action.

---

### Solution Design

InsightLens uses **AWS Lambda**, **CloudWatch Events**, and **API Gateway** to collect reviews from **Google Places**, **Trustpilot**, and optional first-party APIs. API keys are securely stored in **AWS Secrets Manager**. Reviews are normalised, deduplicated, and analysed using **Amazon Comprehend** for sentiment and key-phrase extraction. Structured insights are stored in **DynamoDB** and aggregated weekly into **S3**, enabling **QuickSight (SPICE)** dashboards. Optional **SNS alerts** notify SMEs of negative sentiment spikes.

![InsightLens Architecture](../architecture/insightlens-architecture.png)

---

### Cost Analysis

- **Serverless Lambda**: cost-efficient, pay-per-use.
- **DynamoDB**: fast query and historical storage.
- **S3 + QuickSight**: low-cost data storage and BI visualisation.
- **SNS**: optional alerts with minimal cost.

InsightLens delivers **real-time analytics**, **trend aggregation**, and **proactive alerting**, enabling SMEs to act on insights without managing infrastructure.

---
