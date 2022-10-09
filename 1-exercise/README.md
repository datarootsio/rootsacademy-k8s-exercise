# Exercise 1
Kubernetes basics
## 1) Apply
Apply the yaml provided in the this folder.

```sh
kubectl apply -f my-webserver-pod.yaml
```
This will create a new pod.

## 2) Check the newly created pod
Check that the new pod is create. You can do that with the following command.
```sh
kubectl get pods
```
What do you see?

## 3) Fix the pod
As you can see the pod is broken. Check the logs.
```sh
kubectl logs <name-of-the-pod>
```

Try to fix the pod.   
To fix it you will have to change something in the `my-webserver-pod.yaml`.   
For the change to be applied, first delete the pod and than re-apply the yaml.   
```sh
kubectl delete pod <name-of-the-pod>
kubectl apply -f my-webserver-pod.yaml
```

The exercise is finished when the pod `STATUS` is `RUNNING`