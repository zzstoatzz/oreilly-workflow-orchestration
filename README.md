# oreilly-course

Outline:
Course Overview (10 min)
* Presentation: Introductions and Welcome
* Presentation: Overview of Materials

Negative Engineering and Workflow Orchestration (20 min) - Kalise: 
* Presentation: 
* Negative Engineering - How Production Data Pipelines can Fail
* Consequences of Pipeline Failures
* Common Workflow Patterns
* Exercise: Native Python Work Example
* Presentation: The Need for Workflow Orchestration
* Discussion: What Can You Use Workflow Orchestration For?
* Q&A

Prefect and Basic Orchestration Features (30 min) - Kalise: 
* Presentation: 
* Retries
* Parameters - Validation
* Deployments - including Schedulling
* Task Library - GONE
* Secrets - GONE
* Async execution
* Exercise: Putting Together a Simple Data Pipeline
* Q&A

Break (5 min)

Using Distributed Compute for Parallel Execution (Dask) (20 mins) - Kalise:
* Presentation: 
* What is Dask?
* What makes Dask good for distributed compute?
* Depth-first execution/mapping
* Using Dask for parallelizing tasks
* Exercise: Running a Flow on Dask using Base Prefect Image
* Q&A


Docker and Python Packaging (25 min) - Nate:
* Presentation: 
* The need for Docker
* How to create a Python Package
* Uploading an image to a registry
* Exercise: Building a simple image
* Q&A
Resource: https://medium.com/the-prefect-blog/the-simple-guide-to-productionizing-data-workflows-with-docker-31a5aae67c0a


Advanced Patterns and Subflows (20 min) - Nate:
* Presentation: 
* Orchestration Pattern with Flow of Flows
* Breaking the DAG
* The need for runtime flexibility
* Analytics on top of workflow history (Prefect UI Dashboard and Filters)
* Exercise: Running a Flow without pre-registered components (native Python functions and if-else)
* Discussion: What use cases need runtime flexibility?
* Q&A

Break (10 min)

TO-DO:
Putting a Real Pipeline Together (30 mins) - Nate:
* Presentation: 
* ELT introduction
* Introduction to Airbyte
* Introduction to dbt
* Introduction to Snowflake
* Demo: Constructing and running an end-to-end pipeline
* Q&A and Wrap Up


Oreilly Example:
https://resources.oreilly.com/binderhub/testing-data-pipelines-with-data-validation/-/tree/master/

To-Do:
1. Ask Oreilly about Demo (need Docker and UI access) - can we just share a repo and then share screen?
2. Set date for dry run
