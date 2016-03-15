__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


# assumes that bams are coming in as a list
inputs = ",".join(snakemake.input.bams)

shell("""
module load platypus
platypus callVariants --bamFiles={inputs} --output={snakemake.output} \
  --bufferSize=10000 --maxReads=10000000 \
  --refFile={snakemake.input.ref} --nCPU=${{SLURM_CPUS_ON_NODE}} \
  --filterDuplicates=1 --trimOverlapping=1 >& {snakemake.log}
""")
