erigon
=========

erigon execution layer

**Tests:**
* Ubuntu 22.04 (jammy)

How to run molecule tests
----------------------

```shell
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
make init
make test
```

Make
----

`make init` - Prepare environment
`make test` - Run molecule tests (`molecule -v test`)
`make docs` - Auto-generate `README` (`ansible-doctor`)

Role install
--------------

You can install role by using `ansible-galaxy`:

```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_erigon.git
```

For particular version of this role:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_erigon.git,main
```

Update to latest version:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_erigon.git --upgrade
```

Example of using in `requirements.yml`:
```yaml
---
roles:
  - name: erigon
    src: git+git@github.com:keynodes-org/ansible_erigon.git
    version: main
```

How to use in playbook:
-------------------------

```yaml
- hosts: ansible_hostname
  roles:
    - role: ansible_erigon
```

Variables
===============

Ansible role for deploying erigon Ethereum Execution layer node

## Auto-generated

- [Defaults](#default-vars)
  - [erigon_batch_size](#erigon_batch_size)
  - [erigon_binary_download_url](#erigon_binary_download_url)
  - [erigon_binary_path](#erigon_binary_path)
  - [erigon_bodies_cache](#erigon_bodies_cache)
  - [erigon_chain_name](#erigon_chain_name)
  - [erigon_database_verbosity](#erigon_database_verbosity)
  - [erigon_dev_period](#erigon_dev_period)
  - [erigon_diagnostics](#erigon_diagnostics)
  - [erigon_dir_base](#erigon_dir_base)
  - [erigon_dir_binary](#erigon_dir_binary)
  - [erigon_dir_config](#erigon_dir_config)
  - [erigon_dir_data](#erigon_dir_data)
  - [erigon_dir_ethash_dag](#erigon_dir_ethash_dag)
  - [erigon_dir_log](#erigon_dir_log)
  - [erigon_dir_systemd](#erigon_dir_systemd)
  - [erigon_ethash_dagdir](#erigon_ethash_dagdir)
  - [erigon_externalcl](#erigon_externalcl)
  - [erigon_general_owner](#erigon_general_owner)
  - [erigon_group](#erigon_group)
  - [erigon_jwt_secret_path](#erigon_jwt_secret_path)
  - [erigon_log_console_json](#erigon_log_console_json)
  - [erigon_log_console_verbosity](#erigon_log_console_verbosity)
  - [erigon_log_delays](#erigon_log_delays)
  - [erigon_log_dir_disable](#erigon_log_dir_disable)
  - [erigon_log_dir_json](#erigon_log_dir_json)
  - [erigon_log_dir_prefix](#erigon_log_dir_prefix)
  - [erigon_log_dir_verbosity](#erigon_log_dir_verbosity)
  - [erigon_log_json](#erigon_log_json)
  - [erigon_log_level](#erigon_log_level)
  - [erigon_maxpeers](#erigon_maxpeers)
  - [erigon_metrics](#erigon_metrics)
  - [erigon_netrestrict](#erigon_netrestrict)
  - [erigon_nodiscover](#erigon_nodiscover)
  - [erigon_override_prague](#erigon_override_prague)
  - [erigon_pprof](#erigon_pprof)
  - [erigon_private_api_addr](#erigon_private_api_addr)
  - [erigon_private_api_ratelimit](#erigon_private_api_ratelimit)
  - [erigon_prune_distance](#erigon_prune_distance)
  - [erigon_prune_distance_blocks](#erigon_prune_distance_blocks)
  - [erigon_prune_mode](#erigon_prune_mode)
  - [erigon_reinstall](#erigon_reinstall)
  - [erigon_rpc_accesslist](#erigon_rpc_accesslist)
  - [erigon_rpc_allow_unprotected_txs](#erigon_rpc_allow_unprotected_txs)
  - [erigon_rpc_batch_concurrency](#erigon_rpc_batch_concurrency)
  - [erigon_rpc_batch_limit](#erigon_rpc_batch_limit)
  - [erigon_rpc_gascap](#erigon_rpc_gascap)
  - [erigon_rpc_maxgetproofrewindblockcount_limit](#erigon_rpc_maxgetproofrewindblockcount_limit)
  - [erigon_rpc_returndata_limit](#erigon_rpc_returndata_limit)
  - [erigon_rpc_streaming_disable](#erigon_rpc_streaming_disable)
  - [erigon_rpc_txfeecap](#erigon_rpc_txfeecap)
  - [erigon_systemd_service_name](#erigon_systemd_service_name)
  - [erigon_trustedpeers](#erigon_trustedpeers)
  - [erigon_txpool_accountqueue](#erigon_txpool_accountqueue)
  - [erigon_txpool_accountslots](#erigon_txpool_accountslots)
  - [erigon_txpool_api_addr](#erigon_txpool_api_addr)
  - [erigon_txpool_blobpricebump](#erigon_txpool_blobpricebump)
  - [erigon_txpool_blobslots](#erigon_txpool_blobslots)
  - [erigon_txpool_commit_every](#erigon_txpool_commit_every)
  - [erigon_txpool_disable](#erigon_txpool_disable)
  - [erigon_txpool_globalbasefeeslots](#erigon_txpool_globalbasefeeslots)
  - [erigon_txpool_globalqueue](#erigon_txpool_globalqueue)
  - [erigon_txpool_globalslots](#erigon_txpool_globalslots)
  - [erigon_txpool_lifetime](#erigon_txpool_lifetime)
  - [erigon_txpool_locals](#erigon_txpool_locals)
  - [erigon_txpool_nolocals](#erigon_txpool_nolocals)
  - [erigon_txpool_pricebump](#erigon_txpool_pricebump)
  - [erigon_txpool_pricelimit](#erigon_txpool_pricelimit)
  - [erigon_txpool_totalblobpoollimit](#erigon_txpool_totalblobpoollimit)
  - [erigon_txpool_trace_senders](#erigon_txpool_trace_senders)
  - [erigon_user](#erigon_user)
  - [erigon_verbosity](#erigon_verbosity)
- [Tags](#tags)

- [Dependencies](#dependencies)

---

## Defaults

### erigon_batch_size

Set the batch size for the execution stage.

#### Defaults

```YAML
erigon_batch_size: 512M
```

### erigon_binary_download_url

URL to download the erigon binary.

#### Defaults

```YAML
erigon_binary_download_url: https://github.com/erigontech/erigon/releases/download/v3.0.3/erigon_v3.0.3_linux_amd64.tar.gz
```

### erigon_binary_path

Path the erigon binary.

#### Defaults

```YAML
erigon_binary_path: '{{ erigon_dir_binary }}/erigon'
```

### erigon_bodies_cache

Limit the cache for block bodies.

#### Defaults

```YAML
erigon_bodies_cache: 268435456
```

### erigon_chain_name

Erigon chain name.

#### Defaults

```YAML
erigon_chain_name: sepolia
```

### erigon_database_verbosity

Enabling internal db logs. Very high verbosity levels may require recompile db. Default: 2, means warning.

#### Defaults

```YAML
erigon_database_verbosity: 2
```

### erigon_dev_period

Set the block period to use in developer mode (0 = mine only if transaction pending).

#### Defaults

```YAML
erigon_dev_period: 0
```

### erigon_diagnostics

Disable diagnostics.

#### Defaults

```YAML
erigon_diagnostics: false
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
erigon_dir_systemd: /lib/systemd/system
```

### erigon_ethash_dagdir

Set the directory to store the ethash mining DAGs.

### erigon_externalcl

Enables the external consensus layer.

#### Defaults

```YAML
erigon_externalcl: false
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

### erigon_jwt_secret_path

jwt token path for erigon.

#### Defaults

```YAML
erigon_jwt_secret_path: '{{ erigon_dir_config }}/jwt.hex'
```

### erigon_log_console_json

Format console logs with JSON.

#### Defaults

```YAML
erigon_log_console_json: false
```

### erigon_log_console_verbosity

Set the log level for console logs.

#### Defaults

```YAML
erigon_log_console_verbosity: info
```

### erigon_log_delays

Enable block delay logging.

#### Defaults

```YAML
erigon_log_delays: false
```

### erigon_log_dir_disable

Disable disk logging.

#### Defaults

```YAML
erigon_log_dir_disable: false
```

### erigon_log_dir_json

Format file logs with JSON.

#### Defaults

```YAML
erigon_log_dir_json: false
```

### erigon_log_dir_prefix

Set the file name prefix for logs stored to disk.

#### Defaults

```YAML
erigon_log_dir_prefix: ''
```

### erigon_log_dir_verbosity

Set the log verbosity for logs stored to disk.

#### Defaults

```YAML
erigon_log_dir_verbosity: info
```

### erigon_log_json

Format console logs with JSON.

#### Defaults

```YAML
erigon_log_json: false
```

### erigon_log_level

Force reinstall erigon binary.

#### Defaults

```YAML
erigon_log_level: info
```

### erigon_maxpeers

Set the maximum number of network peers (network disabled if set to 0).

#### Defaults

```YAML
erigon_maxpeers: 100
```

### erigon_metrics

Enable metrics collection and reporting.

#### Defaults

```YAML
erigon_metrics: false
```

### erigon_netrestrict

Restrict network communication to the given IP networks (CIDR masks).

#### Defaults

```YAML
erigon_netrestrict: ''
```

### erigon_nodiscover

Disable the peer discovery mechanism (manual peer addition).

#### Defaults

```YAML
erigon_nodiscover: false
```

### erigon_override_prague

Manually specify the Prague fork time, overriding the bundled setting.

#### Defaults

```YAML
erigon_override_prague: 0
```

### erigon_pprof

Enable the pprof HTTP server.

#### Defaults

```YAML
erigon_pprof: false
```

### erigon_private_api_addr

Set the internal grpc API address.

#### Defaults

```YAML
erigon_private_api_addr: 127.0.0.1:9090
```

### erigon_private_api_ratelimit

Set the amount of requests the server can handle simultaneously.

#### Defaults

```YAML
erigon_private_api_ratelimit: 31872
```

### erigon_prune_distance

Keep state history for the latest N blocks (default: everything).

#### Defaults

```YAML
erigon_prune_distance: 0
```

### erigon_prune_distance_blocks

Keep block history for the latest N blocks (default: everything).

#### Defaults

```YAML
erigon_prune_distance_blocks: 0
```

### erigon_prune_mode

Choose a pruning preset: archive, full, or minimal.

#### Defaults

```YAML
erigon_prune_mode: full
```

### erigon_reinstall

#### Defaults

```YAML
erigon_reinstall: false
```

### erigon_rpc_accesslist

Specify granular (method-by-method) API allowlist.

#### Defaults

```YAML
erigon_rpc_accesslist: ''
```

### erigon_rpc_allow_unprotected_txs

Allow for unprotected (non-EIP155 signed) transactions to be submitted via RPC.

#### Defaults

```YAML
erigon_rpc_allow_unprotected_txs: false
```

### erigon_rpc_batch_concurrency

Limit the amount of goroutines to process 1 batch request.

#### Defaults

```YAML
erigon_rpc_batch_concurrency: 2
```

### erigon_rpc_batch_limit

Set the maximum number of requests in a batch.

#### Defaults

```YAML
erigon_rpc_batch_limit: 100
```

### erigon_rpc_gascap

Set a cap on gas that can be used in eth_call/estimateGas.

#### Defaults

```YAML
erigon_rpc_gascap: 50000000
```

### erigon_rpc_maxgetproofrewindblockcount_limit

Set the max GetProof rewind block count.

#### Defaults

```YAML
erigon_rpc_maxgetproofrewindblockcount_limit: 100000
```

### erigon_rpc_returndata_limit

Set the maximum number of bytes returned from eth_call or similar invocations.

#### Defaults

```YAML
erigon_rpc_returndata_limit: 100000
```

### erigon_rpc_streaming_disable

Disable json streaming for some heavy endpoints.

#### Defaults

```YAML
erigon_rpc_streaming_disable: false
```

### erigon_rpc_txfeecap

Set a cap on transaction fee (in ether) that can be sent via the RPC APIs (0 = no cap).

#### Defaults

```YAML
erigon_rpc_txfeecap: 1
```

### erigon_systemd_service_name

Systemd service name for erigon.

#### Defaults

```YAML
erigon_systemd_service_name: erigon
```

### erigon_trustedpeers

Set the comma-separated enode URLs which are always allowed to connect, even above the peer limit.

#### Defaults

```YAML
erigon_trustedpeers: ''
```

### erigon_txpool_accountqueue

Set the maximum number of non-executable transaction slots permitted per account.

#### Defaults

```YAML
erigon_txpool_accountqueue: 64
```

### erigon_txpool_accountslots

Set the minimum number of executable transaction slots guaranteed per account.

#### Defaults

```YAML
erigon_txpool_accountslots: 16
```

### erigon_txpool_api_addr

Set the txPool api network address (default: use value of --private.api.addr).

#### Defaults

```YAML
erigon_txpool_api_addr: ''
```

### erigon_txpool_blobpricebump

Price bump percentage to replace existing (type-3) blob transaction.

#### Defaults

```YAML
erigon_txpool_blobpricebump: 100
```

### erigon_txpool_blobslots

Set the max allowed total number of blobs (within type-3 txs) per account.

#### Defaults

```YAML
erigon_txpool_blobslots: 48
```

### erigon_txpool_commit_every

Set the how often transactions should be committed to the storage.

#### Defaults

```YAML
erigon_txpool_commit_every: 15s
```

### erigon_txpool_disable

Experimental external pool and block producer. Disabling internal txpool and block producer.

#### Defaults

```YAML
erigon_txpool_disable: false
```

### erigon_txpool_globalbasefeeslots

Set the maximum number of non-executable transactions where only not enough baseFee.

#### Defaults

```YAML
erigon_txpool_globalbasefeeslots: 30000
```

### erigon_txpool_globalqueue

Set the maximum number of non-executable transaction slots for all accounts.

#### Defaults

```YAML
erigon_txpool_globalqueue: 30000
```

### erigon_txpool_globalslots

Set the maximum number of executable transaction slots for all accounts.

#### Defaults

```YAML
erigon_txpool_globalslots: 10000
```

### erigon_txpool_lifetime

Set the maximum amount of time non-executable transaction are queued.

#### Defaults

```YAML
erigon_txpool_lifetime: 3h0m0s
```

### erigon_txpool_locals

Comma separated accounts to treat as locals (no flush, priority inclusion).

#### Defaults

```YAML
erigon_txpool_locals: ''
```

### erigon_txpool_nolocals

Disables price exemptions for locally submitted transactions.

#### Defaults

```YAML
erigon_txpool_nolocals: false
```

### erigon_txpool_pricebump

Price bump percentage to replace an already existing transaction.

#### Defaults

```YAML
erigon_txpool_pricebump: 10
```

### erigon_txpool_pricelimit

Minimum gas price (fee cap) limit to enforce for acceptance into the pool.

#### Defaults

```YAML
erigon_txpool_pricelimit: 1
```

### erigon_txpool_totalblobpoollimit

Set the total limit of number of all blobs in txs within the txpool.

#### Defaults

```YAML
erigon_txpool_totalblobpoollimit: 480
```

### erigon_txpool_trace_senders

Set the comma-separated list of addresses, whose transactions will traced in transaction pool with debug printing.

#### Defaults

```YAML
erigon_txpool_trace_senders: ''
```

### erigon_user

Username for the erigon node.

#### Defaults

```YAML
erigon_user: erigon
```

### erigon_verbosity

Set the log level for console logs.

#### Defaults

```YAML
erigon_verbosity: info
```

## Tags

**_erigon-config_**

**_erigon-install_**

**_erigon-prepare_**

## Dependencies

None.
