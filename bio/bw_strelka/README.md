## Usage

Note that the files for strelka *must* have a '/' in them, even if only
a local file.  

```
rule strelka:
    input:
        tumor_bam="results/bam/{source}/DNA/{source}_tumor_alllibs.md.bam",
        normal_bam="results/bam/{source}/DNA/{source}_normal_alllibs.md.bam",
        tumor_bai="results/bam/{source}/DNA/{source}_tumor_alllibs.md.bam.bai",
        normal_bai="results/bam/{source}/DNA/{source}_normal_alllibs.md.bam.bai",
        ref = config['FASTA'],
        configfile = './config.ini'
    output:
        snvs = "results/bam/{source}/DNA/strelka/results/passed.somatic.snvs.vcf",
        allsnvs = "results/bam/{source}/DNA/strelka/results/all.somatic.snvs.vcf",
        indels = "results/bam/{source}/DNA/strelka/results/passed.somatic.indels.vcf",
        allindels = "results/bam/{source}/DNA/strelka/results/all.somatic.indels.vcf"
    params:
        outdir="results/bam/{source}/DNA/strelka/results/"
    wrapper: "file:bio/bw_strelka"
```

And an example cluster config:

```
    "strelka" :
    {
	"time" : "24:00:00",
	"mem"  : "10000",
	"threads" : "24",
	"lscratch" : "100"
    }
```
	
