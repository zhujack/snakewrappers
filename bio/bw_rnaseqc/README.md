rnaseqc

- memory usage: at least 22g

````
rule rnaseqc:
    input: bam="{base}/{sample}.bam"
    output: "rseqc/{sample}/metrics.tsv"
    params: 
        rulename="rnaseqc",
        sampleFile="'{sample}|{base}/{sample}.bam|{sample}'", 
        outDir="rseqc/{sample}",
        gencode_gc=config["gencode_gc"],
        gencode_annotation=config["gencode_annotation"],
        reference=config["reference"]
    version: config["rnaseqc"]
    log: "rseqc/{sample}/{sample}.bam.log"
    wrapper: "file:bio/bw_rnaseqc"
```