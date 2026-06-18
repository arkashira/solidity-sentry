<think>
Okay, I need to create a PRD.md for the solidity-sentry project. Let me start by understanding the context provided. The repo is a Solidity code analysis and optimization tool aimed at helping developers improve code quality and reduce errors. The existing portfolio includes iceoryx2, which is an IPC library, so I need to make sure solidity-sentry doesn't duplicate that but instead addresses a different validated need.

First, the problem statement. Solidity is used for Ethereum smart contracts, which are critical and costly to have errors in. Common issues include reentrancy, integer overflows, and gas inefficiencies. Current tools might not cover all these aspects or provide actionable fixes. The target users are Solidity developers, especially those working on DeFi, NFTs, and blockchain projects.

Next, goals. The primary goal is to provide a tool that not only identifies issues but also suggests optimizations. Secondary goals could include integration with existing workflows and real-time analysis.

Key features should be prioritized. High-priority features might be static analysis for common vulnerabilities, gas optimization suggestions, and integration with IDEs or CI/CD pipelines. Medium priority could include a CLI tool and a dashboard for tracking issues. Low priority might be community plugins or educational resources.

Success metrics could be the number of issues detected, user adoption rate, reduction in reported bugs, and performance improvements in contracts. Scope should include the core analysis engine and integrations, while excluding things like a full IDE or support for other languages.

I need to ensure that the PRD is grounded in the company's existing knowledge, like using vLLM or SGLang for any AI components, but since this is a code analysis tool, maybe those aren't directly relevant. The datasets available might be used for training models if needed, but the PRD should focus on the tool's features and requirements.

Also, the existing portfolio's iceoryx2 is about IPC, so solidity-sentry is about code analysis, which is a different area. Need to make sure there's no overlap. The growth rate data shows high production of pairs, which might relate to training data if the tool uses ML, but the PRD should be concrete and shippable, so maybe start with static analysis without ML unless it's necessary.

I should structure the PRD with sections: Problem, Target Users, Goals, Key Features (prioritized), Success Metrics, Scope/Out-of-Scope. Use the provided example as a template. Make sure to be specific and professional, avoiding vague statements. Check for any missing elements and ensure alignment with the company's context and existing products.
</think>

# PRD: Solidity Sentry — Smart Contract Code Analysis & Optimization Tool

## Problem
Solidity developers face significant risks from undetected vulnerabilities (reentrancy, integer overflows, gas inefficiencies) and suboptimal code patterns. Current tools either lack depth in vulnerability detection, fail to provide actionable fixes, or require complex setup. Critical smart contracts in DeFi, NFTs, and blockchain applications demand a robust, developer-friendly solution that ensures security and efficiency without disrupting workflows.

## Target Users
- **Primary**: Solidity developers building Ethereum-based smart contracts (DeFi protocols, NFT platforms, DAOs)
- **Secondary**: Blockchain project leads requiring CI/CD integration for code quality gates

## Goals
1. **Core**: Deliver real-time static analysis and optimization suggestions for Solidity codebases
2. **Differentiation**: Provide **actionable fixes** (code snippets + rationale) for detected issues
3. **Integration**: Native support for Hardhat, Truffle, and VS Code extensions
4. **Performance**: Analyze 10k+ line contracts in <5 seconds with <100MB memory footprint

## Key Features (Prioritized)
### High Priority
1. **Vulnerability Scanner**  
   - Detects reentrancy, timestamp dependence, unchecked external calls, and 15+ common CWEs  
   - Risk scoring (Low/Medium/High/Critical) with exploit scenario examples  

2. **Gas Optimization Engine**  
   - Identifies storage access patterns, redundant computations, and SLOAD/SSTORE inefficiencies  
   - Suggests Yul assembly optimizations and struct packing strategies  

3. **Automated Fix Suggestions**  
   - Context-aware code patches (e.g., "Wrap this function in a reentrancy guard")  
   - Before/after gas cost comparisons  

### Medium Priority
4. **CI/CD Integration**  
   - GitHub Action for pre-commit checks  
   - Threshold-based failure rules (e.g., "Block deploy if >5 High-risk issues")  

5. **Dashboard & History**  
   - Track issue resolution progress across commits  
   - Team-wide risk heatmaps  

### Low Priority
6. **Educational Resources**  
   - Interactive tutorials for common fixes  
   - Gas cost calculator for code patterns  

## Success Metrics
- **Adoption**: 10k+ active users in 6 months (tracked via telemetry opt-in)  
- **Impact**: 70% reduction in reported bugs from analyzed contracts  
- **Performance**: 90% of optimizations result in ≥15% gas cost reduction  
- **Retention**: 60% of users integrate into CI/CD pipelines  

## Scope / Out-of-Scope
**In Scope**  
- Solidity 0.8.x-0.8.20 support  
- Ethereum Virtual Machine (EVM) specific optimizations  
- Open-source core with premium add-ons (e.g., enterprise SLAs)  

**Out of Scope**  
- Full IDE development (leverage existing VS Code/Remix integrations)  
- Support for non-EVM languages (Vyper, Move)  
- On-chain monitoring/post-deploy analysis  

---

**Next Steps**:  
1. Finalize rule set with Ethereum Foundation security guidelines  
2. Build prototype for 5 core vulnerabilities + gas optimizations  
3. Validate with 3 DeFi projects in closed beta
