# example

```python
rule bedtools_coverage:
    input: "{base}.bam"
    output: "{base}.cov_hist.tsv"
    log: "logs/{base}.cov_hist.log"
    wrapper: "file:bio/bw_bedtools_coverage"
```
