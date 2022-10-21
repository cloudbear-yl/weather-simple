# Weather-Rainfall-App

Goal:
Create a simple rainfall app that generates real-time data rainfall data when user inputs area name.
Data is extracted from https://api.data.gov.sg/v1/environment/rainfall

This project is a technical assessment.

---

To run the appplication on Docker:
- Pre-requistes: a copy of this repo, Dockerfile

    1. Building the image
       > Command : docker build -t <name>
    2. Verify if the application runs properly as an Docker Image
       > Command : docker run -p <port number> <name>
    3. If Step 2, cancel the previous command. Run the application indefinitely (as detached, in the background)
       > Command : docker run -d -p <port number> <name>

---

To run Docker Container in Kubernetes:

- Minikube
    1. Starting Minikube (This will start Kubectl too)
       > Command : minikube start 
    2. Check for kubectl version and minikube version to ensure its running 
       > Command : kubectl version / minikube version
    
- Kubernetes 
    1. Create pods 
       > Command : kubectl create -f <filename> 
    2. Check if pod is successfully running 
       > Command : kubectl describe pods/<filename> 
    3. Create configmap 
       > Command : kubectl create configmap weather-config --from-file=./<filename> 
    4. Check configmap, it will show a log file
       > kubectl describe configmaps weather-config
