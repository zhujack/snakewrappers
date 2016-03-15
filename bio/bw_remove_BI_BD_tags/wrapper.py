__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

# assumes that bams are coming in as a list

shell("""
module load samtools
( samtools view -h {snakemake.input} | \
  sed 's/\tBI\:Z\:[^\t]*//' | \
  sed 's/\tBI\:Z\:[^\t]*//' | samtools view -bS - > {snakemake.output} ) >& {snakemake.log}
""")
