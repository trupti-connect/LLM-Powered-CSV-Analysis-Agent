# 🤖 LLM-Powered CSV Analysis Agent

An interactive AI-powered data analysis application that allows users to upload CSV files and analyze datasets using natural language questions. Built with **Python, Streamlit, LangChain, and Groq LLMs**, this application simplifies data exploration and helps users gain insights without writing complex code.

## 🚀 Project Overview

The LLM-Powered CSV Analysis Agent enables users to upload their own CSV datasets, explore data, ask questions in plain English, and generate visualizations through an interactive web interface.

It combines Large Language Models (LLMs) with Python data analysis libraries to make data analytics more accessible and efficient.

## ✨ Key Features

- 📂 **CSV File Upload:** Upload and analyze custom CSV datasets.
- 🤖 **AI-Powered Data Analysis:** Ask questions about your dataset using natural language.
- 📊 **Data Visualization:** Generate histograms, bar charts, box plots, scatter plots, and correlation heatmaps.
- 🔍 **Exploratory Data Analysis:** Explore dataset dimensions, columns, data types, and statistical summaries.
- 💬 **Natural Language Interaction:** Get data insights without manually writing SQL or Python queries.
- ⚡ **Interactive Dashboard:** Analyze datasets through a user-friendly Streamlit interface.
- 🧠 **LLM Integration:** Use Groq-hosted language models through LangChain.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| LangChain | LLM integration and agent workflow |
| LangChain Experimental | Pandas DataFrame agent |
| LangChain-Groq | Connect Groq models with LangChain |
| Tabulate | Formatted table output |
| Groq | LLM inference platform |

## 🏗️ Project Architecture

```text
User
  |
  v
Streamlit Web Application
  |
  v
CSV File Upload
  |
  v
Pandas DataFrame
  |
  +----------------------+
  |                      |
  v                      v
LLM-Powered Agent     Data Visualization
  |                      |
  v                      v
Groq LLM              Matplotlib / Seaborn
  |                      |
  v                      v
Natural Language      Charts and Graphs
Answers
  |
  v
Data Insights
```

## 📁 Project Structure

```text
LLM-Powered-CSV-Analysis-Agent/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/trupti-connect/LLM-Powered-CSV-Analysis-Agent.git
```

### 2. Navigate to the Project Folder

```bash
cd LLM-Powered-CSV-Analysis-Agent
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Groq API Key

Get your API key from [Groq Console](https://console.groq.com/).

Enter your API key in the application's sidebar when prompted. Keep your API key private and never commit it to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Example Use Cases

You can upload a CSV file and ask questions such as:

- How many rows and columns are present in this dataset?
- Display the first five records.
- Identify missing values in each column.
- Calculate the average, maximum, and minimum values.
- Which category has the highest sales?
- Identify correlations between numerical variables.
- Generate a histogram for a selected numerical column.
- Summarize the important insights from this dataset.

## 🔮 Future Enhancements

- Support for Excel and multiple file formats.
- Automated data cleaning and missing-value handling.
- Advanced statistical analysis.
- Predictive analytics and machine learning integration.
- Export analysis reports as PDF.
- Conversation history and downloadable insights.
- Deployment with secure API-key management.

## 👩‍💻 Author

**Trupti Choure**

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning | Microsoft Fabric

- **GitHub:** [trupti-connect](https://github.com/trupti-connect)
- **LinkedIn:** [Trupti Choure](https://www.linkedin.com/in/trupti-choure-7466aa402/)

---

⭐ If you find this project useful, consider giving the repository a star!
