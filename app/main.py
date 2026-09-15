from agent import create_research_plan


def main():

    print("================================")
    print("      JARVIS RESEARCH AGENT")
    print("================================")

    question = input("\nWhat would you like me to research?\n> ")

    print("\nCreating research plan...\n")

    plan = create_research_plan(question)

    print("------------- RESEARCH PLAN -------------")
    print(plan)
    print("------------------------------------------")


if __name__ == "__main__":
    main()
