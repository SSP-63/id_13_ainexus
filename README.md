# Student Feedback Analysis

## Project Overview
This project is a web application designed to analyze student feedback effectively using Natural Language Processing (NLP) techniques. It leverages Azure AI Text Analytics to perform sentiment analysis and visualizes the results in an intuitive interface. Users can upload feedback data in CSV format, and the application provides insights through sentiment distribution, keyword analysis, and word clouds.

## Deployment
The project is deployed on Streamlit and can be accessed at the following link:
https://feedbackais.streamlit.app/

## Features
- **Sentiment Analysis**: Classifies feedback into "Satisfactory," "Needs Improvement," and "Neutral."
- **Visualization**: Displays sentiment distribution via a pie chart and a corresponding table.
- **Keyword Analysis**: Generates word clouds for commonly occurring keywords in positive and negative feedback.
- **Easy to Use**: Upload your feedback CSV file and get results instantly.

## Usage Instructions
1. Visit the deployed application:https://feedbackais.streamlit.app/
2. Upload a CSV file containing feedback data (Given in the repo "demo1.csv" use it). The CSV file should have only two columns: **number** and **feedback**, as the current project is configured to process these two columns using the pandas library.
3. View sentiment analysis results, keyword insights, and visualizations.

## Technologies Used
- **Streamlit**: Front-end interface.
- **Azure Text Analytics API**: Sentiment analysis backend.
- **Matplotlib**: Data visualization.
- **WordCloud**: Word cloud generation.
- **Python**: Application logic and data processing.

## How It Works
1. **Data Input**: Upload a CSV file where the feedback text is in the second column.
2. **Analysis**: The Azure Text Analytics API processes the feedback to classify sentiment and extract keywords.
3. **Visualization**: Results are displayed as a pie chart, table, and word clouds for better comprehension.

   ![image](https://github.com/user-attachments/assets/d454f36b-10d6-4e2c-a429-b9ed5e4710fc)


   ![Screenshot 2025-01-27 215318](https://github.com/user-attachments/assets/3f479bfd-0761-4151-a4b7-ff274f855531)


   ![image](https://github.com/user-attachments/assets/ba4972da-5c19-4733-8e0a-ee536e7cc5e1)


## Note
- This project is made by Shreyash Pawar and Ranveer Phakade as a problem statement in hackathon conducted by WCE MLSC community named HackAIBlitz.



