__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell



shell("""
(module load fastqc; \
fastqc --extract -t {snakemake.threads} -o {snakemake.params.outdir} {snakemake.input} ) 2> {snakemake.log}""")


