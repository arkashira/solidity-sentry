import json
from dataclasses import dataclass
from typing import List

@dataclass
class AuditFinding:
    description: str
    severity: str
    remediation_link: str

class SoliditySentry:
    def __init__(self, template_system):
        self.template_system = template_system

    def generate_findings(self, issues: List[dict]) -> List[AuditFinding]:
        findings = []
        for issue in issues:
            description = self.template_system.render(issue['description_template'], issue['description_data'])
            severity = issue['severity']
            remediation_link = issue['remediation_link']
            finding = AuditFinding(description, severity, remediation_link)
            findings.append(finding)
        return findings

class TemplateSystem:
    def render(self, template: str, data: dict) -> str:
        for key, value in data.items():
            template = template.replace(f'{{{{ {key} }}}}', str(value))
        return template

def create_template_system() -> TemplateSystem:
    return TemplateSystem()
