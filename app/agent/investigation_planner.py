import json

from models.troubleshooting import InvestigationPlan, InvestigationStep


SYSTEM_PROMPT = """
You are an AI DevOps investigation planner.

You receive a structured infrastructure issue.

Create a safe, read-only diagnostic investigation plan.

Return ONLY valid JSON:

{
    "steps": [
        {
            "step_number": 1,
            "objective": "",
            "command": "",
            "reason": ""
        }
    ]
}

Rules:

1. Commands must be diagnostic/read-only commands.
2. Never use commands that modify, delete, restart, stop,
   reboot, kill, terminate, or change infrastructure.
3. Start with the simplest diagnostic checks.
4. Each command must help test a possible cause.
5. Prefer Linux commands when the platform is Linux.
6. Prefer kubectl read-only commands for Kubernetes.
7. Prefer AWS CLI read-only commands for AWS.
8. Do not assume a command has already been executed.
9. Do not provide destructive commands.
10. Maximum 8 investigation steps.
"""


def create_investigation_plan(client, model, issue):

    issue_data = {
        "platform": issue.platform,
        "service": issue.service,
        "component": issue.component,
        "problem_type": issue.problem_type,
        "symptoms": issue.symptoms,
        "possible_causes": issue.possible_causes
    }

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": json.dumps(issue_data)
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    data = json.loads(content)

    steps = []

    for step in data.get("steps", []):
        steps.append(
            InvestigationStep(
                step_number=step["step_number"],
                objective=step["objective"],
                command=step["command"],
                reason=step["reason"]
            )
        )

    return InvestigationPlan(
        issue=issue,
        steps=steps
    )

