"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import add_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                add_data,
                inputs=None,
                outputs="example_iris_data"
            )
        ])
