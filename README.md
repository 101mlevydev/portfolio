# Disko

Disko is an application designed to provide insights into Kubernetes clusters by displaying information about images stored within them.

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.


## Features
- **Statistics of Images per Registry**
- **Copy Images Between Registries**
- **Migrate Images in Kubernetes**

## Installation

To use Disko, follow these steps:

1. Clone this repository to your local machine:
`$ git clone https://github.com/dpointk/disko`

2. Navigate to the project directory:
`$ cd disko`

3. Install the required dependencies:
`$ pip install -r requirements.txt`


## Getting Started

- To run Disko, execute the following command in your terminal: `$ python3 disko.py`

- Upon running the Disko application, you will encounter a window appearing on your screen the **Images Registry Manager.**

##

### Images Registry Manager

Upon running the Disko application, you will encounter a window appearing on your screen the **Images Registry Manager.**

### Statistics of Images per Registry

Once the cluster have been scanned, the main window will automatically update to display the following information for the scanned cluster:

- **Registry Name**
- **Number of Images**
- **Percentage of Images**

**Note:** You can view all the images in the cluster along with the timestamp of the scanning by clicking the **Show Images Table** button.

##

### Copy Images Between Registries

Allowing to take an image and copy it to the target registry.

- Click on the **Change Registry** button.
- A window will open for selecting an image to copy.
- Click on **Confirm**
- Another window will open where you can enter the target registry URL, Username, Password, and Tag.
- Then, click on **Submit** to execute the copy operation.

##

### Migrate Images in Kubernetes

This feature helps move a cluster to a chosen registry. It does this by copying current images to the target registry and using these copies to run new pods.











