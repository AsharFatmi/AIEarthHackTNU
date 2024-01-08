
from openai import OpenAI
from config import API_KEY
class gpt:
   
  def __init__(self):
      self.client = OpenAI(
        api_key=API_KEY,
      )
      
  def vagueFilter(self, Problem, Solution):

    completion = self.client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=[
        {"role": "system", 
          "content": "Hello GPT! Your task is to evaluate a project pitch in a detailed and structured manner. Please provide specific labels. Uinsufficient for a thorough evaluation.\
          Filtering Label: Assess as 'Vague' or 'Competent'.\
          Vague: Use this label if the pitch lacks sufficient detail to understand the specific problem or solution. Indicate that it cannot be evaluated against the given parameters, advising to consider it too vague and disregard it for further analysis.\
          Competent: Use this label if the pitch provides enough clarity and detail.\
          Assessment Label: Evaluate as 'Solves the Problem' or 'Does Not Solve the Problem'.\
          Solves the Problem: Assign this label if the solution statement directly and effectively addresses the problem statement.\
          Does Not Solve the Problem: Use this label if there is a disconnect between the problem and the proposed solution or if the solution is ineffective.\
          Output should only contain the assigned labels. Sample Format is shown below: \
          “[Vague or Competent Label]\
          [Solves the Problem or Does Not Solve the Problem]”"},
        
        {"role": "user", 
         "content": "Project Pitch Evaluation Framework:\
          Problem: {}\
          Solution: {}\
          Evaluation Parameters with Ratings and Labels:".format(Problem,Solution)
        }
      ]
    )

    story = completion.choices[0].message.content
    # print(story)
    return story
  
  
  def pitchAnalysis(self, Problem, Solution):

    completion = self.client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=[
        {"role": "system", 
          "content": "Hello GPT! Your task is to evaluate a project pitch comprehensively, providing both quantitative ratings and specific labels. When direct information is not available, use your knowledge to make educated assumptions. Clearly label the nature of each insight as 'Directly from Pitch', 'GPT-Generated Analysis', or 'Not Enough Information'. \
          For each parameter, provide a rating on a scale of 1 to 10 and relevant labels. If you make assumptions, label them as 'GPT-Generated Analysis'. Try to include as much quantitative analysis as possible from credible sources.\
          Problem and Market Need (Rating: ):\
          Evaluate the relevance and demand for this solution in the market.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Solution and Product Viability (Rating: ):\
          Assess the quality, uniqueness, and practicality of the solution.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Market Size and Growth Potential (Rating: ):\
          Estimate the size and growth trajectory of the target market.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Competitive Landscape and Positioning (Rating: ):\
          Analyze the competition and the project's strategic positioning.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Business Model and Monetization Strategy (Rating: ):\
          Examine the clarity and sustainability of the business model and revenue strategies.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Scalability (Rating: ):\
          Evaluate the potential for scalable growth.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Innovation and Technology (Rating: ):\
          Assess the level of technological innovation and advancement.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Team Competence and Experience (Rating: ):\
          Analyze the expertise and experience of the founding team.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Customer Acquisition and Retention Strategy (Rating: ):\
          Review the effectiveness of plans for customer acquisition and retention.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Financial Projections and Health (Rating: ):\
          Check the realism of financial projections, including revenue, cost structure, and profitability.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Traction and Proof of Concept (Rating: ):\
          Evaluate market traction, customer feedback, and proof of concept.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Investment Terms and Valuation (Rating: ):\
          Assess the fairness and attractiveness of investment terms and company valuation.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Legal and Regulatory Compliance (Rating: ):\
          Evaluate compliance with relevant legal and regulatory frameworks.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Risk Assessment (Rating: ):\
          Identify and mitigate potential risks.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Exit Strategy (Rating: ):\
          Assess the clarity and feasibility of the exit strategy for investors.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Sustainability and Environmental Impact (Rating: ):\
          Evaluate environmental sustainability, including waste reduction and resource efficiency.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Social Impact (Rating: ):\
          Assess the social responsibility and ethical impact of the business.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Return on Equity (ROE) (Rating: ):\
          Estimate the potential for high ROE, indicating efficient capital utilization.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Future Growth Potential (Rating: ):\
          Evaluate prospects and strategies for future growth.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Strategic Fit and Synergies (Rating: ):\
          Assess alignment with investor's strategic goals and potential for synergies.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Brand and Reputation Impact (Rating: ):\
          Evaluate potential impact on the investor's brand and reputation.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Cultural Fit (Rating: ):\
          Assess compatibility with the investor's cultural values and ethics.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Innovation Sourcing and Technological Synergy (Rating: ):\
          (For corporate investors) Evaluate potential for sourcing innovation and technology.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Resilience and Adaptability (Rating: ):\
          Assess ability to adapt to market changes and challenges.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Governance and Ethical Practices (Rating: ):\
          Evaluate the quality of governance and ethical conduct.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Circular Economy Principles (Rating: ):\
          Assess integration of circular economy principles in business operations.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Climatic Condition Resilience (Rating: ):\
          Evaluate the resilience of the business model to climatic and environmental changes.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Carbon Footprint and Climate Impact (Rating: ):\
          Assess the startup's carbon footprint and overall climate impact.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Carbon Emission Saving Compared to Existing Solutions (Rating: ):\
          Assess how the startup's solution impacts carbon emissions compared to current solutions.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Cost and Time Saving Due to Circular Economy (Rating: ):\
          Evaluate cost and time savings achieved through circular economy practices.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Type of Circular Economy and Percentage of Circular Economy within the Solution (Rating: ):\
          Identify the type of circular economy model used and its extent within the solution.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Resource Efficiency and Optimization:\
          Assess how efficiently the project uses resources and minimizes waste.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Life Cycle Assessment (LCA):\
          Evaluate the environmental impact of the product or service throughout its entire lifecycle.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Energy Efficiency and Renewable Energy Utilization:\
          Assess the energy efficiency of the project and its integration of renewable energy sources.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Material Sourcing and Traceability:\
          Examine the sourcing of materials and how traceable they are in terms of sustainability.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Biodiversity Impact:\
          Evaluate the impact of the project on biodiversity and natural habitats.\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Additional Labels:\
          Industry: [Label the industry or industries the project impacts]\
          Business Model Type: [Identify the type of business model proposed]\
          Maturity Level: [Assess and label as Early Idea, Developing Concept, Prototype, Market-Ready]\
          Authenticity: [Label as Genuine Idea or Potential Spam]\
          Technology Level: [Label as Existing, Realistic, Proven, Optimistic, Unrealistic, Too Early]\
          Circular Economy Inclusion: [Indicate if the project includes circular economy principles]\
          Type of Circular Economy Model: [Label the specific type of circular economy model, if applicable]\
          Moonshot: [Indicate if the project is a moonshot idea or not]\
          Existing References\
          Provide a list of companies and one line description about the companies that does same or similar work as the idea.\
          Final Summary:\
          Provide a conclusive summary, incorporating ratings, labels, and insights from the analysis.\
          Highlight strengths, areas for improvement, overall potential, and any areas lacking sufficient information.\
          Summarize the overall potential of the project based on the ratings, labels, and insights provided.\
          This evaluation should be detailed and nuanced, utilizing both the provided pitch information and GPT-generated insights to offer a comprehensive analysis with clear labels and assumptions.\
          At the end of your analysis for each parameter, please provide the response in a structured, table-friendly format. Follow this template for each parameter:\
          Parameter Name: [Name of the Parameter]\
          Rating: [Numerical Rating or 'Not Enough Information']\
          Label: [Directly from Pitch / GPT-Generated Analysis / Not Enough Information]\
          Insight: [Brief insight or assumption]\
          Source: [Source of the Insight (if applicable)]\
          This format should be adhered to consistently for all parameters. The structured output will enable us to easily parse and export the data into a table for further analysis and presentation.\
          After the Summary provide: \
          Why it is a good project to pursue: [Include quantifiable data and other information which makes this a good project to shortlist]\
          Potential risk and red flags: [Include quantifiable data, threats and risks associated with pursuing the idea]\
          Total Score from summation of the parameter\
          Example of Structured Output:\
          Parameter Name: Market Size and Growth Potential\
          Rating: 8\
          Label: GPT-Generated Analysis\
          Insight: Based on industry trends and comparative market analysis, the projected market size is estimated to grow by 15% annually over the next five years.\
          Source: Industry Data and Trends Analysis\
          Ensure that the final summary and existing reference is also concise and follows a similar structured format, summarizing key points and overall potential. It should also include a summary of the problem and solution as provided by the initial input."},
        
        {"role": "user", 
         "content": "Project Pitch Evaluation Framework:\
          Problem: {}\
          Solution: {}\
          Evaluation Parameters with Ratings and Labels:".format(Problem,Solution)
        }
      ]
    )

    story = completion.choices[0].message.content
    # print(story)
    with open("openAIresult.txt", 'w') as file:
      # Write the text to the file
      file.write(story)
    return story