__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

# note that strelka requires a ./ for a file in the working directory

shell("""
GB=`expr ${{SLURM_MEM_PER_NODE}} / 1024`
module load manta
TMPDIR=/lscratch/${{SLURM_JOB_ID}}/manta
configManta.py \
  --normalBam {snakemake.input.normal_bam} \
  --tumorBam {snakemake.input.tumor_bam} \
  --referenceFasta /data/CCRBioinfo/public/GATK/bundle/3.1/hg19/ucsc.hg19.fasta \
  --runDir ${{TMPDIR}}

python2 ${{TMPDIR}}/runWorkflow.py -m local -j ${{SLURM_CPUS_ON_NODE}} -g ${{GB}}
cp ${{TMPDIR}}/results/variants/* {snakemake.params.outdir}
cp ${{TMPDIR}}/results/stats/* {snakemake.params.outdir}
""")
