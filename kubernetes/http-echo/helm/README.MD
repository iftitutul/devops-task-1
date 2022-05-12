- To install the chart with the release name my-application in namespace test:

  ```
  helm repo add http-echo-app https://github.com/iftitutul/devops-task-1.git
  helm repo update
  helm install http-echo http-echo-app/kubernetes/http-echo/helm/http-echo --namespace http-echo-ns
  ```

- Uninstall the Chart

  `helm delete http-echo`
