**Propose me the design on How would you deploy software to 5000 systems?**

**Assumption :** All the IP’s are present in the Ansible inventory file (getting this info dynamic inventry).

**Requirements:**

***Deployment strategy:***
* Deployment of software:
	* Fresh installation. [Ansible playbooks]
		* Setup the software
			* 3 tier architecture
			* setup the task like pre_task ans post_task to bring up the applicationn
		*  Containerized - Microservice.
	* Changes on existing installations. [Ansible /Chef /Puppet]
		* Move towards configuration management system.
* Deployment of configuration:
	* Fresh setup:
		* Env based configurations.
			* Based on banks. [As we are financial organization]
			* Based on env type (prod, qa, uat)
			* Run Ansible Playbook locally based on config
	* Existing setup:
		* Move towards configuration management system.
* Testing strategy:
	* Although we will test the ansible playbooks before running it to 5000 systems , a mechanism is still needed to test the changes. I will write the health checks once the software is up & running and check the end point.
	* It is equivalent to liveness probes. Then we will qualify that servers are ready and emit the metric to the time series database (Cost involved) or we can store it in csv & ensure it is done properly.

    
**After installation how to manage/setup CI /CD for environments.**

 - Use Version Control
 - After raising diff
	 - run the unit-tests (use jenkins)
	 - run the functionality test (use jenkins)
	 - run the code-coverage (set the quality gates) (utlizae sonarqube)
	 - code review
	 - land code to version control
 - Use Monitoring and Rollback Triggers
	 - If request is success ratio drops - trigger rollback
	 - If multiple container restart happens - trigger rollback
 - Rollback - Types
	 - System level metrics
		 - CPU Load high
		 - Memory utilization high
		 - FD count increased
	 - Based on Application metrics
		 - Application thread count
		 - Unable to reach downstream services
	 - Based on Business metrics
		 - core business functionality
		 - customer unable to login (after deployment)
 - Use Controlled Environments
	 - QA
	 - UAT
	 - BETA (Pre-prod)
	 - PROD
	 - Canary
 - BlackBox monitoring (run test on out-side the corporate network)
	 - Any failure send notification (very important)