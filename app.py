
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from groq import Groq
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent


# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="LLM-Powered CSV Analysis Agent",
    page_icon="🐣",
    layout="wide"
)

st.title("🐧 LLM-Powered CSV Analysis Agent")
st.caption("AI-powered data analysis using Groq + LangChain + Pandas")


# ---- SIDEBAR ----
st.sidebar.header("⚙️ Configuration")

api_key = st.sidebar.text_input(
    "1. Enter GROQ API Key",
    type="password"
)

uploaded_file = st.sidebar.file_uploader(
    "2. Upload your CSV file",
    type=["csv"]
)

temperature = st.sidebar.slider(
    "Model Temperature",
    0.0,
    1.0,
    0.0
)

st.sidebar.divider()

st.sidebar.info(
    "Powered by Qwen 3.8 27B through Groq."
)


# ---- MAIN CONTENT ----

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("CSV dataset uploaded successfully!")

        # Dataset overview
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Rows", df.shape[0])
        col2.metric("Total Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        tab1, tab2 = st.tabs([
            "💬 Chat with Data",
            "🎨 AI Visualizations"
        ])

        # ---- INITIALIZE MODEL ----
        if api_key:

            llm = ChatGroq(
                model="qwen/qwen3.8-27b",
                temperature=temperature,
                api_key=api_key
            )

            agent = create_pandas_dataframe_agent(
                llm=llm,
                df=df,
                verbose=True,
                allow_dangerous_code=True
            )

            # ---- TAB 1: CHAT WITH DATA ----
            with tab1:

                st.subheader("📄 Dataset Preview")

                st.dataframe(df.head(10), use_container_width=True)

                st.divider()

                user_input = st.text_area(
                    "🗨️ Ask a question about your dataset:",
                    placeholder="Example: What is the average sales value?"
                )

                if st.button("Generate Answer"):

                    if not user_input.strip():

                        st.warning("Please enter your question.")

                    else:

                        try:
                            with st.spinner("🤖 Analyzing your dataset..."):

                                response = agent.invoke({
                                    "input": user_input
                                })

                            st.success("Analysis completed!")

                            st.write(response["output"])

                        except Exception as e:

                            st.error(f"Agent Error: {str(e)}")


            # ---- TAB 2: VISUALIZATIONS ----
            with tab2:

                st.subheader("📊 Dataset Visualizations")

                st.write(
                    "Explore your dataset using charts and graphs."
                )

                viz_type = st.selectbox(
                    "Select visualization",
                    [
                        "Histogram",
                        "Correlation Heatmap",
                        "Bar Chart",
                        "Box Plot",
                        "Scatter Plot"
                    ]
                )

                numeric_columns = df.select_dtypes(
                    include="number"
                ).columns.tolist()

                all_columns = df.columns.tolist()

                if viz_type == "Histogram":

                    column = st.selectbox(
                        "Select numerical column",
                        numeric_columns
                    ) if numeric_columns else None

                    if st.button("Generate Histogram") and column:

                        fig, ax = plt.subplots(figsize=(9, 5))

                        sns.histplot(
                            data=df,
                            x=column,
                            kde=True,
                            ax=ax
                        )

                        ax.set_title(f"Distribution of {column}")

                        st.pyplot(fig)
                        plt.close(fig)

                elif viz_type == "Correlation Heatmap":

                    if st.button("Generate Heatmap"):

                        fig, ax = plt.subplots(figsize=(10, 6))

                        sns.heatmap(
                            df.select_dtypes(include="number").corr(),
                            annot=True,
                            cmap="coolwarm",
                            ax=ax
                        )

                        ax.set_title("Correlation Matrix")

                        st.pyplot(fig)
                        plt.close(fig)

                elif viz_type == "Bar Chart":

                    column = st.selectbox(
                        "Select categorical column",
                        all_columns
                    )

                    if st.button("Generate Bar Chart"):

                        fig, ax = plt.subplots(figsize=(10, 5))

                        df[column].value_counts().head(10).plot(
                            kind="bar",
                            ax=ax
                        )

                        ax.set_title(f"Top 10 Values: {column}")

                        st.pyplot(fig)
                        plt.close(fig)

                elif viz_type == "Box Plot":

                    column = st.selectbox(
                        "Select numerical column",
                        numeric_columns
                    ) if numeric_columns else None

                    if st.button("Generate Box Plot") and column:

                        fig, ax = plt.subplots(figsize=(9, 5))

                        sns.boxplot(
                            data=df,
                            y=column,
                            ax=ax
                        )

                        ax.set_title(f"Outlier Analysis: {column}")

                        st.pyplot(fig)
                        plt.close(fig)

                elif viz_type == "Scatter Plot":

                    if len(numeric_columns) >= 2:

                        x_col = st.selectbox(
                            "Select X-axis",
                            numeric_columns
                        )

                        y_col = st.selectbox(
                            "Select Y-axis",
                            [c for c in numeric_columns if c != x_col]
                        )

                        if st.button("Generate Scatter Plot"):

                            fig, ax = plt.subplots(figsize=(9, 5))

                            sns.scatterplot(
                                data=df,
                                x=x_col,
                                y=y_col,
                                ax=ax
                            )

                            ax.set_title(f"{x_col} vs {y_col}")

                            st.pyplot(fig)
                            plt.close(fig)

                    else:
                        st.warning(
                            "At least two numerical columns are required."
                        )

        else:

            st.info("Enter your Groq API key in the sidebar to activate AI chat.")

    except Exception as e:

        st.error(f"Error loading dataset: {str(e)}")

else:

    st.info("👈 Please upload a CSV file in the sidebar to get started.")
