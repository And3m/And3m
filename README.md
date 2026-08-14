<!--
================================================================================
MAINTENANCE NOTES (not rendered on the profile page)

This is the And3m/And3m special repo -- this file IS the public GitHub profile.
Keep maintenance notes in comments like this one; anything outside a comment is
visible to recruiters.

SOURCE OF TRUTH
  About Me / Experience / Education mirror the resume (Vijay_Kumar_Andem_Resume,
  not stored in this repo). Update those three sections together when the resume
  changes -- do not let the claims drift apart.
  Only badge tools the resume or a linked repo actually backs. No aspirational icons.

HEADER BANNER
  Name and tagline live in the text= and desc= params of ALL THREE capsule-render
  URLs below (mobile / tablet / desktop fallback). Change all three, and keep the
  <img alt> in sync -- the name exists only inside the image, so alt text is what
  screen readers and search indexers see.
  Current tagline: "Senior Business Intelligence & Data Analyst | GenAI Applications"

SNAKE ANIMATION (footer)
  Must use raw.githubusercontent.com/And3m/And3m/output/...
  NOT github.com/And3m/And3m/blob/output/... -- blob URLs return an HTML page and
  render as a broken image. This was a live bug; do not "simplify" it back.

SOCIAL LINKS -- two locations must stay in sync
  1. Header badge row (flat-square: LinkedIn, Portfolio, Email, X, Views)
  2. Footer "Let's Talk" CTA (for-the-badge: LinkedIn, Email)

PROJECTS
  6 max, vertical card format: linked ### heading + one-sentence description +
  inline code tech tags. Overflow goes to the portfolio site.

THEME ("Midnight Blue")
  Stats github_dark_dimmed | streak github-dark-blue | typing #58A6FF
  Gradient customColorList=2,3,12,19,21
  All widgets support dark/light via <picture> + prefers-color-scheme.

LINE BREAKS
  Experience entries and the footer CTA use explicit <br>. A bare newline collapses
  in some renderers (VS Code preview) and turns the entries into run-on paragraphs.

WORKFLOWS (.github/workflows/)
  snake.yml      -- contribution snake, every 12h + push to main (paths-ignore set
                    so the 3d-contrib bot commit doesn't retrigger it)
  3d-contrib.yml -- 3D calendar, daily 1AM UTC, commits to profile-3d-contrib/
  REMOVED: update-readme.yml. It used jamesgeorge007/github-activity-readme, which
  requires START_SECTION:activity and END_SECTION:activity marker comments in this
  file (HTML comment delimiters around each -- they cannot be written literally
  here, since a nested close-comment would terminate this block early).
  Those markers were never present, so it failed on every daily run. If you want it
  back, add the markers AND the workflow together -- one without the other fails.

KNOWN FLAKINESS
  github-readme-stats and streak-stats run on shared public instances that
  rate-limit (429) under load. Blank cards for a few hours are upstream, not a
  config error. Self-hosting the stats card is the only real fix.

COMMIT CONVENTION
  feat: | fix: | update: | chore: | style:
================================================================================
-->

<div align="center">

<!-- Responsive Header Banner -->
<picture>
  <source media="(max-width: 768px)" srcset="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12,19,21&height=190&section=header&text=Vijay%20Kumar%20Andem&fontSize=30&animation=fadeIn&fontAlignY=36&desc=Senior%20BI%20%26%20Data%20Analyst%20%7C%20GenAI%20Applications&descAlignY=60&descAlign=50&descSize=12&fontColor=ffffff">
  <source media="(max-width: 1024px)" srcset="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12,19,21&height=200&section=header&text=Vijay%20Kumar%20Andem&fontSize=42&animation=fadeIn&fontAlignY=36&desc=Senior%20Business%20Intelligence%20%26%20Data%20Analyst%20%7C%20GenAI%20Applications&descAlignY=58&descAlign=50&descSize=14&fontColor=ffffff">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12,19,21&height=200&section=header&text=Vijay%20Kumar%20Andem&fontSize=52&animation=fadeIn&fontAlignY=36&desc=Senior%20Business%20Intelligence%20%26%20Data%20Analyst%20%7C%20GenAI%20Applications&descAlignY=58&descAlign=50&descSize=17&fontColor=ffffff" width="100%" alt="Vijay Kumar Andem — Senior Business Intelligence and Data Analyst, GenAI Applications" />
</picture>

<!-- Typing Animation -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&width=650&height=45&lines=13+Years+Turning+Data+Into+Decisions;Power+BI+%26+Tableau+for+Enterprise+Reporting;LangChain+%26+RAG+Apps+for+Business+Teams" alt="13 years turning data into decisions; Power BI and Tableau for enterprise reporting; LangChain and RAG apps for business teams" />

<br>

**Senior business intelligence and data analyst in Bengaluru, India — 13 years turning operational data into reporting that leadership acts on, now extending into applied generative AI.**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vijay-andem-b2092223/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=vercel&logoColor=white)](https://vijayandem.vercel.app)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:vijayandem@gmail.com)
[![X](https://img.shields.io/badge/X-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/vjandem)
![Views](https://komarev.com/ghpvc/?username=And3m&style=flat-square&color=1f6feb)

**Open to senior roles in business analysis, business intelligence, and AI solutions.**

</div>

---

## About Me

Thirteen years across FMCG, IT services, and healthcare consulting — Infosys, Indegene, IBM, and CavinKare. I work the full stack of the analyst's job: SQL and Python for preparation, Power BI and Tableau for delivery, and the stakeholder conversations that decide what is worth measuring in the first place.

The through-line across those roles is automation: cutting manual reporting effort by over 40% at CavinKare, replacing thousands of recurring weekly data pulls with Python at IBM, and shipping 50+ automated reports at Infosys. Since 2024 I have been extending that same instinct into generative AI — LangChain and RAG applications that let non-technical teams ask questions of business data in plain language, plus local-first tooling with Ollama for privacy-sensitive environments.

---

## Experience

**Business Analyst** · CavinKare · Mar 2022 — Dec 2023<br>
Built automated Power BI dashboards for campaign performance, marketing budget tracking, and ROI across the personal care portfolio, cutting manual reporting effort by over 40%. Analyzed Nielsen and Kantar syndicated data for market share and competitive movement, and presented predictive analysis directly to C-suite stakeholders.

**Marketing Analyst** · IBM · Jul 2016 — Mar 2022<br>
Designed and automated global marketing dashboards in Tableau and Cognos, tracking campaign performance, revenue pipeline, and business partner effectiveness across regions. Automated thousands of recurring weekly data pulls with Python, and built a self-service query application that let non-technical marketing teams retrieve business data without writing SQL.

**Reporting Analyst** · Indegene · Aug 2015 — May 2016<br>
Produced automated marketing and sales performance reporting for Pfizer North America, extracting and modeling large multi-source datasets on short turnaround.

**Data Analyst** · Infosys · Mar 2011 — Aug 2015<br>
Developed and automated 50+ reports and dashboards using SQL, VBA, Advanced Excel, and MS Access for the Income Tax Department's Centralized Processing Centre, translating compliance requirements into operational reporting.

---

## Tools and Technologies

<div align="center">

<img src="https://skillicons.dev/icons?i=python,mysql,postgres,sklearn,git,github,vscode,jupyter&perline=8&theme=dark" alt="Python, MySQL, PostgreSQL, scikit-learn, Git, GitHub, VS Code, Jupyter" />

<br><br>

**Business Intelligence**

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-F2C811?style=flat-square)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)
![IBM Cognos](https://img.shields.io/badge/IBM_Cognos-052FAD?style=flat-square&logo=ibm&logoColor=white)
![Excel](https://img.shields.io/badge/Advanced_Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white)

**Generative AI**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=chainlink&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-4B8BBE?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square)

**Data and Apps**

![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)
![IBM DB2](https://img.shields.io/badge/IBM_DB2-052FAD?style=flat-square&logo=ibm&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

</div>

---

## Featured Projects

### [GenAI for Analysts](https://github.com/And3m/genai-for-analysts)

10-project portfolio demonstrating practical generative AI applications from a business analytics perspective — covering LLM foundations, RAG systems, agentic workflows, fine-tuning, evaluation dashboards, and multimodal document intelligence.

`Python` `LangChain` `LangGraph` `LlamaIndex` `ChromaDB` `Streamlit` `RAG` `AI Agents`

---

### [MCP Data Analysis Toolkit](https://github.com/And3m/mcp-data-analysis-toolkit)

Model Context Protocol server for AI-powered data analysis. Enables LLM agents to discover and execute data processing tools through a standardized protocol interface.

`Python` `MCP` `AI Agents` `LLMs` `Protocol Buffers`

---

### [Interactive AI Chat Agent](https://github.com/And3m/chainlit-ollama-interactive-agent)

Locally-hosted conversational AI with real-time system monitoring, 2048-token responses, and built-in analytics commands. Runs 100% on-device with no external API dependencies.

`Python` `Chainlit` `Ollama` `Llama 3.2` `Real-time Analytics`

---

### [Coffee Shop Sales Dashboard](https://github.com/And3m/Coffee-Shop-Sales-Analysis-Dashboard-Streamlit-Pandas-Plotly) &nbsp; [![Live Demo](https://img.shields.io/badge/Live_Demo-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://coffee-shop-dashboard.streamlit.app)

Interactive Streamlit dashboard with KPIs, trend analysis, and Plotly visualizations for coffee shop sales performance.

`Streamlit` `Pandas` `Plotly` `Python`

---

### [Restaurant Ratings Analysis](https://github.com/And3m/Restaurant-Ratings-Analysis-PowerBI)

5-page Power BI dashboard exploring restaurant distribution across Mexico, consumer behavior patterns, and rating trends with geographic analysis.

`Power BI` `DAX` `Power Query` `Data Modeling`

---

### [LangChain Playbook](https://github.com/And3m/Langchain_playbook)

Comprehensive tutorial collection covering LangChain fundamentals through advanced implementations — chatbots, RAG systems, agents, and vector database integrations.

`Python` `LangChain` `OpenAI` `RAG` `Vector Databases`

---

<div align="center">

**More projects, live dashboards, and write-ups → [vijayandem.vercel.app](https://vijayandem.vercel.app)**

</div>

---

## Education and Certifications

**BSc in Mathematics, Statistics, and Computer Science** — Kakatiya University

**IBM** — Applied Data Science with Python (Level 2) · Machine Learning with Python (Level 1) · Data Science Foundations · Data Analysis with Python · Data Visualization with Python · Deep Learning Essentials · Accelerated Deep Learning with GPU · Agile Explorer

**Optimizely** — X Web Foundations

---

## GitHub Analytics

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=And3m&show_icons=true&theme=github_dark_dimmed&include_all_commits=true&count_private=true" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api?username=And3m&show_icons=true&theme=default&include_all_commits=true&count_private=true" />
  <img height="180" src="https://github-readme-stats.vercel.app/api?username=And3m&show_icons=true&theme=github_dark_dimmed&include_all_commits=true&count_private=true" alt="GitHub Stats" />
</picture>
&nbsp;
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=And3m&layout=compact&langs_count=8&theme=github_dark_dimmed" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=And3m&layout=compact&langs_count=8&theme=default" />
  <img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=And3m&layout=compact&langs_count=8&theme=github_dark_dimmed" alt="Top Languages" />
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=And3m&theme=github-dark-blue" />
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=And3m&theme=default" />
  <img src="https://streak-stats.demolab.com?user=And3m&theme=github-dark-blue" alt="GitHub Streak" />
</picture>

<br><br>

<!-- 3D Contribution Calendar (generated by GitHub Action) -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./profile-3d-contrib/profile-night-rainbow.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./profile-3d-contrib/profile-green-animate.svg" />
  <img src="./profile-3d-contrib/profile-night-rainbow.svg" alt="3D Contribution Calendar" width="100%" />
</picture>

</div>

---

<div align="center">

## Let's Talk

Open to senior roles in business analysis, business intelligence, and AI solutions.<br>
Based in Bengaluru, India — open to remote.

[![LinkedIn](https://img.shields.io/badge/Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vijay-andem-b2092223/)
[![Email](https://img.shields.io/badge/Send_an_Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:vijayandem@gmail.com)

<br>

<!-- Snake Animation -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/And3m/And3m/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/And3m/And3m/output/github-contribution-grid-snake.svg" />
  <img src="https://raw.githubusercontent.com/And3m/And3m/output/github-contribution-grid-snake-dark.svg" alt="Snake animation traversing the GitHub contribution grid" width="100%" />
</picture>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,3,12,19,21&height=80&section=footer" width="100%" alt="" />

</div>
