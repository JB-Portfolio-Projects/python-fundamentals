#4-19-2026 v1.0

def load_text_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().lower()
    
def find_keywords(text, keywords):
    found = []

    for keyword in keywords:
        if keyword.lower() in text:
            found.append(keyword)
    
    return found

def main():
    keywords = [
        #IT /Tech
        "python",
        "programming",
        "sql",
        "aws",
        "Amazon Web Services",
        "cloud",
        "technical support",
        "troubleshooting",
        "windows",
        "active directory",
        "networking",
        "ticketing",
        "help desk",
        "systems administrator",
        "api",
        "excel",
        "data analysis",
        "analytics",
        "user support",
        "cloud platform",
        "scripting",


        #Business / Non-IT / Transferrable
        "communication",
        "leadership",
        "customer service",
        "operations",
        "process imporvement",
        "project management",
        "documentation",
        "training",
        "problem solving",
        "teamwork",
        "coaching",
        "scheduling",
        "quality",
        "supervisor",
        "management",
    ]

    resume_txt = load_text_file("resume.txt")
    job_txt = load_text_file("job.txt")

    resume_matches = find_keywords(resume_txt, keywords)
    job_matches = find_keywords(job_txt, keywords)

    matched_keywords = []
    missing_keywords = []

    for keyword in job_matches:
        if keyword in resume_matches:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    if len(job_matches) > 0:
        match_score = round((len(matched_keywords) / len(job_matches)) * 100, 2)
    else:
        match_score = 0

    print("=== Job Fit Analyzer v1.0 ===")
    print(f"Match Score: {match_score}%")
    print()

    print("Matched Keywords: ")
    if matched_keywords:
        for keyword in matched_keywords:
            print("-", keyword)
    else:
        print("None")

    print()

    if match_score >= 70:
        print("Recommendation: Strong fit. Apply")
    elif match_score >=40:
        print("Recommendation: Possible fir. Review role")
    else:
        print("Recommendation Low Fit. Lower priority")

main()