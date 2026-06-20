import pytest
from solidity_sentry import SoliditySentry, Issue

def test_generate_fix_suggestions():
    issues = [Issue(1, "Syntax error: missing semicolon"), Issue(2, "Type error: invalid type")]
    sentry = SoliditySentry(issues)
    issues_with_fixes = sentry.generate_fix_suggestions()
    assert issues_with_fixes[0].fix_suggestion == "Check syntax and fix errors"
    assert issues_with_fixes[1].fix_suggestion == "Check types and fix errors"

def test_validate_fix_suggestions():
    issues = [Issue(1, "Syntax error: missing semicolon"), Issue(2, "Type error: invalid type"), Issue(3, "Unknown error")]
    sentry = SoliditySentry(issues)
    sentry.generate_fix_suggestions()
    assert sentry.validate_fix_suggestions() == True

def test_apply_fix_suggestions():
    issues = [Issue(1, "Syntax error: missing semicolon"), Issue(2, "Type error: invalid type"), Issue(3, "Unknown error")]
    sentry = SoliditySentry(issues)
    sentry.generate_fix_suggestions()
    applied_issues = sentry.apply_fix_suggestions()
    assert len(applied_issues) == 3

def test_edge_case_empty_issues():
    sentry = SoliditySentry([])
    assert sentry.generate_fix_suggestions() == []
    assert sentry.validate_fix_suggestions() == True
    assert sentry.apply_fix_suggestions() == []
