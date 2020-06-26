# yaml-cli

## Usage

Build the image

```
$ docker build -t yaml-cli .
```

Run the image

```
$ cat users.yaml
users:
- name: Bogdan
$ docker run -it  -v $PWD:/data yaml-cli yaml --query users.0.name="Test" --overwrite-file /data/users.yaml
$ cat users.yaml
users:
- name: Test
```
