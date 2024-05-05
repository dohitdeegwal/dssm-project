
# ATS.

Integerated OpenAi api's to extracts skills from jd & resume and return match rate & skills

### System Requriments:
- Ubuntu OS 20.04
- Python3.10



### Setup Process
1. Create virutal enviroment & Install dependency
    ```
    > python -m venv venv 

    or

    > python -m virtualenv venv

    > venv\Scripts\activate

    > pip install -r requirements.txt

    ```


2. Create .env file in project root
    ```command
    OPENAI_API_KEY=sk-......
    TEMPERATURE=0
    CHAT_MODEL=gpt-3.5-turbo
    ORIGINS=http://127.0.0.1:5137, http://localhost:5137

    ```

   
3. Run Fast api Application
  ```
  Dev mode :
  > uvicorn main:app --host 0.0.0.0 --port 5003 --reload

  Add more workers:
  > uvicorn main:app --host 0.0.0.0 --port 5000 --workers 4

  Default timeout is 30 secs:
  > uvicorn main:app --host 0.0.0.0 --port 5000 --workers 4 --timeout-keep-alive 600

  ```


4. Open Fast Api document
    ```
    Visit > http://127.0.0.1:5000/docs
    ```

## Features

- Resume relevance score  
- Query resumes

