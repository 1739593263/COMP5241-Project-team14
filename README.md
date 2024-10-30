# COMP5241-Project-team14

## Statement
- GPT Wrapper:
Currently there are Generative-AIs that could rate how good a CV is, which is basically one-way and too generalized.
https://www.kickresume.com/en/

- Feature/Description:
  <p>
     In our demo program, the employer can [type out their requirement] of the job post(eg. working exp, role & duty, achievement & award, preferable skills, personality etc ). Then the AI can look up a batch of CV to match-up those     requirements and generate a [summary] of each applicant and give a [ranking] or [rate pass/fail] among those applicants. Nevertheless, we can allow employers to [set weighting for rating]. Like to set rating based on 30% work exp, 30% to that applier match with the company's vision, 40% in technique skill.
  </p> 
  <p>
    Employees can create CVs on this website for themselves. The resume’s writing can be helped by the AI modal, competing for more favor from interviewees. The main features include more proficient CV format, CV rating, and content recommendation. 
(a possible function) Interviewing simulator. According to the uploaded  CV, generating questions for employee and rating their answers.
  </p>
  
- How generative-AI enhance the software product and bring values to the users:
  <p>
    There is generative AI to help people write better CVs. But when everyone uses AI to write a good CV then what distinguishes between how good of the candidates themselves are based on the content, because an AI cannot change how the person has been. Every person has different skills , abilities , personality and experiences. HR can no longer filter the candidate by how good a CV is, now they need to filter out based on how good that person is, which increases the time and effort for them to look at the CV and requires more decision making on hiring candidates. Then there is a need for employers to acquire a system to better and faster filter out the employee that they are looking for based on the context of their job post and the content from the candidate.
  </p>
  
- UI
  1. Drop-box for putting the CV file
  2. input text area for typing the job requirement & detail
  3. Slider to modify rating weight base on pre-defined preferences (work exp, skill, academic)
  4. Option for select between evaluation mechanism (applicant ranking/score)

- Program
  1. Maybe need OCR to scan the CV (we can only accept microsoft word format, then we can get the text directly, then no need OCR)
  2. Logic on compare each candidate’s CV to job post content
  3. Logic on compare among the candidates
  4. Logic on how to batch handle CV file data and deliver a readable format to AI
  5. Logic on how to output the summary/ recommendation reason on a preferred candidate 

- Work allocation
  + Frontend/UI
  + Backend
  + Prompting-Engineering
  + Data-Engineering (Provide the data of the CV for demo)
  + Presentor/Tester/Repo manage


## Project environment
- Streamlit
- Java/Python (one of two)
- SqlLite

## Project Plan
  ### before Week 8
  + Create a repo in github.
  + Draft 1-2 CV per person in pdf. (related to IT field)
  + Research on OCR library or other methods to extract data from CV.
    + Reference: LangChain https://www.youtube.com/watch?v=U3Qz5l3yG4c&list=PL2fGiugrNooiIOPokp4tCZ71kVOdjBcsu&index=10
  + Research on how to connect DB by python. (use SQLite?  Or no DB by just reading data from a csv file?)
  + Think of the UI, streamlit.
    + UI Prototype (Only include minimal & necessary feature): https://www.figma.com/design/EZyO6SsJzaZrr9vjiJi2SB/Comp5241-Project-UI-Prototype?node-id=0-1&t=7eT1cYblMbXBHbqV-1
  + Think of the Prompt
