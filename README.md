# CatBoost for SageMaker Inference
This repository contains three different implementations of using CatBoost for inference on Amazon SageMaker. Each implementation is organized into a separate subfolder and represents a different approach. The three approaches are as follows:

1. BYOC (Bring Your Own Container)
The BYOC subfolder contains an implementation that leverages the BYOC functionality of SageMaker. It allows you to use a custom container to run your CatBoost inference on SageMaker. This approach gives you more flexibility and control over the inference environment.

2. PyTorch-based Approach
The pytorch-base subfolder contains an implementation that integrates CatBoost with PyTorch for inference on SageMaker. This approach leverages the PyTorch framework and provides seamless integration with CatBoost, enabling you to utilize the benefits of both frameworks in your inference workflow.

3. Tricky Approach
The tricky subfolder contains a unique and alternative implementation of using CatBoost for SageMaker inference. This approach may involve unconventional techniques or optimizations that are not typically used. It is provided as an experimental option for advanced users who want to explore non-standard ways of utilizing CatBoost with SageMaker.
