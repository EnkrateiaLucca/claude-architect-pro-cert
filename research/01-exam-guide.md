# Claude Certified Architect – Professional (CCAR-P): Exam Guide Research

Research date: 2026-10-13.

## Context

This file records what Anthropic officially publishes about the Claude Certified Architect – Professional exam: logistics, audience, blueprint, sample items, and the official prep path. It also records how the exam differs from Claude Certified Architect – Foundations and what unofficial community sources say. The course content, practice questions, and cheatsheet in this repo should align to the official blueprint below.

**Headline:** The official Professional exam guide is public. It is an 11-page PDF, "Version 1.0 · Effective July 2026 · Exam code: CCAR-P", linked from the Partner Academy certifications page. [source: https://anthropic-partners.skilljar.com/page/partner-certifications] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

Label conventions: `[source: url]` marks a fetched and read source. `[inferred]` marks my own analysis built on sourced facts. `[unverified]` marks a claim I could not confirm with a fetched page. "Unofficial" marks third-party material.

## Sources

| ID | Source | Type | Fetched |
|----|--------|------|---------|
| S1 | [CCAR-P Exam Guide PDF v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf) | Official, primary | Yes. Downloaded with curl, extracted with `pdftotext -layout` |
| S2 | [CCAR-F Exam Guide PDF v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf) | Official, primary | Yes. Same method |
| S3 | [Partner Academy: Earn your Claude certification](https://anthropic-partners.skilljar.com/page/partner-certifications) | Official | Yes |
| S4 | [Partner Academy: Certification FAQ](https://anthropic-partners.skilljar.com/page/faq-certifications) | Official | Yes |
| S5 | [Partner Academy: Certification policies](https://anthropic-partners.skilljar.com/page/policies-certifications) | Official | Yes |
| S6 | [Partner Academy: Who can take an exam](https://anthropic-partners.skilljar.com/page/certification-eligibility) | Official | Yes |
| S7 | [Partner Academy: CCAR-P exam purchase page](https://anthropic-partners.skilljar.com/claude-certified-architect-professional-certification) | Official | Yes |
| S8 | [Partner Academy: CCAR-P Prep Course (path)](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional) | Official | Yes |
| S9 | [Lesson 1: Claude Platform & Solution Design](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/claude-platform-solution-design) | Official | Yes |
| S10 | [Lesson 2: Enterprise Integration & Production](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/enterprise-integration-production) | Official | Yes |
| S11 | [Lesson 3: Responsible AI, Safety & Risk for Architects](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/responsible-ai-safety-risk-for-architects) | Official | Yes |
| S12 | [Lesson 4: Stakeholder Engagement, Lifecycle & GTM](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/stakeholder-engagement-lifecycle-gtm) | Official | Yes |
| S13 | [Lesson 5: Team Enablement & Operational Productivity](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/developer-productivity-enablement) | Official | Yes |
| S14 | [Partner Academy: Exam prep courses](https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses) | Official | Yes |
| S15 | [Credly: CCAR-P badge](https://www.credly.com/org/anthropic/badge/claude-certified-architect-professional) | Official (Anthropic org on Credly) | Yes |
| S16 | [claude.com: Four role-based certifications (2026-07-23)](https://claude.com/resources/articles/four-role-based-claude-certifications) | Official | Yes |
| S17 | [anthropic.com: Claude Partner Network (2026-03-12)](https://www.anthropic.com/news/claude-partner-network) | Official | Yes |
| S18 | [vkorost/claude-certified-architect-professional-guide (GitHub)](https://github.com/vkorost/claude-certified-architect-professional-guide) | Unofficial, first-hand claim | Yes (README via `gh api`) |
| S19 | [claudecertificationguide.com: CCAR-P exam guide and blueprint](https://claudecertificationguide.com/blog/claude-certified-architect-professional-exam-guide) | Unofficial, not first-hand | Yes |
| S20 | [FlashGenius: CCAR-F vs CCAR-P](https://flashgenius.net/guides/claude-architect-foundations-vs-professional-ccar-f-vs-ccar-p) | Unofficial, not first-hand | Yes |
| F1 | [Level Up Coding: "I passed the CCAR-P exam in two days of prep"](https://levelup.gitconnected.com/i-passed-the-claude-certified-architect-professional-ccar-p-exam-in-two-days-of-prep-31e0bcbe04de) | Unofficial | **Failed**: HTTP 403 via WebFetch and curl (Cloudflare). scribe.rip mirror returned 404 |
| F2 | [LinkedIn: yeolouis, "Passing the ... CCAR-P exam during my second week of paternity leave"](https://sg.linkedin.com/in/yeolouis) | Unofficial | **Failed**: HTTP 999 (LinkedIn bot block) |
| F3 | Reddit search JSON (`reddit.com/search.json?q=CCAR-P`) | Unofficial | **Failed**: HTTP 403 |
| F4 | [Credly individual badge linked from S18](https://www.credly.com/badges/91687ca6-d512-417b-868a-3dba245c59fe) | Official badge record | **Partial**: page shell loaded, earner name and date not rendered |

## Logistics

Values come from the CCAR-P guide, Section 5 "Exam Details at a Glance", unless noted. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

| Item | Value | Source |
|------|-------|--------|
| Credential | Claude Certified Architect – Professional | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Exam code | CCAR-P | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Guide version | "Version 1.0 · Effective July 2026"; Document Control: "1.0 Initial publication July 2026" | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Number of items | 63 | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Item format | "Multiple-choice and multiple-response items; each item states how many responses to select" | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Exam structure | The CCAR-P guide has no "Exam structure" row and no scenario bank. The CCAR-F guide has "4 scenarios drawn from a bank of 6". | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Time limit | 120 minutes. FAQ: "Plan for about 135 minutes of total seat time, which includes check-in, instructions, and a brief post-exam survey." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Delivery | "Proctored: online proctored and/or test center, per program policy". Delivered by Pearson VUE (online OnVUE or Pearson test center). | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Open/closed book | "No. Exams are closed book. Browser translation tools are not permitted under the Pearson proctoring platform." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Languages | "The exam and prep content are available in English and Japanese." (The five CCAR-P prep lesson cards are tagged "Language: English".) | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional] |
| Passing score | "Scaled score of 720 on a scale of 100–1,000" | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Scoring model | "criterion-referenced assessment: each candidate is measured against a fixed performance standard, not against other candidates." Cut score set by "a formal standard-setting study in which trained subject matter experts judged the level of performance expected of a minimally qualified candidate." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Scaled scoring rationale | "Scaled scoring equates scores across exam forms that may have slightly different difficulty." (FAQ; the CCAR-F guide contains the same rationale, the CCAR-P guide omits that sentence.) | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] |
| Result reporting | "Pass/fail with scaled score (100–1,000), plus percent-correct by domain on the score report". Domain percentages "are not used to determine your pass or fail result". Score shown on screen at the end of the exam. | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Fee | $175 USD. "The fee shown at checkout reflects any discount that applies to your partner tier." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/partner-certifications] |
| Discounts | "Registered-tier partners pay full price. Select, Preferred, and Global Premier partners receive 50% off ... Through December 31, 2026, Global Premier partners receive a 100% discount on all certification exams". Retakes pay the full fee with tier discount. | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Validity | "12 months from the date the credential is awarded" | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Renewal | "To renew on time, you review what has changed since you certified and complete a free, non-proctored assessment on the Anthropic Partner Academy." Policies page: "an open-book online assessment ... which extends your certification for another 12 months from your current expiration date. You can retake that assessment as many times as you need." Lapsed holders "must retake the full exam at the full fee". | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/policies-certifications] |
| Prerequisites | "There are no mandatory prerequisites or courses required to sit this exam. The experience above is recommended, not required. The credential is awarded based on exam performance alone." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Foundations required? | No. FAQ: "Foundations is the natural place to start and there's no formal prerequisite, so you can take Professional without holding Foundations. Foundations does not convert or upgrade to Professional automatically." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Eligibility | "Claude certification exams are open to people who work at organizations in the Claude Partner Network." Requires a company email on a domain in the partner record, age 18+, government-issued ID. | [source: https://anthropic-partners.skilljar.com/page/certification-eligibility] |
| Partner network credit | CCAR-P counts toward Claude Partner Network eligibility (Associate does not). | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Retakes | Waits of "14 days after the first, 30 days after the second, and 90 days after the third"; "up to four times within a rolling twelve-month period"; "If you pass, you can't retake the exam to improve your score." Wait and attempt count "reset when the exam moves to a new version". | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/policies-certifications] |
| Cancel/reschedule | **Conflict.** Guide Section 10: "up to 24 hours before your appointment". FAQ and Policies: "at least 48 hours before your appointment". See Open questions. | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://anthropic-partners.skilljar.com/page/policies-certifications] |
| Registration window | "Once you register for an exam, your registration is valid for 5 years." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Practice exam | "The practice exam available on the previous platform was retired in the move to Pearson. The exam guide includes sample questions that show the format and style of what's on the exam." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Badge | Credly badge on pass. Credly skills: AI Governance, Context engineering, Enterprise Architecture, Evaluation & optimization, Integration Architecture, Risk Management, Solution Design, Stakeholder Management. | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://www.credly.com/org/anthropic/badge/claude-certified-architect-professional] |
| NDA | Candidates accept an NDA before the exam; Policies: "not to share, reproduce, or discuss the questions in any form, including in study groups and online forums." | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/policies-certifications] |
| Launch timing | Announced as "(New) Claude Certified Architect: Professional is the advanced credential, covering integration architecture, governance, and evaluation, built for the scale of large enterprises." in a 2026-07-23 article. PDF metadata creation date is 2026-07-08. | [source: https://claude.com/resources/articles/four-role-based-claude-certifications] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |

## Audience and minimally qualified candidate

### Purpose (Section 1–2, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

> The Claude Certified Architect – Professional certification validates that an individual can design, build, and deliver production-grade AI solutions using Anthropic's Claude platform. It is intended for practitioners working in an architect role who select appropriate models, architectures, and API patterns; apply prompt and context engineering; integrate Claude into enterprise systems; and incorporate evaluation, security, compliance, and governance considerations into their designs.

Candidates who earn the credential can demonstrate that they are able to (verbatim):

- Design and prototype AI-driven solutions that address real business problems
- Select appropriate models, architectures, and API patterns for specific use cases
- Implement prompt engineering and context strategies to guide model behavior
- Integrate Claude into production systems using APIs, orchestration tools, and data pipelines
- Apply evaluation, monitoring, and observability practices to ensure solution quality
- Incorporate security, compliance, and governance considerations into system design
- Collaborate with cross-functional stakeholders and communicate architectural decisions effectively

### Intended audience (Section 3, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

> The certification is intended for mid- to senior-level technical professionals who design, build, and deliver production-grade AI solutions using large language models, particularly Claude. This audience primarily includes solution architects, AI/ML engineers, technical leads, and senior software engineers who operate at the intersection of business requirements and technical implementation.

> These professionals translate business problems into scalable AI-driven solutions, including model selection, prompt engineering, orchestration of tools and agents, context management, and ensuring system safety, compliance, and governance. They are often involved in stakeholder engagement, advising clients or internal teams, and leading architectural decisions, including discussions of security, legal, and executive considerations. Candidates typically work across industries such as financial services, healthcare, retail, technology, education, and government.

> This certification is not intended for entry-level developers, casual users of Claude-based applications, or individuals without experience designing end-to-end AI systems. It also excludes roles that are purely non-technical or limited to isolated tasks such as prompt writing without broader system design responsibility.

### Minimally qualified candidate (Section 4, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

> The exam is targeted at the minimally qualified candidate (MQC): an experienced practitioner who combines an engineering mindset with practical, real-world experience deploying AI solutions. The MQC designs, implements, and governs Claude-powered AI solutions within production environments, translating business requirements into scalable, secure, and reliable architectures.

> The MQC demonstrates the ability to design end-to-end AI systems, including prompt and context engineering, retrieval-augmented generation (RAG), API integration, orchestration, and evaluation frameworks, and understand trade-offs related to cost, latency, performance, safety, and maintainability.

Recommended experience (verbatim):

- A foundation in software engineering best practices (modular design, separation of concerns, scalability)
- 3+ years of experience in systems architecture or platform engineering
- 6+ months of hands-on experience with Claude or comparable LLM-based systems in production
- Experience delivering end-to-end systems from discovery through deployment and operationalization

### Credly badge description (verbatim)

[source: https://www.credly.com/org/anthropic/badge/claude-certified-architect-professional]

> The Claude Certified Architect – Professional credential is designed for experienced solution architects. Earners can design and lead enterprise-scale Claude deployments, architect integrations, optimize systems at scale, and apply governance and responsible deployment practices.

### In scope / out of scope

- The CCAR-P guide has **no** "In-Scope Topics", "Out-of-Scope Topics", or "Technologies and Concepts" appendix. The CCAR-F guide has all three (Section 17). [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf]
- The FAQ states the exam guide "lists the domains and task statements the exam covers and is the authoritative source for exam scope." For CCAR-P the 38 objectives in Section 6 are therefore the only official scope statement. [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [inferred]

## Domains and objectives

Section 6 verbatim. "The percentages indicate the approximate proportion of scored items drawn from each domain." "Each domain below lists the tasks a candidate is expected to perform. Exam items are written against these objectives." [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

| # | Content Domain | Weight | Objectives | Approx. items of 63 [inferred] |
|---|----------------|--------|------------|------------------|
| 1 | Solution Design & Architecture | 17% | 6 | ~11 |
| 2 | Claude Models, Prompting & Context Engineering | 13% | 5 | ~8 |
| 3 | Integration | 19% | 8 | ~12 |
| 4 | Evaluation, Testing & Optimization | 16% | 6 | ~10 |
| 5 | Governance, Safety & Risk Management | 14% | 5 | ~9 |
| 6 | Stakeholder Communication & Lifecycle Management | 14% | 5 | ~9 |
| 7 | Developer Productivity & Operational Enablement | 7% | 3 | ~4 |
| | **Total** | **100%** | **38** | 63 |

Weights and objective text: [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]. Item counts are my arithmetic (weight × 63, rounded); the guide does not say whether any of the 63 items are unscored. [inferred]

Unlike CCAR-F, CCAR-P objectives are single bullets with no numbered "Task Statement X.Y" and no "Knowledge of / Skills in" breakdown. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] The numbering below (1.1, 1.2, ...) is mine for cross-referencing. [inferred]

### Domain 1: Solution Design & Architecture (17%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

- 1.1 Translate business problems into Claude-based AI solutions
- 1.2 Design end-to-end architectures (input → processing → output → feedback loops)
- 1.3 Select appropriate architectural patterns (workflow, agentic, augmented LLM)
- 1.4 Design multi-agent systems and orchestration strategies
- 1.5 Apply decomposition techniques for complex problem solving
- 1.6 Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs)

### Domain 2: Claude Models, Prompting & Context Engineering (13%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

- 2.1 Select appropriate Claude models based on trade-offs
- 2.2 Design system prompts, templates, and guardrails
- 2.3 Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)
- 2.4 Optimize context windows and manage token usage
- 2.5 Implement prompt reuse strategies (caching, modular prompts, Skills)

### Domain 3: Integration (19%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

- 3.1 Evaluate tool/agent configuration for capability bloat
- 3.2 Analyze authentication and authorization requirements to identify security gaps
- 3.3 Evaluate accuracy-latency trade-offs and justify configuration decisions
- 3.4 Analyze observability challenges and select monitoring strategies at scale
- 3.5 Design a RAG pipeline with appropriate chunking and indexing strategies
- 3.6 Apply retrieval strategies matched to data shape and query pattern
- 3.7 Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent)
- 3.8 Evaluate progressive discovery vs. monolithic context strategy

### Domain 4: Evaluation, Testing & Optimization (16%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

- 4.1 Define evaluation metrics (accuracy, latency, cost, safety, security)
- 4.2 Design evaluation datasets and test frameworks using mixed methodologies
- 4.3 Conduct A/B testing and iterative improvements
- 4.4 Diagnose system issues (prompt failure, hallucinations, model mismatch)
- 4.5 Optimize token usage, latency, and cost-performance trade-offs
- 4.6 Monitor system performance using logging and observability tools

### Domain 5: Governance, Safety & Risk Management (14%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

- 5.1 Implement guardrails and safety controls
- 5.2 Identify risks, limitations, and failure modes of LLM systems
- 5.3 Apply human-in-the-loop validation strategies
- 5.4 Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP)
- 5.5 Address ethical AI considerations (bias, fairness, transparency)

### Domain 6: Stakeholder Communication & Lifecycle Management (14%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

- 6.1 Conduct structured discovery and requirement gathering
- 6.2 Communicate architectural decisions and trade-offs
- 6.3 Manage stakeholder feedback loops and expectation alignment (including SLAs)
- 6.4 Document architectures and provide implementation guidance
- 6.5 Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

### Domain 7: Developer Productivity & Operational Enablement (7%)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

- 7.1 Configure Claude tools and environments for teams (e.g., Claude Code)
- 7.2 Improve developer workflows using AI-assisted tooling
- 7.3 Support debugging and operational issue resolution

### Official "How to Prepare" (Section 7, verbatim)

[source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

> There is no single required course. Anthropic does not guarantee that any particular resource ensures a passing result.

- Study the exam blueprint in Section 6 and self-assess against each objective
- Review official Anthropic documentation for the Claude API, models, prompt engineering, MCP, and Skills
- Build and operate at least one end-to-end Claude solution, including RAG, evaluation, and observability
- Practice architectural decision-making: model selection, integration protocols, and security trade-offs
- Complete the sample questions in Section 8 to familiarize yourself with item style

## Sample questions

Section 8, verbatim. "These illustrative items show the style and cognitive level of the exam. They are not drawn from the live item bank." [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

**Sample 1 · Domain 3 — Integration**

A team exposes a customer-support agent that can read tickets, draft replies, issue refunds, and delete user accounts. Support staff only ever need to read tickets and draft replies. Applying least-privilege principles, which change best reduces risk?

- A. Add logging to the refund and delete tools so misuse can be audited later.
- B. Remove the refund and delete tools from the agent's configuration entirely.
- C. Keep all tools but add a confirmation prompt before refunds and deletions.
- D. Replace the agent with a larger model that follows instructions more reliably.

**Answer: B.** "Least privilege means removing capabilities the role does not require, eliminating the attack surface rather than monitoring or guarding it. Logging (A) and confirmations (C) are detective/compensating controls, not removal of unnecessary privilege; model size (D) is unrelated to authorization scope."

**Sample 2 · Domain 2 — Models, Prompting & Context**

An application sends the same 8,000-token system prompt and policy document on every request, followed by a short, varying user message. Latency and cost are both concerns. Which optimization most directly addresses both?

- A. Truncate the policy document to the first 1,000 tokens.
- B. Switch to the smallest available model regardless of task fit.
- C. Place the static system prompt and policy before the dynamic content and enable prompt caching.
- D. Move the policy document into a few-shot example block.

**Answer: C.** "Ordering stable content first and enabling prompt caching lets repeated prefixes be reused, reducing both time-to-first-token and per-request cost without discarding required context. Truncation (A) loses needed policy; downsizing blindly (B) risks quality; relocating to few-shot (D) does not create a cacheable, reusable prefix."

**Sample 3 · Domain 4 — Evaluation & Optimization**

A RAG system suddenly returns confident but incorrect answers after a document refresh, while latency and model version are unchanged. What is the most likely first place to investigate?

- A. The model weights have silently changed.
- B. The retrieval/indexing step is returning irrelevant or stale chunks.
- C. The temperature setting is too low.
- D. The context window has shrunk.

**Answer: B.** "Confident-but-wrong answers following a document refresh, with model and latency unchanged, point to retrieval feeding the model poor context, for example a broken re-index or mismatched embeddings. The other options would not be triggered specifically by a document refresh."

Observations [inferred]:

- All three samples are standalone single-answer items with a short stem (2–3 sentences). None uses a shared scenario.
- The distractor pattern repeats: a compensating control instead of a root fix (Sample 1 A/C), a blunt trade-off that sacrifices quality (Sample 2 A/B), and an exotic cause instead of the obvious changed variable (Sample 3 A/D).
- The guide publishes 3 samples. The CCAR-F guide publishes 12 samples plus a "Preparation Exercises" section. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf]

## Prep path

### Path overview

[source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional]

Title: "Claude Certified Architect - Professional Prep Course". Price: "Register | FREE". The exam-prep index lists it as "5 Courses". [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional] [source: https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses]

Tagline (verbatim):

> Learn to design, integrate, and govern production-grade Claude systems end to end, and to defend those design decisions to the stakeholders who fund and approve them.

Description (verbatim):

> By the time an Architect is involved, the question is no longer whether Claude can do the task; it is whether the systems around Claude will integrate and operate as needed. A reference architecture chosen incorrectly is expensive to switch, an integration that skips security review never reaches production, a safety control merely assumed fails at the worst moment, and a design that only the Architect understands falls apart the moment they leave the room. These decisions, what work Claude owns, what form that work takes, which architecture fits, and where each control sits, are made before anyone writes a line of code. This course teaches the end-to-end system designer to make those decisions, defend them against credible alternatives, and deliver solutions that pass security review, earn stakeholder sign-off, and outlast the handoff.

Path learning objectives (verbatim, "By the end of this course, you'll be able to:"):

- Translate an ambiguous business problem into a scoped Claude solution, selecting the reference architecture, model, context strategy, and entry point that keep it accurate and cost-conscious
- Take a solution from proof of concept to production by mapping cost, latency, and reliability to a budget and specifying the integration patterns an enterprise will accept
- Design the full safety stack for a Claude system, placing input screening, output screening, and tool-call authorization so the system fails closed rather than open
- Build evaluations as acceptance criteria and use them as the gate before any model or architecture change
- Route decisions to the right reviewer based on confidence, reversibility, and cost, and map each compliance obligation to a named control, owner, and evidence artifact
- Run structured discovery with non-technical stakeholders, present architectural trade-offs they can act on, and design a handoff that survives your absence
- Enable a team to adopt and operate a live Claude system, from shared configuration and rollout to developer workflows and operational issue resolution

Prerequisites (verbatim): "Before starting this course, we recommend you complete: Claude 101, Claude Code in Action, AI Fluency: Framework & Foundations, Building with the Claude API, Introduction to Model Context Protocol, and AI Capabilities and Limitations."

Who this is for (verbatim): "The Claude Certified Architect Professional course is for the end-to-end Claude system designer who shapes and delivers client solutions from discovery through production design. It suits individuals with experience designing, building, and delivering production-grade AI solutions and using Claude in an architect role."

### Lessons

| # | Lesson | Minutes | Card description (verbatim) | Likely domains [inferred] |
|---|--------|---------|------------------------------|---------------------------|
| 1 | Claude Platform & Solution Design | 238 | "Master the design decisions that translate an ambiguous business problem into a defensible Claude solution architecture." | D1, D2, part of D3 (entry points) |
| 2 | Enterprise Integration & Production | 158 | "Learn to take a designed solution from proof of concept to enterprise-ready production." | D3, D4 |
| 3 | Responsible AI, Safety & Risk for Architects | 114 | "Design the full safety stack for a Claude system, placing each control and deciding what happens when one fails." | D5 |
| 4 | Stakeholder Engagement, Lifecycle & GTM | 178 | "Lead the stakeholder conversations that decide whether a working system actually ships, adopts, and outlasts your involvement." | D6 |
| 5 | Team Enablement & Operational Productivity | 45 | "Learn to enable a team to adopt a live Claude system and run it without depending on you." | D7 |

Titles, minutes, descriptions: [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional]. Total 733 minutes (about 12.2 hours). [inferred]

Lesson pages show "About this course" and learning objectives publicly. Module and sub-lesson lists sit behind Skilljar sign-in and were not visible. [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/claude-platform-solution-design]

#### Lesson 1: Claude Platform & Solution Design (238 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/claude-platform-solution-design]

> Designing solutions with Claude goes beyond choosing a model. Four decisions come before you build: what work Claude owns, what form it takes, which reference architecture to commit to, and which model and context strategy keep the solution accurate and affordable. This module builds the framework for making those decisions, translating a vague request into a proposed solution, and defending your choices against credible alternatives.

- Break down a stakeholder's request into what Claude does, what existing systems do, and what humans do, using the four properties of generative AI as your decision lens
- Choose between an augmented call, a workflow, and an agent by naming what each choice costs
- Pick a reference architecture pattern for the problem shape in front of you and recognize when retrieval is doing a job that live-state should own
- Make defensible model, context-window, and context-strategy decisions, and use evaluations as the gate before any model swap
- Know where each platform entry point fits (Claude.ai, the API, an SDK, Claude Code, or an MCP server) and what customization belongs at each layer
- Distinguish between the Claude entry points a user sees, the build-time interfaces an engineer codes against, and the delivery routes an enterprise procures, and identify which are ruled out by governance or regulated-industry constraints before any other trade-off applies

#### Lesson 2: Enterprise Integration & Production (158 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/enterprise-integration-production]

> A prototype proves Claude can do the task; a production system proves it will keep doing it under real load, cost, and scrutiny. This module covers the specifics that close that gap: quality gates, cost and reliability modeling, feasibility analysis, enterprise integration, and the experimentation methods that confirm a change works before it ships.

- Define success criteria and build an eval suite before writing the first line of production code, distinguishing model-based from code-based evals, selecting eval workflow stages, and using evals as the gating mechanism for any change to a production system
- Work through the POC-to-production checklist, mapping cost and latency to a budget, specifying reliability patterns (retries, fallbacks, circuit breakers), naming failure modes for the chosen architecture, and articulating the mitigation for each, including how to make agentic workflows production-reliable
- Create a use case by estimating call volume, token consumption, and cost, assess technical feasibility against the four AI properties from AI Fluency Foundations, and translate a business problem into a scoped solution architecture with explicit boundary conditions
- Architect a Claude deployment that is ready for the enterprise by specifying integration patterns for compliance, identity (SSO/OAuth), authorization, data handling, and observability instrumentation, placing the right integration (API, SDK, MCP, Claude Code) at each integration point
- Plan and interpret an A/B test or structured experiment on a live Claude system, setting the hypothesis, selecting metrics, estimating the required sample size, and reading a result without overclaiming

#### Lesson 3: Responsible AI, Safety & Risk for Architects (114 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/responsible-ai-safety-risk-for-architects]

> This module addresses the major security question for a live Claude system: what controls stop Claude from refusing a valid request, producing an unfair outcome, or taking an unapproved action. Safety is a set of controls spanning the request path, each with a blind spot the next must catch. The Architect places each one and decides what happens when it fails, because assuming Claude enforces a rule it was never given is the most common way a safety design will break.

- Distinguish between what the model's training reduces and what your application layer must still enforce
- Place input screening, output screening, and tool-call authorization at the appropriate points in the request path and determine when to use model-based versus deterministic checks, so the system fails closed instead of failing open
- Identify where unequal outcomes can arise within a system and define the explanations required for users, regulators, and your own debugging team, so fairness and transparency are built into the design
- Route decisions to the appropriate reviewer/decision maker based on confidence, reversibility, and the cost of a wrong answer, so review effort is focused on the decisions that warrant them
- Map each compliance obligation to a named control, an owner, and an evidence artifact, so the architecture can be accurately audited

#### Lesson 4: Stakeholder Engagement, Lifecycle & GTM (178 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/stakeholder-engagement-lifecycle-gtm]

> You have built systems that work. This module is about the people who decide whether those systems ship and adopt. A finished design still depends on stakeholders: the discovery that sets the real requirements, the meeting that approves or rejects a trade-off, and the handoff that determines whether it lasts. This module covers that work, from structured discovery through trade-off presentations, lifecycle feedback loops, and cross-platform delivery.

- Run a structured discovery conversation with a non-technical stakeholder and translate what you learn into architectural requirements and documented assumptions, so the design traces back to the business case rather than to your own technical preference
- Present an architectural trade-off in terms a business stakeholder can act on by pairing each choice with a cost, a risk, and what a reversal would take, so executive and procurement reviews reach a decision instead of stalling
- Build and operate a stakeholder feedback loop across the deployment lifecycle, naming what triggers review, what an SLA breach requires, and when to iterate versus re-architect, with governance checkpoints built into the same loop
- Lead the Architect's role in a partner go-to-market motion through discovery, a scenario-based demo, technical objection handling, and joint scoping with the Anthropic Applied AI team, so an enterprise opportunity does not stall on questions only you can answer
- Select the deployment entry point and cross-platform strategy for a multi-platform production system, comparing the direct API, Bedrock, Vertex, and third-party routes on latency, compliance, and cost, then produce an outcome document that makes the value legible to a non-technical sponsor and reusable as partner IP

#### Lesson 5: Team Enablement & Operational Productivity (45 min)

[source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/developer-productivity-enablement]

URL slug is `developer-productivity-enablement`, which matches the Domain 7 name. [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional]

> Designing, integrating, and governing a Claude deployment is one job; getting a team to adopt it well is another. This module is about the team around a live system: helping people adopt Claude and stay productive once the system is running. It assumes the system is built and asks how a team adopts it well and keeps it healthy without pulling the Architect into every issue.

- Configure Claude tooling and environments for a team, including the shared configuration, the rollout pattern, the Skills distribution strategy, and the spend controls that belong in team setup
- Improve developer workflows with AI tooling and define the review discipline that keeps AI-generated work trustworthy before it reaches production
- Support debugging and operational issue resolution by connecting symptoms to architecture causes and building the team toward self-sufficiency

### Prep time vs exam weight [inferred]

| Lesson | Share of 733 min | Mapped exam weight |
|--------|------------------|--------------------|
| 1 Platform & Solution Design | 32% | D1 + D2 = 30% |
| 2 Enterprise Integration & Production | 22% | D3 + D4 = 35% |
| 3 Responsible AI, Safety & Risk | 16% | D5 = 14% |
| 4 Stakeholder, Lifecycle & GTM | 24% | D6 = 14% |
| 5 Team Enablement | 6% | D7 = 7% |

Integration and evaluation (35% of the exam) get proportionally less official prep time. Stakeholder/GTM gets proportionally more, partly because Lesson 4 includes partner GTM content (demos, objection handling, joint scoping) that has no matching CCAR-P objective. A course should over-index on D3/D4 relative to the official path. [inferred]

## Differences vs Foundations

### Architect – Foundations (CCAR-F) context

- Official exam code is **CCAR-F**. Community sites use "CCA-F". [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf]
- Launched 2026-03-12 with the Claude Partner Network: "Claude Certified Architect, Foundations, available today for partners." [source: https://www.anthropic.com/news/claude-partner-network]
- Guide Document Control: 0.1 Initial draft February 2026; 0.2 Draft revision June 2026; 1.0 Formatting and layout updates July 2026. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf]
- Price increased "from $99 to $125" effective June 30, 2026. [source: https://anthropic-partners.skilljar.com/page/faq-certifications]

CCAR-F blueprint (verbatim weights): [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf]

| # | Domain | Weight | Task statements |
|---|--------|--------|-----------------|
| 1 | Agentic Architecture & Orchestration | 27% | 1.1–1.7 |
| 2 | Tool Design & MCP Integration | 18% | 2.1–2.5 |
| 3 | Claude Code Configuration & Workflows | 20% | 3.1–3.6 |
| 4 | Prompt Engineering & Structured Output | 20% | 4.1–4.6 |
| 5 | Context Management & Reliability | 15% | 5.1–5.6 |

CCAR-F six scenarios (4 presented per exam): Customer Support Resolution Agent; Code Generation with Claude Code; Multi-Agent Research System; Developer Productivity with Claude; Claude Code for Continuous Integration; Structured Data Extraction. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf]

### Side by side

| Dimension | Foundations (CCAR-F) | Professional (CCAR-P) | Source |
|-----------|----------------------|-----------------------|--------|
| Fee | $125 | $175 | [source: https://anthropic-partners.skilljar.com/page/partner-certifications] |
| Items | 60 | 63 | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Time | 120 min | 120 min | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Structure | "4 scenarios drawn from a bank of 6" | No scenario bank listed; samples are standalone items | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Passing | 720 / 100–1,000 | 720 / 100–1,000 | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Validity | 12 months | 12 months | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Domains | 5 | 7 | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Objective format | 30 numbered task statements, each with "Knowledge of" and "Skills in" | 38 single-line objectives | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Recommended experience | "6+ months of practical experience building with Claude APIs, Agent SDK, Claude Code, and MCP" | "3+ years ... systems architecture or platform engineering" plus "6+ months ... Claude or comparable LLM-based systems in production" | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| Guide length | 39 pages, 12 samples, prep exercises, in/out-of-scope appendix | 11 pages, 3 samples, no exercises, no appendix | [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| FAQ framing | "Foundations proves an architect can build with Claude." | "Professional proves they can design and govern Claude solutions at enterprise scale." | [source: https://anthropic-partners.skilljar.com/page/faq-certifications] |
| Credential description | "for solution architects who design and build agent systems with Claude" | "the advanced credential, covering integration architecture, governance, and evaluation, built for the scale of large enterprises" | [source: https://claude.com/resources/articles/four-role-based-claude-certifications] |

### Content shift [inferred unless tagged]

- **New domains.** CCAR-P Domains 5 (Governance, Safety & Risk, 14%), 6 (Stakeholder Communication & Lifecycle, 14%), and 7 (Developer Productivity & Operational Enablement, 7%) have no CCAR-F counterpart. Together they are 35% of CCAR-P. A third-party site states the same figure. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://claudecertificationguide.com/blog/claude-certified-architect-professional-exam-guide]
- **Altitude.** CCAR-F tests implementation detail: `stop_reason` handling, `tool_choice`, `.mcp.json` scoping, `.claude/rules/` globs, `fork_session`, `-p` in CI, Message Batches API. CCAR-P objectives name no API parameters, file paths, or CLI flags. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]
- **CCAR-F out-of-scope topics that CCAR-P objectives name explicitly.** Each pair is sourced; the conclusion that these moved into scope is mine. Treat them as high-priority gaps for anyone coming from CCAR-F prep.

| CCAR-F out-of-scope (verbatim) [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] | CCAR-P objective or prep text that covers it |
|---|---|
| "Prompt caching implementation details (beyond knowing it exists)" | Obj 2.5 "Implement prompt reuse strategies (caching, modular prompts, Skills)"; Sample 2 [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| "Embedding models or vector database implementation details" | Obj 3.5 "Design a RAG pipeline with appropriate chunking and indexing strategies"; Sample 3 answer cites "mismatched embeddings" [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| "OAuth, API key rotation, or authentication protocol details" | Obj 3.2 "Analyze authentication and authorization requirements"; Lesson 2 "identity (SSO/OAuth), authorization" [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/enterprise-integration-production] |
| "Specific cloud provider configurations (AWS, GCP, Azure)" | Lesson 4 "comparing the direct API, Bedrock, Vertex, and third-party routes" [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/stakeholder-engagement-lifecycle-gtm] |
| "Performance benchmarking or model comparison metrics" | Obj 2.1 "Select appropriate Claude models based on trade-offs"; Obj 4.1 metrics [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] |
| "Constitutional AI, RLHF, or safety training methodologies" | Lesson 3 "Distinguish between what the model's training reduces and what your application layer must still enforce" [source: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/responsible-ai-safety-risk-for-architects] |

- **Overlap.** Multi-agent orchestration (F D1 ↔ P 1.4), task decomposition (F 1.6 ↔ P 1.5), tool scoping (F 2.3 ↔ P 3.1 "capability bloat"), MCP (F D2 ↔ P 3.7), few-shot prompting (F 4.2 ↔ P 2.3), human-in-the-loop (F 5.5 ↔ P 5.3), Claude Code team config (F D3 ↔ P 7.1). CCAR-F knowledge carries over at a higher level of abstraction. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]
- **New-to-CCAR-P technical items.** Agent-to-agent integration (3.7), progressive discovery vs. monolithic context (3.8), A/B testing (4.3), regulatory compliance naming GDPR, HIPAA, FedRAMP (5.4), bias/fairness/transparency (5.5), business value pillars and SLAs (1.6, 6.3). [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]

## Community reports (all unofficial)

The certification NDA forbids discussing questions "in any form, including in study groups and online forums", so first-hand reports are thin on item content. [source: https://anthropic-partners.skilljar.com/page/policies-certifications]

### First-hand reports

1. **vkorost (GitHub README), verified fetch.** "I sat CCAR-P on 1 September 2026 and passed with a scaled score of 973 against a pass mark of 720, missing 2 questions on the whole exam." The author wrote a 21-chapter guide covering "all 38 objectives across the seven exam domains" and states "the exam tests decisions, not features. Much of what it asks has no documentation page behind it, because it is asking how an architect behaves and not how Claude behaves." The author mentions "permission modes and the boundary that gets forgotten" under Governance and "which layer a setting belongs at given who is supposed to be able to override it" under Domain 7. The Credly link in the README loaded only a page shell; earner and date were not visible. The score claim is self-reported. [source: https://github.com/vkorost/claude-certified-architect-professional-guide]
2. **Level Up Coding article, "I passed the Claude Certified Architect Professional (CCAR-P) exam in two days of prep".** Fetch failed (HTTP 403). The search snippet mentions least-privilege tool design and the RAG document-refresh case, which match the official sample questions. It may restate the guide. [unverified]
3. **LinkedIn post by "yeolouis", "Passing the Anthropic Claude Certified Architect Professional (CCAR-P) exam during my second week of paternity leave".** Fetch failed (HTTP 999). The search snippet reports a score of 896/1000. [unverified]

### Secondary write-ups (no first-hand exam experience)

- claudecertificationguide.com (2026-07-24, labelled "independent community resource, not affiliated with or endorsed by Anthropic"): "Professional (CCAR-P) is standalone-item, 63 items, seven domains". The author does not claim to have sat the exam. [source: https://claudecertificationguide.com/blog/claude-certified-architect-professional-exam-guide]
- FlashGenius (updated 2026-08-14, not affiliated): "CCAR-P is harder for most candidates because the questions are likely to demand broader judgment." The author cites no candidate reports. [source: https://flashgenius.net/guides/claude-architect-foundations-vs-professional-ccar-f-vs-ccar-p]
- GitHub hosts many unofficial CCAR-P study repos and practice banks (e.g., Amey-Thakur/CLAUDE-CERTIFICATIONS, jrajath94/ccar-p-study-guide, gsaini/claude-certified-architect-prep). I checked seven READMEs for first-hand claims; only vkorost had one. [source: https://github.com/vkorost/claude-certified-architect-professional-guide]
- Commercial prep (Udemy, Learning Tree, Pluralsight, Training Camp, Tutorials Dojo, Preporato, Educative) exists. None was fetched or evaluated. [unverified]

### Takeaways for the course [inferred]

- Expect standalone decision items: "best change", "most likely root cause", "first place to investigate".
- Correct answers favour removing the root cause over compensating controls, deterministic enforcement over prompt-only rules, and evals as the gate before changes.
- Stakeholder and governance items test architect behaviour (discovery, trade-off framing, control-to-owner-to-evidence mapping) more than product facts.

## Open questions

- **Cancellation window conflict.** Guide Section 10 says 24 hours; FAQ and Policies say 48 hours. The Policies page says the Terms and Conditions and Exam Policy override it. Teach 48 hours (stricter, two official pages) and flag the conflict? [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf] [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://anthropic-partners.skilljar.com/page/policies-certifications]
- **Scenario format.** The FAQ says all exams use "multiple choice and scenario-based multiple response questions". The CCAR-P guide lists no scenario bank and its samples are standalone. Does the live CCAR-P exam use shared scenarios? Unresolved. [source: https://anthropic-partners.skilljar.com/page/faq-certifications] [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]
- **Unscored items.** The guide says weights apply to "scored items" and does not say whether any of the 63 items are unscored pretest items. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]
- **Prep module detail.** Sub-lesson lists for the five prep lessons require Skilljar sign-in with a partner account. An enrolled partner account would let the course map lessons to objectives exactly.
- **Domain 7 tooling scope.** Objective 7.1 says "e.g., Claude Code" and Lesson 5 mentions "Skills distribution" and "spend controls". How much Claude Code admin/settings detail to teach is a judgment call.
- **Model names.** CCAR-P objectives do not name specific Claude models. Teach model-selection reasoning (capability, latency, cost) rather than a model lineup that will date quickly.
