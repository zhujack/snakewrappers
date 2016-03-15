## Description

## Usage

### Rule

```
rule igvtools_count:
    input: "{base}.bam"
    output: "{base}.bam.tdf"
    params: genome="hg19"
    log: "logs/{base}.igvtools_count"
    wrapper: "file:bio/bw_igvtools_count"
```

### Cluster config

```
    "igvtools_count" :
    {
	"time" : "06:00:00",
	"mem"  : "6000"
    }
```
