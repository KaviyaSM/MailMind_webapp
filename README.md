# 📧 MailMind: Smart Email Prioritizer and Gmail Assistant

> An AI-powered system for smart email prioritization, summarization, and intelligent reply generation using NLP and LLMs.

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://mailmind-webapp.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/KaviyaSM/MailMind_webapp.git)
[![Conference Paper](https://img.shields.io/badge/Paper-Conference-blue?style=for-the-badge&logo=googledrive)](https://drive.google.com/file/d/1MsqqhwVA2coV4LteFlj3BnkBxaTHDXMH/view?usp=drive_link)
[![Demo Video](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=googledrive)](https://drive.google.com/file/d/1rrTdhRw0MUk-j0PXEBH-oJ8nKsmGrMqm/view?usp=drive_link)

---

## 👥 Team

| Name | Roll Number |
|------|-------------|
| Kalashree S | 311522243021 |
| Kaviya SM | 311522243024 |
| Kaviyalakshmi K | 311522243025 |

**Department:** Artificial Intelligence & Data Science

**Internal Guide:** Mrs. Pavithra K, M.E., Assistant Professor

**External Guide:** Mr. Muthumaran T, B.Tech., AI & ML Developer

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Abstract](#-abstract)
- [Objectives, Scope & SDG](#-objectives-scope--sdg)
- [Novelty](#-novelty)
- [Literature Survey](#-literature-survey)
- [Existing vs Proposed System](#-existing-vs-proposed-system)
- [System Requirements](#%EF%B8%8F-system-requirements)
- [System Architecture](#-system-architecture)
- [Modules](#-modules)
- [Testing & Validation](#-testing--validation)
- [Performance Analysis](#-performance-analysis)
- [Conclusion & Future Work](#-conclusion--future-work)
- [References](#-references)

---

## 🚨 Problem Statement

With the rapid increase in daily email communication, users face **email overload**, making it difficult to identify and respond to important messages on time. Existing platforms like Gmail lack advanced intelligence to prioritize emails based on context and urgency. As a result, users spend significant time manually sorting, reading, and replying to emails, leading to **reduced productivity**.

There is a need for an AI-based solution that can automatically prioritize emails, summarize content, and generate smart responses to improve efficiency.

---

## 📌 Abstract

MailMind is an AI-powered system for smart email prioritization and Gmail assistance that:

- Uses advanced **NLP and LLMs** to rank emails, detect reply needs, and summarize content
- Generates **context-aware draft responses** automatically
- Supports **attachment analysis** (PDFs, DOCX, Excel, images)
- Features a clean **Streamlit-based UI**
- Enhances productivity by organizing emails intelligently and reducing manual effort

---

## 🎯 Objectives, Scope & SDG

| Scope | Objectives | Sustainability Alignment |
|-------|------------|--------------------------|
| Integration with Gmail for real-time email access | Develop an AI-based email prioritization system | **SDG 9** – Industry, Innovation and Infrastructure |
| Handles email prioritization, summarization, and reply generation | Provide email summarization for quick understanding | Promotes innovation using AI for smarter communication systems |
| Supports attachment analysis and user-friendly interface | Detect reply requirements and generate smart responses | |
| | Improve user productivity and time efficiency | |

---

## 💡 Novelty

What makes MailMind unique:

- ✅ Combines **email prioritization, summarization, and smart reply generation** in a single system
- ✅ Uses **AI + NLP + LLMs** to understand context and urgency — not just keywords
- ✅ **Automatically detects** whether a reply is needed
- ✅ Generates **context-aware, personalized responses**
- ✅ Includes **attachment analysis** along with email content
- ✅ Provides an **interactive Streamlit-based interface** for easy use

---

## 📚 Literature Survey

| # | Author & Year | Title | Mechanism | Drawbacks |
|---|--------------|-------|-----------|-----------|
| 1 | Atharva Patil et al., 2025 | AI-Mail Management System: A Review | AI, NLP, LLM-based email automation with transformers | Lacks prioritization, reply detection |
| 2 | Sudara TSM et al., 2025 | AI-Powered Email Summarization and Assistant System for Internship and Job Offer Management using LLMs | LLM-based summarization, classification, RAG chatbot, semantic matching | Domain-specific, lacks prioritization, limited automation |
| 3 | Kukatla Sai Bharavi et al., 2025 | A Dual Module Approach for High Accuracy Phishing Detection and Email Prioritization using NLP and Machine Learning | NLP, machine learning, phishing detection, rule-based prioritization | Rule-based, lacks context understanding, no summarization or automation |
| 4 | Yusuke Miura et al., 2025 | Understanding and Supporting Formal Email Exchange By Answering AI Generated Questions | Question-answering system using AI for email comprehension | No prioritization, automation, replies, limited practical usability |
| 5 | Mahira Kirmani et al., 2023 | ShortMail: An Email Summarizer System Using Semantic Models and BERT | BERT, semantic models, clustering, summarization | No prioritization, replies, attachments, personalization, limited integration |
| 6 | Benjamin Towle and Ke Zhou, 2023 | End-to-End Autoregressive Retrieval via Bootstrapping for Smart Reply Systems | Autoregressive retrieval, bootstrapping, reply system | Only replies, no prioritization, summarization, personalization, integration |

---

## ⚔️ Existing vs Proposed System

| Existing System | Proposed System (MailMind) | Motivation / Methodology |
|----------------|---------------------------|--------------------------|
| Basic reply suggestion mechanisms | Smart draft response generation | Reduces response time and user effort |
| Cannot identify urgent or high-importance emails | AI-based email prioritization | Highlights urgent and high-priority emails instantly |
| No attachment analysis (PDFs, images, files) | Attachment analysis (PDF, DOCX, Excel, images) | Extracts critical information hidden in attachments |
| No reply-requirement detection | Reply-requirement detection | Ensures no important email is left unanswered |
| No direct Gmail API integration | Direct Gmail API integration (OAuth) | Enables secure, real-time inbox synchronization |
| High manual intervention | Interactive dashboard and chat interface | Improves usability and email insights |

---

## 🛠️ System Requirements

### Hardware Requirements

| Component | Requirement |
|-----------|-------------|
| System | Laptop/PC with minimum 8GB RAM (16GB recommended) |
| Processor | Intel i5 or higher for smooth AI processing |
| Storage | Minimum 256GB SSD (512GB recommended) |
| Internet | High-speed connection for API and LLM access |

### Software Requirements

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| AI/NLP Model | LLM (Gemini) |
| Email Integration | Gmail API |
| Database | SQLite |
| Development Tools | VS Code |

---

## 🏗️ System Architecture

> The system integrates Gmail API with an AI pipeline that handles email fetching, prioritization, summarization, reply generation, and attachment analysis — all served through a Streamlit UI.

---

## 🧩 Modules

1. **Integration and Authentication Module** — OAuth-based Gmail API connection
2. **Gmail Email Fetching and Database Storage** — Retrieves and stores emails in SQLite
3. **Reply Management System** — Detects reply needs and generates smart drafts
4. **Advanced Attachment Handling Module** — Parses PDFs, DOCX, Excel, and images
5. **Streamlit UI Module** — Interactive dashboard and chat interface

---

## ✅ Testing & Validation

- ✔️ Summaries were clear and easy to understand
- ✔️ Generated replies were contextually relevant
- ✔️ Gmail API and AI integration worked without errors
- ✔️ **Overall result:** System performs reliably in real-world scenarios

---

## 📊 Performance Analysis

| Metric | Result |
|--------|--------|
| Email reading time | Significantly reduced |
| Insight delivery | Quick through smart summaries |
| Email load handling | Moderate load handled smoothly |
| Processing latency | Minor delay due to AI inference |
| Overall efficiency | Practical and efficient solution |

---

## 🔮 Conclusion & Future Work

MailMind efficiently manages large volumes of emails using AI and rule-based techniques. It classifies, summarizes, and generates smart replies, improving productivity and response time through a user-friendly Streamlit interface.

### Future Scope

- 📱 Mobile app development
- 🌐 Multilingual support
- 🧠 Personalized user features
- 🔗 Integration with Microsoft Outlook
- ⏰ Smart follow-up reminders

---

## 📖 References

1. R. Radia, "Email Overload Statistics," 2015.
2. J. Johns et al., "Email Prioritization Using Machine Learning," *Journal of Emerging Technologies and Innovative Research (JETIR)*, 2020.
3. "Building AI Email Assistants with LLMs," DEV Community, 2025.
4. "Gmail AI Inbox Prioritization," Mailbird, 2026.
5. N. Sharma, "MailMind Project Specification," 2026.
6. "AI-Mail Management System: A Review," 2025.

---

## 🔗 Links

| Resource | Link |
|----------|------|
| 🚀 Live Demo | [mailmind-webapp.streamlit.app](https://mailmind-webapp.streamlit.app/) |
| 💻 GitHub Repository | [KaviyaSM/MailMind_webapp](https://github.com/KaviyaSM/MailMind_webapp.git) |
| 🎥 Implementation Video | [Google Drive](https://drive.google.com/file/d/1rrTdhRw0MUk-j0PXEBH-oJ8nKsmGrMqm/view?usp=drive_link) |
| 📄 Conference Paper | [Google Drive](https://drive.google.com/file/d/1MsqqhwVA2coV4LteFlj3BnkBxaTHDXMH/view?usp=drive_link) |

---

*Department of Artificial Intelligence & Data Science — April 2026*
