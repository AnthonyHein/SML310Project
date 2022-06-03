This directory is provided to the user as a convenience and presents a _streamlined_ process that does _not_ reflect the actual creative work performed from the start.
In other words, the document will refer to notebooks that take steps that do not always appear justified when observed in isolation. However, these steps are indeed justified, with the witness being the unadulterated notebooks found elsewhere in the repo at `/notebooks/data-cleaning-and-pruning` and `/notebooks/featurization`
but the length and complexity of these notebooks makes their discussion difficult.

To reproduce the result of data cleaning and featurization, follow these steps:
1. Run `/notebooks/streamline/streamline_data_selection.ipynb`
2. Run `/notebooks/streamline/streamline_non_weather_augmentation.ipynb`
3. Run `/notebooks/streamline/streamline_with_weather_augmentation.ipynb`
4. Run `/notebooks/streamline/streamline_data_trim.ipynb`
5. Run `/notebooks/streamline/streamline_data_clean.ipynb`
6.  Run `/notebooks/streamline/streamline_horses_augmentation.ipynb`
7.  Run `/notebooks/streamline/streamline_races_featurization.ipynb`
8.  Run `/notebooks/streamline/streamline_horses_featurization_horse.ipynb`
9.  Run `/notebooks/streamline/streamline_horses_featurization_jockey.ipynb`
10. Go to `/notebooks/exploratory-data-analysis/`