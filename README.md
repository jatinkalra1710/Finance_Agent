# 🏦 AI Fund Strategy Desk: Multi-Agent Equity Research Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google_Gemini-Flash-00A4EF?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📖 Table of Contents
- [Overview](#-overview)
- [Application Showcase](#-application-showcase)
- [System Architecture & AI Crew](#-system-architecture--ai-crew)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Getting Started (Local Installation)](#-getting-started-local-installation)
- [Configuration & API Keys](#-configuration--api-keys)
- [Usage Guide](#-usage-guide)
- [Cloud Deployment](#-cloud-deployment)
- [Future Roadmap](#-future-roadmap)
- [Legal & Compliance Disclaimer](#-legal--compliance-disclaimer)

---

## 🔎 Overview

The **AI Hedge Fund Strategy Desk** is an advanced, open-source web application designed to democratize institutional-grade financial analysis. Built specifically for the Indian equity market (NSE/BSE), this tool leverages the power of Large Language Models (LLMs) and multi-agent orchestration to generate real-time, comprehensive investment memorandums in seconds. 

Whether you are a retail investor looking to understand market sentiment, a developer exploring the capabilities of multi-agent AI systems, or a finance enthusiast studying risk assessment, this repository serves as a practical, deployable blueprint for integrating real-time web scraping, financial APIs, and autonomous AI agents into a seamless web application.

Instead of relying on a single, generic AI prompt, this application mimics a real-world hedge fund strategy desk. It orchestrates a specialized crew of four autonomous AI agents—a Researcher, a Sentiment Analyst, a Risk Officer, and a Lead Analyst—who collaborate sequentially to produce a meticulously formatted, professional executive summary based on the absolute latest market data.

---

## 📸 Application Showcase

> **Note to Developers:** The images below are placeholders. To update them, place your actual screenshots in an `assets` folder within this repository and update the file paths.

### The Analyst Dashboard
<div align="center">
  <img width="1760" height="899" alt="image" src="https://github.com/user-attachments/assets/f005e34c-bbf3-466a-ae49-c27d1aa58054" alt="App UI Dashboard" width="900"/>
  <p><i>A clean, institutional-grade Streamlit interface with dynamic ticker lookup and session-based rate limiting.</i></p>
</div>

### The Generated Investment Memo
<div align="center">
  <img src="https://via.placeholder.com/900x500/1e1e1e/ffffff.png?text=Memo+Screenshot:+Executive+Summary,+Risk+Assessment,+and+Data" alt="Generated Report" width="900"/>
  <p><i>The final output: A professionally formatted Markdown document detailing pricing, sentiment, and macroeconomic risks.</i></p>
</div>

---

## 🧠 System Architecture & AI Crew

This application is powered by **CrewAI**, which allows multiple AI personas to share context and execute tasks in a defined sequence. The workflow is entirely deterministic and relies on real-time data injection.

### The 4-Agent Workflow:

1. **🕵️‍♂️ The Senior Market Researcher:**
   * **Role:** Data Aggregation.
   * **Tools:** `yfinance` for live stock prices/market caps, and `Tavily API` for web scraping.
   * **Task:** Bypasses LLM training cutoffs by fetching the exact stock price as of *today* and scraping the web for the 5 most relevant news articles published in the last 24-48 hours.

2. **📈 The Market Sentiment Analyst:**
   * **Role:** Behavioral Economics.
   * **Task:** Reads the raw data dossier compiled by the Researcher. Analyzes the tone of the news cycle to determine if the prevailing market psychology for the asset is Bullish, Bearish, or Neutral.

3. **⚖️ The Chief Risk Officer:**
   * **Role:** Downside Protection.
   * **Task:** Operates with a highly cautious persona. Reviews the asset against current events to identify 3 major risks (e.g., changing government regulations, macroeconomic inflation headwinds, or sector-specific competition).

4. **💼 The Lead Financial Analyst:**
   * **Role:** Synthesis and Reporting.
   * **Task:** Takes the outputs from the first three agents and drafts a cohesive, professional "Executive Investment Memo" formatted in Indian Rupees (₹), ensuring institutional tone and structure.

---

## ✨ Key Features

* **Real-Time Data Injection:** AI agents are actively prevented from "hallucinating" old data by forcefully injecting `datetime.now()` and live `yfinance` metrics into their system prompts.
* **Resilient Tooling:** Built-in fallback logic ensures that if Yahoo Finance blocks the connection due to rate limits (HTTP 429), the agents automatically pivot to searching Google/Tavily for the live price.
* **Dynamic Ticker Lookup:** Users aren't required to memorize complex Yahoo Finance symbols. The UI provides a curated list of top Indian equities and a direct link to a global ticker lookup directory for custom inputs.
* **Session-State Rate Limiting:** Includes built-in quota management limiting users to 2 reports per day to prevent API exhaustion and manage cloud costs.
* **Compliance-First UI:** Automatically renders strict legal and financial disclaimers on every generated report.

---

## 💻 Technology Stack

* **Frontend Framework:** [Streamlit](https://streamlit.io/)
* **AI Orchestration:** [CrewAI](https://crewai.com/)
* **Large Language Model:** Google Gemini 1.5 Flash (via `langchain-google-genai`)
* **Search / Scraping API:** [Tavily Search API](https://tavily.com/)
* **Financial Data:** `yfinance`

Gemini said
Markdown
# 🏦 AI Hedge Fund Strategy Desk: Multi-Agent Equity Research Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google_Gemini-Flash-00A4EF?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📖 Table of Contents
- [Overview](#-overview)
- [Application Showcase](#-application-showcase)
- [System Architecture & AI Crew](#-system-architecture--ai-crew)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Getting Started (Local Installation)](#-getting-started-local-installation)
- [Configuration & API Keys](#-configuration--api-keys)
- [Usage Guide](#-usage-guide)
- [Cloud Deployment](#-cloud-deployment)
- [Future Roadmap](#-future-roadmap)
- [Legal & Compliance Disclaimer](#-legal--compliance-disclaimer)

---

## 🔎 Overview

The **AI Hedge Fund Strategy Desk** is an advanced, open-source web application designed to democratize institutional-grade financial analysis. Built specifically for the Indian equity market (NSE/BSE), this tool leverages the power of Large Language Models (LLMs) and multi-agent orchestration to generate real-time, comprehensive investment memorandums in seconds. 

Whether you are a retail investor looking to understand market sentiment, a developer exploring the capabilities of multi-agent AI systems, or a finance enthusiast studying risk assessment, this repository serves as a practical, deployable blueprint for integrating real-time web scraping, financial APIs, and autonomous AI agents into a seamless web application.

Instead of relying on a single, generic AI prompt, this application mimics a real-world hedge fund strategy desk. It orchestrates a specialized crew of four autonomous AI agents—a Researcher, a Sentiment Analyst, a Risk Officer, and a Lead Analyst—who collaborate sequentially to produce a meticulously formatted, professional executive summary based on the absolute latest market data.

---

## 📸 Application Showcase

> **Note to Developers:** The images below are placeholders. To update them, place your actual screenshots in an `assets` folder within this repository and update the file paths.

### The Analyst Dashboard
<div align="center">
  <img src="https://via.placeholder.com/900x500/1e1e1e/ffffff.png?text=UI+Screenshot:+Dashboard,+Dropdowns,+and+Execution+Panel" alt="App UI Dashboard" width="900"/>
  <p><i>A clean, institutional-grade Streamlit interface with dynamic ticker lookup and session-based rate limiting.</i></p>
</div>

### The Generated Investment Memo
<div align="center">
  <img src="https://via.placeholder.com/900x500/1e1e1e/ffffff.png?text=Memo+Screenshot:+Executive+Summary,+Risk+Assessment,+and+Data" alt="Generated Report" width="900"/>
  <p><i>The final output: A professionally formatted Markdown document detailing pricing, sentiment, and macroeconomic risks.</i></p>
</div>

---

## 🧠 System Architecture & AI Crew

This application is powered by **CrewAI**, which allows multiple AI personas to share context and execute tasks in a defined sequence. The workflow is entirely deterministic and relies on real-time data injection.

### The 4-Agent Workflow:

1. **🕵️‍♂️ The Senior Market Researcher:**
   * **Role:** Data Aggregation.
   * **Tools:** `yfinance` for live stock prices/market caps, and `Tavily API` for web scraping.
   * **Task:** Bypasses LLM training cutoffs by fetching the exact stock price as of *today* and scraping the web for the 5 most relevant news articles published in the last 24-48 hours.

2. **📈 The Market Sentiment Analyst:**
   * **Role:** Behavioral Economics.
   * **Task:** Reads the raw data dossier compiled by the Researcher. Analyzes the tone of the news cycle to determine if the prevailing market psychology for the asset is Bullish, Bearish, or Neutral.

3. **⚖️ The Chief Risk Officer:**
   * **Role:** Downside Protection.
   * **Task:** Operates with a highly cautious persona. Reviews the asset against current events to identify 3 major risks (e.g., changing government regulations, macroeconomic inflation headwinds, or sector-specific competition).

4. **💼 The Lead Financial Analyst:**
   * **Role:** Synthesis and Reporting.
   * **Task:** Takes the outputs from the first three agents and drafts a cohesive, professional "Executive Investment Memo" formatted in Indian Rupees (₹), ensuring institutional tone and structure.

---

## ✨ Key Features

* **Real-Time Data Injection:** AI agents are actively prevented from "hallucinating" old data by forcefully injecting `datetime.now()` and live `yfinance` metrics into their system prompts.
* **Resilient Tooling:** Built-in fallback logic ensures that if Yahoo Finance blocks the connection due to rate limits (HTTP 429), the agents automatically pivot to searching Google/Tavily for the live price.
* **Dynamic Ticker Lookup:** Users aren't required to memorize complex Yahoo Finance symbols. The UI provides a curated list of top Indian equities and a direct link to a global ticker lookup directory for custom inputs.
* **Session-State Rate Limiting:** Includes built-in quota management limiting users to 2 reports per day to prevent API exhaustion and manage cloud costs.
* **Compliance-First UI:** Automatically renders strict legal and financial disclaimers on every generated report.

---

## 💻 Technology Stack

* **Frontend Framework:** [Streamlit](https://streamlit.io/)
* **AI Orchestration:** [CrewAI](https://crewai.com/)
* **Large Language Model:** Google Gemini 1.5 Flash (via `langchain-google-genai`)
* **Search / Scraping API:** [Tavily Search API](https://tavily.com/)
* **Financial Data:** `yfinance`

---


⚠️ Legal & Compliance Disclaimer
This application and its source code are strictly for educational, demonstrative, and software development purposes.

**Not Financial Advice:** The information, reports, and sentiment analysis generated by this application do not constitute a recommendation, solicitation, or offer to buy or sell any securities or financial instruments.

**Regulatory Status:** The creators and contributors of this repository are NOT registered with the Securities and Exchange Board of India (SEBI), the SEC, or any other financial regulatory body as Investment Advisors, Research Analysts, or Portfolio Managers.

**AI Limitations:** The reports are synthesized by Artificial Intelligence. AI models are prone to hallucination, data misalignment, and logical errors. Real-time data fetched via APIs may be delayed or inaccurate.

**Market Risk:** Investments in the equity market are subject to severe market risks. Users should conduct their own independent due diligence and consult with a certified financial planner before making any investment decisions.
