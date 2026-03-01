# Senior Mindset — Behavioral Interview Preparation

## Overview

The Senior Mindset module covers the behavioral and strategic thinking patterns that distinguish senior and staff engineers from mid-level ICs. These topics appear repeatedly in behavioral rounds at top companies and are evaluated through the STAR method, leadership principles, and scenario-based questions.

```mermaid
mindmap
  root((Senior Mindset))
    Ownership & Accountability
      Scope Progression
      Anti-Patterns
      IC vs Team Ownership
    Prioritization
      ICE / RICE
      Effort-Impact Matrix
      Eisenhower Matrix
    Technical Decisions
      ADRs & RFCs
      One-Way vs Two-Way Doors
      Consensus Building
    Buy vs Build
      TCO Analysis
      Vendor Lock-In
      Core vs Commodity
    Cross-Team Collaboration
      API Contracts
      Async Communication
      Platform Teams
    Mentorship & Culture
      Code Review
      Onboarding
      Knowledge Sharing
    Managing Tech Debt
      Debt Quadrant
      Quantifying Impact
      Refactoring Strategies
    Saying No with Data
      Yes-And Technique
      Negotiation
      Managing Up
```

## Topic Map

```mermaid
flowchart LR
    subgraph Foundation["Foundation Layer"]
        A[01 Ownership Thinking]
        B[02 Prioritization Frameworks]
    end

    subgraph Decisions["Decision Layer"]
        C[03 Technical Decisions]
        D[04 Buy vs Build]
    end

    subgraph Execution["Execution Layer"]
        E[05 Cross-Team Collaboration]
        F[06 Mentorship & Culture]
    end

    subgraph Sustainability["Sustainability Layer"]
        G[07 Managing Tech Debt]
        H[08 Saying No with Data]
    end

    A --> C
    A --> E
    B --> C
    B --> D
    B --> H
    C --> D
    C --> G
    E --> F
    G --> H
    D --> G
```

## Topic Table

| # | Topic | Key Concepts | Typical Interview Questions | Priority |
|---|-------|-------------|---------------------------|----------|
| 01 | Ownership Thinking | Scope progression, anti-patterns, IC vs team ownership | "Tell me about a time you took ownership beyond your role" | High |
| 02 | Prioritization Frameworks | ICE, RICE, Eisenhower, effort-impact | "How do you decide what to work on?" | High |
| 03 | Technical Decisions | ADRs, RFCs, one-way/two-way doors | "Walk me through a major technical decision" | High |
| 04 | Buy vs Build | TCO, vendor lock-in, core vs commodity | "When would you build vs buy?" | Medium |
| 05 | Cross-Team Collaboration | API contracts, async comms, dependencies | "How do you work across teams?" | High |
| 06 | Mentorship & Culture | Code review, onboarding, pair programming | "How do you grow engineers on your team?" | Medium |
| 07 | Managing Tech Debt | Debt quadrant, quantifying, refactoring | "How do you handle tech debt?" | High |
| 08 | Saying No with Data | Yes-and technique, negotiation, managing up | "How do you push back on unrealistic timelines?" | High |

## Recommended Study Order

### Week 1 — Foundation
1. **01-Ownership Thinking** — Sets the baseline mindset for everything else
2. **02-Prioritization Frameworks** — Core skill that feeds into all decision-making

### Week 2 — Decisions
3. **03-Technical Decisions** — How to make and document architectural choices
4. **04-Buy vs Build** — Applying decision frameworks to a common dilemma

### Week 3 — Execution
5. **05-Cross-Team Collaboration** — Working across boundaries at scale
6. **06-Mentorship & Culture** — Multiplying impact through others

### Week 4 — Sustainability
7. **07-Managing Tech Debt** — Long-term system health and strategic refactoring
8. **08-Saying No with Data** — Protecting capacity and negotiating scope

## How These Topics Connect

```mermaid
flowchart TD
    OWN[Ownership Thinking] -->|drives| PRI[Prioritization]
    PRI -->|informs| TD[Technical Decisions]
    TD -->|applies to| BVB[Buy vs Build]
    OWN -->|enables| CTC[Cross-Team Collaboration]
    CTC -->|deepens via| MEN[Mentorship & Culture]
    TD -->|reveals| MTD[Managing Tech Debt]
    PRI -->|supports| SNO[Saying No with Data]
    MTD -->|requires| SNO

    style OWN fill:#2d6a4f,color:#fff
    style PRI fill:#2d6a4f,color:#fff
    style TD fill:#40916c,color:#fff
    style BVB fill:#40916c,color:#fff
    style CTC fill:#52b788,color:#000
    style MEN fill:#52b788,color:#000
    style MTD fill:#74c69d,color:#000
    style SNO fill:#74c69d,color:#000
```

## Progress Tracker

| # | Topic | Read | Notes Made | Stories Prepared | Mock Practice | Confident |
|---|-------|:----:|:----------:|:----------------:|:-------------:|:---------:|
| 01 | Ownership Thinking | [ ] | [ ] | [ ] | [ ] | [ ] |
| 02 | Prioritization Frameworks | [ ] | [ ] | [ ] | [ ] | [ ] |
| 03 | Technical Decisions | [ ] | [ ] | [ ] | [ ] | [ ] |
| 04 | Buy vs Build | [ ] | [ ] | [ ] | [ ] | [ ] |
| 05 | Cross-Team Collaboration | [ ] | [ ] | [ ] | [ ] | [ ] |
| 06 | Mentorship & Culture | [ ] | [ ] | [ ] | [ ] | [ ] |
| 07 | Managing Tech Debt | [ ] | [ ] | [ ] | [ ] | [ ] |
| 08 | Saying No with Data | [ ] | [ ] | [ ] | [ ] | [ ] |

## Story Bank Template

For each topic, prepare 2-3 STAR stories. Use this template:

```
### Story Title: [Short descriptive name]
- **Situation**: [Context — company, team, project, timeline]
- **Task**: [Your specific responsibility and what was expected]
- **Action**: [What YOU did — be specific, use "I" not "we"]
- **Result**: [Quantified outcome — metrics, impact, learning]
- **Applicable Topics**: [Which of the 8 topics this story covers]
```

A single strong story can often apply to 2-3 topics. Aim for 6-8 total stories that collectively cover all 8 topics.
