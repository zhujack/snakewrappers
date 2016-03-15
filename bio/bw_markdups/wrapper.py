__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


shell("""
MEM="8"
        module load picard
java -Xmx${{MEM}}g -jar $PICARDJARPATH/picard.jar MarkDuplicates VALIDATION_STRINGENCY=SILENT I={snakemake.input} O={snakemake.output} AS=true 2> {snakemake.log}""")

