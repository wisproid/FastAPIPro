Create secret to pull image from docker hub private
```
kubectl create secret -n <namespace> docker-registry dockerhub-secret --docker-username=<your-dockerhub-username> --docker-password=<your-dockerhub-password> --docker-email=<your-email>
```