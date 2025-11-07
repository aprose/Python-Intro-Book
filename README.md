# Python-Intro-Book

A comprehensive introduction to Python for Deep Learning, featuring practical examples and tutorials.

## Contents

### Deep Learning for Time Series Analysis

This repository includes a JupyterLab notebook demonstrating deep learning techniques for time series forecasting using PyTorch with NVIDIA CUDA GPU support.

**File**: `time_series_deep_learning.ipynb`

#### Features

- **CUDA/GPU Support**: Automatic detection and utilization of NVIDIA GPUs for accelerated training
- **LSTM Neural Networks**: Implementation of Long Short-Term Memory networks for time series prediction
- **Dummy Data Generation**: Synthetic time series data with trend, seasonality, and noise components
- **Complete Pipeline**: Data preprocessing, model training, evaluation, and visualization
- **Model Checkpointing**: Save and load trained models for future use

#### Topics Covered

1. CUDA/GPU detection and configuration
2. Time series data generation with realistic patterns
3. Data normalization and sequence preparation
4. LSTM model architecture design
5. Training loop with validation
6. Learning rate scheduling
7. Multi-step ahead forecasting
8. Performance visualization and metrics
9. Model persistence

## Getting Started

### Prerequisites

- Python 3.8 or higher
- (Optional) NVIDIA GPU with CUDA support for accelerated training

### Installation

1. Clone this repository:
```bash
git clone https://github.com/aprose/Python-Intro-Book.git
cd Python-Intro-Book
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

**Note**: For CUDA support, you may need to install the CUDA-enabled version of PyTorch. Visit [PyTorch's official website](https://pytorch.org/get-started/locally/) for platform-specific installation instructions.

For example, for CUDA 11.8:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Running the Notebook

1. Start JupyterLab:
```bash
jupyter lab
```

2. Open `time_series_deep_learning.ipynb` in your browser

3. Run all cells sequentially to:
   - Check CUDA availability
   - Generate synthetic time series data
   - Train an LSTM model
   - Visualize predictions
   - Evaluate model performance

## Understanding the Model

### LSTM Architecture

The notebook implements a 2-layer LSTM network with:
- **Input**: Time series sequences (default length: 50 timesteps)
- **Hidden Layers**: 64 LSTM units per layer with dropout
- **Output**: Single predicted value for the next timestep

### Data Generation

Synthetic data includes:
- **Trend**: Linear increase over time
- **Seasonality**: Daily and weekly patterns
- **Noise**: Random fluctuations

This mimics real-world time series data like temperature, stock prices, or sensor readings.

### Training Process

- **Loss Function**: Mean Squared Error (MSE)
- **Optimizer**: Adam with learning rate scheduling
- **Batch Size**: 32 sequences per batch
- **Epochs**: 50 (configurable)
- **Train/Test Split**: 80/20

## GPU Acceleration

The notebook automatically detects and uses NVIDIA GPUs when available:

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
```

Benefits of GPU acceleration:
- **Faster Training**: 5-10x speedup for typical workloads
- **Larger Models**: Train bigger networks with more parameters
- **Batch Processing**: Handle larger batch sizes efficiently

## Expected Results

After training, you should see:
- Decreasing training and validation loss
- Predictions closely following actual time series patterns
- RMSE and MAE metrics showing model accuracy

## Customization

You can modify:
- **Sequence Length**: Adjust `seq_length` for longer/shorter input sequences
- **Model Size**: Change `hidden_size` and `num_layers` for model capacity
- **Data Characteristics**: Modify trend, seasonality, and noise parameters
- **Training Duration**: Increase `num_epochs` for better convergence

## Dependencies

See `requirements.txt` for the complete list. Key packages:
- **PyTorch**: Deep learning framework with CUDA support
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **JupyterLab**: Interactive notebook environment

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- PyTorch team for the excellent deep learning framework
- NVIDIA for CUDA support enabling GPU acceleration
