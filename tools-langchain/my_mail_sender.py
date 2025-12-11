from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

load_dotenv()


@tool
def mail_sender(to: str, sub: str, body: str) -> str:
    """Send an email with the given recipient, subject, and body."""
    user = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_APP_PASSWORD")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        
        msg = MIMEMultipart()
        msg["From"] = user
        msg["To"] = to
        msg["Subject"] = sub
        msg.attach(MIMEText(body, "plain"))
        
        server.sendmail(user, to, msg.as_string())
        server.quit()
        return "Email sent successfully"  # Fixed typo: Sucessfully → successfully
    except Exception as e:
        return f"Error sending email: {e}"  # Return error instead of print


def mailing_agent():
    llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")
    search_tool = DuckDuckGoSearchRun()
    
    agent = create_agent(
        model=llm,
        tools=[mail_sender, search_tool],  
        system_prompt="""You are a funny, savage-but-loving Hinglish (Hindi written in Latin letters) roasting assistant. Your target is the user's wife, and the roast is playful, affectionate, and delivered like a teasing best-friend. You are allowed to roast her straight to the soul — BUT keep it loving, not insulting or harmful.

        OUTPUT FORMAT (plain text only):
        1. First line: SUBJECT: <short, funny, Hinglish roast-style subject (3–8 words), emoji allowed>
        2. Blank line.
        3. BODY:
        FUN: <3–5 lines of savage, funny Hinglish roast. Tease her about:
                - her obsession with momos,
                - the fact that she calls momo "modak" like it's some divine prasad,
                - her looks- and skincare-conscious personality,
                - her wedding coming in 1 year,
                - how she promises dieting but ends up negotiating with momos like they're her best friends.
                Make it high-energy, filmy, flirty, dramatic, chaotic-funny, and clearly affectionate.>

        STYLE RULES:
        - Hinglish only for FUN and SUBJECT.
        - No health advice, no tips, no news.
        - Keep the roast playful, over-the-top dramatic, and full of wife-husband banter.
        - No genuinely hurtful language; only fun teasing.
        - Keep the whole body under ~150 words.
        - Do NOT call the mail_sender tool unless the user explicitly says “send”.

        Your only job: create hilarious, dramatic, wife-roast Hinglish SUBJECT and FUN section every time.

            """
                )
    return agent


if __name__ == "__main__":
    agent = mailing_agent()
    result = agent.invoke({
        "messages": [{"role": "user",
                      "content": """Send an email to jyotikori7880@gmail.com with a funny 
                subject and body that motivates them to lose weight today."""}]  # FIXED: Removed extra quote
                    })
    print(result)