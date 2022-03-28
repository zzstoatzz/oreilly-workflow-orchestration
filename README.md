# Intro to Workflow Orchestration

<p align="center">
   <img src="https://www.prefect.io/assets/img/prefect-logo-gradient-navy.0cb04f87.svg" width="500" style="max-width: 500px;">
</p>

**Build, run, and monitor data pipelines at scale**

Instructors:
[Kalise Richmond](https://www.linkedin.com/in/kaliserichmond/) - Sales Engineer, Prefect
[Nathan Nowack](https://www.linkedin.com/in/nathan-nowack-a6b59b143/) - Solutions Engineer, Prefect

About:
Data engineers and scientists spend most of their time on negative or defensive engineering, writing code to handle unpredictable failures such as resources going down, APIs intermittently failing, or malformed data corrupting data pipelines. Workflow orchestration tools help eliminate negative engineering, allowing engineers and scientists to focus on the problems they are solving. Modern data applications have evolved, and orchestrators such as Prefect are providing more runtime flexibility and the ability to leverage distributed compute through Dask.

Discover how workflow orchestration can free you up to build solutions, not just avert failures. You’ll learn about basic orchestration features such as retries, scheduling, parameterization, caching, and secret management, and you’ll construct real data pipelines.

Outline:
Course Overview (10 min)
* Presentation: Introductions and Welcome
* Presentation: Overview of Materials

Negative Engineering and Workflow Orchestration (20 min)
* Presentation: 
* Negative Engineering - How Production Data Pipelines can Fail
* Consequences of Pipeline Failures
* Common Workflow Patterns
* Exercise: Native Python Work Example
* Presentation: The Need for Workflow Orchestration
* Discussion: What Can You Use Workflow Orchestration For?
* Q&A

Prefect and Basic Orchestration Features (30 min) 
* Presentation: 
* Retries
* Parameters - Validation
* Deployments - including Schedulling
* Collections - Slack Task
* Async execution
* Exercise: Putting Together a Simple Data Pipeline
* Q&A

Break (5 min)

Using Distributed Compute for Parallel Execution (Dask) (20 mins)
* Presentation: 
* What is Dask?
* What makes Dask good for distributed compute?
* Depth-first execution/mapping
* Using Dask for parallelizing tasks
* Exercise: Running a Flow on Dask using Base Prefect Image
* Q&A


Docker and Python Packaging (25 min)
* Presentation: 
* The need for Docker
* How to create a Python Package
* Uploading an image to a registry
* Exercise: Building a simple image
* Q&A
Resource: https://medium.com/the-prefect-blog/the-simple-guide-to-productionizing-data-workflows-with-docker-31a5aae67c0a


Advanced Patterns and Subflows (20 min)
* Presentation: 
* Orchestration Pattern with Flow of Flows
* Breaking the DAG
* The need for runtime flexibility
* Analytics on top of workflow history (Prefect UI Dashboard and Filters)
* Exercise: Running a Flow without pre-registered components (native Python functions and if-else)
* Discussion: What use cases need runtime flexibility?
* Q&A

Break (10 min)

Putting a Real Pipeline Together (30 mins)
* Presentation: 
* ELT introduction
* Introduction to Airbyte
* Introduction to dbt
* Introduction to Snowflake
* Demo: Constructing and running an end-to-end pipeline
* Q&A and Wrap Up