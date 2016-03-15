platypus

- memory usage: at least 64g
- threads: up to 32

```
rule platypus:
    input: bams=_get_bams(), # as list of strings
           reference='path/to/fasta'
    output: temp("variant/germline/platypus/all_{chrom}.vcf") # regions not implemented yet
    params: batch="-l nodes=1:gpfs:g128 -q ccr"
    log: "variant/germline/platypus/logs/all_{chrom}.vcf.log"
    wrapper: "file:bio/bw_platypus"
```

Note: consider running on a per-chromosome basis and then combining.