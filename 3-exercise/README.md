# Exercise 3
You deployed a webserver, but you don't have access to it, what a shame. In the exercise we will expose it to the wide world.

## 1 apply
Deploy a `NodePort` service that targets the deployment we applied in exercise 2.
Update the `service.yaml` to do the above.   
https://kubernetes.io/docs/concepts/services-networking/service/

The `nodePort` should be `30303`.

To apply.
```sh
kubectl apply -f service.yaml
```

To view.
```sh
kubectl get service
```

To delete.
```sh
kubectl delete service <service-name>
```

## 2 access
If you did things correctly you should see a page in your web browser when going to:
```
localhost:30303
```

Open a browser in cognito mode and check if you get put on the same pod.  