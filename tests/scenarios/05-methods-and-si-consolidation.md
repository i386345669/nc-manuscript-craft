# Synthetic methods revision request

This is an invented teaching case. Produce a concise English main Methods paragraph and a consolidated Supplementary Methods section from the material below. Correct the current summaries where needed and eliminate duplicate descriptions. Keep a short record of where essential information was retained. Do not rerun models or calculate new performance results.

## Current main Methods

"We selected the threshold using Youden's index, averaging the resulting performance estimates over the runs. The default threshold was used when values were tied."

## Current Supplementary Methods

Section S2: "The classification procedure selected a threshold in each training run. Predictions from the runs were combined to obtain the final prediction. Records without an outcome were excluded."

Section S6: "Each run used the same candidate thresholds. A positive prediction included values equal to the final threshold. Records without an outcome were excluded before the inner split. The population was defined by the prespecified eligibility file, rather than by whether a prediction could be produced."

## Recorded execution

The execution manifest identifies code version `lesson-2`, configuration `cost-3`, and output `saved-2`. The author confirms that this code and configuration produced the supplied saved output.

```python
from statistics import median

def threshold_for_run(rows):
    return min(rows, key=lambda row: ((3 * row['fn'] + row['fp']) / row['n'], row['threshold']))['threshold']

selected = [threshold_for_run(rows) for rows in inner_oof_rows_by_run]
final_threshold = median(selected)
final_probability = {record: median(values) for record, values in outer_probabilities_by_record.items()}
predicted_positive = {record: p >= final_threshold for record, p in final_probability.items()}
```

Configuration: thresholds [0.20, 0.35, 0.50], false-negative cost 3, false-positive cost 1. `inner_oof_rows_by_run` contains predictions from the inner training procedure only. `outer_probabilities_by_record` contains held-out probabilities, with the same record identifiers in both runs. Performance was evaluated once on the aggregated held-out probabilities and classifications.

Saved selection table:

| Run | Threshold | False positives | False negatives | n |
|---|---:|---:|---:|---:|
| 1 | 0.20 | 12 | 1 | 100 |
| 1 | 0.35 | 8 | 2 | 100 |
| 1 | 0.50 | 5 | 4 | 100 |
| 2 | 0.20 | 11 | 1 | 100 |
| 2 | 0.35 | 7 | 2 | 100 |
| 2 | 0.50 | 4 | 3 | 100 |

Saved output: per-run thresholds 0.35, 0.35; final threshold 0.35. The manifest records no refitting after prediction aggregation.

