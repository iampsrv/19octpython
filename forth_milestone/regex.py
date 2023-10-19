import re

text ="Python has become popular among developers today, and it is preferred by a large number of organizations as Python helps developers be productive and confident about the software they’re building. Benefits that make Python the best fit for machine learning and AI-based projects include simplicity and consistency, access to great libraries and frameworks for AI and machine learning (ML), flexibility, platform independence, and a wide community. These add to the overall popularity of the language contact us at email@example.com"

# pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
match = re.findall(pattern, text)
print(match)

