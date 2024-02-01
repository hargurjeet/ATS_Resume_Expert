# ATS_Resume_Expert

ATS_Resume_Expert is a data science application powered by Google Gemini Pro APIs and built using LangChain. It compares the job description of a job application against your resume and provides a score of match percentage. It also provides suggestions to improve your resume on keywords and areas.

## Requirements

To run this application, you will need:

- Python 3.8 or higher
- Google Gemini Pro API key
- LangChain library
- Other dependencies listed in requirements.txt

## Installation

To install this application, follow these steps:

- Clone this repository to your local machine
- Navigate to the project folder and create a virtual environment
- Activate the virtual environment and install the dependencies
- Set up your Google Gemini Pro API key as an environment variable
- Run the main.py script

## Usage

To use this application, you will need to:

- Provide a job description file in txt format
- Provide a resume file in pdf format
- Run the app.py script with the file paths as arguments
- Wait for the application to process the files and generate the output
- View the output file in the output folder, which will contain the match score and suggestions

## Example

Here is an example of how to run the application with sample files:

```
python main.py job_description.txt resume.pdf

The output file will look something like this:
Match score: 75%

Suggestions:

- Add more keywords related to data analysis, such as pandas, numpy, matplotlib, etc.
- Highlight your achievements and skills in bullet points
- Use active verbs and concise language
- Proofread your resume for spelling and grammar errors
``` 


## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
If you have any questions, feedback, or suggestions, feel free to contact me at gurjeet333@gmail.com.
