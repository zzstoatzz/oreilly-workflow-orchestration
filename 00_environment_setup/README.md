# Let's get our development environment set up! 🚀

docker is a great entrypoint (pun somewhat intended) into world of engineering! let's use it to follow along with some data engineering ideas:

## what we need
- terminal
- [docker engine installation](https://docs.docker.com/engine/install/)
- [Prefect Cloud Free account](https://universal.prefect.io/signin/register) (grab an API key and save it somewhere safe!)
- will to dev some ops and engineer some data

# what we'll do
- pull down a public [docker container image](https://docs.docker.com/get-started/overview/) with everything we need for our demo
- use our fancy container image to run a process locally that checks for work to run
- define and schedule work to run with prefect