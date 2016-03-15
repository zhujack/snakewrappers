__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell



shell("""
(module load bwa; module load samtools; bwa mem {snakemake.params.RG} -t ${{SLURM_CPUS_ON_NODE}} \
{snakemake.params.index} {snakemake.input.sample} \
  | samtools view -Sbh - \
  | samtools sort -m 20G -T {snakemake.params.prefix} -o {snakemake.output} - ) 2> {snakemake.log}""")

