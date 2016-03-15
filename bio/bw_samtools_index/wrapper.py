__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell



shell("""
(module load samtools
samtools index {snakemake.input} ) 2> {snakemake.log}""")

