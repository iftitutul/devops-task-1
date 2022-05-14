http-echo-chart
---------------

This Kubernetes manifests file/ helm chart deploys the Hashicorp `http-echo` docker image in kubernetes


### Run Kubernetes manifests file:
   ```
   git clone https://github.com/iftitutul/devops-task-1.git
   cd kubernetes/http-echo/k8s
   kubectl apply -f .
   ```

### Helm Charts

- Create the namespace `http-echo-ns`
  
  `kubectl create namespace http-echo-ns`

  
- To install the chart with the release name `http-echo-app` in namespace `http-echo-ns`:

  ```
  git clone https://github.com/iftitutul/devops-task-1.git
  cd kubernetes/http-echo/
  helm install http-echo helm-charts/ --namespace=http-echo-ns --values helm-charts/values.yaml
  ```

- Check the template
  
  `helm template helm-charts --dry-run --debug`

- Upgrade the Chart 

  `helm upgrade http-echo helm-charts/ --namespace=http-echo-ns --values helm-charts/values.yaml`

- Uninstall the Chart

  `helm delete http-echo`
