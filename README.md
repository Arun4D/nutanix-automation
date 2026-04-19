# Nutanix Automation with AIOps Multi-Agent Platform

This project implements an enterprise-grade AIOps platform on Nutanix covering Day 0, Day 1, and Day 2 operations using a multi-agent architecture. The system orchestrates provisioning, patching, scaling, and remediation by tying together Nutanix AHV, ServiceNow, and a Data Lake.

## Architecture & Features
- **Multi-Agent AI Architecture**: 
  - `Intent Agent`: Parses user intent from chat or prompts.
  - `Nutanix Data Agent`: Fetches AHV cluster telemetry (capacity, usage, networks) and syncs to a Data Lake.
  - `Decision Agent`: Evaluates risk and cluster capacity constraints to approve or halt operations.
  - `Action Agent`: Builds Nutanix automation payloads tailored for AHV operations.
  - `Insight Agent`, `Monitoring Agent`, `Risk Agent`, `ServiceNow Agent`, `Execution Agent` complete the lifecycle.
- **ServiceNow Governance**: All operations pass through SNOW for CMDB tracking and explicit Change/RITM approvals.
- **Data-Driven Operations**: Telemetry and historical execution data are stored in a Data Lake for analytical insights.
- **End-to-End Automation**: Outputs structured automation payloads for Day 1 (Provisioning) and Day 2 (Patching, Remediation) actions.

## Project Structure
- `ai_agents/`: Contains the core multi-agent orchestration logic.
  - `orchestrator.py`: The pipeline manager that coordinates parallel data gathering and sequential decision-making across agents.
  - `agents/`: The directory containing individual AI agents (e.g., `nutanix_data_agent.py`, `action_agent.py`).
- `agents.md`: The architectural blueprint and master prompt for the platform.

## Next Steps
- Integrate actual Nutanix Prism Central APIs inside `nutanix_data_agent.py`.
- Hook up Terraform and Ansible executors to consume payloads from `execution_agent.py`.
- Connect to a real SNOW instance in `snow_agent.py`.
