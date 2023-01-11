"""
This is a boilerplate pipeline 'reporting'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import compare_passenger_capacity_exp, compare_passenger_capacity_go
from .nodes import create_confusion_matrix

def create_pipeline(**kwargs) -> Pipeline:
    """This is a simple pipeline which generates a plot"""
    return pipeline(
        [
            node(
                func=compare_passenger_capacity_exp,
                inputs="preprocessed_shuttles",
                outputs="shuttle_passenger_capacity_plot_exp",
            ),
            node(
                func=compare_passenger_capacity_go,
                inputs="preprocessed_shuttles",
                outputs="shuttle_passenger_capacity_plot_go",
            ),
            node(
                func=create_confusion_matrix,
                inputs="companies",
                outputs="dummy_confusion_matrix",
            ),
        ]
    )