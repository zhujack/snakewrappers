__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

# note that strelka requires a ./ for a file in the working directory

shell("""
TMPDIR=/lscratch/${{SLURM_JOB_ID}}/strelka/
module load strelka
${{STRELKA_INSTALL_DIR}}/bin/configureStrelkaWorkflow.pl \
  --normal={snakemake.input.normal_bam} \
  --tumor={snakemake.input.tumor_bam} \
  --ref={snakemake.input.ref} \
  --config={snakemake.input.configfile} \
  --output-dir=${{TMPDIR}}
make -j ${{SLURM_CPUS_ON_NODE}} -C ${{TMPDIR}}
cp ${{TMPDIR}}/results/* {snakemake.params.outdir}
""")
