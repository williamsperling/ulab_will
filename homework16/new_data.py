import torch

# Define a function to generate data and add noise
def generate_noisy_data(num_samples=100, noise_factor=0.1):
    # Generate synthetic data (e.g., a simple function of x1 and x2)
    data_x = torch.randn(num_samples, 2)  # 100 samples with 2 features
    
    # Generate the target data (simple function: y = x1 + x2)
    data_y = (data_x[:, 0] + data_x[:, 1]).view(-1, 1)
    
    # Add noise to the data (e.g., Gaussian noise)
    noise = noise_factor * torch.randn_like(data_y)
    data_y_noisy = data_y + noise
    
    # Return the noisy data
    return data_x, data_y_noisy