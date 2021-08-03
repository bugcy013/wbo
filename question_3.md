**CI - Stuff**

 - Start the containters
```
wbo  ➜ docker-compose up -d
Creating network "wbo_default" with the default driver
Creating my-jenkins ... done
Creating jjb        ... done
wbo  ➜ docker-compose ps
   Name                 Command               State                          Ports
---------------------------------------------------------------------------------------------------------
jjb          /bin/sh -c pip install jen ...   Up
my-jenkins   /sbin/tini -- /usr/local/b ...   Up      50000/tcp, 0.0.0.0:8083->8080/tcp,:::8083->8080/tcp
wbo  ➜
```

Note: If you starting freshly we need to the intail setup, like setup the password and install the plugins

```
# Get the initial admin password
docker exec my-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

 - How to list the jobs
```
wbo  ➜ jenkins-jobs  --conf ./jenkins-jobs.ini list

INFO:root:Matching jobs: 2
hello_dsl
hello_freestyle
```

 - How to create/update the jobs
```
wbo  ➜ jenkins-jobs  --conf ./jenkins_jobs.ini update jenkins-jobs
INFO:jenkins_jobs.cli.subcommand.update:Updating jobs in ['jenkins-jobs'] ([])
INFO:root:Caching type parameters of parameters = jenkins_jobs.modules.parameters:Parameters
INFO:root:Caching type builders of builders = jenkins_jobs.modules.builders:Builders
INFO:jenkins_jobs.builder:Number of jobs generated:  1
INFO:jenkins_jobs.builder:Creating jenkins job helloworld_job
INFO:jenkins_jobs.cli.subcommand.update:Number of jobs updated: 1
INFO:jenkins_jobs.builder:Number of views generated:  0
INFO:jenkins_jobs.cli.subcommand.update:Number of views updated: 0

```

* How to delete the job
```
wbo  ➜ jenkins-jobs  --conf ./jenkins-jobs.ini delete test-dsl
```