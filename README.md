# Temporal Modeling of Embryo Development

## Overview

This project studies ordered stage classification and developmental-event
localization in human embryo time-lapse microscopy. The private research system
combines visual encoders, temporal modeling, and vision-language models.

## Dataset

### Nantes Human Embryo Time-Lapse Dataset

The project uses the public Human Embryo Time-Lapse Video Dataset released by
Gomez et al. It contains 704 embryo time-lapse videos, seven focal planes per
embryo, approximately 2.4 million images, and annotations for 16 developmental
events.

The images and annotations are not redistributed here. Users must download the
dataset from its official source and comply with its license, ethical terms, and
applicable institutional review requirements.

### Official Resources

- [Human embryo time-lapse video dataset on Zenodo](https://zenodo.org/records/7912264)
- Gomez et al., *A time-lapse embryo dataset for morphokinetic parameter
  prediction*, Data in Brief 42 (2022) 108258:
  [full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9120221/)
- [Dataset DOI 10.5281/zenodo.6390798](https://doi.org/10.5281/zenodo.6390798)

## Technical Scope

The private project evaluates visual backbones from model families such as
Qwen2.5-VL, MiniCPM-V, and LLaVA/CLIP, together with recurrent or Transformer
temporal modeling. These references identify the model families only; the
private adaptation and training design is not disclosed.

## Environment

### Recommended Software

- Linux x86_64;
- Python 3.10;
- PyTorch 2.3 or later;
- Torchvision 0.18 or later;
- CUDA 12.1 for GPU execution;
- Transformers 4.46 or later;
- NumPy 1.24 or later;
- Pillow 10 or later;
- pandas 2.0 or later;
- scikit-learn 1.3 or later.

### Installation

```bash
conda env create -f environment.yml
conda activate embryo-temporal-public
```

The public snapshot does not automatically download the embryo dataset or any
pretrained vision-language model.

## Hardware

The research code was developed on a Linux workstation with:

- 4 × NVIDIA GeForce RTX 3090 GPUs, 24 GB per GPU;
- 2 × Intel Xeon E5-2680 v4 CPUs, 28 cores and 56 threads in total;
- approximately 188 GB of system memory;
- NVIDIA driver 530.30.02.

Small evaluation utilities can run on a CPU. Memory requirements for the private
vision-language experiments depend on model size, sequence length, numerical
precision, and the parameter-freezing strategy.

## Repository Contents

- `src/metrics.py`: generic frame-accuracy and transition-error examples;
- `environment.yml`: Conda environment specification;
- `requirements.txt`: minimal dependencies;
- `.gitignore`: exclusions for data, annotations, weights, and outputs.

## Disclaimer

This project is intended for research only. It does not provide medical advice
and is not a clinical embryo-assessment system.

