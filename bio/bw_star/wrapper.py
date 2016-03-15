__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

# inputs:
#     fastq:
#     gtf:
# params:
#     genomeDir
#     

# expects a list of string, ['read1','read2','read1_2','read2_2',...]
x = snakemake.input.fastqs
fastqs=' '.join([','.join([x[i] for i in range(0,len(x),2)]),','.join([x[i] for i in range(1,len(x),2)])])
# fastqs will be a string that looks like "read1,read1_2 read2,read2_2"
# note no spaces around comma for fastq, but there are spaces aroudn comma for RG!

shell("""
module load STAR/2.5.1b
STAR --runMode alignReads \
    --runThreadN ${{SLURM_CPUS_ON_NODE}} \
    --sjdbGTFfile {snakemake.input.gtf} \
    --outFilterType BySJout \
    --outFilterMultimapNmax 20 \
    --alignSJoverhangMin 8 \
    --alignSJDBoverhangMin 1 \
    --outFilterMismatchNmax 999 \
    --alignIntronMin 20 \
    --alignIntronMax 1000000 \
    --alignMatesGapMax 1000000 \
    --genomeDir {snakemake.params.genomeDir} \
    --readFilesIn {fastqs} \
    --readFilesCommand zcat \
    --chimSegmentMin 20 \
    --chimJunctionOverhangMin 15 \
    --chimOutType WithinBAM \
    --quantMode GeneCounts \
    --twopassMode Basic \
    --outSAMtype BAM SortedByCoordinate \
    --outSAMstrandField intronMotif \
    --outFilterIntronMotifs RemoveNoncanonicalUnannotated \
    --outSAMattrRGline {snakemake.params.RG} \
    --outFileNamePrefix {snakemake.params.outDir} """)
