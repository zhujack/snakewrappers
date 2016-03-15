__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


shell("""
module load igvtools
igvtools count {snakemake.input} {snakemake.output} {snakemake.params.genome}
""")
