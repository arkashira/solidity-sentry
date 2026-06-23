import pytest
from src.solidity_sentry import SoliditySentry, TemplateSystem, AuditFinding, create_template_system

def test_generate_findings():
    template_system = TemplateSystem()
    sentry = SoliditySentry(template_system)
    issues = [
        {
            'description_template': 'Issue {{ issue_id }}: {{ issue_name }}',
            'description_data': {'issue_id': 1, 'issue_name': 'Example Issue'},
            'severity': 'high',
            'remediation_link': 'https://example.com/remediation'
        }
    ]
    findings = sentry.generate_findings(issues)
    assert len(findings) == 1
    finding = findings[0]
    assert finding.description == 'Issue 1: Example Issue'
    assert finding.severity == 'high'
    assert finding.remediation_link == 'https://example.com/remediation'

def test_template_system_render():
    template_system = TemplateSystem()
    template = 'Hello, {{ name }}!'
    data = {'name': 'John'}
    rendered = template_system.render(template, data)
    assert rendered == 'Hello, John!'

def test_create_template_system():
    template_system = create_template_system()
    assert isinstance(template_system, TemplateSystem)
