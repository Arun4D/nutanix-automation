# MASTER BUILD PROMPT (END-TO-END PLATFORM)

You are a Senior Platform Engineering, AIOps, and Cloud Automation Architect.

Help me DESIGN and BUILD a complete enterprise-grade AIOps platform on Nutanix covering Day 0, Day 1, and Day 2 operations using Terraform, Ansible, GitHub Actions, ServiceNow, Data Lake, Graph Database, and AI multi-agents.

I want practical, implementation-ready output (not theory).

---

# 🎯 OBJECTIVES

Build a platform that:

1. Automates full server lifecycle:

   * Day 0 (Foundation): Bare-metal provisioning. Automate node imaging, hypervisor installation (AHV), and cluster formation using **Nutanix Foundation APIs**.
   * Day 1 (Provisioning): Infrastructure-as-Code. 
    - Build base OS images (Gold Images) using **HashiCorp Packer** with the Nutanix AHV builder.
    - Provision Clusters, VMs, and Networks using the **Nutanix Terraform Provider**.
   * Day 1.5 (Configuration): OS-level setup. Deploy applications and harden OS configurations using **Ansible** or Nutanix Cloud Manager (NCM) Self-Service.
   * Day 2 (Operations): Maintenance and scaling.
    - Automate AOS, AHV, and Firmware updates via **Nutanix Lifecycle Manager (LCM) APIs**.
    - Implement auto-remediation, monitoring, and horizontal scaling.

2. Uses ServiceNow as the control plane:

   * All actions must go through ServiceNow (RITM or Change)
   * Utilizes standard SNOW Table API and Scripted REST APIs for bidirectional syncing
   * Exposes explicit Webhook receivers to trigger downstream execution engines upon approval
   * CMDB stores current state
   * Custom Activity Table stores lifecycle history

3. Provides full traceability:

   * Track every action:

     * Create, patch, deploy, resize, backup, migration
   * Track migration:

     * VMware / Hyper-V → Nutanix
   * Maintain lineage (old VM → new VM)

4. Implements AI Ops Assistant:

   * Chat-based interface (Backstage or UI)
   * Uses multi-agent architecture
   * Cannot bypass ServiceNow

5. Implements monitoring + auto-remediation:

   * Auto-configure monitoring during build
   * Alerts trigger AI → decision → ServiceNow → fix
   * Dev = auto execution
   * Prod = approval required

6. Uses Data Lake:

   * Store raw logs, metrics, activity events
   * Used for AI insights and analytics

7. Uses Graph Database:

   * Store relationships:

     * server → app → change → alert → migration
   * Enable lineage, impact analysis, root cause analysis

8. Provides dashboard:

   * Infra health
   * Alerts
   * AI actions
   * Server lifecycle timeline

---

# 🧱 REQUIRED ARCHITECTURE

Design the system with these layers:

1. User Layer:

   * Backstage / Chat UI

2. AI Layer (multi-agent):

   * Intent Agent
   * Decision Agent
   * Risk Agent
   * Insight Agent
   * Monitoring Agent
   * Action Agent
   * ServiceNow Agent
   * Execution Agent
   * Builder Agent (optional)

3. Governance Layer:

   * ServiceNow:

     * RITM
     * Change
     * CMDB
     * Activity Table

4. Orchestration Layer:

   * GitHub Actions

5. Execution Layer:

   * Terraform (infra provisioning)
   * Ansible (config, patching, apps)
   * Migration tool (VMware/Hyper-V → Nutanix)

6. Infrastructure Layer:

   * Nutanix AHV

7. Observability Layer:

   * Prometheus / Logs / Alertmanager
   * Grafana dashboard

8. Data Layer:

   * Data Lake (S3 / ADLS)
   * Graph DB (Neo4j or equivalent)

---

# 🔄 REQUIRED FLOWS (DETAILED)

Generate step-by-step flows for:

1. Server build (Day 0)
2. App deployment (Day 1)
3. Patch management (Day 2)
4. Auto-remediation (alerts → fix)
5. Resource scaling (CPU/disk expansion)
6. Migration (VMware/Hyper-V → Nutanix)
7. Audit / history query
8. AI-driven recommendation

---

# 🧠 AI DESIGN REQUIREMENTS

1. Multi-agent architecture
2. Each agent must have:

   * responsibility
   * API contract
3. Show interaction between agents
4. Show how AI uses:

   * ServiceNow (state)
   * Data Lake (history)
   * Graph DB (relationships)

---

# 🗄️ DATA DESIGN

Provide:

1. ServiceNow schema:

   * CMDB fields
   * Activity table structure

2. Event schema (JSON for pipelines)

3. Data Lake structure:

   * folder layout
   * partitioning

4. Graph DB schema:

   * nodes
   * relationships

---

# 🔌 INTEGRATION DESIGN

Provide:

1. API contracts:

   * AI ↔ ServiceNow
   * ServiceNow ↔ GitHub Actions
   * Pipeline → Data Lake
   * Graph builder service

2. Webhook design

---

# ⚙️ IMPLEMENTATION DETAILS

Provide:

1. GitHub Actions pipeline design
2. Terraform module structure
3. Ansible role structure
4. Migration workflow
5. Monitoring setup automation

---

# 🔐 GOVERNANCE RULES

* No production execution without approval
* Every action must:

  * have request ID
  * be logged
  * be traceable

---

# 📊 OUTPUT FORMAT

* Use diagrams (ASCII)
* Provide step-by-step flows
* Provide real implementation structure
* Avoid generic explanations

---

# 🚀 GOAL

I want to use your output to:

* Build PoC
* Scale to enterprise
* Implement AIOps with full automation + traceability

Focus on practical, production-ready architecture and implementation.


---

