# oreilly-course

Outline:
Course Overview (10 min)
* Presentation: Introductions and Welcome
* Presentation: Overview of Materials

Negative Engineering and Workflow Orchestration (20 min): 
* Presentation: 
* Negative Engineering - How Production Data Pipelines can Fail
* Consequences of Pipeline Failures
* Common Workflow Patterns
* Exercise: Native Python Work Example
* Presentation: The Need for Workflow Orchestration
* Discussion: What Can You Use Workflow Orchestration For?
* Q&A

Prefect and Basic Orchestration Features (30 min): 
* Presentation: 
* Retries, Parameters, Timeouts
* Scheduling
* Task Library
* Secrets
* Async execution
* Exercise: Putting Together a Simple Data Pipeline
* Q&A

Break (5 min)

Docker and Python Packaging (25 min):
* Presentation: 
* The need for Docker
* How to create a Python Package
* Uploading an image to a registry
* Exercise: Building a simple image
* Q&A



Using Distributed Compute for Parallel Execution (Dask) (20 mins):
* Presentation: 
* What is Dask?
* What makes Dask good for distributed compute?
* Depth-first execution/mapping
* Using Dask for parallelizing tasks
* Exercise: Running a Flow on Dask 
* Q&A

Advanced Patterns and Subflows (20 min)
* Presentation: 
* Typing and Pydantic
* Orchestration Pattern with Flow of Flows
* Breaking the DAG
* The need for runtime flexibility
* Analytics on top of workflow history
* Exercise: Running a Flow without pre-registered components
* Discussion: What use cases need runtime flexibility?
* Q&A

Break (10 min)

Putting a Real Pipeline Together (30 mins):
* Presentation: 
* ELT introduction
* Introduction to Airbyte
* Introduction to dbt
* Introduction to Snowflake
* Exercise: Constructing and running an end-to-end pipeline
* Q&A and Wrap Up


Oreilly Example:
https://resources.oreilly.com/binderhub/testing-data-pipelines-with-data-validation/-/tree/master/

To-Do:
1. Ask Oreilly about Demo (need Docker and UI access)
