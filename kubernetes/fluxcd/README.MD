[fluxcd](https://fluxcd.io/docs/)
-------------------------------------
Flux is an Open and extensible continuous delivery solution for Kubernetes. Flux is a GitOps tool for Kubernetes that synchronizes the state of manifests in a Git repository to what is running in a cluster. So what is GitOps? Is it a new tool in the market? GitOps provides a way for developers to manage operational workflow for using Kubernetes using Git. It is all about using a version-controlled system for the deployment of applications in Kubernetes. So Developers can directly push the code into production from the version-controlled system like Git. Moreover, any changes made can be easily tracked and reverted in case of any chaos.

- Install the Flux CLI on Mac

  `brew install fluxcd/tap/flux`

- To configure your shell to load flux bash completions add to your profile (`vim ~/.zshrc`):
  
  `command -v flux >/dev/null && . <(flux completion zsh)`

- Check the flux command
  
  ```
  source ~/.zshrc
  flux -h
  flux --version
  ```
- Export your GitHub personal access token and username
  
  ```
  export GITHUB_TOKEN=<your-token>
  export GITHUB_USER=<your-username>
  ```
- Check you have everything needed to run Flux by running the following command

  `flux check --pre`

- Run the bootstrap command
  ```
  flux bootstrap github \
  --owner=$GITHUB_USER \
  --repository=fluxcd \
  --branch=main \
  --path=./clusters/my-cluster \
  --personal
  ```
  
    The bootstrap command above does following:

    - Creates a git repository fleet-infra on your GitHub account
    - Adds Flux component manifests to the repository
    - Deploys Flux Components to your Kubernetes Cluster
    - Configures Flux components to track the path `/clusters/my-cluster/` in the repository

- Verify FluxCD pods are running
  
  `kubectl get pods --namespace flux-system`

- Verify that the controller have started
  
  `flux check`

- Create the kubernetes namespace
  
  `kubectl create ns http-echo`

- go to `fluxcd` repo and add below folder structure `http-echo`
  
    ```
    └── clusters
        └── my-cluster
            ├── flux-system
            │   ├── gotk-components.yaml
            │   ├── gotk-sync.yaml
            │   └── kustomization.yaml
            └── http-echo
                ├── gitrepo.yaml
                └── helmrelease.yaml

    4 directories, 5 files
    ```

- Create `gitrepo.yaml` and `helmrelease.yaml` file and apply configuration again running bootstrap command

  ```
  flux bootstrap github \
  --owner=$GITHUB_USER \
  --repository=fluxcd \
  --branch=main \
  --path=./clusters/my-cluster \
  --personal
  ```

- Check the all components of the namespace `flux-system`

  ```
  kubectl get all -n flux-system
  kubectl get gitrepository -n flux-system
  kubectl describe gitrepository -n flux-system
  kubectl get helmchart -n flux-system
  kubectl describe helmchart -n flux-system
  ```

- Check the `http-echo` application

  `kubectl get all -n http-echo`


- Uninstall Flux components, its custom resources and namespace
  
  `flux uninstall --namespace=flux-system`
  `flux uninstall --namespace=http-echo`

- Uninstall Flux but keep the namespace
  
  `flux uninstall --namespace=http-echo --keep-namespace=true`


### Links

- [fluxcd repo](https://github.com/iftitutul/fluxcd)
- [Helm Charts](https://github.com/iftitutul/helm-charts)
