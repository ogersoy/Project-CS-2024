# Change to fit your account
PRJ_DIR=/crex/uppmax2024-2-18

# Singularity
export SINGULARITY_CACHEDIR=${PRJ_DIR}/nobackup/SINGULARITY_CACHEDIR
export SINGULARITY_TMPDIR=${PRJ_DIR}/nobackup/SINGULARITY_TMPDIR
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR

# Apptainer
export APPTAINER_CACHEDIR=${PRJ_DIR}/nobackup/SINGULARITY_CACHEDIR
export APPTAINER_TMPDIR=${PRJ_DIR}/nobackup/SINGULARITY_TMPDIR
mkdir -p $APPTAINER_CACHEDIR $APPTAINER_TMPDIR

# Disabling cache completelly - perfect when you only need to pull containers
# export SINGULARITY_DISABLE_CACHE=true
# export APPTAINER_DISABLE_CACHE=true