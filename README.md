# ansible_erigon

Ansible role for deploying Erigon Ethereum Execution layer node

## Auto-generated

- [Defaults](#default-vars)
  - [erigon_binary_download_url](#erigon_binary_download_url)
  - [erigon_binary_path](#erigon_binary_path)
  - [erigon_dir_base](#erigon_dir_base)
  - [erigon_dir_binary](#erigon_dir_binary)
  - [erigon_dir_config](#erigon_dir_config)
  - [erigon_dir_data](#erigon_dir_data)
  - [erigon_dir_ethash_dag](#erigon_dir_ethash_dag)
  - [erigon_dir_log](#erigon_dir_log)
  - [erigon_dir_systemd](#erigon_dir_systemd)
  - [erigon_ethash_dagdir](#erigon_ethash_dagdir)
  - [erigon_extra_systemd_directives](#erigon_extra_systemd_directives)
  - [erigon_general_owner](#erigon_general_owner)
  - [erigon_group](#erigon_group)
  - [erigon_http_api](#erigon_http_api)
  - [erigon_jwt_secret_path](#erigon_jwt_secret_path)
  - [erigon_log_level](#erigon_log_level)
  - [erigon_node_config](#erigon_node_config)
  - [erigon_private_api_addr](#erigon_private_api_addr)
  - [erigon_reinstall](#erigon_reinstall)
  - [erigon_systemd_service_name](#erigon_systemd_service_name)
  - [erigon_user](#erigon_user)
- [Tags](#tags)

- [Dependencies](#dependencies)

---

## Defaults

### erigon_binary_download_url

URL to download the erigon binary.

#### Defaults

```YAML
erigon_binary_download_url:
  https://github.com/erigontech/erigon/releases/download/v3.0.3/erigon_v3.0.3_linux_amd64.tar.gz
```

### erigon_binary_path

Path the erigon binary.

#### Defaults

```YAML
erigon_binary_path: '{{ erigon_dir_binary }}/erigon'
```

### erigon_dir_base

Base directory for erigon installation.

#### Defaults

```YAML
erigon_dir_base: /opt/erigon
```

### erigon_dir_binary

#### Defaults

```YAML
erigon_dir_binary: /usr/local/bin
```

### erigon_dir_config

Directory for erigon configuration files.

#### Defaults

```YAML
erigon_dir_config: '{{ erigon_dir_base }}/config'
```

### erigon_dir_data

Directory for erigon data storage.

#### Defaults

```YAML
erigon_dir_data: '{{ erigon_dir_base }}/data'
```

### erigon_dir_ethash_dag

#### Defaults

```YAML
erigon_dir_ethash_dag: '{{ erigon_dir_data }}/erigon-ethash'
```

### erigon_dir_log

Directory for erigon log files.

#### Defaults

```YAML
erigon_dir_log: '{{ erigon_dir_base }}/logs'
```

### erigon_dir_systemd

Systemd service directory for erigon.

#### Defaults

```YAML
erigon_dir_systemd: /etc/systemd/system
```

### erigon_ethash_dagdir

Set the directory to store the ethash mining DAGs.

### erigon_extra_systemd_directives

Erigon systemd service configuration.

#### Defaults

```YAML
erigon_extra_systemd_directives:
  - Restart=on-failure
  - RestartSec=10
  - TimeoutStopSec=30
```

### erigon_general_owner

General owner for erigon system files.

#### Defaults

```YAML
erigon_general_owner: root
```

### erigon_group

Group for running the erigon node.

#### Defaults

```YAML
erigon_group: erigon
```

### erigon_http_api

#### Defaults

```YAML
erigon_http_api: eth,debug,net,trace,web3,erigon,txpools
```

### erigon_jwt_secret_path

jwt token path for erigon.

#### Defaults

```YAML
erigon_jwt_secret_path: '{{ erigon_dir_config }}/jwt.hex'
```

### erigon_log_level

Force reinstall erigon binary.

### erigon_node_config

#### Defaults

```YAML
erigon_node_config:
  - name: chain
    value: sepolia
  - name: verbosity
    value: info
  - name: http.api
    value: '{{ erigon_http_api }}'
  - name: http.addr
    value: 127.0.0.1
  - name: http.port
    value: 8545
  - name: authrpc.addr
    value: 127.0.0.1
  - name: authrpc.port
    value: 8545
  - name: private.api.addr
    value: 127.0.0.1:9090
  - name: externalcl
    value: true
  - name: datadir
    value: '{{ erigon_dir_data }}'
  - name: ethash.dagdir
    value: '{{ erigon_dir_ethash_dag }}'
```

### erigon_private_api_addr

Set the internal grpc API address.

### erigon_reinstall

#### Defaults

```YAML
erigon_reinstall: false
```

### erigon_systemd_service_name

Systemd service name for erigon.

#### Defaults

```YAML
erigon_systemd_service_name: erigon
```

### erigon_user

Username for the erigon node.

#### Defaults

```YAML
erigon_user: erigon
```

## Tags

**_erigon-config_**

**_erigon-install_**

**_erigon-prepare_**

## Dependencies

None.
