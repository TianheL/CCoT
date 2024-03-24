import base64 
from openai import OpenAI

client = OpenAI(
        api_key="Your OpenAI API Key",
        base_url="Your OpenAI API Base"
    )

def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def template_gen_sg(ques):
    return f"Question: {ques}\n For the provided image and its associated question, generate a scene graph in JSON format that includes the following:\n1. Objects that are relevant to answering the question.\n2. Object attributes that are relevant to answering the question.\n3.Object relationships that are relevant to answering the question.\nYou should answer the scene graph only, and you should not answer the question.\nScene Graph:"

def template_gen_ans(ques, sg):
    return f"Scene Graph:\n{sg}\nUse the image and scene graph as context and answer the following question:\nQuestion: {ques}\nAnswer with the option's letter from the given choices directly."

def gen_sg(client, question, image_path):
    encoded_image = encode_image(image_path)
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            {"type": "text", "text": template_gen_sg(question)},
        ],
        }
    ],
    temperature = 0,
    max_tokens = 300,
    )

    return response.choices[0].message.content

def gen_ans(client, question, image_path, sg):
    encoded_image = encode_image(image_path)
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            {"type": "text", "text": template_gen_ans(question, sg)},
        ],
        }
    ],
    temperature = 0,
    max_tokens = 300,
    )

    return response.choices[0].message.content

if __name__=="__main__":
    question = "What’s the man doing?\n(A) Catching a ball (B) Sleeping (C) Throwing a frisbee (D) Drawing"
    sg=gen_sg(client,question,'Frisbee.jpg')
    print(sg)
    ans=gen_ans(client,question,'Frisbee.jpg',sg)
    print(ans)
