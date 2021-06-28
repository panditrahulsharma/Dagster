first pipeline
https://docs.dagster.io/tutorial/intro-tutorial/single-solid-pipeline







commands:-
	dagster pipeline execute -f hello_world.py

	dagit -f hello_world.py


#-------------------------read the docs carefully----------
https://docs.dagster.io/getting-started


"""
Solids are individual units of computation that we wire together to form pipelines.
By default, all solids in a pipeline execute in the same process. In production environments,
Dagster is usually configured so that each solid executes in its own process.

In this section, we'll cover how to define a simple pipeline with a single solid, and then execute it.
"""


Solids are individual units of computation that we wire together to form pipelines. By default, all solids in a pipeline execute in the same process. In production environments, Dagster is usually configured so that each solid executes in its own process.

In this section, we'll cover how to define a simple pipeline with a single solid, and then execute it.