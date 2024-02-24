from kubernetes import client, config

# Load the Kubernetes configuration from default location
config.load_kube_config()

# Create API clients for different Kubernetes resources
api_instance = client.CoreV1Api()
api_extensions = client.ExtensionsV1beta1Api()
api_apps = client.AppsV1Api()

# Get cluster information
cluster_info = api_instance.read_api_versions()
print("Cluster Info:")
print(cluster_info)

# Get nodes in the cluster
nodes = api_instance.list_node().items
print("Nodes:")
for node in nodes:
    print(f"Name: {node.metadata.name}")
    print(f"Status: {node.status.phase}")
    print("----")

# Get pods in the cluster
pods = api_instance.list_pod_for_all_namespaces().items
print("Pods:")
for pod in pods:
    print(f"Name: {pod.metadata.name}")
    print(f"Namespace: {pod.metadata.namespace}")
    print(f"Status: {pod.status.phase}")
    print("----")

# Get deployments in the cluster
deployments = api_apps.list_deployment_for_all_namespaces().items
print("Deployments:")
for deployment in deployments:
    print(f"Name: {deployment.metadata.name}")
    print(f"Namespace: {deployment.metadata.namespace}")
    print(f"Replicas: {deployment.spec.replicas}")
    print("----")

# Get services in the cluster
services = api_instance.list_service_for_all_namespaces().items
print("Services:")
for service in services:
    print(f"Name: {service.metadata.name}")
    print(f"Namespace: {service.metadata.namespace}")
    print(f"Type: {service.spec.type}")
    print("----")
