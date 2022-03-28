# Getting Started with Workflow Orchestration

<p align="center">
   <img src="https://www.prefect.io/assets/img/prefect-logo-gradient-navy.0cb04f87.svg" width="500" style="max-width: 500px;">
</p>

**Build, run, and monitor data pipelines at scale**

Prepared for [O'Reilly Media](https://www.oreilly.com/live-events/getting-started-with-workflow-orchestration/0636920069056/0636920069055/)

## Instructors:

* [Kalise Richmond](https://www.linkedin.com/in/kaliserichmond/) - Sales Engineer, Prefect
* [Nathan Nowack](https://www.linkedin.com/in/nathan-nowack-a6b59b143/) - Solutions Engineer, Prefect

## About this course:

Data engineers and scientists spend most of their time on negative or defensive engineering, writing code to handle unpredictable failures such as resources going down, APIs intermittently failing, or malformed data corrupting data pipelines. Workflow orchestration tools help eliminate negative engineering, allowing engineers and scientists to focus on the problems they are solving. Modern data applications have evolved, and orchestrators such as Prefect are providing more runtime flexibility and the ability to leverage distributed compute through Dask.

Discover how workflow orchestration can free you up to build solutions, not just avert failures. You’ll learn about basic orchestration features such as retries, scheduling, parameterization, caching, and secret management, and you’ll construct real data pipelines.

## Let's get our development environment set up! 🚀

For this course you will need:

### Python

Python greater than version 3.6 is required. Version 3.6 is reaching end of life soon.

* Packages in the `requirements.txt` file
    * prefect==2.0b2 - workflow orchestration
    * beautifulsoup4 - web scraping
    * jupyter        - interactive notebooks

Ideally, you can create a virtual environment (conda, pipenv, poetry) to install the dependencies.

To install the requirements with pip:

```
pip install -r requirements.txt
```

### Docker

<p align="left">
   <img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" width="200" style="max-width: 200px;">
</p>


[Docker](https://www.docker.com/) is a great entrypoint (pun somewhat intended) into world of engineering! We'll be using it to provide reproducible environments to execute our workflows in. We also have a section devoted to Docker.

- [To install Docker](https://docs.docker.com/engine/install/)

### Optional Dependencies

These are optional dependencies but were added in the `requirements.txt` for convenience.

<p align="left">
   <img src="https://raw.githubusercontent.com/airbytehq/airbyte/f8ce9f2155fb1687fa12dcfbe7705cc70dc2898d/docs/.gitbook/assets/airbyte_new_logo.svg" width="200" style="max-width: 200px;">
   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Snowflake_Logo.svg/2560px-Snowflake_Logo.svg.png" width="200" style="max-width: 200px;">
   <img src="https://raw.githubusercontent.com/dbt-labs/dbt-core/fa1ea14ddfb1d5ae319d5141844910dd53ab2834/etc/dbt-core.svg" width="200" style="max-width: 200px;">
</p>

For the advanced section of this course, we will use a couple of common data engineering tools:
- your own [Airbyte](https://docs.airbyte.com/#quick-start) instance
- [Snowflake trial account](https://signup.snowflake.com)
- install [dbt](https://docs.getdbt.com/dbt-cli/install/overview) to run transforms on your warehouse objects

## Cloning the repo 

<p align="left"> To clone the repo and run locally 
   <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="20" style="max-width: 20px;">
</p>

```
git clone https://github.com/zzstoatzz/oreilly-workflow-orchestration.git
```

And then each notebook can be viewed and executed. Some of the code will extend beyond the notebooks because data workflows glue other tools (sometimes non-Python) together.

## Contact Us

For any questions, feel free to reach to out us!

* Kalise - kalise@prefect.io
* Nate - nate@prefect.io

The [Prefect Slack](https://www.prefect.io/slack/) is also a good resource for Prefect and Workflow Orchestration questions.

## Further Resources

Listed below are the documentation pages for the tools used:

Data Movement 

* [Prefect](https://orion-docs.prefect.io/)
* [Airbyte](https://docs.airbyte.com/)
* [dbt](https://docs.getdbt.com/)
* [Snowflake](https://resources.snowflake.com/)

Distributed Computing

* [Dask](https://docs.dask.org/en/latest/)
* [Ray](https://docs.ray.io/en/latest/)
