# **InsightLens**

### Customer Review Intelligence for SMEs

![InsightLens Docs](./docs/overview.md)

---

## 🚩 1. Problem

Independent businesses and SMEs struggle to collect, analyse, and act on customer feedback efficiently. Reviews are scattered across platforms like **Google Places**, **Trustpilot**, and potentially first-party websites. Manual monitoring is time-consuming, error-prone, and offers little insight into sentiment trends or recurring issues, making it difficult to respond proactively to negative feedback and improve customer experience.

---

## ✅ 2. Solution

**InsightLens** provides a **serverless, automated review analytics platform** built using **AWS Lambda**, **CloudWatch Events**, **API Gateway**, **Amazon Comprehend**, **DynamoDB**, **S3**, and **Amazon QuickSight**. It enables SMEs to track sentiment trends, recurring issues, and take proactive action on feedback.

Key features:

- **Scalable ingestion pipeline** using Lambda to collect reviews from multiple sources. API credentials are securely stored in **AWS Secrets Manager**. Optional **API Gateway** enables on-demand fetching.
- **NLP processing** via Amazon Comprehend to extract sentiment, themes, and key phrases.
- **Structured insights** stored in DynamoDB for fast querying and historical trend analysis.
- **Aggregation layer** that exports weekly summaries to S3 for **QuickSight (SPICE)** dashboards, visualising trends, recurring pain points, and brand health.
- **Optional SNS alerting** for negative sentiment spikes, allowing SMEs to respond proactively without managing infrastructure or machine-learning services.

---

## 🏗️ 3. Architecture

**Core Components:**

- **AWS Lambda** – Handles review ingestion, normalisation, sentiment analysis, and aggregation.
- **API Gateway** – Optional manual trigger for ad-hoc ingestion.
- **CloudWatch Event Rule** – Scheduled daily or weekly ingestion.
- **AWS Secrets Manager** – Secure storage of API credentials.
- **Amazon DynamoDB** – Stores structured review insights.
- **Amazon S3** – Stores raw JSON and aggregated summaries for QuickSight dashboards.
- **Amazon Comprehend** – Performs NLP sentiment and key-phrase analysis.
- **Amazon QuickSight** – Provides interactive dashboards and visualisation.
- **SNS Topic** – Optional alerting for high negative sentiment.

The architecture separates **ingestion**, **analysis**, **aggregation**, and **visualisation** layers, making it scalable, maintainable, and cost-efficient for SMEs.

---

## 📈 4. Impact

- **Automates review collection** across multiple sources, reducing manual effort.
- **Delivers actionable sentiment insights** in real time, helping businesses respond quickly to negative feedback.
- **Provides trend analysis** for recurring issues and overall customer experience.
- **Serverless design** ensures low operational overhead and scalable cost-efficient execution.
- **Optional alerts** enable proactive mitigation of customer dissatisfaction.

---

## 🖼️ 5. Architecture High-Level Diagram Layout

The architecture diagram illustrates **InsightLens’** various layers, including: ingestion, analysis, aggregation, and visualisation. The noted AWS services interact seamlessly, ensuring secure, automated review analytics and dashboard visualisation.

<img width="1925" height="1524" alt="diagram-export-12-12-2025-12_26_10" src="https://github.com/user-attachments/assets/5e51764c-89bb-401d-8b65-e0ed10f90b44" />

---
