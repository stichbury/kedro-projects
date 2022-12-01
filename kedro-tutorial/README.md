# kedro tutorial

## What is this?	
This is the basic starter for spaceflights (based on Kedro 18.4, so it is just two pipelines with no namespaces/modular pipeline stuff in it).

I've added a third pipeline to the starter code which I've called "reporting" and this is the test/example for the plotly/matplotlib charts in kedro viz.

There's a `my_shareable_pipeline.json` file in the project root which is the output of:

```bash
kedro run
kedro viz
kedro viz --save-file my_shareable_pipeline.json
```