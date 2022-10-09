# Exercise 2

Instead of having 1 pod, we want 3 instance of the pod. To do this use a `deployment`.  
## 1) delete
First delete the old pod.
```sh
kubectl delete pod my-webserver-pod
```

## 2) apply deployment
Look at the k8s doc and fill in the `my-webserver-deployment.yaml`. Use the same image/port/env vars as exercise 1.    
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

To apply your changes:
```sh
kubectl apply -f my-webserver-deployment.yaml
```

To inspect the deployment:
```sh
kubectl get deployment
```

To inspect each pod managed by the deployment:
```sh
kubectl get pods
```

## 3) finish
If you see that the deployment is 3/3 READY you did the exercise correct.