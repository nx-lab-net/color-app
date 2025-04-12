# Linux Command Cheatsheet

1. Delete blank lines after each line in a file
    
    ```bash
    sed '/^$/d'[file]
    ```
    
2. Replace the word and save in the new version of the file for all occurrences 
    
    ```bash
    sed  "s/happy/enchanted/g" chap1  >chap1.new
    ```
    
3. Archive a folder 
    
    ```yaml
    tar -czvf archive.tar.gz /path/to/folder
    ```
    
4. Extract  the archived folder
    
    ```yaml
    tar -xzvf <file>
    ```
    
5. Find a sting in a block of text starting with a specific  and replace 
    
    ```bash
    sed -i 's/^Server=.*/Server=new.zabbix.server/' /etc/zabbix/zabbix_agent2.conf
    ```
    
6. Get the lines starting with Jul1 in the specified log file 
    
    ```bash
    sed -n '/^Jul  1/ p' /var/log/secure
    ```
    
7. Copy the content of the file into a clipboard #MAC
    
    ```yaml
    cat file.txt | pbcopy
    ```
    
8. Create a file with cat command
    
    ```bash
    cat > filename
    Hello World
    Today is a beautiful day 
    ^C
    ```
    
9. Find a file by name ignoring case sensitivity
    
    ```yaml
    find / -iname file.bin
    ```
    
10. Generate public key from private key and copy to clipboard
    
    ```bash
    ssh-keygen -y -f private_key_rsa > pbcopy
    ```
    
11. Get info about the CPU
    
    ```bash
    lscpu
    ```
    
12. Get info about the RAM 
    
    ```bash
    free -m
    ```
    
13. Get info about the storage 
    
    ```bash
    df -h
    ```
    
14. Get info about the files’ sizes in the folder 
    
    ```bash
    du -ahc | sort -tr
    ```
    
15. Get the location of a program 
    
    ```bash
    which docker-compose
    ```
    
16. Curl with host header
    
    ```yaml
    curl http://example.com --header 'Host: path.example.com'
    ```
    
17. Get the exit status of the previous command 
    
    ```yaml
    echo $?
    ```
    
18. List disk usage 
    
    ```yaml
    **du -sh /***
    ```
    
19. Prune all docker images 
    
    ```yaml
    docker image prune -af
    ```
    
20. Review docker cache storage 
    
    ```yaml
    docker system df
    ```
    
21. Prune docker system cache
    
    ```yaml
    docker system prune -f
    ```
    
22. List the file with size and last modified time
    
    ```jsx
    ls -larth
    ```
    
23. Check the users currently logged in to the server 
    
    ```jsx
    w
    ```
    
24. Restart DNS in MAC OS 
    
    ```jsx
    sudo killall -HUP mDNSResponder
    sudo dscacheutil -flushcache
    ```
    
25. Which process consumes the most CPU 
    
    ```jsx
    ps aux --sort=-%cpu | head -n 10
    ```
    
26. Which process consumes the most RAM 
    
    ```jsx
    ps aux --sort=-%mem | head -n 10
    ```
    
27. Hardware status information 
    
    ```jsx
    vmstat 5
    ```
    
28. Information about hardware
    
    ```jsx
    nmon
    ```
    
29. SSH through another server
    
    ```jsx
    ssh   -J ngrigoryan@20.163.203.92   ngrigoryan@10.10.10.24
    ```
    
30. Clean docker from images and cache
    
    ```yaml
    docker rmi $(docker images -aq) --force && docker system prune
    ```
    
31. Install Azure CLI with one command 
    
    ```yaml
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    ```
    
32. K8s aliases
    
    ```yaml
    alias p="kubectl get po" && \
    alias d="kubectl describe po" && \
    alias l="kubectl logs" && \
    alias s="kubectl get service"
    ```
    
33. Search and replace in vim 
    
    ```yaml
    :%s/verification/frontend/g
    ```
    
34. Get file from the private server that has only outbound
    
    ```yaml
    curl -F "file=@/root/tf-appgraph.png" https://file.io
    ```
    
35. Delete stuck on terminating namespace
    
    ```yaml
    kubectl get namespace <namespace-name> -o json | jq '.spec.finalizers=[]' | kubectl replace --raw "/api/v1/namespaces/<namespace-name>/finalize" -f -
    
    ```
    
36. ACR move image 
37. 

```yaml
az login
az account set --subscription 1d3efde8-100e-4f6d-8298-3813cd0105aa
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/artemis/inference:2.1.8-pe --image zerosystems/artemis/inference:2.1.8-pe-mercer
```

1. f
2. f
3. f
4. f
5. f

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/artemis/document-preprocessing-service:2.1.2 --image zerosystems/artemis/document-preprocessing-service:2.1.2-mercer
```

inference:2.1.8-pe-mercer

```yaml
helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=verify-console.ropers.com \
  --set replicas=1 \
  --set bootstrapPassword=ad1KX4BrgoYMKINdIZSW8jmgsH9hZrgCm3lOX+eTBV+ACRD3ad8O

```

```yaml
helm upgrade rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set ingress.ingressClassName=nginx \
  --set hostname=verify-console.ropers.com

```

verify-dps

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/verify/document-preprocessing-service:fasken-0.0.558 --image zerosystems/verify/document-preprocessing-service:0.0.558
```

verify-verification

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/verify/verification:fasken-0.0.726 --image zerosystems/verify/verification:0.0.726
```

verify-ui

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/verify/ui:fasken-0.0.430 --image zerosystems/verify/ui:0.0.430
```

verify-inference

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/verify/inference:fasken-0.0.662 --image zerosystems/verify/inference:0.0.662
```

dt inference-mapping

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/data-transformation/dt_inference_mapping:1.5.10 --image zerosystems/data-transformation/dt_inference_mapping:1.5.10
```

dt inference transformation

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/data-transformation/dt_inference_transformation:1.5.10 --image zerosystems/data-transformation/dt_inference_transformation:1.5.10
```

dt frontend

```yaml
az acr import --name [zerosystems --source](http://zerosystemseng.azurecr.io/zerosystems/data-transformation/dt_backend:1.3.3) zerosystemseng.azurecr.io/zerosystems/data-transformation/dt_frontend:1.6.4 --image zerosystems/data-transformation/dt_frontend:1.6.4
```

dt_backend

```yaml
az acr import --name [zerosystems --source](http://zerosystemseng.azurecr.io/zerosystems/data-transformation/dt_backend:1.3.3) zerosystemseng.azurecr.io/zerosystems/data-transformation/dt_backend:1.6.4 --image zerosystems/data-transformation/dt_backend:1.6.4
```

```yaml
az acr import --name zerosystems --source zerosystemseng.azurecr.io/zerosystems/verify/inference:0.0.589 --image zerosystems/verify/inference:0.0.589 
```

```yaml
ngrigoryan@zerosystems.com
G/558829419407uw
```

```yaml
docker run --network host cloudflare/cloudflared:latest tunnel --no-autoupdate run --token eyJhIjoiOTk5MmI0NmU5NjNhMWNmYzM4YzkzOGI0ZWZlNDhjNjAiLCJ0IjoiNWM3ZGYzZjEtNWE5Zi00NTYzLWJmMGItMjIyYzhmNGUzMWY4IiwicyI6Ik5UWXdabUZqTW1VdE1USTNOaTAwTWpreUxUZ3pOMll0TVdGbU1HRTNZV015TmpOayJ9 
```

AQCEVe2tP0Md2xptp-tBX0BYUHyWeCrss2QNpKWlh-1P_ohus91hQR5o2GVlCGGYHWyU826ayn9zwxlDvp6D59qUmegW7ofCP9sDaVSq3UjzYOCWeIO7wB3Ha385o_Vgegw3PR4fZTxT7VPcqipTgo6ig6WGwNwiP6oEr6mWsDFwffNtpv1iDmYiPu2TFuccqCIrHtFPRrshJs07xgo4v2mrYvZ62mBUh6mnyX-RfY5oblK3U-zzow

```yaml
curl -X POST https://accounts.spotify.com/api/token \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -H "Authorization: Basic OTUyZmZkNmYxNGIxNDU4NzgwOTkxMWI2NTUwMTZhYWI6NzJiNDcyN2IzYThhNDkyM2JmZGM1MDM3MWViZjUyOGI=" \
     -d "grant_type=authorization_code" \
     -d "code=AQAzWOkC5F8jSGHbFUpQRPZusH--n33kOV0ACAgOE0zNoB9tUIrt9RGRbiRGy1kbHizD8JZVAUMgy7fEzfuECdLUpYlInrLpndfCnZPL6O2tw20IBa6YyaEuPsEnTLuafi0d9q4IG_OAahCl2BCzhl-2hmAP1qpFOB40oHd6YQVRc6IWU1vrNb-eFltQgXZAEBI-v-tYY6QwfOCj0adYEMf1UbYM4lNgqGtiTyDIu0DQ5HT_XFspRA" \
     -d "redirect_uri=http://localhost:8888/callback"

```

auth code

```yaml
https://accounts.spotify.com/authorize?response_type=code&client_id=952ffd6f14b14587809911b655016aab&scope=user-read-playback-state%20user-modify-playback-state&redirect_uri=http://localhost:8888/callback

```

dt_inference_transformation_backup

```yaml
   spec:
      containers:
      - command:
        - python3
        - ./src/inference_service/app.py
        - inference_vllm
        - structured_llm_7b_gptq
        envFrom:
        - configMapRef:
            name: cm-dt-inference-mapping
        image: zerosystems.azurecr.io/zerosystems/data-transformation/dt_inference_mapping:1.4.2
```

az acr import --name zerosystems --source [zerosystemseng.azurecr.io/zerosystems/verify/verification:0.0.664](http://zerosystemseng.azurecr.io/zerosystems/verify/verification:0.0.664) --image zerosystems/verify/verification:0.0.664
