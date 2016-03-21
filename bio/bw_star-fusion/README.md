star-fusion

- memory usage: at least 22g

````
rule star-fusion:
    input: "{base}/Chimeric.out.junction"
    output: "{base}/star-fusion.fusion_candidates.final.abridged"
    params: 
        rulename="star-fusion",
        batch="-c 2 --mem=22g --gres=lscratch:100",
        star_fusion_outdir="{base}",
        genome_lib_dir="/data/CCRBioinfo/public/STAR/GRCh37_gencode_v19_CTAT_lib"
    version: config["star-fusion"]
    log: "{base}/star-fusion.log"
    wrapper: "file:bio/bw_star-fusion"
```