import json
from dataclasses import dataclass
from typing import List

@dataclass
class Issue:
    id: int
    description: str
    fix_suggestion: str = None

class SoliditySentry:
    def __init__(self, issues: List[Issue]):
        self.issues = issues

    def generate_fix_suggestions(self):
        for issue in self.issues:
            if issue.description.startswith("Syntax error"):
                issue.fix_suggestion = "Check syntax and fix errors"
            elif issue.description.startswith("Type error"):
                issue.fix_suggestion = "Check types and fix errors"
            else:
                issue.fix_suggestion = "Unknown error: please investigate"
        return self.issues

    def validate_fix_suggestions(self):
        if not self.issues:
            return True
        valid_issues = [issue for issue in self.issues if issue.fix_suggestion is not None]
        return len(valid_issues) == len(self.issues)

    def apply_fix_suggestions(self):
        applied_issues = []
        for issue in self.issues:
            if issue.fix_suggestion is not None:
                # Apply fix suggestion
                print(f"Applied fix suggestion for issue {issue.id}")
                applied_issues.append(issue)
        return applied_issues
