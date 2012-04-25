#!/bin/sh
export SIMICS_HOST=amd64-linux

mkdir -p new-workspace
cd new-workspace
tgt_wrk_spc=`pwd`
cd /opt/virtutech/simics3/bin/
./workspace-setup $tgt_wrk_spc
cd $tgt_wrk_spc
cp ../time_in_domains_full.simics .

./simics /mnt/ganfs/C224068035/simics-workspace/xen_noBoost_3domU_BenchesRunning.config -no-win -batch-mode time_in_domains_full.simics > ../screen_dump.out
