#!/bin/sh
#BSUB -q gpuv100
#BSUB -J 02-baseline-adam-no-aug
#BSUB -n 8
#BSUB -R "span[block=1]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -W 00:30
#BSUB -R "rusage[mem=32GB]"
#BSUB -u andersbthuesen@gmail.com
#BSUB -B
#BSUB -N
#BSUB -o logs/%J.out
#BSUB -e logs/%J.err

nvidia-smi
module load cuda/11.1.1

PATH=~/miniconda3/bin:$PATH

python main.py --model BaselineCNN --optimizer SGD --lr 0.1 --epochs 100 --augmentation 0
