#4-19-2026 v1.0
#4-27-2026 v1.1

def load_text_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().lower()
    
def find_skill_matches(text, keyword_groups):
    found_skills = []

    for skill, phrases in keyword_groups.items():
        for phrase in phrases:
            if phrase.lower() in text:
                if skill not in found_skills:
                    found_skills.append(skill)
                break

    return found_skills

def main():
    keyword_groups = {
        #IT /Tech
        "software engineering": ["software egineering", "software development", "application development", "programming", "coding"],
        "python": ["python", "python scripting", "programming", "scripting"],
        "sql": ["sql", "structured query language", "databae queries"],
        "aws": ["aws", "amazon web services", "cloud platform", "cloud"],
        "technical support": ["technical support", "user support", "help desk", "it support"],
        "troubleshooting": ["troubleshooting", "issue resolution", "problem resolution", "debugging"],
        "windows": ["windows", "windows environment", "microsoft windows"],
        "active directory": ["active directory", "ad administration", "directory services"],
        "networking": ["networking", "network support", "tcp/ip", "dns"],
        "ticketing": ["ticketing", "ticket system", "service ticket", "incident tickets"],
        "systems administration": ["systems administrator", "system administrator", "systems administration"],
        "api": ["api", "apis", "application programming interface"],
        "excel": ["excel", "microsoft excel", "spreadhessts"],
        "data analysis": ["data analysis", "analytics", "reporting", "data reporting"],
        "cybersecruity": ["cybersecurity", "security", "information security"],

        #Business/other
        "communication": ["communication", "written communication", "verbal communication"],
        "leadership": ["leadership", "team leadership", "leading teams"],
        "customer service": ["customer service", "client service", "customer support"],
        "operations": ["operations", "operational support", "buisness support"],
        "process improvement": ["process improvement", "continuous improvement", "workflow improvement"],
        "project management": ["project management", "project coordination", "project planning"],
        "documentation": ["documentation", "documenting", "written procedures", "process documents"],
        "training": ["training", "coaching", "mentopring", "onboarding"],
        "problem solving": ["problem solving", "critical thinking", "analytical thinking"],
        "teamwork": ["teamwork", "collaboration", "cross-functional collaboration"],
        "scheduling": ["scheduling", "workforce scheduling", "planning schedules"],
        "quality": ["quality", "quality assurance", "quality control"],
        "supervision": ["supervisor", "supervision", "team supervision", "management"],
    }
    resume_txt = load_text_file("resume.txt")
    job_txt = load_text_file("job.txt")

    resume_matches = find_skill_matches(resume_txt, keyword_groups)
    job_matches = find_skill_matches(job_txt, keyword_groups)


    matched_skills = []
    missing_skills = []

    for skill in job_matches:
        if skill in resume_matches:
            matched_skills.append(skill)
        else:
            if skill not in missing_skills:
                missing_skills.append(skill)

    if len(job_matches) > 0:
        match_score = round((len(matched_skills) / len(job_matches)) * 100, 2)
    else:
        match_score = 0

    print("=== Job Fit Analyzer v1.1 ===")
    print(f"Match Score: {match_score}%")
    print()

    print("Matched Skills: ")
    if matched_skills:
        for skill in matched_skills:
            print("-", skill)
    else:
        print("None")


    if match_score >= 70:
        print("Recommendation: Strong fit. Apply")
    elif match_score >=40:
        print("Recommendation: Possible fit. Review role")
    else:
        print("Recommendation Low Fit. Lower priority")
main()