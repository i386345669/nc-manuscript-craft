# Synthetic evaluation fixture: resume and source update

Use the supplied skill to resume a small English manuscript. Do not start from scratch. All data below are invented for evaluation. No browsing, new analysis, translation or file-format generation is requested.

## Current saved state

- Mode: targeted revision of a mature descriptive resource paper.
- Accepted Introduction I-01 and Methods M-01 below are protected.
- Result R-02 is defined by source S-02, version 1 in the saved draft.
- Dependencies: abstract A-01, Results paragraph P-02, Table 1 T-01, Figure 2 legend L-02. None of the accepted Introduction/Methods text depends on the changed mean.
- New authoritative source S-02 version 2 corrects only the summer mean from 6.1 to 6.3 mg/L and its supplied difference from −2.2 to −2.0 mg/L. Other counts and the other-month mean remain unchanged.
- Desired output: updated affected texts, unchanged protected texts, a short change list and a resumable status summary. English only. Keep the observational interpretation and existing reference marker [1].

## Protected Introduction I-01

Stable station identifiers make it possible to follow the same monitoring locations over time. We organized monthly observations into station histories to support descriptive seasonal comparisons.

## Protected Methods M-01

Records were mapped to a fixed sampling dictionary. Descriptive means used complete records without imputation. Calculations used NumPy [1].

## Abstract A-01

The resource contains four station histories with 44 complete monthly records. Mean dissolved oxygen was 6.1 mg/L in summer and 8.3 mg/L in other months, a descriptive difference of −2.2 mg/L.

## Results P-02

The 11 complete summer records had mean dissolved oxygen of 6.1 mg/L. The 33 complete records from other months had a mean of 8.3 mg/L. The supplied descriptive mean difference was −2.2 mg/L. No inferential comparison was performed.

## Table 1 T-01

| Period | Complete records | Mean dissolved oxygen |
|---|---:|---:|
| Summer | 11 | 6.1 mg/L |
| Other months | 33 | 8.3 mg/L |

## Figure 2 legend L-02

Figure 2 | Seasonal descriptive means. Bars show 6.1 mg/L for summer and 8.3 mg/L for other months, based on 11 and 33 complete records, respectively. No error bars or inferential test are shown.

Reference marker [1] retains its existing software-attribution role. No new reference is requested. The evaluator specifies the only output file you may write.
