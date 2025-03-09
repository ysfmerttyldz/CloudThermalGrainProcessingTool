Image Processing Tool: Cloud Thermal and Grain Effect
This tool processes images by adding cloud-like effects and film grain. It is designed to be fast, accurate, and easy to use. Below are the instructions for setting up and using the tool.

Table of Contents
-Installation
-Usage
-Folder Structure
-Parameters
-Recommended Settings

Installation
Step 1: Install Required Packages
Upgrade pip (Python package manager):
python -m pip install --upgrade pip
Install the required libraries:
pip install opencv-python numpy pillow noise matplotlib

Microsoft C++ Build Tools (Required for some libraries):
Download and install the Microsoft C++ Build Tools.
During installation, ensure you select the C++ build tools and Windows SDK options.

Usage
Step 1: Prepare the Folder Structure
Create the following folder structure for your project:

Copy
Project/
│
├── Inputs/ # Place your input images here
├── Outputs/ # Processed images will be saved here
│ ├── Cloud/ # Cloud-processed images
│ └── Grain/ # Grain-processed images
│
├── Controller.py # Main script
└── Alpha_Mask.png # Alpha mask (will be generated automatically)

Step 2: Run the Tool
-Place your images in the Inputs folder.
-Open a terminal in the project directory.
-Run the following command:

python Controller.py alpha_multiplier gamma_param opacity_factor grain_intensity

Parameters
-alpha_multiplier Multiplier for the mask’s alpha values.
-gamma_param Controls the amount of cloud in the mask (should not be lower than 1).
-opacity_factor Affects the opacity of all clouds after the mask is created (final step).
-grain_intensity Controls the intensity of the film grain effect.

For the best results, use the following settings:
-python Controller.py 0.8 2 0.9 0.7

Notes
-Ensure all dependencies are installed correctly.
-Adjust the parameters (alpha_multiplier, gamma_param, opacity_factor, grain_intensity) to achieve the desired effect.
-If you encounter any issues, ensure that the Microsoft C++ Build Tools are installed.If it is not related with Microsoft C++
Build Tools or any package problem you can send mail me. ysfmertyldzz@mail.com

THANK YOU!
