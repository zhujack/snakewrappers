## Description

Runs the [manta]() structural variant caller

## Usage

### Rule example

```
rule manta:
    output:
        vcfs = expand("results/bam/{{source}}/DNA/manta/results/{fname}",fname="candidateSmallIndels.vcf.gz  candidateSmallIndels.vcf.gz.tbi  candidateSV.vcf.gz  candidateSV.vcf.gz.tbi  diploidSV.vcf.gz  diploidSV.vcf.gz.tbi  somaticSV.vcf.gz  somaticSV.vcf.gz.tbi".split()),
        stats = expand("results/bam/{{source}}/DNA/manta/results/{fname}",fname="alignmentStatsSummary.txt  svCandidateGenerationStats.tsv  svCandidateGenerationStats.xml  svLocusGraphStats.tsv".split())
    input:
        tumor_bam="results/bam/{source}/DNA/{source}_tumor_alllibs.md.bam",
        normal_bam="results/bam/{source}/DNA/{source}_normal_alllibs.md.bam",
        tumor_bai="results/bam/{source}/DNA/{source}_tumor_alllibs.md.bam.bai",
        normal_bai="results/bam/{source}/DNA/{source}_normal_alllibs.md.bam.bai",
        ref = config['FASTA']
    params:
        outdir = "results/bam/{source}/DNA/manta/results/"
    wrapper: "file:bio/bw_manta"
```

### Cluster config

```
    "manta" :
    {
	"time" : "24:00:00",
	"mem"  : "20000",
	"threads" : "24",
	"lscratch" : "100"
    }
```
