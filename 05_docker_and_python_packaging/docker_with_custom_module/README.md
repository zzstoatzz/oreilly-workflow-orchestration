This is an example of how to run the setup for Docker RunConfig + Local Storage.

The `setup.py` is to make this a module so that I can import the components. Use `pip install -e .` to install your module in the Docker image.

Steps

1. Build the Docker image with `docker build . -t test:latest`
2. Register the flow with `python workflow/flow.py`
3. Start your agent with `prefect agent docker start`
4. Run the flow with a `Quick Run` from the UI
