"""Placement Eligibility Checker - a beginner-friendly console project."""


def ask_yes_no(question):
    """Keep asking until the user enters yes or no."""
    while True:
        answer = input(question).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please enter yes or no.")


def get_number(question, number_type=float, minimum=0):
    """Read a valid non-negative number from the user."""
    while True:
        try:
            value = number_type(input(question).strip())
            if value < minimum:
                print(f"Please enter a value of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please try again.")


def check_company_eligibility(student):
    """Return eligible companies and reasons for ineligible companies."""
    cgpa = student["cgpa"]
    backlogs = student["backlogs"]
    skills = student["skills"]
    internship = student["internship"]

    companies = {
        "TCS": (cgpa >= 6.0 and backlogs == 0,
                "CGPA must be at least 6.0 and backlogs must be 0"),
        "Infosys": (cgpa >= 6.5 and backlogs == 0,
                    "CGPA must be at least 6.5 and backlogs must be 0"),
        "Wipro": (cgpa >= 6.5 and ("python" in skills or "java" in skills),
                  "CGPA must be at least 6.5 and you need Python or Java"),
        "Accenture": (cgpa >= 7.0 and internship,
                      "CGPA must be at least 7.0 and internship experience is required"),
        "Amazon": (cgpa >= 8.0 and {"python", "dsa"}.issubset(skills) and internship,
                   "CGPA must be at least 8.0, with Python, DSA, and an internship"),
        "Google": (cgpa >= 8.5 and {"python", "dsa", "projects"}.issubset(skills) and internship,
                   "CGPA must be at least 8.5, with Python, DSA, projects, and an internship"),
    }

    eligible = [name for name, (is_eligible, _) in companies.items() if is_eligible]
    not_eligible = [
        (name, reason) for name, (is_eligible, reason) in companies.items()
        if not is_eligible
    ]
    return eligible, not_eligible


def print_recommendations(student):
    """Show useful next steps based on the student's current profile."""
    cgpa = student["cgpa"]
    skills = student["skills"]

    missing_top_skills = [
        skill for skill in ["Python", "DSA", "Projects", "System Design", "Competitive Programming"]
        if skill.lower() not in skills
    ]

    print("\nMissing Skills for Top Product Companies:")
    if missing_top_skills:
        for skill in missing_top_skills:
            print(f"- {skill}")
    else:
        print("- Great work! Your core skills are covered.")

    print("\nRecommendations to become eligible for Google:")
    recommendations = []
    if cgpa < 8.5:
        recommendations.append("Increase CGPA to 8.5 or higher.")
    if "python" not in skills:
        recommendations.append("Learn and practice Python.")
    if "dsa" not in skills:
        recommendations.append("Strengthen Data Structures and Algorithms (DSA).")
    if "projects" not in skills:
        recommendations.append("Build at least one strong project and add it to your resume.")
    if not student["internship"]:
        recommendations.append("Complete an internship.")

    if recommendations:
        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:
        print("- Your profile already meets the listed Google criteria!")


def main():
    print("=" * 45)
    print("      PLACEMENT ELIGIBILITY CHECKER")
    print("=" * 45)

    cgpa = get_number("Enter your CGPA (out of 10): ")
    while cgpa > 10:
        print("CGPA cannot be greater than 10.")
        cgpa = get_number("Enter your CGPA (out of 10): ")

    student = {
        "cgpa": cgpa,
        "backlogs": get_number("Enter number of backlogs: ", int),
        "skills": set(),
        "internship": ask_yes_no("Do you have internship experience? (yes/no): "),
    }

    for skill in ["Python", "Java", "DSA", "Projects"]:
        if ask_yes_no(f"Do you know {skill}? (yes/no): "):
            student["skills"].add(skill.lower())

    eligible, not_eligible = check_company_eligibility(student)
    total_companies = len(eligible) + len(not_eligible)
    readiness_score = round((len(eligible) / total_companies) * 100)

    print("\n" + "=" * 45)
    print("ELIGIBLE COMPANIES")
    print("=" * 45)
    if eligible:
        for company in eligible:
            print(f"[ELIGIBLE] {company}")
    else:
        print("You are not eligible for the listed companies yet.")

    print("\nNOT ELIGIBLE")
    print("=" * 45)
    for company, reason in not_eligible:
        print(f"[NOT ELIGIBLE] {company} ({reason})")

    print(f"\nPlacement Readiness Score: {readiness_score}%")
    print_recommendations(student)


if __name__ == "__main__":
    main()
