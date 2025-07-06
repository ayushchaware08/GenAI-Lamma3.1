import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Load environment variables (finds .env file)
load_dotenv()


class Chain:
    # Initialize the LLM with Groq API key
    def __init__(self):
        self.llm = ChatGroq(
            model_name='deepseek-r1-distill-llama-70b',
            temperature=0,
            api_key=os.environ["GROQ_API_KEY"]
        )

    def extract_job(self, cleaned_text):
        # text extraction promt Template
        promt_extract = PromptTemplate.from_template(
            '''
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION
            The scraped text id from the carrer's page of a website.
            your job is to extract the job posting and return them in JSON format containing following keys: 'role', experience', 'skills', and 'description'.
            only return the valid JSON. make sure no other key present insise the key-value pair.
            ### VALID JSON (NO PREAMBLE):
            '''
        )
        # invoke chain
        chain_extract = promt_extract | self.llm
        res = chain_extract.invoke(input ={'page_data': cleaned_text}) # str output
        # parse the output
        try:
            json_parser = JsonOutputParser()
            json_res = json_parser.parse(res.content) # parsed into json
        except OutputParserException as e:
            raise ValueError(f"Failed to parse output: {e}")

        return json_res if isinstance(json_res, list) else [json_res]

    # another chain for email generation
    def generate_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            you are Ayush, a Software developer Engineer, working at some company. ayush, a passionate and curious learner diving deep into tech from the ground up. I started with C++ and problem-solving, and now I’m actively building full-stack AI web apps and exploring machine learning projects in NLP and computer vision. 
            I’m currently preparing for placements, with a strong focus on DSA, project development, and real-world impact through AI. I constantly seek opportunities to collaborate, learn, and grow in the tech ecosystem.
            ayush was tech co-lead of google developer group.
            Your job is to write a cold email to the recruter regarding the job mentioned above describing the capability of ayush in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase ScriboTech's portfolio: {link_list}
            Remember you are Ayush, SDE at ScriboTech.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            
            """
            )

        # invoke chain
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content  # return the generated email content


    
# check  api key 
if __name__ == "main":
    print(os.getenv("GROQ_API_KEY") or "API_KEY not found")
