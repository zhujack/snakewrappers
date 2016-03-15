############
#       GATK Best Practices
############
# rule GATK:
# input: bam="{base}/{sample}/{sample}.bwa.dd.bam",
#   bai="{base}/{sample}/{sample}.bwa.dd.bam.bai",
#   ref=config["reference"],
#   phase1=config["1000G_phase1"],
#   mills=config["Mills_and_1000G"]
# output:
#   bam="{base}/{sample}/{sample}.bwa.final.bam",
#   index="{base}/{sample}/{sample}.bwa.final.bam.bai",
#   log:    "log/gatk.{sample}"
#   version: config["GATK"]
# params:
#   rulename  = "gatk",
#   batch     = config["job_gatk"]
__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell



shell("""
#######################
MEM="48"
module load GATK
java -Xmx${{MEM}}g -Djava.io.tmpdir=/lscratch/${{SLURM_JOBID}} -jar $GATK_JAR \
    -T RealignerTargetCreator -R {snakemake.input.ref} -nt ${{SLURM_CPUS_ON_NODE}} -known {snakemake.input.phase1} -known {snakemake.input.mills} \
    -I {snakemake.input.bam} -o /lscratch/${{SLURM_JOBID}}/realignment.intervals > {snakemake.log} 2>&1
java -Xmx${{MEM}}g -Djava.io.tmpdir=/lscratch/${{SLURM_JOBID}} -jar $GATK_JAR \
    -T IndelRealigner -R {snakemake.input.ref} -known {snakemake.input.phase1} -known {snakemake.input.mills} \
    -I {snakemake.input.bam} --targetIntervals /lscratch/${{SLURM_JOBID}}/realignment.intervals \
    -o /lscratch/${{SLURM_JOBID}}/lr.bam >>{snakemake.log} 2>&1
java -Xmx${{MEM}}g -Djava.io.tmpdir=/lscratch/${{SLURM_JOBID}} -jar $GATK_JAR \
    -T BaseRecalibrator -R {snakemake.input.ref} -knownSites {snakemake.input.phase1} -knownSites {snakemake.input.mills} \
    -I /lscratch/${{SLURM_JOBID}}/lr.bam -nct ${{SLURM_CPUS_ON_NODE}} \
    -o /lscratch/${{SLURM_JOBID}}/recalibration.matrix.txt >>{snakemake.log} 2>&1
java -Xmx${{MEM}}g -Djava.io.tmpdir=/lscratch/${{SLURM_JOBID}} -jar $GATK_JAR \
    -T PrintReads -R {snakemake.input.ref} -I /lscratch/${{SLURM_JOBID}}/lr.bam \
    -nct ${{SLURM_CPUS_ON_NODE}} \
    -o {snakemake.output.bam} -BQSR /lscratch/${{SLURM_JOBID}}/recalibration.matrix.txt >>{snakemake.log} 2>&1
######################
""")
