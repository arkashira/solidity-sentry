from solidity_sentry import SoliditySentry, Issue

def test_identify_issues():
    sentry = SoliditySentry()
    issues = sentry.identify_issues("example_code")
    assert len(issues) == 2
    assert issues[0].id == 1
    assert issues[1].id == 2

def test_generate_fix_suggestions():
    sentry = SoliditySentry()
    issues = [
        Issue(1, "Issue 1: Variable not initialized"),
        Issue(2, "Issue 2: Function not called"),
    ]
    issues_with_fixes = sentry.generate_fix_suggestions(issues)
    assert issues_with_fixes[0].fix_suggestion == "Initialize variable before use"
    assert issues_with_fixes[1].fix_suggestion == "Call function to avoid unused code"

def test_validate_fix_suggestions():
    sentry = SoliditySentry()
    issues_with_fixes = [
        Issue(1, "Issue 1: Variable not initialized", "Initialize variable before use"),
        Issue(2, "Issue 2: Function not called", "Call function to avoid unused code"),
    ]
    assert sentry.validate_fix_suggestions(issues_with_fixes) == True

    issues_without_fixes = [
        Issue(1, "Issue 1: Variable not initialized"),
        Issue(2, "Issue 2: Function not called"),
    ]
    assert sentry.validate_fix_suggestions(issues_without_fixes) == False

def test_apply_fix_suggestions():
    sentry = SoliditySentry()
    issues_with_fixes = [
        Issue(1, "Issue 1: Variable not initialized", "Initialize variable before use"),
        Issue(2, "Issue 2: Function not called", "Call function to avoid unused code"),
    ]
    applied_fixes = sentry.apply_fix_suggestions(issues_with_fixes)
    assert applied_fixes == "Applied fix for issue 1: Initialize variable before use\nApplied fix for issue 2: Call function to avoid unused code"
