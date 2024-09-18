# Postmortem: Nginx Memory Allocation Outage

## Issue Summary
- **Duration**: 2024-09-15 14:00 UTC to 2024-09-15 15:30 UTC (1 hour 30 minutes)
- **Impact**: 70% of users experienced slow page load times or complete inaccessibility to our e-commerce platform. Users encountered timeouts and 502 errors when attempting to complete purchases or browse the website.
- **Root Cause**: Misconfigured memory allocation in the Nginx server caused it to be overwhelmed during a traffic surge, leading to critical processes failing.

## Timeline
- **14:00 UTC** – Issue detected via performance monitoring alert indicating high response times.
- **14:05 UTC** – On-call engineer notified by customer complaints of slow load times and failures during checkout.
- **14:10 UTC** – Initial investigations focused on network issues and potential external DDoS attacks.
- **14:20 UTC** – Misleading debugging path: suspected a memory leak caused by a new feature, rolled back the codebase, but the issue persisted.
- **14:35 UTC** – Memory usage metrics indicated server resource exhaustion; escalated to the infrastructure team.
- **14:45 UTC** – Investigations shifted to the Nginx server, revealing abnormal memory spikes.
- **15:00 UTC** – Discovered Nginx misconfiguration causing insufficient memory allocation.
- **15:15 UTC** – Nginx memory allocation adjusted, and the server was restarted.
- **15:30 UTC** – Full service restoration; performance returned to normal levels.

## Root Cause and Resolution
**Root Cause**: The Nginx `worker_rlimit_nofile` parameter was set too low, limiting the number of files and processes the server could handle. A sudden surge in traffic caused the server to run out of resources, resulting in memory exhaustion and 502 errors.

**Resolution**: The `worker_rlimit_nofile` parameter was increased to better handle traffic load. Server memory allocation was optimized, and the Nginx server was restarted, restoring normal functionality. Monitoring confirmed the platform's performance returned to normal.

## Corrective and Preventative Measures
- **Monitoring Enhancements**: Improve memory and resource usage monitoring for early detection of similar issues.
- **Stress Testing**: Enhance stress tests to simulate higher traffic loads and ensure the system can handle peak loads.
- **Configuration Audits**: Implement periodic audits of Nginx and server configurations to prevent misconfigurations.

### TODOs:
1. Add memory and process limit monitoring for all production servers.
2. Review and update Nginx server configuration to handle larger traffic loads.
3. Conduct quarterly stress tests simulating peak traffic scenarios.
4. Implement an automated script to verify configuration settings post-deployment.
5. Create a runbook for quicker identification of resource-related issues during future incidents.
