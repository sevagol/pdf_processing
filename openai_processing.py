from langchain.chat_models import ChatOpenAI
import json
from langchain.schema.messages import HumanMessage, SystemMessage
def image_captioning(img_base64):
    chat = ChatOpenAI(model="gpt-4-vision-preview",
                    max_tokens=3072, api_key=st.secrets.openai_key)

    msg = chat.invoke(
        [
            HumanMessage(
                content=[
                    {"type": "text", "text":"This is Statement of Grades for the student. Return just a json of student details, university details, including but not limited to name, course, discipline and grades, credit, subject name, course code and semester from the above. Where value is empty put NaN"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_base64}"
                        },
                    },
                ]
            )
        ]
    )
    return msg.content.replace("```","").replace("json","")
    


