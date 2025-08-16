# ORACLE FUTURE • Hybrid Autonomous Quantum AI (Offline + Online Upgrade)
A futuristic Streamlit-based Immortal AI UI which works *fully offline*, but automatically unlocks advanced live integrations (OpenAI, JIRA, OracleDocs, Google OCR, etc.) simply by adding keys into a `.env` file — no code changes required.

---

## 🚀 Features (Hybrid Mode Enabled)

| Module                        | Offline Mode Ready ✅ | Auto-Upgradable 🔓  |
|-------------------------------|------------------------|---------------------|
| Audit Log Analyzer            | Yes                    | n/a                 |
| Voice-to-Text (Whisper)       | Yes (local CPU)        | Yes → cloud whisper |
| YouTube Transcript            | Yes (no-key)           | Yes → Google OCR    |
| Universal Search (PDF + YT)   | Yes (local RAG)        | Yes → Multi-RAG     |
| Oracle Error Lookup           | Yes (regex DB)         | Yes → GenAI+Docs    |
| Knowledge Graph               | Yes                    | -                   |
| Cosmic Apex Deploy (Sim)      | Yes                    | -                   |

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Recommended Deployment (Free VM)
Due to the large size of the AI models, this application requires significant disk space and may not run on free shared-hosting platforms like Streamlit Cloud.

**The best option is to use a free Virtual Machine (VM) from a major cloud provider.** This will give you the necessary resources and full control over the environment.

### Why a VM?
- **More Resources:** Free-tier VMs offer more disk space and memory.
- **Full Control:** Install any package or dependency without restriction.
- **No Platform Limits:** Avoid resource caps (disk, memory, CPU) and timeouts.

### How to Get a Free VM
- **Google Cloud Platform (GCP):** Offers an "Always Free" `e2-micro` VM.
- **Amazon Web Services (AWS):** Has a 12-month "Free Tier" for `t2.micro` VMs.
- **Oracle Cloud (OCI):** Provides a very generous "Always Free" tier with multiple VMs.

### Basic Steps to Deploy on a VM
1.  Choose a provider and create a free-tier Linux VM (Ubuntu is a great choice).
2.  Connect to your VM using SSH.
3.  Clone this Git repository onto the VM.
4.  Install Python and then run `pip install -r requirements.txt`. This should now complete successfully.
5.  Run the app: `streamlit run app.py --server.port 8080`
6.  Open the port (e.g., 8080) in your VM's firewall/security group settings so you can access the app from your web browser using the VM's public IP address.
