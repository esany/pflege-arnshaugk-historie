# Execution Profile — ChatGPT Deep Research

**Date checked:** 2026-09-22  
**Applies to:** Generic System Analysis + Finding-Driven Deep Research Prompt v3  
**Not part of the vendor-neutral Core.**

Use this profile when executing the Core in ChatGPT and the task requires deep multi-source research.

1. Start the task in ChatGPT's dedicated **Deep research** mode (for example via `/Deepresearch` or the current Deep research entry point).
2. Provide the Core prompt plus the project/repository sources that the environment can actually read.
3. Review the proposed research plan before execution. Ensure it follows:
   `project reconstruction → problem clusters → Research Agenda → finding-driven research`
   rather than jumping directly to a generic literature survey.
4. During execution, intervene only if the research drifts away from material findings, skips central Tier-A clusters, or turns into solution design.
5. Preserve citations/source links and record major inaccessible source classes or repository-access limits.
6. The final report must follow the Core's stop boundary; Deep Research mode does not authorize solution synthesis.

Current OpenAI product documentation is the authority for how Deep research is activated and which sources it can access. Product UI and availability may change; do not copy those details into the Core method.

Reference checked 2026-09-22: https://help.openai.com/en/articles/10500283-deep-research
