# 🎯Automated MCQ Generation: by Text/PDF - Langchain OpenAI LLM 🐦🔗

"
 Aims to automate the creation of multiple-choice questions (MCQs) from textual content or PDF documents. 
 Leveraging Langchain's Language Model (LLM), the project utilizes advanced natural language processing techniques to analyze provided text or documents, extract key information, and generate sets of MCQs. 
 This process streamlines the creation of assessment materials, aiding educators, content creators, or organizations in rapidly generating quiz-style questions from textual resources.
"


https://github.com/rohitdiwane/gen-mcq-openai/assets/140241900/7386406a-8eef-4033-af14-cf8e74fd8efc

## Features
- Upload text or PDF files as input.
- Generate a customizable number of MCQs (3-50).
- Specify the subject of the MCQs.
- Set the complexity level (e.g., Simple, Medium, Complex).
- View generated MCQs in a tabular format with a review.
- Token usage and cost estimation for OpenAI API calls.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd mcq_gen_project
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your web browser at `http://localhost:8501`.

3. Use the form to:
   - Upload a PDF or text file.
   - Specify the number of MCQs to generate.
   - Enter the subject.
   - Define the complexity level of the questions.

4. Click the **Create MCQs** button to generate the questions.

## File Structure

```
mcq_gen_project/
├── src/
│   ├── mcqgenrator/
│   │   ├── utils.py       # Utility functions for reading files and processing data
│   │   ├── mcqgenrator.py # Core MCQ generation logic
│   │   ├── logger.py      # Logging utilities
├── app.py                 # Streamlit application script
├── requirements.txt       # List of Python dependencies
├── .env                   # Environment variables (ignored by Git)
├── README.md              # Project documentation
```

## Dependencies
- **Python** 3.8+
- **Streamlit**
- **LangChain**
- **OpenAI**
- **pandas**
- **dotenv**

Install dependencies using `pip install -r requirements.txt`.

## Error Handling
The application handles errors gracefully and displays relevant error messages. If an issue occurs:
- Ensure that the uploaded file is in a supported format (PDF or text).
- Check your OpenAI API key in the `.env` file.
- Review the traceback logs for more details.

## API Cost Tracking
The application provides details on:
- Total tokens used
- Prompt tokens
- Completion tokens
- Total cost

These details are logged and displayed in the console during runtime.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.


