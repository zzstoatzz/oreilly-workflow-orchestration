# Let's get our development environment set up! 🚀

docker is a great entrypoint (pun somewhat intended) into world of engineering! let's use it to follow along with some data engineering ideas:

## what we need
- install prefect
```console
$ pip install 'prefect==2.0b2'
```

- [install docker](https://docs.docker.com/engine/install/)


Optional:

- your own [airbyte](https://docs.airbyte.com/#quick-start) instance
- [snowflake trial account](https://signup.snowflake.com)
- install jupyter to interact locally with our notebooks
```console
$ pip install jupyter

$ cd ../../oreilly-course

$ jupyter notebook
```
- install [dbt](https://docs.getdbt.com/dbt-cli/install/overview) to run transforms on your warehouse objects

```console
$ pip install dbt-core dbt-snowflake
```