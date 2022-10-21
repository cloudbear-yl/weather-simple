# weather-simple

Goal:
Create a simple rainfall app that generates real-time data rainfall data when user inputs area name.
Data is extracted from data.gov.sg

This project is a technical assessment.

---

To run the appplication on Docker:
Pre-requistes:
Dockerfile

    1. Building the image
    > Command : docker build -t <name>
    2. Verify if the application runs properly as an Docker Image
    > Command : docker run -p <port number> <name>
    3. If step 2, cancel the previous command. Run the application indefinitely (as detached, in the background)
    > Command : docker run -d -p <port number> <name>

To run in Kubernetes:
(a) Minikube - Start minikube which will also start kubectl > Command : minikube start - Check for kubectl version and minikube version to ensure its running > Command : kubectl version / minikube version
(b) Kubernetes - Create pods > Command : kubectl create -f <filename> - Check if pod is successfully running > Command : kubectl describe pods/<filename> - Create configmap > Command : kubectl create configmap weather-config --from-file=./<filename> - Check configmap, it will show a log file > kubectl describe configmaps weather-config
