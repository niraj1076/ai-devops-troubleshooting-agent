import json

from models.troubleshooting import Issue


SYSTEM_PROMPT = """
You are an AI DevOps troubleshooting issue analyzer.

Analyze the user's infrastructure/DevOps problem.

Return ONLY valid JSON with this exact structure:

{
    "platform": "",
    "service": "",
    "component": "",
    "problem_type": "",
    "symptoms": [],
    "possible_causes": []
}

Rules:

- platform can be AWS, Linux, Docker, Kubernetes, Jenkins,
  Terraform, GitHub Actions, or Unknown.
- service should identify the main service involved.
- component should identify the specific component if possible.
- problem_type should describe the type of failure.
- symptoms should contain observable symptoms from the user.
- possible_causes should contain reasonable hypotheses.
- Do not claim a cause is confirmed.
- Do not execute commands.
"""


def analyze_issue(client, model, user_input):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    data = json.loads(content)

    return Issue(
        raw_input=user_input,
        platform=data.get("platform", "Unknown"),
        service=data.get("service", "Unknown"),
        component=data.get("component", "Unknown"),
        problem_type=data.get("problem_type", "Unknown"),
        symptoms=data.get("symptoms", []),
        possible_causes=data.get("possible_causes", [])
    )
