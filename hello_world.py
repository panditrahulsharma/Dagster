from dagster import pipeline, solid


@solid
def get_name():
    return "dagster"


@solid
def hello(context, name: str):
    context.log.info(f"Hello, {name}!")

@solid
def hello_world(context, name: str):
    context.log.info(f"Hello, {name}!")


@pipeline
def hello_pipeline():
    hello(get_name())
    hello_world(get_name())
