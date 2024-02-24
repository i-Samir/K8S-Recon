**K8S_Recon** is a python script uses the Kubernetes client library to interact with the Kubernetes API. It loads the configuration, creates API client instances for different Kubernetes resources (core, extensions, apps), and then retrieves and prints information about the cluster, nodes, pods, deployments, and services.

### Installation
```
git clone https://github.com/i-Samir/K8S-Recon.git
pip install kubernetes
```
##### This script is tested on kind locally
kind is a tool for running local Kubernetes clusters using Docker container “nodes”.
kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

